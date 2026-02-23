import os, sys
from tkinter import Tk, filedialog
from PyPDF2 import PdfReader
import pandas as pd
from dotenv import load_dotenv
from data_cleaning import *
from pathlib import Path
from chunking import sentence_based_chunking as chunk_this
from summarizer import summarize_text

def file_location():
    file_path = filedialog.askopenfilename(                             #Module of Tk
    title="Select a file",
    filetypes=[
        ("Text files", "*.txt"),
        ("PDF files", "*.pdf")
    ]
    )
    
    if not file_path:
        print("No file selected")
        return None

    return file_path

def read_txt(file_path: str)-> str:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
        

def read_pdf(file_path: str)-> str:
    reader = PdfReader(file_path)
    content = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            content += text

    return content

def main():
    Tk().withdraw()                                                          #GUI window is skipped immediately
    file_path = file_location()
    if file_path is None:
            sys.exit(0)                                                     #sys.exit(0) should be used instead of exit()
    extension = os.path.splitext(file_path)[1].lower()                      #os.path returns -> (file path, extension)


    if extension == ".txt":
        content = read_txt(file_path)

    elif extension == ".pdf":
        content = read_pdf(file_path)

    else:
        content = "Unsupported file type"
        print(content)
        sys.exit(0)


    clean_text = clean(content)
    chunks = chunk_this(clean_text)                                 #chunking completed and stored in chunks

    #next step is tokenization

    chunk_summaries = []

    for chunk in chunks:
        summary = summarize_text(chunk)
        chunk_summaries.append(summary)

    final_summary = " ".join(chunk_summaries)

    print("\nFINAL SUMMARY:\n")
    print(final_summary)


if __name__ == "__main__":
     main()
     
