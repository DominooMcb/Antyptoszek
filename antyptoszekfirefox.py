import os
import time
import subprocess

print("[*] Przygotowanie do eksterminacji ptoszka...")
time.sleep(2)
print("[!] Ptosek wykryty. Eliminacja w toku...")

# Próba zabicia procesu Firefox
try:
    subprocess.run(["taskkill", "/F", "/IM", "firefox.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("[✓] Ptosek pomyślnie zneutralizowany.")
except Exception as e:
    print("[✗] Coś poszło nie tak przy zabijaniu ptoszka:", e)

time.sleep(1)
