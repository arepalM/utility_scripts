# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 19:26:18 2022

@author: hokie
"""

import os
import imageio

# Directory containing png files
png_dir = 'pngs'


base = os.getcwd()
path = os.path.join(base,png_dir)
os.chdir(path)

images = []
# Sort all png files based on output times
for file_name in sorted(os.listdir(path)):
    if file_name.endswith('.png'):
        file_path = os.path.join(path, file_name)
        images.append(imageio.imread(file_path))
imageio.mimsave('animation.gif', images)
