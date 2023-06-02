import numpy as np
import cv2 as cv
from typing import Tuple


def find_heads(image: np.ndarray) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Finds boxer and enemy head
    inputs:
        image: game image
    return: ((boxer_x, boxer_y)(enemy_x, enemy_y))
    """
    if len(image.shape) == 3:
        # make it gray scale
        image = np.sum(image, axis=-1) / 3

    image = image[30:, 30:].astype(np.uint8)
    image_copy = np.copy(image)

    # Apply thresholding to convert the image to binary
    binary_image = np.zeros_like(image)
    binary_image[image > 180] = 255

    # Find contours in the binary image
    contours, _ = cv.findContours(
        binary_image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Find the contour with the largest area
    largest_contour = max(contours, key=cv.contourArea)

    # Iterate through the contours and find the bounding rectangle
    x, y, w, h = cv.boundingRect(largest_contour)

    # Calculate the center point of the bounding rectangle
    myhead_x = x + 10
    myhead_y = y + h // 2
    # Draw a circle at the center of the bounding box

    # Apply thresholding to convert the image to binary
    image = image_copy
    binary_image = np.zeros_like(image)
    binary_image[image < 50] = 255

    # Find contours in the binary image
    contours, _ = cv.findContours(
        binary_image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Find the contour with the largest area
    largest_contour = max(contours, key=cv.contourArea)

    # Iterate through the contours and find the bounding rectangle
    x, y, w, h = cv.boundingRect(largest_contour)

    # Calculate the center point of the bounding rectangle
    enemyhead_x = x + w - 10
    enemyhead_y = y + h // 2

    return (myhead_x, myhead_y), (enemyhead_x, enemyhead_y)


def encode_state(boxer: Tuple[int, int], enemy: Tuple[int, int]):
    """
    Encode boxers state
    input:
        boxer: (boxer_x, boxer_y) boxer position
        enemy: (enemy_x, enemy_y) enemy position
    return: (int) encoded state 
    """
    x_sign = 1 if boxer[0] > enemy[0] else 2
    y_sign = 1 if boxer[0] > enemy[0] else 2

    x_distance = abs(boxer[0] - enemy[0])
    y_distance = abs(boxer[1] - enemy[1])

    x_distance = 1 if x_distance < 20 else 2 if x_distance < 40 else 3 if x_distance < 60 else 4
    y_distance = 1 if y_distance < 20 else 2 if y_distance < 40 else 3 if y_distance < 60 else 4

    return x_distance*1000 + y_distance*100 + x_sign*10 + y_sign
