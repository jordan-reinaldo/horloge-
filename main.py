import time

heure_actuelle = (13, 10, 55)
heure_reveil = (13, 11, 00)

def alarme(heure_reveil, heure_actuelle):
    if heure_actuelle == heure_reveil:
        print("C'est l'heure du réveil")

def format_12h(h, m, s):
    am_pm = "AM" if h < 12 else "PM"
    h = h % 12 #Cette ligne convertit l'heure du format 24 heures au format 12 heures. L'opérateur % (modulo) est utilisé pour obtenir le reste de la division de h par 12.
    h = 12 if h == 0 else h #Dans le format 12 heures, minuit ou midi est représenté par 12 et non 0. Cette ligne remplace donc 0 par 12 si h devient 0 après la conversion.
    return f"{h:02d}:{m:02d}:{s:02d} {am_pm}" #Cette ligne retourne l'heure formatée

def afficher_heure(heure_actuelle, mode_12h=False):
    h, m, s = heure_actuelle

    while True:
        alarme(heure_reveil, (h, m, s))

        if mode_12h:
            heure = format_12h(h, m, s)
        else:
            heure = f"{h:02d}:{m:02d}:{s:02d}"

        print(heure, end="\r")
        s += 1

        if s == 60:
            s = 0
            m += 1
            if m == 60:
                m = 0
                h += 1
                if h == 24:
                    h = 0

# test
afficher_heure(heure_actuelle, mode_12h=False)  