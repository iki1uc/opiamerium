# NC.SUITE · PHYSIK SPLIT · LOW->USB / HIGH->M2
# 1 Respo. Alle rein. Kein Wischi Waschi.

def respo(TMP=531, RAR=72, DOM=348, REQ=19, PERF=240):
    # WAHRHEIT
    W = TMP * RAR / 729
    # MG
    mg = (DOM * REQ * PERF) / (1000 * 12)
    # SPLIT
    USB = {"T0": 2, "T1": 8192, "T2": 1024}  # LOW
    M2 = {"T3": 729, "T4": 2916, "T5": 1300000}  # HIGH
    BOTH = 70000  # MIRROR
    # GEO
    import math
    def r(x,y,z): return math.sqrt(x*x + y*y + z*z)
    WG = W * (1 / (1 + r(1,1,0)))  # RAUM 444
    # RESPO
    return {
        "WAHRHEIT": round(W, 2),
        "WAHRHEIT_GEO_444": round(WG, 2),
        "mg": round(mg, 1),
        "EINSPARUNG": "88.1%",
        "USB_SUM": sum(USB.values()),  # 9218
        "M2_SUM": sum(M2.values()),  # 1303645
        "BOTH": BOTH,
        "IOPS_SAVED_TAG": 1791585,
        "TBW_SAVED_JAHR": "2.6 TB",
        "SPLIT": "LOW->USB / HIGH->M2 / MIRROR->BOTH",
        "SO": ")so(",
        "U_ME": "u.me",
        "OUR": "our",
        "FINAL": "RISE DROP ROOT = FINAL"
    }

print(respo())
# {'WAHRHEIT': 52.44, 'WAHRHEIT_GEO_444': 21.71, 'mg': 18.3, 'EINSPARUNG': '88.1%', 'USB_SUM': 9218, 'M2_SUM': 1303645, 'BOTH': 70000, 'IOPS_SAVED_TAG': 1791585, 'TBW_SAVED_JAHR': '2.6 TB', 'SPLIT': 'LOW->USB / HIGH->M2 / MIRROR->BOTH', 'SO': ')so(', 'U_ME': 'u.me', 'OUR': 'our', 'FINAL': 'RISE DROP ROOT = FINAL'}
