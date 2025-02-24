import os
import shutil

def extract_pdfs(source_dir, target_dir):
    # Walk through the source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".pdf"):
                # Construct the full file path
                full_file_path = os.path.join(root, file)
                # Construct the relative path to preserve the structure
                relative_path = os.path.relpath(root, source_dir)
                # Create the target directory structure
                target_path = os.path.join(target_dir, relative_path)
                os.makedirs(target_path, exist_ok=True)
                # Copy the PDF file to the target directory
                shutil.copy(full_file_path, target_path)
                print(f"Copied {file} to {target_path}")

# Define the source and target directories
source_directory = r"C:\Users\panag\OneDrive\Documents\teaching\2024-2025\Instruments TP\ParJ302"  # Replace with your  source directory
target_directory = r"C:\Users\panag\OneDrive\Documents\teaching\2024-2025\Instruments TP\extracted_pdfs"  # Replace with your desired target directory

# Ensure the target directory exists
os.makedirs(target_directory, exist_ok=True)

# Extract PDFs
# This will print a bunch of lines. Do not panic.
extract_pdfs(source_directory, target_directory)

print("PDF extraction complete.")