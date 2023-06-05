import os
import zipfile
from datetime import datetime
import config

def zip_folder(folder_paths, output_path):
    for folder_path in folder_paths:
        total_files = 0
        for root, dirs, files in os.walk(folder_path):
            if os.path.basename(root) in ['Capturas de tela', 'Telegram Desktop']:
                continue
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.basename(file_path).startswith('backup-') and file_path.endswith('.zip'):
                    continue
                total_files += 1

        with zipfile.ZipFile(output_path.format(folder=os.path.basename(folder_path)), 'w', zipfile.ZIP_DEFLATED) as zipf:
            print(f"Creating zip file: {output_path.format(folder=os.path.basename(folder_path))}")
            print(f"Total files to be zipped: {total_files}")
            
            progress_count = 0
            for root, dirs, files in os.walk(folder_path):
                if os.path.basename(root) in config.exceptions:
                    continue
                dirs[:] = [d for d in dirs if not d.startswith('.')]
                for file in files:
                    file_path = os.path.join(root, file)
                    if os.path.basename(file_path).startswith('backup-') and file_path.endswith('.zip'):
                        continue
                    arcname = os.path.join(os.path.basename(folder_path), os.path.relpath(file_path, folder_path))
                    zipf.write(file_path, arcname=arcname)
                    
                    progress_count += 1
                    print(f"Progress: {progress_count}/{total_files} files zipped")
                    print(f"Zipping file: {file_path}")

current_date = datetime.now().strftime('%Y-%m-%d')

folders_to_zip = config.backup_files
output_zip = config.final_zip + current_date + '.zip'

zip_folder(folders_to_zip, output_zip)