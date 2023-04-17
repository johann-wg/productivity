# '_'를 기준으로 병합
from PyPDF2 import PdfFileWriter, PdfReader, PdfMerger
import os

# 파일이 있는 폴더 경로
folder_path = '/users/desktop/test'

# 파일 이름 분리 후 첫 번째 문자 추출
file_groups = {}
for filename in os.listdir(folder_path):
    # 기준으로 정할 문자 입력 '_'
    name_parts = filename.split('_')
    group_name = name_parts[0]

    if group_name not in file_groups:
        file_groups[group_name] = []

    file_groups[group_name].append(filename)

# 각 그룹의 파일들을 하나의 PDF로 병합
for group_name, filenames in file_groups.items():
    pdf_merger = PdfMerger()

    for filename in filenames:
        pdf_path = os.path.join(folder_path, filename)
        pdf_reader = PdfReader(open(pdf_path, 'rb'))
        pdf_merger.append(pdf_reader)

    output_path = os.path.join(folder_path, f'{group_name}.pdf')
    with open(output_path, 'wb') as pdf_file:
        pdf_merger.write(pdf_file)
