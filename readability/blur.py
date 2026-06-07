import cv2


def blur_score(region):
    gray = cv2.cvtColor(
        region,
        cv2.COLOR_BGR2GRAY
    )

    return cv2.Laplacian(
        gray,
        cv2.CV_64F
    ).var()