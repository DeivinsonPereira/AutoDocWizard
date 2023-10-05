import tkinter as tk
from gui import PDFToDOCXConverter

if __name__ == "__main__":
    root = tk.Tk()
    converter = PDFToDOCXConverter(root)
    converter.pack()
    root.iconbitmap("icon.ico")  # Substitua "icon.ico" pelo nome do seu arquivo de ícone
    root.title("AutoDocWizard")

    root.mainloop()