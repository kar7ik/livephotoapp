import numpy as np
import cv2
import pyautogui
from datetime import datetime
import glob
import imageio
import os

DIR = "/home/kar7ik/livephotoapp/livephotoapp/live-photos/live-photos_"

livephoto = []

curr_time = str(datetime.now())
dirr = DIR+curr_time
# creating new directory everytime with timestamp to retain raw images
if not os.path.exists(dirr):
    os.mkdir(dirr)

for x in range(15):
    image = pyautogui.screenshot()

# convert RGB it to numpy array and BGR
# write it to the disk

    image = cv2.cvtColor(np.array(image),
                         cv2.COLOR_RGB2BGR)

# writing it to the disk using opencv
    cv2.imwrite(DIR+curr_time+"/IMG_" +
                str(datetime.now())+".png", image)

livephoto = glob.glob(
    DIR+curr_time+"/*.png")


images = []
for photo in livephoto:
    images.append(imageio.imread(photo))
imageio.mimsave(
    '/home/kar7ik/livephotoapp/livephotoapp/live-photo-gif/livephoto_' +
    str(datetime.now())+'.gif', images, duration=0.25)


print("Done")
