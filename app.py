from readability.analyser import analyse_image

results = analyse_image("sample_images/black.png")

for result in results:
    print()
    print(result.region.text)
    print(f"FG: {result.foreground_luminance:.1f}")
    print(f"BG: {result.background_luminance:.1f}")
    print(f"Contrast: {result.contrast_ratio:.2f}")