import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# === НАСТРОЙКИ ===
save_folder = ""  # 👉 Папка на телефоне
os.makedirs(save_folder, exist_ok=True)

# === ВВОД КОЛИЧЕСТВА ПРОЦЕССОВ ===
try:
    num_urls = int(input("Сколько ссылок вы хотите обработать? "))
except ValueError:
    print("Введите корректное число.")
    exit()

# === ВВОД ССЫЛОК ===
urls = []
for i in range(num_urls):
    u = input(f"[{i+1}] Введите ссылку: ").strip()
    urls.append(u)

# === ФУНКЦИЯ ПАРСИНГА ОДНОЙ ССЫЛКИ ===
def download_images_from_url(url, folder, base_count=0):
    print(f"\n[*] Загружаем страницу: {url}")
    try:
        response = requests.get(url, timeout=10)
    except Exception as e:
        print(f"[!] Ошибка загрузки страницы {url}: {e}")
        return 0

    soup = BeautifulSoup(response.text, "html.parser")
    images = soup.find_all("img")
    print(f"[*] Найдено изображений: {len(images)}")

    count = 0
    for img in images:
        src = img.get("src")
        if not src:
            continue

        img_url = urljoin(url, src)
        parsed = urlparse(img_url)
        ext = os.path.splitext(parsed.path)[1].lower()

        if ext not in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"]:
            print(f"[!] Пропущено (не изображение): {img_url}")
            continue

        try:
            print(f"[>] Скачиваем: {img_url}")
            img_data = requests.get(img_url, timeout=5).content
            filename = os.path.join(folder, f"image_{base_count + count + 1}{ext}")
            with open(filename, "wb") as f:
                f.write(img_data)
            print(f"[+] Сохранено: {filename}")
            count += 1
        except Exception as e:
            print(f"[!] Ошибка при загрузке {img_url}: {e}")
    return count

# === ОБРАБОТКА ВСЕХ ССЫЛОК ===
total_downloaded = 0
for index, link in enumerate(urls):
    total_downloaded += download_images_from_url(link, save_folder, base_count=total_downloaded)

print(f"\n[✓] Готово! Всего скачано изображений: {total_downloaded}")
