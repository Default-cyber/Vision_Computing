import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

config_tessdata = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'

idiomas_instalados = pytesseract.get_languages(config=config_tessdata)

print("-" * 30) #this is new
print(" Idiomas disponíveis no seu Tesseract:")

for idioma in idiomas_instalados: #loop
    print(f" -> {idioma}")

print("-" * 30)


