import cv2
import pytesseract
import tempfile
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = \
    r'C:\Program Files\Tesseract-OCR\tesseract'


def ocr_from_image(img_path):
    img1 = cv2.imread(img1_path)
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    filename = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    cv2.imwrite(filename.name, gray)

    text = pytesseract.image_to_string(Image.open(filename.name))
    print(text)

    cv2.imshow("Image", img1)
    cv2.imshow("Output", gray)
    cv2.waitKey(0)


img1_path = '20211217_153004422_iOS.jpg'
ocr_from_image(img1_path)
