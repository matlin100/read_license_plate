import cv2
import re
from LicensePlateRecognition.find_candidates import find_candidates
from LicensePlateRecognition.preprocess_image import preprocess_image
import numpy as np

def filter_license_plate_text(raw_text):
    # Improved pattern that considers potential license plate formats more broadly
    pattern = r"[A-Z0-9]{7,8}"
    filtered_text = ''.join(re.findall(pattern, raw_text.upper()))
    digits_only = re.sub(r'\D', '', filtered_text)
    if 7 <= len(digits_only) <= 8:
        return digits_only
    return None


def read_license_plate(frame, reader):
    binary = preprocess_image(frame)

    # Find license plate candidates
    candidates = find_candidates(binary, frame)

    for x, y, w, h in candidates:
        plate_img = frame[y:y+h, x:x+w]
        result = reader.readtext(plate_img, detail=0)  # Using detail=0 for text only
        license_plate_text = filter_license_plate_text(' '.join(result))

        # Draw rectangle around the license plate
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        if license_plate_text:
            # Annotate the detected text only if license plate text is recognized
            cv2.putText(frame, license_plate_text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
            cv2.imshow('License Plate Recognition', frame)
            cv2.waitKey(1)
            return license_plate_text, plate_img

    # Always return a tuple; (None, None) if no valid plate is found
    cv2.imshow('License Plate Recognition', frame)
    cv2.waitKey(1)
    return None, None
