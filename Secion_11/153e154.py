import cv2
import os
import pytesseract

# configuration necessary , because we need of tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# every time place "r" before the directory
caminho_foto = r'testeocr.jpeg'  # it is in the same directory

# test if the path is correct
if not os.path.exists(caminho_foto):
    print(f"error: archive not found in path: {caminho_foto}")
    print("To place exact path in caminho_foto")
else:
    imagem = cv2.imread(caminho_foto)

    #if dont have a image, will go error
    if imagem is None:
        print("Error: the archive is here, but opencv could not read it (may be corrupted).")
    else:

        # 1. cv2.imshow Post BGR correct.
        # 2. converter for gray
        # 3. BGRA2BGR just make if the image have transparency. we will go using BGR2GRAY.
        image_ocr = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)  # Convert to grayscale for better OCR

        print("Correct! Image loaded and converted to grayscale.")

        # post results
        cv2.imshow('Teste', image_ocr)

        # will execute ocr
        texto = pytesseract.image_to_string(image_ocr)
        print("-" * 30)
        print("Text extrating")
        print(texto)
        print("-" * 30)

        cv2.waitKey(0)
        cv2.destroyAllWindows()