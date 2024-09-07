import os
import glob

def remove_txt_files(root_folder):
    # Use glob to find all .txt files in the folder and subfolders
    for txt_file in glob.glob(os.path.join(root_folder, '**', '*.html'), recursive=True):
        try:
            os.remove(txt_file)
            print(f'Removed: {txt_file}')
        except Exception as e:
            print(f'Error removing {txt_file}: {e}')

# Replace 'your_folder_path' with the path to your folder
root_folder = 'novels'
remove_txt_files(root_folder)
