import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# === НАСТРОЙ ===
q1 = input("url: ")
url = q1
save_folder = ""  # 

# === СОЗДАНИЕ ПАПКИ ===
os.makedirs(save_folder, exist_ok=True)

# === ПОЛУЧАЕМ HTML ===
print(f"[*] Загружаем страницу: {url}")
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# === НАХОДИМ КАРТИНКИ ===
images = soup.find_all("img")
print(f"[*] Найдено изображений: {len(images)}")

count = 0
for img in images:
    src = img.get("src")
    if not src:
        continue

    # ПОЛНЫЙ URL
    img_url = urljoin(url, src)
    parsed = urlparse(img_url)
    ext = os.path.splitext(parsed.path)[1].lower()

    # Фильтр по расширению
    if ext not in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"]:
        print(f"[!] Пропущено (не изображение): {img_url}")
        continue

    try:
        print(f"[>] Скачиваем: {img_url}")
        img_data = requests.get(img_url, timeout=5).content
        filename = os.path.join(save_folder, f"image_{count + 1}{ext}")
        with open(filename, "wb") as f:
            f.write(img_data)
        print(f"[+] Сохранено: {filename}")
        count += 1
    except Exception as e:
        print(f"[!] Ошибка при загрузке {img_url}: {e}")

print(f"[✓] Готово! Скачано {count} изображений.")
