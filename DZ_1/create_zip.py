import zipfile
import os

def zipdir(path, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(path):
            for file in files:
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, path)
                zipf.write(full_path, relative_path)

zipdir('vfs_folder', 'vfs.zip')
