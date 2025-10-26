#!/usr/bin/env python3
import os
import subprocess
import time
import sys

# Tylko Windows — szybkie sprawdzenie
if os.name != "nt":
    print("To skrypt przeznaczony dla Windows (taskkill/color/title/pause).")
    sys.exit(1)

# Ustaw tytuł okna i kolor (tak jak 'title' i 'color' w bat)
os.system("title Zamykanie ptoszka")
os.system("color 0C")  # 0C = czarne tło, czerwony tekst

print()
print("xd")
print()
print("zaraz ptoszka rozwalimy :)")
time.sleep(2)

# Próba zamknięcia Opery (cicho)
try:
    result = subprocess.run(
        ["taskkill", "/F", "/IM", "opera.exe"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
except Exception as e:
    print("Błąd podczas wywoływania taskkill:", e)
    result = None

# Sprawdzenie kodu zakończenia jak w %errorlevel%
if result is not None and result.returncode == 0:
    print()
    print("ptoszek zostal zamknięty")
else:
    print()
    print("Nie znaleziono procesu")

print()
# Zatrzymanie konsoli (zamiennik 'pause')
os.system("pause")
