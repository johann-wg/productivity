# Python 모듈용 Aspose.Words 가져오기
import aspose.words as aw

# PDF 파일 로드
pdf = aw.Document("/Users/desktop/test.pdf")

# TXT 파일에서 텍스트 추출 및 저장
pdf.save("/Users/desktop/extracted-text.txt")


# 아래의 코드는 docx파일로 저장하는 코드
# def extract_text_from_pdf(pdf_path, output_path):
#     # PDF 파일 로드
#     pdf = aw.Document(pdf_path)

#     # 텍스트 추출
#     text = pdf.get_text()

#     # 텍스트를 docx 파일로 저장
#     doc = aw.Document()
#     builder = aw.DocumentBuilder(doc)
#     builder.write(text)
#     doc.save(output_path)

# if __name__ == "__main__":
#     pdf_path = "/Users/desktop/test/테스트-테스트.pdf"  # PDF 파일 경로
#     output_path = "/Users/desktop/test/테스트-테스트.docx"  # 저장할 docx 파일 경로
#     extract_text_from_pdf(pdf_path, output_path)
