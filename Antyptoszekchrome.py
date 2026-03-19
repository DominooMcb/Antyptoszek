import os
import subprocess
import time

# Niebieski kolor i tytuł
os.system("title")

print("xd\nzaraz go rozwalimy :)")
time.sleep(1.5)

# Próba zamknięcia wszystkich procesów Chrome
result = subprocess.run(
    ["taskkill", "/F", "/IM", "chrome.exe", "/T"],
    capture_output=True
)

# Krótki wynik
if result.returncode == 0:
    print("\nZniszczony ")
else:
    print("\nNie znaleziono go ")

print("-" * 15)
os.system("pause")