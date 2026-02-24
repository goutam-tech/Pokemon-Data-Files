import csv
import requests
import os
from PIL import Image
from dotenv import load_dotenv

load_dotenv()
downloadDir = "filter_downloads/"
urls_file = "URLs/URLs.txt"
csv_file_pokemon_path = os.getenv("CSV_PATH_POKEMON")

# Ensure downloads folder exists
if not os.path.exists(downloadDir):
    os.makedirs(downloadDir)

def normalize_name(name: str) -> str: 
    # Decode URL encoding (e.g. %27 → ') 
    decoded = urllib.parse.unquote(name) # decode %27 → ' 
    normalized = decoded.lower().replace("_", "").replace(".", "").replace("'", "").replace("’", "").replace(" ", "")
    return normalized

special_cases = {
    "nidoran♀": "nidoran",   # Bulbapedia uses plain "nidoran"
    "nidoran♂": "nidoran",   # same here
    "farfetch'd": "farfetchd",   # matches url_map
    "mr. mime": "mrmime",        # matches url_map
    "porygon2": "porygon2"       # matches url_map
}

def is_corrupted(file_path):
    """Check if an existing file is corrupted or invalid."""
    try:
        with Image.open(file_path) as img:
            img.verify()
        return False
    except Exception:
        return True

def download_file(url, file_path):
    """Download a single file from URL to file_path."""
    try:
        r = requests.get(url, stream=True, timeout=10)
        if r.status_code == 200:
            with open(file_path, "wb") as file:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
            print("Downloaded:", file_path)
        else:
            print("Failed:", url, "Status:", r.status_code)
    except Exception as e:
        print("Error downloading", url, ":", e)

# Load URLs into a dictionary keyed by lowercase name
url_map = {}
with open(urls_file, "r") as f:
    for line in f:
        url = line.strip()
        if not url:
            continue
        # Extract name from URL (e.g., "0011Metapod.png" → "Metapod")
        filename = os.path.basename(url)
        name_part = filename.split(".")[0]  # "0011Metapod"
        # Remove leading digits to isolate name
        name = "".join([c for c in name_part if not c.isdigit()])
        url_map[name.lower()] = url

# Read CSV and download matching images
with open(csv_file_pokemon_path, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        poke_id = row["Id"]
        poke_name = row["Name"].lower()

        if poke_name in special_cases: 
            poke_name = special_cases[poke_name]

        if poke_name not in url_map:
            print(f"No URL found for: {row['Name']} (normalized: {poke_name})")
            continue

        url = url_map[poke_name]
        file_path = os.path.join(downloadDir, f"{poke_id}.png")

        if not os.path.exists(file_path) or is_corrupted(file_path):
            download_file(url, file_path)
