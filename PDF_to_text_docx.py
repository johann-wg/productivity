# PDF의 텍스트를 추출 후 docx로 저장. OCR되어 있는 PDF만 가능
import aspose.words as aw

# PDF 파일 로드
pdf = aw.Document('/Users/jjong/desktop/test/example.pdf')

# PDF 텍스트 추출
text = pdf.to_string(aw.SaveFormat.TEXT)

# DOCX 문서 생성
doc = aw.Document()
para = doc.first_section.body.first_paragraph 
para.append_child(aw.Run(doc, text))

# DOCX 파일로 저장
doc.save('/Users/jjong/desktop/테스트-테스트.docx')