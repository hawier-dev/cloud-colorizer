import laspy
import numpy as np
import rasterio as rio
from tqdm import tqdm

from functions import success_message


class LasFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.las_file = laspy.read(file_path)
        self.las_file = laspy.convert(self.las_file, point_format_id=2)

    def colorize_from_image(self, image_path):
        success_message("Starting", "Colorizing point cloud")
        raster = rio.open(image_path)

        coords = np.dstack((self.las_file.x, self.las_file.y))[0]

        r_colors = []
        g_colors = []
        b_colors = []

        with tqdm(total=len(coords)) as pbar:
            for i, point in enumerate(coords):
                for val in raster.sample([(point[0], point[1])]):
                    r_colors.append(val[0])
                    g_colors.append(val[1])
                    b_colors.append(val[2])
                pbar.update(1)

        self.las_file.red = r_colors
        self.las_file.green = g_colors
        self.las_file.blue = b_colors

        success_message("Finished", "Colorizing point cloud")

    def save(self, path):
        self.las_file.write(path)
