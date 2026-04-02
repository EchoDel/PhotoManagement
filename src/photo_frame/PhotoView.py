"""


Built based on the pong example, https://kivy.org/doc/stable/tutorials/pong.html,
and the image display example of https://stackoverflow.com/questions/23651781/how-to-display-an-image-using-kivy
"""


import random
from pathlib import Path
from typing import Dict

from kivy.clock import Clock
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

from pillow_heif import register_heif_opener

from photo_frame.config_management import setup_program_config_file, get_program_config, load_photo_config, \
    ProgramConfig, choose_folder, get_root_folder

config_path = Path('local_config.json')

register_heif_opener()


class Picture(Widget):
    '''Picture is the class that will show the image with a white border and a
    shadow. They are nothing here because almost everything is inside the
    picture.kv. Check the rule named <Picture> inside the file, and you'll see
    how the Picture() is really constructed and used.

    The source property will be the filename to show.
    '''
    source = StringProperty(None)


class PhotoView(BoxLayout):
    image = ObjectProperty(None)

    def __init__(self, config_path: Path = config_path, *kwargs):
        super().__init__()

        Clock.schedule_once(self.starter_photo)

        setup_program_config_file()
        self.program_config = get_program_config(config_path)
        self.photos_config = load_photo_config(self.program_config)

        self.current_photo = None
        self.current_folder = None
        self.seen_pictures = []

    def starter_photo(self, dt):
        # Replace the given image source value:

        picture = Picture(source='/media/echo/Games1/TestPicture/2024 Jonny BBQ/3d5f3615-2b9f-4d4e-b817-ba21a8b3738d.jpg')
        # picture.Image.size = (Window.width, Window.height)  # Set size to full window dimensions
        picture.children[0].size = (Window.width, Window.height)
        self.add_widget(picture)
        # self.ids.imageView.source = '/media/echo/Games1/TestPicture/2024 Jonny BBQ/3d5f3615-2b9f-4d4e-b817-ba21a8b3738d.jpg'

    def sample_photo(self, dt):
        if self.program_config['sampling_strategy'] == 'folder':
            file_to_display = self.sample_config_maintain_folder(self.photos_config, self.program_config)
        else:
            file_to_display = self.sample_config_random(self.photos_config)

        if file_to_display.suffix.lower() == '.cr2':
            pass
            # todo load image with pillow then pass to kivy, https://stackoverflow.com/questions/51806100/display-pil-image-on-kivy-canvas#52340135
        elif file_to_display.suffix.lower() == '.mp4':
            pass
        else:
            self.display_photo(str(file_to_display))

    def display_photo(self, file_to_display: str):
        self.clear_widgets()
        picture = Picture(source=file_to_display)
        picture.children[0].size = (Window.width, Window.height)
        self.add_widget(picture)

    def sample_config_random(self, photos_config: Dict[Path, float]) -> Path:
        config = {key: random.random() * value for key, value in photos_config.items()}
        return max(config, key=config.get)

    def sample_config_maintain_folder(self, config_dict: dict, program_config: ProgramConfig, new_folder: bool = False):
        if self.current_folder is None or random.random() < 0.05 or new_folder:
            self.current_folder = choose_folder(config_dict, program_config['folder_sampling_level'])
            self.seen_pictures = []

        images_to_pick_from = {key: value for key, value in config_dict.items()
                               if get_root_folder(key, program_config[
                'folder_sampling_level']) == self.current_folder and key not in self.seen_pictures}
        if len(images_to_pick_from) == 0:
            image = self.sample_config_maintain_folder(config_dict, program_config, True)
        else:
            image = self.sample_config_random(images_to_pick_from)
        self.seen_pictures.append(image)
        return image
