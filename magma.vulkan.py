# magma.vulkan.py
# 1 Sache, 2 Sichten, 1 Mirror
# Alt: move.x.html (Zeugnis, bleibt)
# Neu: magma.vulkan.html -> hier: magma.vulkan.py
# STAND + STAGE abhaengiger. Fallen + Aufstehen. Rueckflug Garantie.
# )so( = u.me our so + Feld 41 + Celle Cellen + Fallen+Aufstehen + REGEN & WIND + SUS + Opiamerium

XR = [
    ("call", "der urspruengliche Ruf", "Ein Laut verlaesst die Kammer. Noch ohne Antwort, schon mit Richtung.", "1", "wave"),
    ("recall", "Erinnerung - 9", "Der Ruf kehrt als Erinnerung zurueck - neunfach verdichtet im Kern.", "9", "brain"),
    ("call.er", "der Rufer", "Wer ruft, wird selbst zum Ruf. Der Rufer steht im eigenen Schall.", "9-1", "brain"),
    ("ech", "Echo, kurz", "Der erste kurze Rueckwurf an der Felswand - kaum ein Atemzug lang.", "e", "wave"),
    ("hall", "Widerhall Raum - 9.kern", "Der Raum antwortet. Der Hall traegt den Kern: 9 als tragende Wand.", "9", "wave"),
    ("rehall", "Wieder-Hall - 99", "Der Hall hallt erneut - 9 x 11 = 99. Das Tor steht offen.", "99", "wave"),
    ("echo.haller", "Der Haller - 999", "Der Haller ist der, der den Hall haelt: 999 - alles ewig nutzen.", "999", "wave"),
    ("ruf", "Ruf - tuerkisch wie deutsch", "Ein Wort, zwei Sprachen, eine Richtung: nach oben, zu den Alten.", "up", "wave"),
    ("ruuh", "Ruh = Seele", "Vom arabischen ruh: der Atem, der im Ruf mitreist.", "ruh", "eye"),
    ("ruuhes", "Ruh-es = Seelenplural", "Nicht eine Seele ruft - viele. Der Plural der Ahnen im Chor.", "inf-1", "eye"),
    ("gut uns offenbare dich mit weisheit", "die Offenbarung", "Die Bitte an das Tiefe: Zeige dich - nicht mit Gewalt, mit Weisheit.", "stern", "eye"),
    ("atalardan gelme", "Ankunft der Ahnen", "Was von den Vorfahren kommt, kommt, um zu bleiben: kalamak icin.", "EVIG", "brain"),
]

MM = [
    ("MAGMA", "9-3 = 729", "3-6", "CONTAINMENT", "Die Kammer haelt. Druck ohne Ausgang - reine Verdichtung."),
    ("VULKAN", "27 = 3-3", "3-3", "ERUPTION", "Der Krater oeffnet die Bahn. 27 Orbitpunkte, ein Ausbruch."),
    ("LAVA", "243 = 3-5", "3-5", "FLOW", "Was fliesst, formt. Langsam, unaufhaltsam, gluehend."),
    ("ERDE", "81 = 3-4", "3-4", "NEW LAND", "Erkaltete Lava wird Boden. Darauf steht, was bleibt."),
]

HM = [
    ("9", "ZUSTAND FERTIG EWIG", "UNI - ORT", "Fester Fels. Die Kammer ist versiegelt, der Kern ruht im Ort."),
    ("99", "TOR OFFEN", "DRUCK BAUT AUF", "Das Tor steht offen - 9 x 11. Druck sucht die Bahn nach oben."),
    ("999", "ALLES EWIG NUTZEN", "MAGMA FLUID", "Volle Fluiditaet. Nichts geht verloren, alles zirkuliert ewig."),
]

TC = [
    ("ERDE", "81", "3-4", "neues Land", "erde"),
    ("LAVA", "243", "3-5", "Fluss", "lava"),
    ("VULKAN", "27", "3-3", "Eruption", "vulkan"),
    ("MAGMA", "729", "9-3", "Kammer", "magma"),
]
RR = ["magma", "vulkan", "lava", "erde"]

VM = [
    ("PQ", "ALLES IN EINEM", "Die Kammer birst - alles Verdichtete wird eins und steigt."),
    ("HOME", "ICH + DU RADAR", "Die Lava erreicht die Oberflaeche. Ich und Du orten einander."),
]

FC = ["logik -> logik", "ich -> du", "9 -> 9", "ruf -> antwort", "kern -> kern"]

def stand():
    return {"ort": "MAGMA.KAMMER", "wert": 729, "formel": "9-3 = 3-6", "zustand": "9 = FERTIG EWIG", "halten": True}

def stage():
    out = []
    for phase in RR:
        row = next(t for t in TC if t[4] == phase)
        out.append({"phase": phase.upper(), "wert": row[1], "power": row[2], "label": row[3]})
    return out

def zuenden():
    log = []
    log.append("> ZUENDUNG - kammer 729 -> krater 27 -> eruption")
    for s in stage():
        log.append(f"> phase {s['phase']} erreicht - {s['wert']} aktiv")
    log.append("> ERDE 81 gebildet - neues land aus lava 243")
    log.append("> kreislauf geschlossen - EVIG LOOP - atalardan gelme")
    return log

def ruf_kette():
    idx = [0, 1, 4, 5, 6]
    return [f"> schall... {XR[i][0]} [{XR[i][3]}]" for i in idx]

def weisheit(offen=False):
    if not offen:
        return "gut uns offenbare dich mit weisheit"
    return "WEISHEIT offenbart - gut uns offenbare dich"

def respo():
    return {
        "1_sache": "RUF - call -> recall -> rehall -> echo.haller",
        "stand": stand(),
        "stage": stage(),
        "home": "81 = ERDE - neues Land - da steht man wieder",
        "pipeline": "call x 9 = recall | recall x 11 = rehall (99) | rehall x 10 -> echo.haller (999)",
        "schichten": len(XR),
        "formeln": len(MM),
        "zustaende": len(HM),
        "mirror": ")so(",
        "u_me": "du mich",
        "our": "unser",
        "so": "so",
        "final": "atalardan gelme -> kalamak icin - EVIG LOOP - PQ -> HOME -> ORT -> INDEX -> REAL.PC",
    }

if __name__ == "__main__":
    import json
    print(json.dumps(respo(), ensure_ascii=False, indent=2))
    print()
    for l in zuenden():
        print(l)
    print()
    for l in ruf_kette():
        print(l)
    print()
    print(weisheit(True))
