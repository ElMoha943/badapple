# get pixels from image

from PIL import Image
import numpy as np
import cv2
import time
import os
from os.path import exists

def get_pixels(image_path):
    im = Image.open(image_path)
    im = im.convert('L')
    im = im.resize((80, 45))
    pixels = np.array(im)
    return pixels

def get_ascii(pixels):
    ascii_chars = " .,:;irsXA253hMHGS#9B&@"
    ascii_pixels = []
    for row in pixels:
        ascii_row = []
        for pixel in row:
            ascii_row.append(ascii_chars[pixel // 25])
        ascii_pixels.append(ascii_row)
    return ascii_pixels

def print_ascii(ascii_pixels):
    for row in ascii_pixels:
        print(''.join(row))

# get frame from video
def getFrames(path):
    frames = []
    cap = cv2.VideoCapture(path)
    current_frame = 0
    # get frame every 10 frames until end of video
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frames.append(f"frameIn/frame{current_frame}.jpg")
            if(not exists(f"frameIn/frame{current_frame}.jpg")):
                cv2.imwrite(f"frameIn/frame{current_frame}.jpg", frame)
            current_frame += 1
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

# get frames from frameIn folder


getFrames("badapple.mp4")

for i in range(len(os.listdir('frameIn/'))):
    print_ascii(get_ascii(get_pixels(f"frameIn/frame{i}.jpg")))
    # 24 fps
    time.sleep(1/24)
    #clear screen
    print("\033[H\033[J")