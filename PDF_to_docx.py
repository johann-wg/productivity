# pdf의 텍스트 및 이미지 모두 docx로 변환
from pdf2docx import Converter

# convert pdf to docx
pdf_file = '/Users/desktop/test/테스트-테스트.pdf'
docx_file = '/Users/desktop/test/테스트-테스트.docx'

# create a Converter instance
cv = Converter(pdf_file)

# convert pdf to docx
cv.convert(docx_file)

# close converter instance
cv.close()
