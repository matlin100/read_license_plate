import cv2

def preprocess_image(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Dynamic contrast adjustment
    equalized = cv2.equalizeHist(gray)
    # Noise reduction
    blurred = cv2.GaussianBlur(equalized, (5, 5), 0)
    # Adaptive thresholding
    binary = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return binary


