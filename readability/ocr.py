# readability/ocr.py

import easyocr

from .models import OCRRegion


_reader = None


def get_reader():
    global _reader

    if _reader is None:
        _reader = easyocr.Reader(
            ["en"],
            gpu=False,  # set True later if you have CUDA
        )

    return _reader


def extract_text(image_path: str) -> list[OCRRegion]:
    reader = get_reader()

    results = reader.readtext(image_path)

    regions = []

    for bbox, text, confidence in results:
        xs = [point[0] for point in bbox]
        ys = [point[1] for point in bbox]

        x = int(min(xs))
        y = int(min(ys))

        width = int(max(xs) - x)
        height = int(max(ys) - y)

        regions.append(
            OCRRegion(
                text=text,
                confidence=float(confidence),
                x=x,
                y=y,
                width=width,
                height=height,
            )
        )

    return regions