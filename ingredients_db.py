# Ingredient Safety Database
# Sources: FDA GRAS list, EFSA evaluations, CSPI Chemical Cuisine ratings
# Severity: "safe", "mildly_safe", "harmful"

INGREDIENTS_DB = {
    # ─── NATURAL / COMMON ───
    "water": {
        "description": "Universal solvent and most abundant ingredient in most food products.",
        "severity": "safe",
        "reason": "Essential for life. No health risk whatsoever.",
        "category": "base"
    },
    "salt": {
        "description": "Sodium chloride, used for flavoring and preservation.",
        "severity": "mildly_safe",
        "reason": "Safe in small amounts but excessive intake linked to high blood pressure and cardiovascular disease.",
        "category": "mineral"
    },
    "sodium chloride": {
        "description": "Chemical name for common table salt.",
        "severity": "mildly_safe",
        "reason": "Safe in moderate amounts. High intake associated with hypertension.",
        "category": "mineral"
    },
    "sugar": {
        "description": "Sucrose derived from sugarcane or sugar beet, used as a sweetener.",
        "severity": "mildly_safe",
        "reason": "Natural but excessive consumption contributes to obesity, diabetes, and tooth decay.",
        "category": "sweetener"
    },
    "sucrose": {
        "description": "Common table sugar composed of glucose and fructose.",
        "severity": "mildly_safe",
        "reason": "Natural sweetener; overconsumption leads to metabolic issues.",
        "category": "sweetener"
    },
    "glucose": {
        "description": "Simple sugar, the body's primary energy source.",
        "severity": "safe",
        "reason": "Essential energy molecule naturally found in food and the body.",
        "category": "sweetener"
    },
    "fructose": {
        "description": "Natural sugar found in fruits and honey.",
        "severity": "mildly_safe",
        "reason": "Natural origin, but high intake (especially as HFCS) linked to liver issues and metabolic syndrome.",
        "category": "sweetener"
    },
    "high fructose corn syrup": {
        "description": "Processed sweetener made from corn starch with elevated fructose content.",
        "severity": "harmful",
        "reason": "Linked to obesity, insulin resistance, fatty liver disease, and metabolic syndrome with regular consumption.",
        "category": "sweetener"
    },
    "corn syrup": {
        "description": "Sweetener derived from corn starch, primarily glucose.",
        "severity": "mildly_safe",
        "reason": "High glycemic index; excessive use contributes to blood sugar spikes and weight gain.",
        "category": "sweetener"
    },
    "honey": {
        "description": "Natural sweetener produced by bees from flower nectar.",
        "severity": "safe",
        "reason": "Natural, contains antioxidants. Safe for adults; avoid for infants under 1 year.",
        "category": "sweetener"
    },
    "maple syrup": {
        "description": "Natural sweetener derived from maple tree sap.",
        "severity": "safe",
        "reason": "Natural sweetener with trace minerals. Moderate consumption is safe.",
        "category": "sweetener"
    },
    "stevia": {
        "description": "Natural zero-calorie sweetener derived from the Stevia rebaudiana plant.",
        "severity": "safe",
        "reason": "FDA GRAS status. Natural origin, no known adverse effects at normal consumption.",
        "category": "sweetener"
    },
    "aspartame": {
        "description": "Artificial sweetener approximately 200 times sweeter than sugar.",
        "severity": "harmful",
        "reason": "WHO classified as 'possibly carcinogenic' (Group 2B) in 2023. Contraindicated for people with phenylketonuria. Linked to headaches in sensitive individuals.",
        "category": "sweetener"
    },
    "saccharin": {
        "description": "Oldest artificial sweetener, 300–500 times sweeter than sugar.",
        "severity": "mildly_safe",
        "reason": "Once suspected carcinogen; removed from hazard list. Still debated; some studies suggest gut microbiome disruption.",
        "category": "sweetener"
    },
    "sucralose": {
        "description": "Chlorinated artificial sweetener marketed as Splenda.",
        "severity": "mildly_safe",
        "reason": "FDA approved, but recent research suggests it may disrupt gut bacteria and has potential genotoxic effects at high doses.",
        "category": "sweetener"
    },
    "acesulfame potassium": {
        "description": "Artificial sweetener also known as Ace-K, often used with other sweeteners.",
        "severity": "mildly_safe",
        "reason": "FDA approved but limited long-term human studies. Some animal studies suggest potential issues with metabolism.",
        "category": "sweetener"
    },
    "acesulfame-k": {
        "description": "Artificial sweetener also known as Ace-K.",
        "severity": "mildly_safe",
        "reason": "FDA approved; limited long-term data. Some concern over effects on gut microbiome.",
        "category": "sweetener"
    },

    # ─── FATS & OILS ───
    "vegetable oil": {
        "description": "Oil extracted from plant sources such as soybean, sunflower, or canola.",
        "severity": "mildly_safe",
        "reason": "Generally safe but highly processed versions contain inflammatory omega-6 fatty acids. Avoid if partially hydrogenated.",
        "category": "fat"
    },
    "palm oil": {
        "description": "Edible vegetable oil derived from the fruit of oil palms.",
        "severity": "mildly_safe",
        "reason": "High in saturated fat; excessive intake may raise LDL cholesterol. Also has significant environmental concerns.",
        "category": "fat"
    },
    "sunflower oil": {
        "description": "Oil extracted from sunflower seeds.",
        "severity": "safe",
        "reason": "Good source of vitamin E. Safe in moderate amounts; high-oleic versions are preferable.",
        "category": "fat"
    },
    "canola oil": {
        "description": "Oil derived from rapeseed, widely used in cooking.",
        "severity": "safe",
        "reason": "Low in saturated fat, good omega-3 content. FDA GRAS. Safe for general consumption.",
        "category": "fat"
    },
    "olive oil": {
        "description": "Oil pressed from olives, a staple of the Mediterranean diet.",
        "severity": "safe",
        "reason": "Rich in monounsaturated fats and antioxidants. Associated with cardiovascular benefits.",
        "category": "fat"
    },
    "butter": {
        "description": "Dairy fat made by churning cream.",
        "severity": "mildly_safe",
        "reason": "Natural fat but high in saturated fat; moderate consumption is acceptable for most people.",
        "category": "fat"
    },
    "trans fat": {
        "description": "Partially hydrogenated oils that extend shelf life of processed foods.",
        "severity": "harmful",
        "reason": "Strongly linked to heart disease, stroke, and type 2 diabetes. Banned or restricted in many countries.",
        "category": "fat"
    },
    "partially hydrogenated oil": {
        "description": "Vegetable oil processed to be solid at room temperature, containing trans fats.",
        "severity": "harmful",
        "reason": "Major source of artificial trans fats. Raises LDL, lowers HDL. FDA banned in 2018 in the US.",
        "category": "fat"
    },
    "hydrogenated vegetable oil": {
        "description": "Fully or partially hydrogenated plant oils used in processed foods.",
        "severity": "harmful",
        "reason": "Contains trans fats linked to cardiovascular disease. Restricted in many countries.",
        "category": "fat"
    },
    "cocoa butter": {
        "description": "Natural fat extracted from cocoa beans.",
        "severity": "safe",
        "reason": "Natural ingredient with stearic acid which is neutral for cholesterol. Safe in normal amounts.",
        "category": "fat"
    },
    "lard": {
        "description": "Rendered pig fat used in cooking and baking.",
        "severity": "mildly_safe",
        "reason": "Natural animal fat; high in saturated fat but also contains beneficial monounsaturated fats.",
        "category": "fat"
    },

    # ─── FLOUR & GRAINS ───
    "wheat flour": {
        "description": "Powder made by grinding wheat grain, used in baking.",
        "severity": "safe",
        "reason": "Safe for most people. Contains gluten — avoid if you have celiac disease or gluten sensitivity.",
        "category": "grain"
    },
    "whole wheat flour": {
        "description": "Flour made from the complete wheat kernel including bran and germ.",
        "severity": "safe",
        "reason": "Nutritious, high in fiber. Safe for most; unsuitable for those with gluten intolerance.",
        "category": "grain"
    },
    "corn starch": {
        "description": "Fine powder extracted from corn (maize) endosperm.",
        "severity": "safe",
        "reason": "Widely used thickener. FDA GRAS. Safe in typical dietary amounts.",
        "category": "grain"
    },
    "cornstarch": {
        "description": "Fine white powder from corn, used as a thickening agent.",
        "severity": "safe",
        "reason": "GRAS status. No known adverse effects at normal consumption levels.",
        "category": "grain"
    },
    "oats": {
        "description": "Whole grain cereal crop, rich in beta-glucan fiber.",
        "severity": "safe",
        "reason": "Highly nutritious. Associated with cholesterol reduction. Safe for most people.",
        "category": "grain"
    },
    "rice flour": {
        "description": "Flour made from finely milled rice, often used as a gluten-free alternative.",
        "severity": "safe",
        "reason": "Safe for most people including those with celiac disease. Nutritious grain flour.",
        "category": "grain"
    },
    "modified starch": {
        "description": "Starch that has been physically, enzymatically, or chemically treated.",
        "severity": "mildly_safe",
        "reason": "Generally safe (FDA GRAS) but the modification process varies; some forms may cause digestive issues in sensitive individuals.",
        "category": "grain"
    },
    "modified food starch": {
        "description": "Chemically or physically altered starch used as a thickener or stabilizer.",
        "severity": "mildly_safe",
        "reason": "FDA approved; considered safe but may be derived from wheat (gluten concern) or corn (GMO concern).",
        "category": "grain"
    },

    # ─── DAIRY ───
    "milk": {
        "description": "Nutrient-rich liquid produced by mammals, rich in calcium and protein.",
        "severity": "safe",
        "reason": "Highly nutritious. Safe for most; avoid if lactose intolerant or allergic to milk proteins.",
        "category": "dairy"
    },
    "skim milk": {
        "description": "Milk with most fat content removed.",
        "severity": "safe",
        "reason": "Nutritious, lower in calories than whole milk. Safe for most people.",
        "category": "dairy"
    },
    "whey": {
        "description": "Liquid remaining after milk has been curdled and strained.",
        "severity": "safe",
        "reason": "High-quality protein source. Safe for most people; avoid if allergic to dairy.",
        "category": "dairy"
    },
    "whey protein": {
        "description": "Protein concentrate or isolate derived from whey.",
        "severity": "safe",
        "reason": "Safe, high-quality complete protein. Generally well-tolerated; avoid with dairy allergy.",
        "category": "dairy"
    },
    "casein": {
        "description": "Primary protein in mammalian milk, comprising about 80% of cow's milk protein.",
        "severity": "safe",
        "reason": "Natural milk protein. Safe for most; may be problematic for those with milk protein allergy.",
        "category": "dairy"
    },
    "lactose": {
        "description": "Natural sugar found in milk and dairy products.",
        "severity": "safe",
        "reason": "Safe for most; causes digestive issues (bloating, cramps) in lactose-intolerant individuals.",
        "category": "dairy"
    },
    "cream": {
        "description": "High-fat dairy product skimmed from the top of milk.",
        "severity": "mildly_safe",
        "reason": "Natural dairy product; high in saturated fat. Moderate consumption acceptable for most people.",
        "category": "dairy"
    },
    "cheese": {
        "description": "Fermented dairy product made from milk curds.",
        "severity": "safe",
        "reason": "Good source of calcium and protein. Natural fermented food. Safe in moderation.",
        "category": "dairy"
    },

    # ─── PROTEINS ───
    "soy protein": {
        "description": "Protein isolated from soybeans, used in many processed foods.",
        "severity": "mildly_safe",
        "reason": "Generally safe; contains phytoestrogens. Concerns exist about GMO sourcing and potential thyroid effects in sensitive individuals.",
        "category": "protein"
    },
    "soy protein isolate": {
        "description": "Highly refined soy protein with most fat and carbohydrates removed.",
        "severity": "mildly_safe",
        "reason": "FDA GRAS but highly processed. Contains phytoestrogens; best consumed in moderation.",
        "category": "protein"
    },
    "egg": {
        "description": "Whole egg used as a binding agent, emulsifier, and nutrient source.",
        "severity": "safe",
        "reason": "Highly nutritious complete protein. Common allergen — avoid if egg allergy is present.",
        "category": "protein"
    },
    "egg white": {
        "description": "The clear liquid portion of an egg, primarily albumin protein.",
        "severity": "safe",
        "reason": "Excellent lean protein source. Safe for most; common allergen.",
        "category": "protein"
    },
    "egg yolk": {
        "description": "The yellow portion of an egg, rich in fat and nutrients.",
        "severity": "safe",
        "reason": "Nutrient-dense; contains vitamins A, D, E, K. Safe in moderation despite cholesterol content.",
        "category": "protein"
    },
    "gelatin": {
        "description": "Protein derived from animal collagen, used as a gelling agent.",
        "severity": "safe",
        "reason": "FDA GRAS. Natural animal-derived protein. Not suitable for vegetarians/vegans.",
        "category": "protein"
    },
    "pea protein": {
        "description": "Plant-based protein extracted from yellow split peas.",
        "severity": "safe",
        "reason": "Good plant protein with no known adverse effects. Safe for most people.",
        "category": "protein"
    },

    # ─── PRESERVATIVES ───
    "sodium benzoate": {
        "description": "Common food preservative used to prevent bacterial and mold growth.",
        "severity": "harmful",
        "reason": "Can form benzene (a known carcinogen) when combined with vitamin C. Linked to hyperactivity in children.",
        "category": "preservative"
    },
    "potassium sorbate": {
        "description": "Synthetic preservative used to inhibit mold and yeast growth.",
        "severity": "mildly_safe",
        "reason": "FDA GRAS but some individuals report skin and eye irritation. May cause allergic reactions in sensitive people.",
        "category": "preservative"
    },
    "sodium nitrate": {
        "description": "Preservative and color fixative used in processed meats.",
        "severity": "harmful",
        "reason": "Can form carcinogenic nitrosamines in the body. Linked to increased risk of colorectal cancer and heart disease.",
        "category": "preservative"
    },
    "sodium nitrite": {
        "description": "Preservative and antimicrobial agent used in cured and processed meats.",
        "severity": "harmful",
        "reason": "Forms nitrosamines which are known carcinogens. WHO classifies processed meats (containing nitrites) as Group 1 carcinogen.",
        "category": "preservative"
    },
    "bha": {
        "description": "Butylated hydroxyanisole — synthetic antioxidant preservative.",
        "severity": "harmful",
        "reason": "Listed as 'reasonably anticipated to be a human carcinogen' by the US National Toxicology Program.",
        "category": "preservative"
    },
    "butylated hydroxyanisole": {
        "description": "Synthetic antioxidant used to preserve fats and oils.",
        "severity": "harmful",
        "reason": "Classified as possible carcinogen. Shown to promote tumor growth in animal studies.",
        "category": "preservative"
    },
    "bht": {
        "description": "Butylated hydroxytoluene — synthetic antioxidant preservative.",
        "severity": "mildly_safe",
        "reason": "FDA approved but controversial. Some studies suggest carcinogenic potential; others show antioxidant benefits. Avoid in large amounts.",
        "category": "preservative"
    },
    "butylated hydroxytoluene": {
        "description": "Synthetic antioxidant added to fats, oils, and fat-containing foods.",
        "severity": "mildly_safe",
        "reason": "GRAS status but some animal studies link it to tumor promotion. Moderate concern.",
        "category": "preservative"
    },
    "tbhq": {
        "description": "Tertiary butylhydroquinone — petroleum-derived preservative.",
        "severity": "harmful",
        "reason": "Derived from petroleum. At high doses shown to cause DNA damage and promote tumor growth in animal studies.",
        "category": "preservative"
    },
    "sodium propionate": {
        "description": "Preservative used in baked goods to prevent mold growth.",
        "severity": "safe",
        "reason": "FDA GRAS. Naturally found in some cheeses. No significant health concerns at normal food levels.",
        "category": "preservative"
    },
    "calcium propionate": {
        "description": "Preservative commonly used in bread and bakery products.",
        "severity": "safe",
        "reason": "FDA GRAS. Naturally produced in some fermented foods. Generally well tolerated.",
        "category": "preservative"
    },
    "citric acid": {
        "description": "Naturally occurring acid found in citrus fruits, used as preservative and flavoring.",
        "severity": "safe",
        "reason": "FDA GRAS. Naturally found in many fruits. Safe for most people at normal dietary levels.",
        "category": "preservative"
    },
    "ascorbic acid": {
        "description": "Vitamin C used as a nutritional supplement and antioxidant preservative.",
        "severity": "safe",
        "reason": "Essential vitamin. FDA GRAS. Beneficial antioxidant. Very high doses may cause digestive upset.",
        "category": "preservative"
    },
    "tocopherols": {
        "description": "Vitamin E compounds used as natural antioxidant preservatives.",
        "severity": "safe",
        "reason": "Natural vitamin E. FDA GRAS. Beneficial antioxidant with no known harms at food levels.",
        "category": "preservative"
    },
    "sorbic acid": {
        "description": "Naturally occurring preservative used to inhibit mold and yeast.",
        "severity": "safe",
        "reason": "FDA GRAS. Naturally found in some berries. Well tolerated by most people.",
        "category": "preservative"
    },
    "vinegar": {
        "description": "Dilute acetic acid produced through fermentation, used as preservative and flavoring.",
        "severity": "safe",
        "reason": "Natural fermented product. FDA GRAS. Safe and may have modest health benefits.",
        "category": "preservative"
    },

    # ─── FOOD COLORING ───
    "red 40": {
        "description": "Synthetic red food dye also known as Allura Red AC.",
        "severity": "harmful",
        "reason": "Linked to hyperactivity in children. EU requires warning label. Derived from petroleum. Possible carcinogen under review.",
        "category": "coloring"
    },
    "allura red": {
        "description": "Synthetic petroleum-derived red food dye (Red 40).",
        "severity": "harmful",
        "reason": "Associated with hyperactivity in children. EU mandates warning label on products containing it.",
        "category": "coloring"
    },
    "yellow 5": {
        "description": "Synthetic yellow food dye also known as Tartrazine.",
        "severity": "harmful",
        "reason": "Linked to hyperactivity in children and allergic reactions, especially in aspirin-sensitive individuals. EU warning label required.",
        "category": "coloring"
    },
    "tartrazine": {
        "description": "Synthetic yellow azo dye used as food coloring.",
        "severity": "harmful",
        "reason": "Causes reactions in aspirin-sensitive individuals and hyperactivity in children. EU warning label required.",
        "category": "coloring"
    },
    "yellow 6": {
        "description": "Synthetic orange-yellow food dye also known as Sunset Yellow.",
        "severity": "harmful",
        "reason": "Part of the 'Southampton Six' dyes linked to hyperactivity in children. EU requires warning label.",
        "category": "coloring"
    },
    "blue 1": {
        "description": "Synthetic blue food dye also known as Brilliant Blue FCF.",
        "severity": "mildly_safe",
        "reason": "FDA approved. Some animal studies show potential for accumulation in tissues at high doses. Generally considered safe at food levels.",
        "category": "coloring"
    },
    "blue 2": {
        "description": "Synthetic blue food dye also known as Indigo Carmine.",
        "severity": "mildly_safe",
        "reason": "FDA approved; some studies show increased tumor incidence in rats at very high doses.",
        "category": "coloring"
    },
    "caramel color": {
        "description": "Brown coloring made by heat-treating carbohydrates.",
        "severity": "mildly_safe",
        "reason": "Class III and IV caramel color contains 4-MEI, a possible carcinogen. California requires warning label for products with significant 4-MEI.",
        "category": "coloring"
    },
    "annatto": {
        "description": "Natural yellow-orange food coloring from the seeds of the achiote tree.",
        "severity": "safe",
        "reason": "Natural plant-derived colorant. Generally safe; rare allergic reactions reported.",
        "category": "coloring"
    },
    "turmeric": {
        "description": "Natural yellow spice and coloring agent from the Curcuma longa plant.",
        "severity": "safe",
        "reason": "Natural spice with anti-inflammatory properties. Very safe at food levels.",
        "category": "coloring"
    },
    "beta carotene": {
        "description": "Natural orange pigment found in carrots and other orange vegetables.",
        "severity": "safe",
        "reason": "Natural provitamin A. FDA GRAS. Beneficial antioxidant. Safe at food levels.",
        "category": "coloring"
    },

    # ─── EMULSIFIERS & STABILIZERS ───
    "lecithin": {
        "description": "Natural emulsifier derived from soybeans, eggs, or sunflower seeds.",
        "severity": "safe",
        "reason": "FDA GRAS. Naturally occurring phospholipid. Well tolerated; some soy-allergic individuals may react.",
        "category": "emulsifier"
    },
    "soy lecithin": {
        "description": "Emulsifier derived from soybean oil processing.",
        "severity": "safe",
        "reason": "FDA GRAS. Very low protein content means most soy-allergic people can tolerate it. Generally safe.",
        "category": "emulsifier"
    },
    "mono and diglycerides": {
        "description": "Emulsifiers derived from glycerol and fatty acids, used to blend fat and water.",
        "severity": "mildly_safe",
        "reason": "FDA GRAS but may contain small amounts of trans fat. Widely used; generally safe but worth monitoring in high-fat diets.",
        "category": "emulsifier"
    },
    "polysorbate 80": {
        "description": "Synthetic emulsifier derived from sorbitol and oleic acid.",
        "severity": "mildly_safe",
        "reason": "FDA approved but some studies suggest it may disrupt gut microbiome and intestinal barrier. More research needed.",
        "category": "emulsifier"
    },
    "polysorbate 60": {
        "description": "Synthetic emulsifier used in baked goods and frozen desserts.",
        "severity": "mildly_safe",
        "reason": "FDA approved; some concern about gut microbiome disruption similar to Polysorbate 80.",
        "category": "emulsifier"
    },
    "carrageenan": {
        "description": "Natural polysaccharide extracted from red seaweed, used as a thickener.",
        "severity": "mildly_safe",
        "reason": "Natural origin but some research links it to intestinal inflammation. Degraded form (poligeenan) is harmful; food-grade is debated.",
        "category": "emulsifier"
    },
    "xanthan gum": {
        "description": "Polysaccharide produced by bacterial fermentation, used as a thickener.",
        "severity": "safe",
        "reason": "FDA GRAS. Natural fermentation product. Very safe; may cause minor digestive discomfort in very large amounts.",
        "category": "emulsifier"
    },
    "guar gum": {
        "description": "Natural thickener derived from guar beans.",
        "severity": "safe",
        "reason": "FDA GRAS. Natural plant fiber. Safe; very high doses may cause digestive issues.",
        "category": "emulsifier"
    },
    "locust bean gum": {
        "description": "Natural thickener derived from carob tree seeds.",
        "severity": "safe",
        "reason": "FDA GRAS. Natural plant-derived ingredient. Safe for most people.",
        "category": "emulsifier"
    },
    "pectin": {
        "description": "Natural polysaccharide found in fruit cell walls, used as a gelling agent.",
        "severity": "safe",
        "reason": "Naturally occurring in fruits. Soluble fiber with beneficial effects on cholesterol and blood sugar.",
        "category": "emulsifier"
    },
    "agar": {
        "description": "Natural gelling agent derived from red algae.",
        "severity": "safe",
        "reason": "FDA GRAS. Natural, vegetarian alternative to gelatin. No known adverse effects.",
        "category": "emulsifier"
    },
    "cellulose": {
        "description": "Plant fiber used as a filler, thickener, and anti-caking agent.",
        "severity": "safe",
        "reason": "Natural plant fiber. Indigestible. FDA GRAS. No health concerns.",
        "category": "emulsifier"
    },
    "methylcellulose": {
        "description": "Chemically modified cellulose used as thickener and emulsifier.",
        "severity": "safe",
        "reason": "FDA GRAS. Not absorbed by the body. Used as dietary fiber supplement. Safe.",
        "category": "emulsifier"
    },

    # ─── FLAVOR ENHANCERS ───
    "monosodium glutamate": {
        "description": "Sodium salt of glutamic acid, used as a flavor enhancer (umami).",
        "severity": "mildly_safe",
        "reason": "FDA GRAS but some individuals report 'MSG symptom complex' (headaches, flushing). Scientific consensus considers it safe for most people.",
        "category": "flavor"
    },
    "msg": {
        "description": "Monosodium glutamate — common umami flavor enhancer.",
        "severity": "mildly_safe",
        "reason": "FDA GRAS. Safe for most people. Some sensitive individuals may experience mild symptoms.",
        "category": "flavor"
    },
    "natural flavors": {
        "description": "Flavor compounds derived from natural sources including plants and animals.",
        "severity": "mildly_safe",
        "reason": "FDA regulated but the term is broad and may include hundreds of chemicals. Hard to assess without specifics.",
        "category": "flavor"
    },
    "artificial flavors": {
        "description": "Synthetically produced flavor compounds not derived from natural sources.",
        "severity": "mildly_safe",
        "reason": "FDA approved but synthetic origin raises concerns for some consumers. Generally considered safe at food levels.",
        "category": "flavor"
    },
    "yeast extract": {
        "description": "Savory flavoring made from yeast cells, naturally high in glutamates.",
        "severity": "safe",
        "reason": "Natural ingredient. Good source of B vitamins. Contains natural glutamates similar to MSG.",
        "category": "flavor"
    },
    "autolyzed yeast": {
        "description": "Yeast that has been broken down to release flavor compounds.",
        "severity": "safe",
        "reason": "Natural flavor source. FDA GRAS. MSG-sensitive individuals may wish to limit intake.",
        "category": "flavor"
    },
    "disodium inosinate": {
        "description": "Flavor enhancer derived from fish or meat, often used with MSG.",
        "severity": "mildly_safe",
        "reason": "Generally safe; but gout sufferers should avoid (high purine content). Usually paired with MSG to amplify flavor.",
        "category": "flavor"
    },
    "disodium guanylate": {
        "description": "Flavor enhancer derived from dried fish or seaweed.",
        "severity": "mildly_safe",
        "reason": "FDA approved; gout patients should avoid. Amplifies MSG effect. Generally safe.",
        "category": "flavor"
    },

    # ─── LEAVENING AGENTS ───
    "baking soda": {
        "description": "Sodium bicarbonate, a leavening agent that produces CO2 when heated.",
        "severity": "safe",
        "reason": "FDA GRAS. Natural mineral compound. Safe in normal cooking amounts.",
        "category": "leavening"
    },
    "sodium bicarbonate": {
        "description": "Chemical name for baking soda, used as a leavening agent.",
        "severity": "safe",
        "reason": "FDA GRAS. Safe at food levels. Very high doses can affect blood pH but food amounts are harmless.",
        "category": "leavening"
    },
    "baking powder": {
        "description": "Mixture of sodium bicarbonate with acid salts, used as a leavening agent.",
        "severity": "safe",
        "reason": "FDA GRAS. Standard baking ingredient. Safe at normal use levels.",
        "category": "leavening"
    },
    "yeast": {
        "description": "Single-celled fungi used to leaven bread and ferment beverages.",
        "severity": "safe",
        "reason": "Natural organism used in baking and brewing for millennia. Safe for most people.",
        "category": "leavening"
    },

    # ─── VITAMINS & MINERALS ───
    "niacin": {
        "description": "Vitamin B3, often added to fortify flour and cereals.",
        "severity": "safe",
        "reason": "Essential B vitamin. FDA GRAS. Important for energy metabolism.",
        "category": "vitamin"
    },
    "thiamine": {
        "description": "Vitamin B1 used to fortify grains and cereals.",
        "severity": "safe",
        "reason": "Essential B vitamin. Safe and important for nerve and muscle function.",
        "category": "vitamin"
    },
    "riboflavin": {
        "description": "Vitamin B2 used as a nutrient supplement and yellow coloring agent.",
        "severity": "safe",
        "reason": "Essential B vitamin. Natural yellow pigment. FDA GRAS. Very safe.",
        "category": "vitamin"
    },
    "folic acid": {
        "description": "Synthetic form of folate (vitamin B9) added to fortify foods.",
        "severity": "safe",
        "reason": "Essential vitamin, especially important for pregnant women. Safe at food fortification levels.",
        "category": "vitamin"
    },
    "vitamin c": {
        "description": "Ascorbic acid used as vitamin C supplement and antioxidant preservative.",
        "severity": "safe",
        "reason": "Essential vitamin with antioxidant properties. Very safe at food levels.",
        "category": "vitamin"
    },
    "vitamin e": {
        "description": "Fat-soluble vitamin used as an antioxidant in foods.",
        "severity": "safe",
        "reason": "Essential fat-soluble vitamin. FDA GRAS. Protective antioxidant.",
        "category": "vitamin"
    },
    "vitamin d": {
        "description": "Fat-soluble vitamin added to dairy and fortified foods.",
        "severity": "safe",
        "reason": "Essential vitamin for bone health. Safe at food fortification levels.",
        "category": "vitamin"
    },
    "iron": {
        "description": "Essential mineral added to fortify grains and cereals.",
        "severity": "safe",
        "reason": "Essential mineral for blood health. Safe at food fortification levels.",
        "category": "mineral"
    },
    "calcium": {
        "description": "Essential mineral for bone health, often added to dairy alternatives.",
        "severity": "safe",
        "reason": "Essential mineral. FDA GRAS. Important for bone and muscle health.",
        "category": "mineral"
    },
    "potassium": {
        "description": "Essential electrolyte mineral found naturally in many foods.",
        "severity": "safe",
        "reason": "Essential mineral for heart and muscle function. Safe at dietary levels.",
        "category": "mineral"
    },
    "zinc": {
        "description": "Essential trace mineral important for immune function.",
        "severity": "safe",
        "reason": "Essential mineral. FDA GRAS. Safe at food fortification levels.",
        "category": "mineral"
    },

    # ─── ACIDITY REGULATORS ───
    "lactic acid": {
        "description": "Naturally occurring acid produced by fermentation, used as preservative and flavoring.",
        "severity": "safe",
        "reason": "Naturally produced in fermentation. FDA GRAS. Safe for most people.",
        "category": "acid"
    },
    "malic acid": {
        "description": "Natural acid found in apples and other fruits, used for tartness.",
        "severity": "safe",
        "reason": "Naturally found in fruits. FDA GRAS. Safe at food levels.",
        "category": "acid"
    },
    "tartaric acid": {
        "description": "Natural acid found in grapes and tamarind, used as flavoring.",
        "severity": "safe",
        "reason": "Naturally occurring. FDA GRAS. Safe at normal food levels.",
        "category": "acid"
    },
    "phosphoric acid": {
        "description": "Inorganic acid used to add tartness to colas and processed foods.",
        "severity": "mildly_safe",
        "reason": "FDA GRAS but excessive intake linked to reduced bone density by interfering with calcium absorption.",
        "category": "acid"
    },
    "acetic acid": {
        "description": "The main component of vinegar, used as a preservative and flavoring.",
        "severity": "safe",
        "reason": "Natural fermentation product. FDA GRAS. Safe at food levels.",
        "category": "acid"
    },

    # ─── ANTI-CAKING AGENTS ───
    "silicon dioxide": {
        "description": "Fine powder used as an anti-caking agent to prevent clumping.",
        "severity": "safe",
        "reason": "FDA GRAS. Not absorbed by the body. Naturally found in many foods. Safe at food levels.",
        "category": "anti-caking"
    },
    "calcium silicate": {
        "description": "Anti-caking agent used in salt, baking powder, and spices.",
        "severity": "safe",
        "reason": "FDA GRAS. Inert mineral compound. Safe at food levels.",
        "category": "anti-caking"
    },

    # ─── SPICES & HERBS ───
    "pepper": {
        "description": "Common spice from Piper nigrum used for flavoring.",
        "severity": "safe",
        "reason": "Natural spice used worldwide. Safe for most people; may irritate sensitive digestive systems.",
        "category": "spice"
    },
    "garlic": {
        "description": "Pungent bulb used as flavoring with known health benefits.",
        "severity": "safe",
        "reason": "Natural ingredient with antibacterial and cardiovascular benefits. Safe for most.",
        "category": "spice"
    },
    "garlic powder": {
        "description": "Dehydrated and ground garlic used as a spice.",
        "severity": "safe",
        "reason": "Natural spice. Safe for most people.",
        "category": "spice"
    },
    "onion powder": {
        "description": "Dehydrated and ground onion used as a flavoring agent.",
        "severity": "safe",
        "reason": "Natural spice. Contains beneficial flavonoids. Safe for most.",
        "category": "spice"
    },
    "cinnamon": {
        "description": "Aromatic spice from tree bark, used in baking and confectionery.",
        "severity": "safe",
        "reason": "Natural spice with antioxidant properties. Safe at food levels.",
        "category": "spice"
    },
    "paprika": {
        "description": "Ground spice made from dried red peppers.",
        "severity": "safe",
        "reason": "Natural spice rich in antioxidants. Safe for most people.",
        "category": "spice"
    },

    # ─── NUTS & SEEDS ───
    "almonds": {
        "description": "Tree nuts rich in healthy fats, protein, and vitamin E.",
        "severity": "safe",
        "reason": "Highly nutritious. Safe for most; common tree nut allergen.",
        "category": "nut"
    },
    "peanuts": {
        "description": "Legumes commonly used in snacks, butters, and confectionery.",
        "severity": "safe",
        "reason": "Nutritious food; one of the most common and severe food allergens. Safe for non-allergic individuals.",
        "category": "nut"
    },
    "coconut": {
        "description": "Tropical fruit used for its flesh, milk, oil, and water.",
        "severity": "safe",
        "reason": "Natural food. FDA GRAS. High in saturated fat but contains beneficial MCTs.",
        "category": "nut"
    },
    "sesame": {
        "description": "Small seeds used in cooking and oil production.",
        "severity": "safe",
        "reason": "Nutritious seed; one of the top 9 allergens in the US. Safe for non-allergic individuals.",
        "category": "nut"
    },
    "flaxseed": {
        "description": "Small seeds rich in omega-3 fatty acids and fiber.",
        "severity": "safe",
        "reason": "Highly nutritious. Rich in ALA omega-3. FDA GRAS. Safe for most.",
        "category": "seed"
    },
    "chia seeds": {
        "description": "Small seeds from the Salvia hispanica plant, rich in omega-3 and fiber.",
        "severity": "safe",
        "reason": "Highly nutritious superfood. No known adverse effects at food levels.",
        "category": "seed"
    },
}

