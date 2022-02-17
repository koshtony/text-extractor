from PIL import Image
import time
import re
from alive_progress import alive_bar
from pytesseract import pytesseract as pt
def text_extract():
        print("=============================================\n")
        tes_loc=str(input("Image path: \n"))
        print("==============================================\n")
        with alive_bar(200, bar = 'bubbles', spinner = 'notes2') as bar:
            for i in range(200):
                time.sleep(0.03)
                bar()  
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        image_path = tes_loc
        img = Image.open(image_path) 
        pt.tesseract_cmd = path_to_tesseract
        t_lst=pt.image_to_string(img)
        print("=============output Text======================\n")
        print(t_lst)
        print("====================END========================\n")
def main():
    while True:
        text_extract()
main()