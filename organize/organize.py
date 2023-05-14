#####################################################################
### SIMPLE RENAME ###################################################
#####################################################################

# from pathlib import Path

# root_dir = Path('files')
# file_paths = root_dir.iterdir()

# for path in file_paths:
#     new_filename = 'new-' + path.stem + path.suffix
#     new_filepath = path.with_name(new_filename)
#     print(new_filepath)
#     path.rename(new_filepath)








#####################################################################
### NESTED FOLDER FILES RENAME ######################################
#####################################################################

# from pathlib import Path

# root_dir = Path('files')
# file_paths = root_dir.glob('**/*')

# for path in file_paths:
#     if path.is_file():
#         parent_folder = path.parts[-2]
#         grandparent_folder = path.parts[-3]
#         new_filename = grandparent_folder + '-' + parent_folder + '-' + path.name
#         new_filepath = path.with_name(new_filename)
#         path.rename(new_filepath) 





#####################################################################
### RENAME WITH DATE ################################################
#####################################################################

# from pathlib import Path
# from datetime import datetime

# root_dir = Path('files')
# file_paths = root_dir.glob('**/*')

# for path in file_paths:
#     if path.is_file():
#         stats = path.stat()
#         second_created = stats.st_ctime
#         date_created = datetime.fromtimestamp(second_created)
#         date_created_str = date_created.strftime('%Y-%m-%d__%H-%M-%S')

#         new_filename = date_created_str + '__' + path.name
#         new_filepath = path.with_name(new_filename)
#         path.rename(new_filepath) 



#####################################################################
### CREATE ZIP FILE #################################################
#####################################################################
# from pathlib import Path
# import zipfile

# root_dir = Path('files')
# archive_path = root_dir / Path('archive.zip')

# with zipfile.ZipFile(archive_path, 'w') as zf:
#     for path in root_dir.rglob('*.txt'):
#         zf.write(path)
#         # path.unlink() 


#####################################################################
### EXTRACT ZIP FILE ################################################
#####################################################################
# from pathlib import Path
# import zipfile

# root_dir = Path('.')
# destination_path = Path('destination')

# for path in root_dir.glob('*.zip'):
#     with zipfile.ZipFile(path, 'r') as zf:
#         final_path = destination_path / Path(path.stem)
#         zf.extractall(path=final_path)



#####################################################################
### SEARCH FOR FILES ################################################
#####################################################################
# from pathlib import Path

# root_dir = Path('destination')
# search_term = '14'

# for path in root_dir.rglob('*'):
#     if path.is_file():
#         if search_term in path.stem:
#             print(path.absolute())
            


#####################################################################
### DESTROY PERMANENTLY FILES #######################################
#####################################################################
# from pathlib import Path

# root_dir = Path('destination')

# for path in root_dir.glob('*.txt'):
#     with open(path, 'wb') as f:
#         f.write(b'')
#     path.unlink()


#####################################################################
### MOVE FILES ######################################################
#####################################################################
import os
import shutil
from pathlib import Path

destination_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

input_paths = [
    os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'),
    str(Path.home() / "Downloads")
]

image_suffixes = ['.jpg', '.png', '.psd'] 
book_suffixes = ['.pdf', '.epub']
audio_suffixes = ['.m4a']
torrent_suffixes = ['.torrent']
archive_suffixes = ['.zip']


for input_path in input_paths:
    for f in os.listdir(input_path):
        for suffix in image_suffixes:
            if f.endswith(suffix):
                shutil.move(f'{input_path}/{f}', f'{destination_path}/images/{f}')
        for suffix in book_suffixes:
            if f.endswith(suffix):
                shutil.move(f'{input_path}/{f}', f'{destination_path}/books/{f}')
        for suffix in audio_suffixes:
            if f.endswith(suffix):
                shutil.move(f'{input_path}/{f}', f'{destination_path}/audios/{f}')
        for suffix in torrent_suffixes:
            if f.endswith(suffix):
                shutil.move(f'{input_path}/{f}', f'{destination_path}/torrents/{f}')
        for suffix in archive_suffixes:
            if f.endswith(suffix):
                shutil.move(f'{input_path}/{f}', f'{destination_path}/archives/{f}')
