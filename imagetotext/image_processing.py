import cv2
import pytesseract

# Path to Tesseract executable (change this if necessary)
# pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'


def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text


def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def remove_noise(image):
    return cv2.medianBlur(image, 5)


def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


if __name__ == '__main__':
    # Load image
    img = cv2.imread(
        '/Users/dylanimal/Desktop/Django_Lectures_env/Django_Lectures/news_aggregator/image.png')

    # Preprocess image
    gray = get_grayscale(img)
    noise = remove_noise(gray)
    thresh = thresholding(noise)

    # Perform OCR
    text = ocr_core(thresh)

    # Save results to file
    # output_file = input("Enter output file name: ")
    # with open(output_file, 'w') as f:
    #     f.write(text)
