# PDF 파일을 OCR한 다음에 docx로 저장하기. 성능이 너무 안 좋음. 그냥 안 됨.
import pytesseract
from pdf2image import convert_from_path
from docx import Document

# 한국어 학습 데이터 경로 추가
custom_config = r'--oem 3 --psm 6 tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ --tessdata-dir "C:/Tesseract-OCR/tessdata"'

# pytesseract가 인식하는 환경변수 경로 지정
pytesseract.pytesseract.tesseract_cmd = r'/Tesseract-OCR/tesseract.exe'

poppler_path = r"C:/poppler-0.68.0/bin"
pages = convert_from_path('/Users/jjong/desktop/test/테스트-테스트.pdf', poppler_path=poppler_path)


# PDF 파일을 이미지로 변환
pages = convert_from_path('/Users/jjong/desktop/test/테스트-테스트.pdf')

# 이미지에서 텍스트 추출
text = ''
for page in pages:
    text += pytesseract.image_to_string(page)

doc = Document()
doc.add_paragraph(text)
doc.save('/Users/jjong/desktop/example.docx')
