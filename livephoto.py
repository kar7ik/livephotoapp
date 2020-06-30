import numpy as np
import cv2
import pyautogui
from datetime import datetime
import glob
import imageio


livephoto = []


for x in range(5):
    image = pyautogui.screenshot()

# convert RGB it to numpy array and BGR
# so we can write it to the disk

    image = cv2.cvtColor(np.array(image),
                         cv2.COLOR_RGB2BGR)

# writing it to the disk using opencv
    cv2.imwrite("/home/kar7ik/livephotoapp/livephotoapp/live-photos/IMG_" +
                str(datetime.now())+".png", image)

livephoto = glob.glob(
    "/home/kar7ik/livephotoapp/livephotoapp/live-photos/*.png")


images = []
for photo in livephoto:
    images.append(imageio.imread(photo))
imageio.mimsave(
    '/home/kar7ik/livephotoapp/livephotoapp/live-photo-gif/livephoto.gif', images,duration=5)
