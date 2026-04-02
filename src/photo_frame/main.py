import logging
from pathlib import Path

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.video import Video

from photo_frame.PhotoView import PhotoView

config_path = Path('local_config.json')
logger = logging.getLogger(__name__)

class PhotoViewerApp(App):
    def build(self):
        game = PhotoView()
        Clock.schedule_interval(game.sample_photo, 1)
        return game
#
# class MyApp(App):
#     def build(self):
#         return Video(source='/media/echo/Games1/TestPicture/2024_Arthur/VID_20240913_174338.mp4')
#
#
# class MyApp(App):
#     def build(self):
#         return Video(source='/media/echo/Games1/TestPicture/2024_Arthur/IMG_1445.mov')
#
#

def main(config_path: Path = config_path):
    # from photo_frame.UI import convert_to_bytes, G_SIZE, graph, window
    #
    # logging.basicConfig(filename='photo_frame.log', level=logging.INFO)
    #
    # # Read the photos to display
    # setup_program_config_file()
    # program_config = (
    #     get_program_config(config_path))
    # photos_config = load_photo_config(program_config)
    #
    # previous_image = ""
    # keep_going = True
    # while keep_going:
    #     if program_config['sampling_strategy'] == 'folder':
    #         file_to_display = sample_config_maintain_folder(photos_config, program_config)
    #     else:
    #         file_to_display = sample_config_random(photos_config)
    #
    #     logger.info(f"{datetime.datetime.now()}, {file_to_display}")
    #     if not previous_image == file_to_display:
    #         try:
    #             img_data, img_width, img_height = convert_to_bytes(str(file_to_display), resize=G_SIZE)
    #
    #             if 'image_id' in locals():
    #                 graph.delete_figure(image_id)
    #
    #             image_id = graph.draw_image(data=img_data,
    #                                         location=((G_SIZE[0] - img_width) / 2,
    #                                                   G_SIZE[1]))
    #             previous_image = file_to_display
    #         except Exception as E:
    #             print(E)
    #             photos_config[file_to_display] = 0
    #             save_config_file(program_config['photos_config'], photos_config)
    #             continue
    #
    #     for x in range(program_config['seconds_to_show'] * 10):
    #         event, values = window.read(timeout=100)
    #         if event in (sg.WINDOW_CLOSED, "-ESCAPE-"):
    #             keep_going = False
    #             break
    #
    # window.close()
    PhotoViewerApp().run()


if __name__ == "__main__":
    # photos_config = {key: value for key, value in photos_config.items() if '2019_Bristol' in str(key)}
    main()
