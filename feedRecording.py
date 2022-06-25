import os, sys
import socket
from imutils import build_montages
from datetime import datetime
import numpy as np
import imagezmq
import argparse, imutils, cv2
from matplotlib import pyplot as plt

# frame_dim = [width, hight]
frame_dim = [1280, 1024]

imageHub = imagezmq.ImageHub(open_port='tcp://*:8081')

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


def main():
    s.bind(('', '8081'))
    print('Socket bind complete')
    s.listen(10)
    print('Socket now listening')
    conn,addr=s.accept()
    while True:
        (_, frames) = imageHub.recv_image()
        cv2.imshow(frames)
        plt.show()
        break

if __name__ == '__main__':
    main()