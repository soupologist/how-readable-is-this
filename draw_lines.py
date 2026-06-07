import cv2
import easyocr

reader = easyocr.Reader(["en"])

image = cv2.imread("sample_images/cbfc.png")

results = reader.readtext("sample_images/cbfc.png")

for bbox, text, confidence in results:
    pts = [(int(x), int(y)) for x, y in bbox]

    cv2.polylines(
        image,
        [cv2.convexHull(
            cv2.UMat(
                __import__("numpy").array(pts)
            ).get()
        )],
        True,
        (0, 255, 0),
        2,
    )

cv2.imwrite("output.png", image)