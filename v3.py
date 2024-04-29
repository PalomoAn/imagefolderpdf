import os
import img2pdf

def clean_folder_name(folder_name):
    # Remove square brackets
    cleaned_name = folder_name.replace("[", "").replace("]", "")
    
    # Replace specific strings
    cleaned_name = cleaned_name.replace("", "").replace("", "")
    
    return cleaned_name

def convert_images_to_pdf(directory_path):
    # Extract the folder name from the directory path
    folder_name = os.path.basename(directory_path)
    
    # Clean the folder name
    cleaned_folder_name = clean_folder_name(folder_name)
    
    # List all files in the directory and filter only JPEG and PNG images
    image_files = [os.path.join(directory_path, i) for i in os.listdir(directory_path) 
                   if i.lower().endswith(".jpg") or i.lower().endswith(".png")]

    # Check if there are any image files
    if image_files:
        # Convert the list of JPEG and PNG images to a single PDF file
        pdf_bytes = img2pdf.convert(image_files)

        # Write the PDF content to a file
        with open(f"{cleaned_folder_name}.pdf", "wb") as file:
            file.write(pdf_bytes)
            
        print(f"PDF created: {cleaned_folder_name}.pdf")
    else:
        print(f"No JPEG or PNG files found in the folder: {cleaned_folder_name}")

def convert_subfolders_to_pdf(main_directory):
    # Iterate through each subfolder in the main directory
    for subdir in os.listdir(main_directory):
        subfolder_path = os.path.join(main_directory, subdir)
        # Check if the item in the main directory is a subfolder
        if os.path.isdir(subfolder_path):
            # Call the function to convert images to PDF for the subfolder
            convert_images_to_pdf(subfolder_path)

# Replace the main directory path with the folder containing subfolders with images
main_directory_path = "C:/Users/PC/Folder"

# Call the function to convert each subfolder's images to PDF
convert_subfolders_to_pdf(main_directory_path)
