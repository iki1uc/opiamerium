# pat.py — PAT = Prüfstand — patch.js RAUS, pat.py REIN
# Korrekter Name: PAT, nicht patch. Name = Nutzung.
# PAT = Prüfstand für Namen wie soin.js. Code + Name Neugestaltung.
# 1 Sache, 2 Sichten, 1 Mirror. 1 Funktion triggert 1 andere.
# Brain 2 brain LAN. Local only. Kein Aua.

import re

# --- PAT ergänzen: 6 Muster, aus JS -> PY ---
# JS: /.../gi  -> PY: re.compile(..., re.IGNORECASE)
# JS: ([^"\']+) = Quelle. PY: gleich, aber PY-Syntax.

PAT = [
    # 1. script src — <script src="...">
    (re.compile(r'<script[^>]+src\s*=\s*["\']([^"\']+)["\']', re.IGNORECASE),
     "script src"),
    # 2. dynamischer import() — import("...")
    (re.compile(r'\bimport\s*\(\s*["\']([^"\']+)["\']', re.IGNORECASE),
     "dynamischer import()"),
    # 3. new Worker() — new Worker("...")
    (re.compile(r'new\s+Worker\s*\(\s*["\']([^"\']+)["\']', re.IGNORECASE),
     "new Worker()"),
    # 4. importScripts() — importScripts("...")
    (re.compile(r'importScripts\s*\(\s*["\']([^"\']+)["\']', re.IGNORECASE),
     "importScripts()"),
    # 5. serviceWorker.register() — serviceWorker.register("...")
    (re.compile(r'serviceWorker\.register\s*\(\s*["\']([^"\']+)["\']', re.IGNORECASE),
     "serviceWorker.register()"),
    # 6. iframe srcdoc (inline HTML) — <iframe srcdoc="...">
    (re.compile(r'<iframe[^>]+srcdoc\s*=\s*["\']', re.IGNORECASE),
     "iframe srcdoc (inline HTML)"),
]

# --- Gefährliche Schemas, aus Alt soin.js ---
# javascript: / data: / vbscript: -> bad, 50
BAD_SCHEMAS = [
    (re.compile(r'^\s*javascript\s*:', re.IGNORECASE), "javascript:"),
    (re.compile(r'^\s*data\s*:', re.IGNORECASE), "data:"),
    (re.compile(r'^\s*vbscript\s*:', re.IGNORECASE), "vbscript:"),
]

# --- 1 Respo: PAT prüfen ---
def pat_pruefen(text: str):
    """PAT = Prüfstand. 1 Text rein, 1 Respo raus."""
    treffer = []
    for muster, name in PAT:
        for m in muster.finditer(text or ""):
            quelle = m.group(1) if m.lastindex else "(inline)"
            treffer.append({
                "muster": name,
                "quelle": quelle,
                "stufe": "bad" if _ist_bad(quelle) else "pruefen",
                "punkte": 50 if _ist_bad(quelle) else 10,
            })
    return {
        "SO": ")so(",
        "PAT": "Prüfstand",
        "datei_alt": "patch.js RAUS",
        "datei_neu": "pat.py REIN",
        "korrekter_name": "pat.py — Name = Nutzung = Prüfstand",
        "treffer_n": len(treffer),
        "treffer": treffer,
        "respo": "OK" if not treffer else "NOK — prüfen",
        "stand": "STAND" if not treffer else "STAGE — prüfen",
    }

def _ist_bad(quelle: str) -> bool:
    q = (quelle or "").strip().lower()
    return q.startswith(("javascript:", "data:", "vbscript:"))

def add(name: str, quelle: str, punkte: int):
    """Alt soin.js: add('bad', ..., 50) -> PY: gleich."""
    return {"name": name, "quelle": quelle, "punkte": punkte, "stufe": "bad" if punkte >= 50 else "pruefen"}

if __name__ == "__main__":
    test = '<script src="x.js"></script> <iframe srcdoc="<p>hi</p>"> new Worker("w.js") import("y.js")'
    import json
    print(json.dumps(pat_pruefen(test), indent=2, ensure_ascii=False))
    print(add("bad", "javascript:alert(1)", 50))
