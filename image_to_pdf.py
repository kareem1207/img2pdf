import img2pdf
import os

img_folder = input("Enter the path of the folder containing images: ")  
output_pdf = input("Enter the path of the output PDF file with the pdf name at the end: ")

img_folder=img_folder.replace("\\","/")
output_pdf=output_pdf.replace("\\","/")

if os.path.isdir(output_pdf):
    raise ValueError("The output path must be a file, not a directory.")

os.makedirs(os.path.dirname(output_pdf), exist_ok=True)

image_files = [
    os.path.join(img_folder, file)
    for file in os.listdir(img_folder)
    if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'tiff','svg'))
]

if not image_files:
    print("No valid image files found in the folder.")
else:
    with open(output_pdf, "wb") as pdf_file:
        pdf_file.write(img2pdf.convert(image_files))
    print(f"Successfully created PDF: {output_pdf}")
