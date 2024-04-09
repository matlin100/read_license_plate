from LicensePlateRecognition.lpr import *


image_paths = [
        '/Users/yechezkelmatlin/PycharmProjects/read_license_plate/test/images/1.jpeg',
        '/Users/yechezkelmatlin/PycharmProjects/read_license_plate/test/images/2.jpeg',
        '/Users/yechezkelmatlin/PycharmProjects/read_license_plate/test/images/3.jpeg',
        '/Users/yechezkelmatlin/PycharmProjects/read_license_plate/test/images/4.jpeg',
        '/Users/yechezkelmatlin/PycharmProjects/read_license_plate/test/images/5.jpeg',
        '/Users/yechezkelmatlin/PycharmProjects/read_license_plate/test/images/images.jpeg',
        '/Users/yechezkelmatlin/PycharmProjects/read_license_plate/test/images/images (1).jpeg'
        '/Users/yechezkelmatlin/PycharmProjects/read_license_plate/test/images/images (2).jpeg'
    ]
def test_by_image(reader):

    for image_path in image_paths:
        frame = cv2.imread(image_path)
        if frame is None:
            print(f"Failed to load image {image_path}")
            continue

        license_plate_text, plate_img = read_license_plate(frame, reader)

        if license_plate_text:
            print(f"License Plate Detected: {license_plate_text}")
            cv2.imshow('License Plate', plate_img)
            cv2.waitKey(3)
        else:
            print("No license plate detected.")

    cv2.destroyAllWindows()
