from LicensePlateRecognition.lpr import *
from test.test_by_image import test_by_image
from easyocr import Reader
import time

def main():
    reader = Reader(['en'])   # Initialize the EasyOCR reader once
    cap = cv2.VideoCapture(0)  # Use 0 for the default webcam

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        license_plate_text, plate_img = read_license_plate(frame, reader)  # Pass the reader

        if license_plate_text:
            print(license_plate_text)
            cv2.putText(frame, f"License Plate: {license_plate_text}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('License Plate', plate_img)  # Show the cropped license plate image

        # else:
        #     print("No license plate detected.")

        # cv2.imshow('License Plate Recognition', frame)  # Show the frame with any annotations

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Break the loop on 'q' key press
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    reader = Reader(['en'])  # Initialize the EasyOCR reader once here
    test_by_image(reader)  # Pass the reader to the function
    main()
