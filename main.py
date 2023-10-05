import tkinter as tk
from gui import PDFToDOCXConverter

if __name__ == "__main__":
    root = tk.Tk()
    converter = PDFToDOCXConverter(root)
    converter.pack()

    root.mainloop()