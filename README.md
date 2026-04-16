# Ingreanalyser

An AI-powered web application that analyses product ingredient labels and classifies each ingredient as **Safe**, **Mildly Safe**, or **Harmful** — based on a curated safety database sourced from FDA GRAS, EFSA, and CSPI Chemical Cuisine ratings.

---

## Features

- 🔐 JWT-based login and authentication
- 📋 Paste any product's ingredient list and get instant analysis
- 🟢 🟡 🔴 Per-ingredient severity classification (Safe / Mildly Safe / Harmful)
- 📊 Summary stats — total ingredients, counts per severity level
- 🗃️ 2000+ ingredients in local database (no API key required)
- 🔍 Fuzzy matching for alternate names and E-numbers
- 💡 Example presets to test instantly (Soda, Chips, Bread, Candy, Yogurt)
- ⚡ Works fully offline — no external AI API needed

---

## Tech Stack

| Layer    | Technology                        |
|----------|-----------------------------------|
| Frontend | HTML, CSS, JavaScript             |
| Backend  | Python, FastAPI                   |
| Auth     | JWT (PyJWT)                       |
| Database | Local dataset (FDA / EFSA / CSPI) |

---

## Project Structure

```
ingreanalyser/
├── main.py             ← FastAPI backend (routes, auth, analysis logic)
├── ingredients_db.py   ← Ingredient safety database (200+ entries)
├── requirements.txt    ← Python dependencies
├── index.html          ← Frontend (single-page app)
├── .gitignore
└── README.md
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Swaritsingh1/IngreAnalyser.git
cd ingreanalyser
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the backend

```bash
python -m uvicorn main:app --reload --port 8000
```

API live at: `http://localhost:8000`  
Interactive docs at: `http://localhost:8000/docs`

### 4. Open the frontend

Open `index.html` directly in your browser, or serve it locally:

```bash
python -m http.server 3000
```

Then visit `http://localhost:3000`

---

## Default Login Credentials

| Username | Password    |
|----------|-------------|
| admin    | password123 |
| user     | user123     |

To add more users, edit the `USERS` dictionary in `main.py`:

```python
USERS = {
    "admin": "password123",
    "yourname": "yourpassword",
}
```

---

## API Endpoints

| Method | Endpoint  | Description                       | Auth Required |
|--------|-----------|-----------------------------------|---------------|
| GET    | /         | Health check                      | No            |
| POST   | /login    | Authenticate and get JWT token    | No            |
| POST   | /analyse  | Analyse an ingredients list       | Yes (Bearer)  |

### Example `/analyse` request

```json
POST /analyse
Authorization: Bearer <your_token>

{
  "ingredients_text": "Water, Sugar, Sodium Benzoate, Citric Acid, Red 40"
}
```

### Example response

```json
{
  "ingredients": [
    {
      "name": "Water",
      "description": "Universal solvent...",
      "severity": "safe",
      "reason": "Essential for life.",
      "found_in_db": true
    },
    {
      "name": "Sodium Benzoate",
      "description": "Common food preservative...",
      "severity": "harmful",
      "reason": "Can form benzene when combined with vitamin C...",
      "found_in_db": true
    }
  ],
  "overall_assessment": "harmful",
  "summary": "Analysed 5 ingredient(s): 2 safe, 1 mildly safe, 2 harmful.",
  "total": 5,
  "safe_count": 2,
  "mildly_safe_count": 1,
  "harmful_count": 2,
  "unknown_count": 0
}
```

---

## Severity Classification

| Level          | Meaning                                                               |
|----------------|-----------------------------------------------------------------------|
| ✅ Safe         | Naturally occurring, well-studied, no known health risks              |
| ⚠️ Mildly Safe  | Generally safe but may affect sensitive individuals                   |
| ❌ Harmful      | Known health risks, controversial additives, or restricted in some countries |

---

## Data Sources

The ingredient safety database is built from:

- **FDA GRAS** — Generally Recognized as Safe substances list
- **EFSA** — European Food Safety Authority evaluations  
- **CSPI Chemical Cuisine** — Center for Science in the Public Interest additive ratings
- **WHO / IARC** — World Health Organization carcinogen classifications

---

## License

MIT License — free to use, modify, and distribute.

---

## Author

Built by [Swarit Singh](https://github.com/Swaritsingh1)
