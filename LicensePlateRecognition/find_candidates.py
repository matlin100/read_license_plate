import cv2
import numpy as np

def filter_yellow_color(img):
    # Convert to HSV color space for color filtering
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Define range of yellow color in HSV
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    # Threshold the HSV image to get only yellow colors
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    return mask

def find_candidates(binary, original_img):
    # Apply color filtering to find yellow regions (potential license plates)
    yellow_mask = filter_yellow_color(original_img)
    # Combine the yellow color mask with the binary image
    combined_mask = cv2.bitwise_and(binary, binary, mask=yellow_mask)

    contours, _ = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    candidates = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = w / float(h)
        area = cv2.contourArea(cnt)
        rect_area = w * h
        solidity = area / float(rect_area)
        # Adjusted parameters for better matching to local license plates
        if 3 <= aspect_ratio <= 5 and 1000 < area < 30000 and solidity > 0.4:
            candidates.append((x, y, w, h))
    return candidates
