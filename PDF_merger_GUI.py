import os
from PyPDF2 import PdfMerger
import tkinter as tk
from tkinter import filedialog

def merge_pdfs(pdf_dir, result_dir):
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
    result_path = os.path.join(result_dir, "완성-_-b.pdf")
    with open(result_path, "wb") as output:
        pdf_merger.write(output)

# GUI 생성
root = tk.Tk()
root.title("PDF 파일 병합 프로그램")
root.geometry("300x250")

def select_pdf_dir():
    pdf_dir = filedialog.askdirectory()
    pdf_entry.delete(0, tk.END)
    pdf_entry.insert(0, pdf_dir)

def select_result_dir():
    result_dir = filedialog.askdirectory()
    result_entry.delete(0, tk.END)
    result_entry.insert(0, result_dir)

# PDF 폴더 경로 선택 버튼 추가
pdf_label = tk.Label(root, text="병합할 PDF 폴더:")
pdf_label.pack(pady=10)
pdf_entry = tk.Entry(root)
pdf_entry.pack()
pdf_button = tk.Button(root, text="폴더 선택", command=select_pdf_dir)
pdf_button.pack()

# 결과 파일 경로 선택 버튼 추가
result_label = tk.Label(root, text="결과 파일 경로:")
result_label.pack(pady=10)
result_entry = tk.Entry(root)
result_entry.pack()
result_button = tk.Button(root, text="폴더 선택", command=select_result_dir)
result_button.pack()

def button_click():
    pdf_dir = pdf_entry.get()
    result_dir = result_entry.get()
    if not pdf_dir or not result_dir:
        return
    merge_pdfs(pdf_dir, result_dir)
    
# 실행 버튼 추가
button = tk.Button(root, text="실행", command=button_click, width=13, height=3)
button.pack(pady=25)

root.mainloop()
