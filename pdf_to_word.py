"""
Convert PDF ke Word (.docx)
Install dulu library-nya: pip install pdf2docx
"""

from pdf2docx import Converter
import sys
import os


def pdf_to_word(pdf_path: str, docx_path: str = None, start_page: int = 0, end_page: int = None):
    """
    Convert file PDF menjadi file Word (.docx)

    Parameters:
        pdf_path   : path file PDF sumber
        docx_path  : path file Word tujuan (opsional, default nama sama dgn PDF)
        start_page : halaman awal (index mulai dari 0)
        end_page   : halaman akhir (None = sampai halaman terakhir)
    """
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(f"File tidak ditemukan: {pdf_path}")

    if docx_path is None:
        docx_path = os.path.splitext(pdf_path)[0] + ".docx"

    print(f"Mengonversi: {pdf_path} -> {docx_path}")

    cv = Converter(pdf_path)
    cv.convert(docx_path, start=start_page, end=end_page)
    cv.close()

    print("Selesai! File Word tersimpan di:", docx_path)
    return docx_path


if __name__ == "__main__":
    # Cara pakai lewat command line:
    # python pdf_to_word.py input.pdf [output.docx]

    if len(sys.argv) < 2:
        print("Cara pakai: python pdf_to_word.py <file.pdf> [output.docx]")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_docx = sys.argv[2] if len(sys.argv) > 2 else None

    pdf_to_word(input_pdf, output_docx)
