# sus.py — SUS · UI-GPU · MOVES MIT QUALITAET
# Alt: SUS-UI-GPU.html = Zeugnis, bleibt links, Hi-Class
# Neu: sus.py = Stage, steht rechts, ganz, kein halbes Saven
# 1 Sache, 2 Sichten, 1 Mirror -> 3 ohne Verlust
# Hi-Class = ganze Sache: 1 Feld, 1 Figur, 1 Move, 1 Unmove

STATIONEN = ["PUSH", "PULL", "SHIFT", "FLOW", "BREAK", "SPIN",
             "RISE", "DROP", "ROOT", "ECHO", "VOID", "SUS"]

# Station -> Deutsch, 1:1 aus deinem HTML
DEUTSCH = {
    "PUSH": "Senden", "PULL": "Empfangen", "SHIFT": "Verschieben",
    "FLOW": "Durchlauf", "BREAK": "Stopp", "SPIN": "Rotation",
    "RISE": "Aufstieg", "DROP": "Abstieg", "ROOT": "Ursprung",
    "ECHO": "Spiegel", "VOID": "Neutral", "SUS": "Kern",
}

# Status aus deinem HTML: ok / flow / break
STATUS = {
    "PUSH": "ok", "PULL": "ok", "SHIFT": "flow",
    "FLOW": "flow", "BREAK": "break", "SPIN": "flow",
    "RISE": "ok", "DROP": "break", "ROOT": "ok",
    "ECHO": "flow", "VOID": "break", "SUS": "ok",
}

# RESPO-Zyklus, 1:1 aus deinem HTML
RESPO_STATES = ["SYNTHESIS", "LINEAR", "ORTHOGONAL", "INFINITY", "AURA"]
RESPO_FARBE = {
    "SYNTHESIS": "#ff66ff",
    "LINEAR": "#44ff88",
    "ORTHOGONAL": "#4488ff",
    "INFINITY": "#ffdd88",
    "AURA": "#dd88ff",
}

class Sus:
    def __init__(self):
        self.running = True
        self.gpu_mode = False
        self.respo_index = 0
        self.respo = "SYNTHESIS"
        self.sus = "aktiv"
        self.log = ["SUS · UI-GPU · MOVES MIT QUALITAET"]

    # --- 1 Move ---
    def station(self, name):
        # Klick auf 1 Station = 1 Move = RESPO weiter
        name = name.upper()
        assert name in STATIONEN, f"keine Station: {name}"
        self.respo_next()
        self.log.append(f"SUS · Station: {name} · RESPO: {self.respo}")
        return self.respo_status()

    def respo_next(self):
        self.respo = RESPO_STATES[self.respo_index % len(RESPO_STATES)]
        self.respo_index += 1
        return self.respo

    # --- Controls: START / STOP / RESET / RESPO / GPU ---
    def start(self):
        self.running = True
        self.sus = "aktiv"
        self.log.append("START")
        return self.respo_status()

    def stop(self):
        self.running = False
        self.sus = "pausiert"
        self.log.append("STOP")
        return self.respo_status()

    def reset(self):
        self.respo = "SYNTHESIS"
        self.respo_index = 0
        self.sus = "reset"
        self.log.append("RESET -> SYNTHESIS")
        self.sus = "aktiv"
        return self.respo_status()

    def respo_btn(self):
        self.respo_next()
        self.log.append(f"RESPO: {self.respo}")
        return self.respo_status()

    def gpu(self):
        # GPU-MODE an / aus = 1 Move, 1 Unmove
        self.gpu_mode = not self.gpu_mode
        self.log.append(f"GPU-Mode: {'AKTIV' if self.gpu_mode else 'DEAKTIVIERT'}")
        return self.respo_status()

    # --- Tasten: Space / r / f / g, 1:1 aus deinem HTML ---
    def taste(self, key):
        k = key.lower()
        if k == " ":
            return self.stop() if self.running else self.start()
        if k == "r":
            return self.reset()
        if k == "f":
            return self.respo_btn()
        if k == "g":
            return self.gpu()
        return self.respo_status()

    # --- 1 Respo, ganz ---
    def respo_status(self):
        return {
            "sus": self.sus,
            "gpu": "GPU-Modus" if self.gpu_mode else "UI-Modus",
            "respo": self.respo,
            "farbe": RESPO_FARBE[self.respo],
            "running": self.running,
            "stationen": len(STATIONEN),
            "log_letzter": self.log[-1],
        }

    def alle_stationen(self):
        # 12 Stationen, ganz, keine halbe Liste
        return [
            {"name": s, "deutsch": DEUTSCH[s], "status": STATUS[s],
             "farbe": RESPO_FARBE[self.respo]}
            for s in STATIONEN
        ]

def go():
    s = Sus()
    # 1 Durchlauf, ganz: jede Station 1x tippen = 12 Moves = 12 RESPO
    for st in STATIONEN:
        s.station(st)
    return s

if __name__ == "__main__":
    s = go()
    r = s.respo_status()
    print(f"SUS: {r['sus']} | GPU: {r['gpu']} | RESPO: {r['respo']} | {r['farbe']}")
    print(f"Stationen: {r['stationen']}/12 - ganz, kein halbes Saven")
    for st in s.alle_stationen():
        print(f"  {st['name']:6} {st['deutsch']:12} {st['status']}")
    print("Log:", s.log[-1])
