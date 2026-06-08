from .ocr import extract_text

from .image_utils import (
    load_image,
    crop_region,
)

from .masks import create_text_mask

from .foreground import (
    foreground_luminance
)

from .background import (
    background_luminance
)

from .contrast import (
    contrast_ratio
)

from .models import AnalysisResult


def analyse_image(image_path):
    image = load_image(image_path)

    regions = extract_text(image_path)

    results = []

    for region in regions:
        crop = crop_region(
            image,
            region
        )

        if crop.size == 0:
            continue

        mask = create_text_mask(crop)

        fg = foreground_luminance(
            crop,
            mask
        )

        bg = background_luminance(
            crop,
            mask
        )

        contrast = contrast_ratio(
            fg,
            bg
        )

        results.append(
            AnalysisResult(
                region=region,
                foreground_luminance=fg,
                background_luminance=bg,
                contrast_ratio=contrast,
            )
        )

    return results