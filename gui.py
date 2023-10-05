import tkinter as tk
from tkinter import filedialog
from AutoDocWizard import convert_pdf_to_docx
from tkinter import ttk


class PDFToDOCXConverter(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.pdf_file_entry = tk.Entry(self)
        self.docx_file_entry = tk.Entry(self)
        self.pdf_file_button = tk.Button(self, text="Anexar PDF", command=self.browse_pdf_file, bg="blue", fg="white", font=("Helvetica", 12, "bold"))
        self.convert_button = tk.Button(self, text="Converter", command=self.convert, bg="green", fg="white", font=("Helvetica", 12, "bold"))

        self.pdf_file_entry.pack()
        self.docx_file_entry.pack()
        self.pdf_file_button.pack()
        self.convert_button.pack()

    def browse_pdf_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        self.pdf_file_entry.delete(0, tk.END)
        self.pdf_file_entry.insert(0, file_path)

    def convert(self):
        pdf_file = self.pdf_file_entry.get()
        docx_file = self.docx_file_entry.get()

        convert_pdf_to_docx(pdf_file, docx_file)

if __name__ == "__main__":
    root = tk.Tk()
    converter = PDFToDOCXConverter(root)
    converter.pack()

    root.mainloop()