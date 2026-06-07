import cv2
import numpy as np


def edge_density(region):
    gray = cv2.cvtColor(
        region,
        cv2.COLOR_BGR2GRAY
    )

    edges = cv2.Canny(
        gray,
        100,
        200
    )

    return (
        np.count_nonzero(edges)
        / edges.size
    )