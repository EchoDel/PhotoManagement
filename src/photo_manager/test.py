import json
from pathlib import Path
from typing import List
from shutil import move

from tqdm import tqdm


input_folder = Path('C:/Users/red_p/Documents/PicturesToSort')
output_folders = Path('//rhino/photos/photos')
deleted_files_metadata_location = Path('//rhino/photos/deleted_files_metadata.json')

input_files = [x.name for x in input_folder.glob('*.*')]
current_files = [x.name for x in tqdm(output_folders.glob('**/*.*'))]

if deleted_files_metadata_location.exists():
    with open(deleted_files_metadata_location, 'r') as file:
        deleted_files_metadata = json.load(file)
else:
    deleted_files_metadata = []


already_uploaded = [x for x in input_files if x in current_files]
already_deleted = [x for x in input_files if x in deleted_files_metadata]
to_sort = [x for x in input_files if (x not in current_files) & (x not in deleted_files_metadata)]


def move_images(input_folder: Path, files_to_move: List[str], folder_name: str):
    output_folder = input_folder / folder_name
    output_folder.mkdir(parents=True, exist_ok=True)
    for x in files_to_move:
        move(input_folder / x, output_folder / x)


move_images(input_folder, already_uploaded, folder_name='already_uploaded')
move_images(input_folder, already_deleted, folder_name='already_deleted')
move_images(input_folder, to_sort, folder_name='to_sort')


# find the files which are no longer in the to sort folder then append to the deleted and save to the output folder
input_file_metadata = input_folder / 'metadata.json'
with open(input_file_metadata, 'w') as file:
    json.dump(input_files, file)


new_current_files = [x.name for x in tqdm(output_folders.glob('**/*.*'))]
still_to_be_sorted = [x.name for x in (input_folder / 'to_sort').glob('*.*')]

newly_deleted_files = [x for x in input_files if (x not in new_current_files) & (x not in still_to_be_sorted)]

deleted_files_metadata += newly_deleted_files

with open(deleted_files_metadata_location, 'w') as file:
    json.dump(deleted_files_metadata, file)
