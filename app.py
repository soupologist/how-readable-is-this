# main.py

from readability.ocr import extract_text

regions = extract_text("sample_images/superman.png")

for region in regions:
    print(region)