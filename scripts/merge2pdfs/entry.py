import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def merge_pdfs(pdf1_path, pdf2_path, output_path):
    try:
        import PyPDF2
    except ImportError:
        install("PyPDF2")
        import PyPDF2

    # Open the first PDF
    pdf1 = open(pdf1_path, 'rb')
    pdf1_reader = PyPDF2.PdfReader(pdf1)
    
    # Open the second PDF
    pdf2 = open(pdf2_path, 'rb')
    pdf2_reader = PyPDF2.PdfReader(pdf2)
    
    # Create a new PDF writer object
    pdf_writer = PyPDF2.PdfWriter()
    
    # Add all pages of the first PDF
    for page_num in range(len(pdf1_reader.pages)):
        page = pdf1_reader.pages[page_num]
        pdf_writer.add_page(page)
    
    # Add all pages of the second PDF
    for page_num in range(len(pdf2_reader.pages)):
        page = pdf2_reader.pages[page_num]
        pdf_writer.add_page(page)
    
    # Write the combined PDF to a new file
    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)
    
    # Close the input PDF files
    pdf1.close()
    pdf2.close()

# Example usage:
if len(sys.argv) == 5:
    pdf1_path = sys.argv[2]
    pdf2_path = sys.argv[3]
    output_path = sys.argv[4]
    merge_pdfs(pdf1_path, pdf2_path, output_path)
else:
    print("requires 3 params: pdf1_path, pdf2_path, output_path")
    