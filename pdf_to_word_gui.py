"""
PDF to Word Converter - Modern Light GUI
Install dulu:
    pip install customtkinter pdf2docx
Jalankan:
    python pdf_to_word_gui.py
"""

import os
import threading
import customtkinter as ctk
from tkinter import filedialog, messagebox
from pdf2docx import Converter

# ---------- Konfigurasi tema ----------
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

ACCENT = "#4F6EF7"
ACCENT_HOVER = "#3C58D9"
BG = "#F7F8FC"
CARD = "#FFFFFF"
TEXT_MAIN = "#1F2333"
TEXT_SUB = "#8A8FA3"
SUCCESS = "#22C55E"
BORDER = "#E7E9F3"


class PDFToWordApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PDF to Word Converter")
        self.geometry("560x480")
        self.minsize(480, 440)
        self.configure(fg_color=BG)

        self.pdf_path = None
        self.output_path = None

        self._build_ui()

    # ---------------------------------------------------------------
    def _build_ui(self):
        # ===== Header =====
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", padx=32, pady=(28, 8))

        ctk.CTkLabel(
            header, text="PDF → Word",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=TEXT_MAIN
        ).pack(anchor="w")

        ctk.CTkLabel(
            header, text="Konversi file PDF menjadi dokumen Word (.docx)",
            font=ctk.CTkFont(size=13),
            text_color=TEXT_SUB
        ).pack(anchor="w", pady=(2, 0))

        # ===== Card: Drop / Pilih File =====
        self.card = ctk.CTkFrame(
            self, fg_color=CARD, corner_radius=16,
            border_width=1, border_color=BORDER
        )
        self.card.pack(fill="x", padx=32, pady=16)

        self.file_icon = ctk.CTkLabel(
            self.card, text="📄", font=ctk.CTkFont(size=34)
        )
        self.file_icon.pack(pady=(28, 6))

        self.file_label = ctk.CTkLabel(
            self.card, text="Belum ada file dipilih",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=TEXT_MAIN
        )
        self.file_label.pack()

        self.file_sub = ctk.CTkLabel(
            self.card, text="Klik tombol di bawah untuk memilih file PDF",
            font=ctk.CTkFont(size=12),
            text_color=TEXT_SUB
        )
        self.file_sub.pack(pady=(2, 18))

        self.choose_btn = ctk.CTkButton(
            self.card, text="Pilih File PDF",
            command=self.choose_file,
            fg_color=ACCENT, hover_color=ACCENT_HOVER,
            corner_radius=10, height=40, width=180,
            font=ctk.CTkFont(size=13, weight="bold")
        )
        self.choose_btn.pack(pady=(0, 26))

        # ===== Progress bar =====
        self.progress = ctk.CTkProgressBar(
            self, height=8, corner_radius=6,
            fg_color="#E7E9F3", progress_color=ACCENT
        )
        self.progress.set(0)
        self.progress.pack(fill="x", padx=32, pady=(4, 4))

        self.status_label = ctk.CTkLabel(
            self, text="Menunggu file...",
            font=ctk.CTkFont(size=12), text_color=TEXT_SUB
        )
        self.status_label.pack(anchor="w", padx=33, pady=(0, 12))

        # ===== Convert Button =====
        self.convert_btn = ctk.CTkButton(
            self, text="Convert ke Word",
            command=self.start_conversion,
            fg_color=SUCCESS, hover_color="#16A34A",
            corner_radius=10, height=46,
            font=ctk.CTkFont(size=14, weight="bold"),
            state="disabled"
        )
        self.convert_btn.pack(fill="x", padx=32, pady=(4, 8))

        # ===== Footer =====
        ctk.CTkLabel(
            self, text="Didukung oleh pdf2docx",
            font=ctk.CTkFont(size=11), text_color=TEXT_SUB
        ).pack(pady=(4, 10))

    # ---------------------------------------------------------------
    def choose_file(self):
        path = filedialog.askopenfilename(
            title="Pilih file PDF",
            filetypes=[("PDF files", "*.pdf")]
        )
        if not path:
            return

        self.pdf_path = path
        filename = os.path.basename(path)
        size_kb = os.path.getsize(path) / 1024
        size_str = f"{size_kb:.0f} KB" if size_kb < 1024 else f"{size_kb/1024:.1f} MB"

        self.file_icon.configure(text="✅")
        self.file_label.configure(text=filename)
        self.file_sub.configure(text=f"{size_str} • siap dikonversi")
        self.convert_btn.configure(state="normal")
        self.status_label.configure(text="File siap dikonversi.")
        self.progress.set(0)

    # ---------------------------------------------------------------
    def start_conversion(self):
        if not self.pdf_path:
            return

        self.output_path = os.path.splitext(self.pdf_path)[0] + ".docx"
        self.convert_btn.configure(state="disabled", text="Mengonversi...")
        self.choose_btn.configure(state="disabled")
        self.status_label.configure(text="Sedang mengonversi, mohon tunggu...")
        self.progress.configure(mode="indeterminate")
        self.progress.start()

        thread = threading.Thread(target=self._convert_worker, daemon=True)
        thread.start()

    def _convert_worker(self):
        try:
            cv = Converter(self.pdf_path)
            cv.convert(self.output_path)
            cv.close()
            self.after(0, self._on_success)
        except Exception as e:
            self.after(0, lambda: self._on_error(str(e)))

    def _on_success(self):
        self.progress.stop()
        self.progress.configure(mode="determinate")
        self.progress.set(1)
        self.status_label.configure(
            text=f"Selesai! Tersimpan di: {self.output_path}",
            text_color=SUCCESS
        )
        self.convert_btn.configure(state="normal", text="Convert ke Word")
        self.choose_btn.configure(state="normal")

        messagebox.showinfo(
            "Konversi Selesai",
            f"File berhasil dikonversi:\n{self.output_path}"
        )

    def _on_error(self, error_msg):
        self.progress.stop()
        self.progress.configure(mode="determinate")
        self.progress.set(0)
        self.status_label.configure(text="Gagal mengonversi file.", text_color="#EF4444")
        self.convert_btn.configure(state="normal", text="Convert ke Word")
        self.choose_btn.configure(state="normal")

        messagebox.showerror("Error", f"Terjadi kesalahan:\n{error_msg}")


if __name__ == "__main__":
    app = PDFToWordApp()
    app.mainloop()
