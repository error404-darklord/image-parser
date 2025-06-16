import os
import requests
from colorama import init, Fore, Back, Style
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# MENU LOAD
def menu_load():
    P = "ENTER TO EXIT"
    MENU = """
                                                                
▀███▀▀▀██▄      ██     ▀███▀▀▀██▄  ▄█▀▀▀█▄████▀▀▀███▀███▀▀▀██▄  
  ██   ▀██▄    ▄██▄      ██   ▀██▄▄██    ▀█ ██    ▀█  ██   ▀██▄ 
  ██   ▄██    ▄█▀██▄     ██   ▄██ ▀███▄     ██   █    ██   ▄██  
  ███████    ▄█  ▀██     ███████    ▀█████▄ ██████    ███████   
  ██         ████████    ██  ██▄  ▄     ▀██ ██   █  ▄ ██  ██▄   
  ██        █▀      ██   ██   ▀██▄██     ██ ██     ▄█ ██   ▀██▄ 
▄████▄    ▄███▄   ▄████▄████▄ ▄███▄▀█████▀▄██████████████▄ ▄███▄
"""
    print(MENU)
    print("             ")
    print("         " + P)
    print("             ")
    

menu_load()

# === НАСТРОЙКИ ===
save_folder = '/storage/emulated/0/P.H.H.D'  # 👉 Папка на телефоне
os.makedirs(save_folder, exist_ok=True)

# === ВВОД КОЛИЧЕСТВА ССЫЛОК ===
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

# === ФУНКЦИЯ СКАЧИВАНИЯ ИЗОБРАЖЕНИЙ ===
def download_images_from_url(url, folder, base_count=0):
    print(f"\n[*] Загружаем страницу: {url}")
    try:
        response = requests.get(url, timeout=10)
    except Exception as e:
        print(f"[!] Ошибка загрузки страницы {url}: {e}")
        return 0

    soup = BeautifulSoup(response.text, "html.parser")

    # Поиск всех изображений
    resources = []
    for tag in soup.find_all("img"):
        src = tag.get("src")
        if src:
            resources.append(src)

    print(f"[*] Найдено изображений: {len(resources)}")

    count = 0
    allowed_exts = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".heic", ".heif", ".tiff", ".tif", ".raw", ".psd", ".ico", ".dds", ".apng", ".tga", ".xcf"]

    for res in resources:
        file_url = urljoin(url, res)
        parsed = urlparse(file_url)
        ext = os.path.splitext(parsed.path)[1].lower()

        if ext not in allowed_exts:
            print(f"[!] Пропущено (не изображение): {file_url}")
            continue

        try:
            print(f"[>] Скачиваем: {file_url}")
            file_data = requests.get(file_url, timeout=5).content
            filename = os.path.join(folder, f"image_{base_count + count + 1}{ext}")
            with open(filename, "wb") as f:
                f.write(file_data)
            print(f"[+] Сохранено: {filename}")
            count += 1
        except Exception as e:
            print(f"[!] Ошибка при загрузке {file_url}: {e}")

    return count

# === ОБРАБОТКА ВСЕХ ССЫЛОК ===
total_downloaded = 0
for index, link in enumerate(urls):
    total_downloaded += download_images_from_url(link, save_folder, base_count=total_downloaded)

print(f"\n[✓] Готово! Всего скачано изображений: {total_downloaded}")