import os
import img2pdf

# Replace the directory path with the folder containing JPEG images to be converted
directory_path = "C:/Users/PC/Franken Fran/[SnoopyCool] Vol. 1 Ch. 1"

# List all files in the directory and filter only JPEG images (ending with ".jpg")
image_files = [os.path.join(directory_path, i) for i in os.listdir(directory_path) if i.lower().endswith(".jpg") or i.lower().endswith(".png") ]

# Check if there are any image files
if image_files:
    # Convert the list of JPEG images to a single PDF file
    pdf_bytes = img2pdf.convert(image_files)

    # Write the PDF content to a file (make sure you have write permissions for the specified file)
    with open("output.pdf", "wb") as file:
        file.write(pdf_bytes)
else:
    print("No JPEG files found in the specified directory.")
