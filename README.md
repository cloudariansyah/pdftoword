# PDF to Word Converter

Aplikasi sederhana untuk mengonversi file PDF menjadi dokumen Word (`.docx`), tersedia dalam dua versi:

- **CLI** (`pdf_to_word.py`) — dijalankan lewat terminal/command line.
- **GUI** (`pdf_to_word_gui.py`) — antarmuka modern light UI berbasis `customtkinter`.

Konversi menggunakan library [`pdf2docx`](https://github.com/dothinking/pdf2docx), yang menjaga layout, tabel, dan gambar seakurat mungkin.

---

## 📁 Isi Project

```
.
├── pdf_to_word.py        # Versi command line (CLI)
├── pdf_to_word_gui.py    # Versi GUI (modern light theme)
├── requirements.txt      # Daftar dependensi
└── README.md
```

---

## ⚙️ Instalasi

Pastikan Python sudah terpasang (disarankan Python 3.9 ke atas).

1. (Opsional tapi disarankan) buat virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate      # Mac/Linux
   venv\Scripts\activate         # Windows
   ```

2. Install semua dependensi:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Cara Menjalankan

### Versi GUI (disarankan)

```bash
python pdf_to_word_gui.py
```

Langkah di aplikasi:
1. Klik **"Pilih File PDF"**, lalu pilih file yang ingin dikonversi.
2. Klik **"Convert ke Word"**.
3. Tunggu proses selesai — file `.docx` akan otomatis tersimpan di folder yang sama dengan file PDF sumber, dengan nama yang sama.

### Versi CLI

```bash
python pdf_to_word.py <file.pdf> [output.docx]
```

Contoh:

```bash
python pdf_to_word.py dokumen.pdf
python pdf_to_word.py dokumen.pdf hasil_konversi.docx
```

Bisa juga dipakai sebagai modul di script Python lain:

```python
from pdf_to_word import pdf_to_word
pdf_to_word("dokumen.pdf", "hasil.docx")
```

---

## 🧩 Dependensi

| Package        | Kegunaan                                  |
|----------------|--------------------------------------------|
| `pdf2docx`     | Mesin konversi PDF ke Word                 |
| `customtkinter`| Komponen UI modern untuk versi GUI         |

Isi lengkap ada di [`requirements.txt`](./requirements.txt).

---

## ⚠️ Catatan & Batasan

- PDF hasil **scan/gambar** (bukan teks asli) akan dikonversi apa adanya sebagai gambar, karena `pdf2docx` tidak melakukan OCR. Untuk kasus ini dibutuhkan pendekatan tambahan (misalnya `pytesseract`).
- Layout PDF yang sangat kompleks (multi-kolom, elemen grafis rumit) berpotensi tidak 100% identik setelah dikonversi ke Word.
- Versi GUI menjalankan proses konversi di thread terpisah agar aplikasi tidak freeze, namun tetap membutuhkan waktu tergantung ukuran file.

---

## 🛠️ Rencana Pengembangan (opsional)

- [ ] Drag & drop file PDF langsung ke jendela aplikasi
- [ ] Pilih folder output custom
- [ ] Mode batch (convert banyak file sekaligus)
- [ ] Dukungan OCR untuk PDF hasil scan

---

## 📄 Lisensi

Bebas digunakan dan dimodifikasi untuk kebutuhan pribadi maupun proyek internal.
