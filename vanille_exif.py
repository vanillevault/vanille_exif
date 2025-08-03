#!/usr/bin/env python3
# Coded by Vanille

from PIL import Image
from PIL.ExifTags import TAGS
import sys

def extract_exif(image_path):
    try:
        img = Image.open(image_path)
        exif_data = img._getexif()

        if not exif_data:
            print("[!] No se encontraron metadatos EXIF.")
            return

        print(f"\n[+] EXIF data de '{image_path}':\n")
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            print(f"{tag:25}: {value}")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 vainilla_exif.py <imagen.jpg>")
    else:
        extract_exif(sys.argv[1])