# Aliases for common alternate names
ALIASES = {
    "e621": "monosodium glutamate",
    "e951": "aspartame",
    "e954": "saccharin",
    "e955": "sucralose",
    "e950": "acesulfame potassium",
    "e129": "red 40",
    "e102": "yellow 5",
    "e110": "yellow 6",
    "e133": "blue 1",
    "e211": "sodium benzoate",
    "e202": "potassium sorbate",
    "e250": "sodium nitrite",
    "e251": "sodium nitrate",
    "e320": "bha",
    "e321": "bht",
    "e319": "tbhq",
    "e322": "lecithin",
    "e471": "mono and diglycerides",
    "e433": "polysorbate 80",
    "e415": "xanthan gum",
    "e412": "guar gum",
    "e440": "pectin",
    "e406": "agar",
    "e407": "carrageenan",
    "e300": "ascorbic acid",
    "e330": "citric acid",
    "e270": "lactic acid",
    "e296": "malic acid",
    "e334": "tartaric acid",
    "e338": "phosphoric acid",
    "e160a": "beta carotene",
    "e160b": "annatto",
    "e100": "turmeric",
    "e150": "caramel color",
    "e150a": "caramel color",
    "e150d": "caramel color",
    "e500": "sodium bicarbonate",
    "e501": "baking soda",
    "e551": "silicon dioxide",
    "e631": "disodium inosinate",
    "e627": "disodium guanylate",
    "vitamin b1": "thiamine",
    "vitamin b2": "riboflavin",
    "vitamin b3": "niacin",
    "vitamin b9": "folic acid",
    "vitamin b12": "riboflavin",
    "hfcs": "high fructose corn syrup",
}
