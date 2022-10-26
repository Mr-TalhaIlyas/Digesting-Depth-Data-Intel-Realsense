#%%

import os
from datetime import datetime

import cv2
import pyrealsense2
from tqdm import trange
import numpy as np
import matplotlib.pyplot as plt
from realsense_depth import DepthCamera
# Get the color map by name:
cm = plt.get_cmap('jet')
dt = datetime.now().strftime("%Y%m%d_%H%M")

out_rgb = cv2.VideoWriter(f'{os.getcwd()}/rgb_{dt}.avi', cv2.VideoWriter_fourcc('M','J','P','G'),
                          30, (640, 480))

out_depth = cv2.VideoWriter(f'{os.getcwd()}/depth_{dt}.avi', cv2.VideoWriter_fourcc('M','J','P','G'),
                          30, (640, 480))

dc = DepthCamera()

while True:

    ret, depth_frame, rgb_frame = dc.get_frame()
    depth_abs = cv2.convertScaleAbs(depth_frame, alpha=0.03)
    depth_cmap = cv2.applyColorMap(depth_abs, cv2.COLORMAP_JET)
    
    out_rgb.write(rgb_frame)
    out_depth.write(depth_cmap)
    
    cv2.imshow('depth_frame', depth_cmap)
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        print('done')
        break

cv2.destroyAllWindows()
dc.release()
out_rgb.release()
out_depth.release()

