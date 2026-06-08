import cv2


def create_text_mask(region):
    gray = cv2.cvtColor(
        region,
        cv2.COLOR_BGR2GRAY
    )

    _, mask = cv2.threshold(
        gray,
        180,
        255,
        cv2.THRESH_BINARY
    )

    return mask