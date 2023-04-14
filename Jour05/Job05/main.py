def toilette(M, H):
    HM = H / 100
    DJ = 5 * 2 * HM
    DS = DJ * 7
    DT = DS * M
    return f"Pour {M} marches de {H} cm, le gardien parcours {DT:.2f} m par semaine"

print(toilette(100, 20))