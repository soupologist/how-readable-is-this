import cv2
import numpy as np

def relative_luminance(rgb):
    r, g, b = rgb

    return (
        0.2126 * r +
        0.7152 * g +
        0.0722 * b
    )

def average_luminance(region):
    gray = cv2.cvtColor(
        region,
        cv2.COLOR_BGR2GRAY
    )

    return float(np.mean(gray))