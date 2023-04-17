import os
from PyPDF2 import PdfMerger

# PDF 파일 경로 설정
pdf_dir = "/Users/jjong/desktop/test"
result_dir = "/Users/jjong/desktop"
result_name = "결과 파일명.pdf"

# PDF 파일 결합용 객체 생성
pdf_merger = PdfMerger()

# PDF 파일 목록 가져오기
pdf_files = os.listdir(pdf_dir)

# PDF 파일을 결합하여 하나의 파일로 만듦
for pdf_file in pdf_files:
    if pdf_file.endswith(".pdf"):
        pdf_path = os.path.join(pdf_dir, pdf_file)
        pdf_merger.append(open(pdf_path, 'rb'))

# 결과 파일 저장
result_path = os.path.join(result_dir, result_name)
with open(result_path, "wb") as output:
    pdf_merger.write(output)
