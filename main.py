from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import json
import os
import jwt
import datetime
import re
from typing import Optional
from ingredients_db import INGREDIENTS_DB, ALIASES

app = FastAPI(title="Ingreanalyser API", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

JWT_SECRET = os.getenv("JWT_SECRET", "ingreanalyser_secret_key_2024")
JWT_ALGORITHM = "HS256"

USERS = {
    "admin": "password123",
    "user": "user123",
}

security = HTTPBearer()

class LoginRequest(BaseModel):
    username: str
    password: str

class IngredientTextRequest(BaseModel):
    ingredients_text: str

class Ingredient(BaseModel):
    name: str
    description: str
    severity: str
    reason: str
    found_in_db: bool

class AnalyseResponse(BaseModel):
    ingredients: list[Ingredient]
    overall_assessment: str
    summary: str
    total: int
    safe_count: int
    mildly_safe_count: int
    harmful_count: int
    unknown_count: int

def create_token(username: str) -> str:
    payload = {
        "sub": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24),
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

def normalize(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[*®™()[\]{}]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def lookup_ingredient(raw_name: str) -> dict:
    key = normalize(raw_name)
    if key in INGREDIENTS_DB:
        return {"name": raw_name, **INGREDIENTS_DB[key], "found_in_db": True}
    if key in ALIASES:
        resolved = ALIASES[key]
        if resolved in INGREDIENTS_DB:
            return {"name": raw_name, **INGREDIENTS_DB[resolved], "found_in_db": True}
    for db_key, db_val in INGREDIENTS_DB.items():
        if db_key in key or key in db_key:
            return {"name": raw_name, **db_val, "found_in_db": True}
    for alias, resolved in ALIASES.items():
        if alias in key:
            if resolved in INGREDIENTS_DB:
                return {"name": raw_name, **INGREDIENTS_DB[resolved], "found_in_db": True}
    return {
        "name": raw_name,
        "description": "This ingredient was not found in our safety database.",
        "severity": "mildly_safe",
        "reason": "No safety data available in our database. Treat with caution and consult a nutritionist.",
        "found_in_db": False,
        "category": "unknown"
    }

def parse_ingredients_text(text: str) -> list:
    text = re.sub(
        r'^(ingredients|contains|ingr\.|ingr:|ingredient list|ingredients list)\s*[:.]?\s*',
        '', text, flags=re.IGNORECASE
    )
    parts = re.split(r'[,;\n]+', text)
    cleaned = []
    for part in parts:
        part = part.strip().strip('.')
        part = re.sub(r'^[\d\.\-\•\*]+\s*', '', part).strip()
        if 1 < len(part) < 80:
            cleaned.append(part)
    return cleaned

def compute_overall(ingredients: list) -> tuple:
    safe = sum(1 for i in ingredients if i["severity"] == "safe")
    mild = sum(1 for i in ingredients if i["severity"] == "mildly_safe")
    harmful = sum(1 for i in ingredients if i["severity"] == "harmful")
    unknown = sum(1 for i in ingredients if not i.get("found_in_db", True))
    total = len(ingredients)
    if harmful > 0:
        overall = "harmful"
    elif mild > safe:
        overall = "mildly_safe"
    else:
        overall = "safe"
    harmful_names = [i["name"] for i in ingredients if i["severity"] == "harmful"]
    summary_parts = [f"Analysed {total} ingredient(s): {safe} safe, {mild} mildly safe, {harmful} harmful, {unknown} unknown."]
    if harmful_names:
        summary_parts.append(f"Ingredients of concern: {', '.join(harmful_names[:3])}{'...' if len(harmful_names) > 3 else ''}.")
    if unknown > 0:
        summary_parts.append(f"{unknown} ingredient(s) were not found in our database and marked mildly safe by default.")
    return overall, " ".join(summary_parts)

@app.get("/")
def root():
    return {"message": "Ingreanalyser API v2 (local dataset mode) is running"}

@app.post("/login")
def login(data: LoginRequest):
    stored_password = USERS.get(data.username)
    if not stored_password or stored_password != data.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = create_token(data.username)
    return {"access_token": token, "token_type": "bearer", "username": data.username}

@app.post("/analyse", response_model=AnalyseResponse)
def analyse_ingredients(data: IngredientTextRequest, username: str = Depends(verify_token)):
    if not data.ingredients_text.strip():
        raise HTTPException(status_code=400, detail="Ingredients text cannot be empty.")
    raw_list = parse_ingredients_text(data.ingredients_text)
    if not raw_list:
        raise HTTPException(status_code=400, detail="Could not parse any ingredients from the provided text.")
    results = [lookup_ingredient(name) for name in raw_list]
    overall, summary = compute_overall(results)
    safe_c = sum(1 for r in results if r["severity"] == "safe")
    mild_c = sum(1 for r in results if r["severity"] == "mildly_safe")
    harm_c = sum(1 for r in results if r["severity"] == "harmful")
    unk_c  = sum(1 for r in results if not r.get("found_in_db", True))
    return AnalyseResponse(
        ingredients=[Ingredient(**{k: v for k, v in r.items() if k != "category"}) for r in results],
        overall_assessment=overall,
        summary=summary,
        total=len(results),
        safe_count=safe_c,
        mildly_safe_count=mild_c,
        harmful_count=harm_c,
        unknown_count=unk_c,
    )
