import cv2
import pytesseract
import tempfile
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = \
    r'/opt/homebrew/bin/tesseract'
# r'C:\Program Files\Tesseract-OCR\tesseract'


def ocr_from_image(img_path):
    img = cv2.imread(img_path, 0)
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    filename = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    gray = cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255,
                         cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    gray = cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255,
                         cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    gray = cv2.threshold(cv2.medianBlur(img, 3), 0, 255,
                         cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    gray = cv2.adaptiveThreshold(cv2.GaussianBlur(img, (5, 5), 0), 255,
                                 cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, 31, 2)
    gray = cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9, 75, 75), 255,
                                 cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, 31, 2)
    gray = cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255,
                                 cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, 31, 2)
    cv2.imwrite(filename.name, gray)

    text = pytesseract.image_to_string(Image.open(filename.name))
    print(text)

    cv2.imshow("Image", img)
    cv2.imshow("Output", gray)
    cv2.waitKey(0)


# img1_path = '20211217_153004422_iOS.jpg'
# ocr_from_image(img1_path)

captcha1 = 'captcha1.jpg'
ocr_from_image(captcha1)
