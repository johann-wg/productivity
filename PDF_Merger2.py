import os
from PyPDF2 import PdfMerger

folder_path = '/Users/desktop/test'
merged_file_path = os.path.expanduser('~') + '/desktop/result.pdf'

pdf_merger = PdfMerger()

for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        pdf_merger.append(open(os.path.join(folder_path, filename), 'rb'))

with open(merged_file_path, 'wb') as output_file:
    pdf_merger.write(output_file)
