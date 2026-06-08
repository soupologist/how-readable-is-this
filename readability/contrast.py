def normalize_luminance(value):
    return value / 255.0

def contrast_ratio(
    foreground,
    background
):
    l1 = normalize_luminance(foreground)
    l2 = normalize_luminance(background)

    lighter = max(l1, l2)
    darker = min(l1, l2)

    return (
        lighter + 0.05
    ) / (
        darker + 0.05
    )