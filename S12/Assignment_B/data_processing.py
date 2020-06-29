import os
import math

import pandas as pd
import numpy as np

from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class AnnotatedData(object):
    def __init__(self):
        self.annotated_data = None
        self.image_data = {}
        self.annotated_df_proccesed = pd.DataFrame()

    def load(self, json_path):
        with open(json_path) as f:
            self.annotated_data = eval(f.read())
        return self.annotated_data

    def process_images(self, image_path):
        for filename in os.listdir(image_path):
            im = Image.open(os.path.join(image_path, filename))
            width, height = im.size
            self.image_data.update({filename:{"height":height, "width":width}})

    def process_data(self, annotated_data):
        data = []
        for key, img_data in annotated_data.items():
            temp_dict = {}
            for img_attr in img_data['regions']:
                temp_dict = {'name': img_data['filename'] }

                img_shape_attr = img_attr['shape_attributes']
                temp_dict['bbox_height'] = img_shape_attr['height']
                temp_dict['bbox_width'] = img_shape_attr['width']
                temp_dict['bbox_x'] = img_shape_attr['x']
                temp_dict['bbox_y'] = img_shape_attr['y']

                img_data_dict = self.image_data[img_data['filename']]
                temp_dict['img_height'] = img_data_dict["height"]
                temp_dict['img_width'] = img_data_dict["width"]
                
                temp_dict['bbox_rel_height'] = img_shape_attr['height']/temp_dict['img_height']
                temp_dict['bbox_rel_width'] = img_shape_attr['width']/temp_dict['img_width']
                temp_dict['bbox_rel_log_height'] = math.log(temp_dict['bbox_rel_height'])
                temp_dict['bbox_rel_log_width'] = math.log(temp_dict['bbox_rel_width'])
            data.append(temp_dict)
        
        self.annotated_df_proccesed = pd.DataFrame.from_dict(data, orient='columns')
        return self.annotated_df_proccesed

    def plot_scatter(self, log_values=False):
        if log_values:
            self.annotated_df_proccesed.plot.scatter('bbox_rel_log_width', 'bbox_rel_log_height')
        else:
            self.annotated_df_proccesed.plot.scatter('bbox_rel_width', 'bbox_rel_height')

    def plot_images(self, image_path, annotated_data, num_of_images=5):
        # Create figure and axes
        fig, axs = plt.subplots(1, ncols=num_of_images, figsize=(10,10))

        for i, ax in enumerate(axs.flat):
            im = np.array(Image.open(os.path.join(image_path, annotated_data.iloc[i]['name'])))

            # Display the image
            ax.imshow(im)

            # Create a Rectangle patch
            rect = patches.Rectangle((annotated_data.iloc[i]['bbox_x'], annotated_data.iloc[i]['bbox_y']), 
                                    annotated_data.iloc[i]['bbox_width'], annotated_data.iloc[i]['bbox_height'],
                                    linewidth=3 ,edgecolor='r', facecolor='none')

            # Add the patch to the Axes
            ax.add_patch(rect)

        plt.axis('off')
        plt.show()