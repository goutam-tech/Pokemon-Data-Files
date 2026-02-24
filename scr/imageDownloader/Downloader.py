# import requests
# import re
# import os.path

# # This script will download all files from the URLs/URLs.txt and put them in Downloads directory
# downloadDir = "downloads/"

# while True:
#     response = input("Redownload All files ?(Y,N): ")
#     if response in ["Y", "y"]:
#         ReDownloadOnlyCorruptedFiles = False
#         break
#     if response in ["n", "n"]:
#         ReDownloadOnlyCorruptedFiles = True
#         # Re-download only corrupted files (sometimes <1kb corrupted files are downloaded from Bulbapedia)
#         print("Only new/ corrupted files will be downloaded")
#         break


# def Download(FileName):
#     with open(FileName, "wb") as file:
#         for chunk in r.iter_content(chunk_size=1024):
#             if chunk:
#                 file.write(chunk)
#         print("Downloaded: " + url)


# f = open("URLs/URLs.txt", "r")
# Lines = f.readlines()
# URLs = []
# for line in Lines:
#     URLs.append(line.strip())  # Stripping the newline character
# f.close()

# # Downloading
# for url in URLs:
#     try:
#         id = re.search(r"/\d\d\d\d", url).group(0)
#         id = id[1:]
#         fileToDownload = downloadDir + id + ".png"
#         r = requests.get(url, stream=True)
#         if not ReDownloadOnlyCorruptedFiles:
#             Download(fileToDownload)  # (Re-)Download all files unconditionally
#         elif os.path.exists(fileToDownload):
#             file_stat = os.stat(fileToDownload)
#             if file_stat.st_size < 1000:
#                 Download(fileToDownload)  # Re-download only corrupted files
#         else:
#             Download(fileToDownload)  # Download new file
#     except AttributeError:
#         print("An Error Occured for: " + id)

import requests
import re
import os
from PIL import Image

downloadDir = "downloads/"

# Ensure downloads folder exists
if not os.path.exists(downloadDir):
    os.makedirs(downloadDir)

# Ask user whether to redownload all files
while True:
    response = input("Redownload All files ? (Y/N): ").strip().lower()
    if response == "y":
        ReDownloadOnlyCorruptedFiles = False
        break
    elif response == "n":
        ReDownloadOnlyCorruptedFiles = True
        print("Only new/corrupted files will be downloaded")
        break

def is_corrupted(file_path):
    """Check if an existing file is corrupted or invalid."""
    try:
        with Image.open(file_path) as img:
            img.verify()  # Verify integrity
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

# Read URLs
with open("URLs/URLs.txt", "r") as f:
    URLs = [line.strip() for line in f if line.strip()]

# Process each URL
for url in URLs:
    match = re.search(r"(\d+)", url)
    if not match:
        print("Could not extract ID from:", url)
        continue

    # Pad ID to 4 digits (e.g., 20 -> 0020)
    id = match.group(1).zfill(4)
    file_path = os.path.join(downloadDir, f"{id}.png")

    if not ReDownloadOnlyCorruptedFiles:
        download_file(url, file_path)
    elif os.path.exists(file_path):
        if is_corrupted(file_path):
            print("Corrupted file detected, re-downloading:", file_path)
            download_file(url, file_path)
    else:
        download_file(url, file_path)