# readability/analyser.py

from .ocr import extract_text
from .image_utils import load_image, crop_region

from .luminance import average_luminance
from .complexity import edge_density
from .blur import blur_score

from .models import AnalysisResult


def analyse_image(image_path: str) -> list[AnalysisResult]:
    image = load_image(image_path)

    text_regions = extract_text(image_path)

    results = []

    for region in text_regions:
        cropped = crop_region(image, region)

        # OCR occasionally gives weird boxes
        if cropped.size == 0:
            continue

        brightness = average_luminance(cropped)
        complexity = edge_density(cropped)
        blur = blur_score(cropped)

        result = AnalysisResult(
            text=region.text,
            brightness=brightness,
            complexity=complexity,
            blur=blur,
            score=0.0,  # placeholder for now
        )

        results.append(result)

    return results