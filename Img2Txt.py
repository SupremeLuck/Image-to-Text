from PIL import Image
from PIL import ImageEnhance
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\liu.sijia\AppData\Local\Tesseract-OCR\tesseract.exe'
 
img = Image.open('test.png')
img = img.convert('RGB')  #这里也可以尝试使用L
enhancer = ImageEnhance.Color(img)
 
enhancer = enhancer.enhance(0)
enhancer = ImageEnhance.Brightness(enhancer)
enhancer = enhancer.enhance(2)
enhancer = ImageEnhance.Contrast(enhancer)
enhancer = enhancer.enhance(8)
enhancer = ImageEnhance.Sharpness(enhancer)
img = enhancer.enhance(20)



# text = pytesseract.image_to_string(img, lang='chi_sim') # Read Chinese-Simple
text = pytesseract.image_to_string(img, lang='jpn') # Read Japanese

with open('test.txt', 'w', encoding='utf-8') as f:
    f.write(text)
