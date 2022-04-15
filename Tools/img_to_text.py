import pytesseract
import cv2

# Ler Imagem

def converter():
    imagem = cv2.imread('image.jpg')

    # pedir para lera  imagem
    caminho = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    pytesseract.pytesseract.tesseract_cmd = caminho
    texto = pytesseract.image_to_string(imagem, lang="por")
    return texto