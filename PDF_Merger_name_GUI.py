from PyPDF2 import PdfMerger, PdfReader
import tkinter as tk
from tkinter import filedialog
import os

# 파일 이름 분리 문자 설정
SEPARATOR = '_'

def merge_pdfs(folder_path, separator):
    # 파일 이름 분리 후 첫 번째 문자 추출
    file_groups = {}
    for filename in os.listdir(folder_path):
        name_parts = filename.split(separator)
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

def select_folder_path():
    folder_path = filedialog.askdirectory()
    folder_path_var.set(folder_path)

def merge_pdfs_gui():
    folder_path = folder_path_var.get()
    separator = separator_var.get()
    merge_pdfs(folder_path, separator)

# tkinter GUI 생성
root = tk.Tk()
root.title("PDF 병합 프로그램")

# 폴더 경로 선택 버튼
folder_path_var = tk.StringVar()
folder_path_label = tk.Label(root, text="폴더 경로:")
folder_path_label.grid(row=0, column=0)
folder_path_entry = tk.Entry(root, textvariable=folder_path_var, width=30)
folder_path_entry.grid(row=0, column=1)
folder_path_button = tk.Button(root, text="폴더 선택", command=select_folder_path)
folder_path_button.grid(row=0, column=2)

# 파일 이름 분리 문자 설정
separator_var = tk.StringVar()
separator_var.set(SEPARATOR)
separator_label = tk.Label(root, text="파일 이름 분리 문자:")
separator_label.grid(row=1, column=0)
separator_entry = tk.Entry(root, textvariable=separator_var, width=10)
separator_entry.grid(row=1, column=1)

# PDF 병합 버튼
merge_button = tk.Button(root, text="PDF 병합", command=merge_pdfs_gui)
merge_button.grid(row=2, column=1)

root.mainloop()
