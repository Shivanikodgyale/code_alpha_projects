import os
import shutil

# Define the directory to be organized
source_dir = '/path/to/your/folder'
destination_dir = '/path/to/your/organized/folder'

# File type categories
file_categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mkv'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar', '.tar.gz']
}

def organize_files():
    # Check if the destination folder exists, if not, create it
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    # Loop through each file in the source directory
    for filename in os.listdir(source_dir):
        # Get the file extension
        file_ext = os.path.splitext(filename)[1].lower()

        # Identify the category for this file extension
        category_folder = None
        for category, extensions in file_categories.items():
            if file_ext in extensions:
                category_folder = category
                break
        
        # If no category is found, skip the file
        if category_folder:
            # Create the category folder if it doesn't exist
            category_path = os.path.join(destination_dir, category_folder)
            if not os.path.exists(category_path):
                os.makedirs(category_path)
            
            # Move the file to the category folder
            shutil.move(os.path.join(source_dir, filename), os.path.join(category_path, filename))
            print(f"Moved {filename} to {category_folder} folder.")

if _name_ == "_main_":
    organize_files()
    print("File organization completed!")