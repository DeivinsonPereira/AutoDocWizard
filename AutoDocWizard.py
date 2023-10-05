from pdf2docx import Converter


def convert_pdf_to_docx(pdf_file, docx_file):
    try:
        # Create a PDF to DOCX conversion object
        cv = Converter(pdf_file)

        # Execute the conversion
        cv.convert(docx_file, start=0, end=None)

        # Close the conversion object
        cv.close()

        print(f'Conversion completed: {pdf_file} -> {docx_file}')
    except Exception as e:
        print(f"An error occurred during the conversion: {e}")


if __name__ == "__main__":
    # Replace 'input.pdf' with the name of your source PDF file.
    pdf_file = 'path.pdf'

    # Replace 'output.docx' with the name of the destination DOCX file.
    docx_file = 'path.docx'

    convert_pdf_to_docx(pdf_file, docx_file)