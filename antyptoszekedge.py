#!/usr/bin/env python3
import os
import subprocess
import time
import sys

def _sanitize(s: str) -> str:
    # usuwa niepożądane słowa z komunikatów wyświetlanych użytkownikowi
    return s.replace("taskkill", "").replace("msedge", "")

# Tylko Windows
if os.name != "nt":
    print("Ten skrypt działa tylko na Windows (używa poleceń systemowych).")
    sys.exit(1)

os.system('title Zamykanie ptoszka na Edge')
os.system('color 0C')  # 0C = czarne tło, czerwony tekst

print()
print("xd")
print()
print("zaraz ptoszka na Edge rozwalimy :)")
time.sleep(2)

# Wywołanie polecenia systemowego do zamknięcia Edge (cicho)
try:
    result = subprocess.run(
        ["taskkill", "/F", "/IM", "msedge.exe"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
except Exception as e:
    # wyjątek sanitizujemy przed wypisaniem
    msg = _sanitize(f"Błąd podczas wykonywania polecenia systemowego: {e}")
    print()
    print(msg)
    result = None

# Sprawdzenie kodu zakończenia — komunikaty bez 'taskkill' i 'msedge'
if result is not None and result.returncode == 0:
    print()
    print("ptoszek na Edge zostal zamkniety")
else:
    print()
    print("Nie znaleziono procesu przeglądarki")

print()
os.system("pause")
