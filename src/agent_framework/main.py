#!/usr/bin/env python3.8
import cv2
import time
import logging
import argparse

from typing import NoReturn 


logging.basicConfig(filename="log.txt", level=logging.INFO)

def main() -> NoReturn:
    fps = 25

    cap = cv2.VideoCapture(0)
    cap.set(3, 720)
    cap.set(4,480)
    cap.set(5, fps)
    
    frame_counter = 0
    while True:
        frame = cap.read()[1]
        frame_counter += 1

        if frame_counter >= fps * 2:
            frame_counter = 0
            cv2.imwrite('../bin/current_frame.jpg', frame)

        # @@ todo: read agent ipc context for data to display
        # frame = cv2.putText(frame, f'', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        if cv2.waitKey(1) == 27:
            break

        cv2.imshow('output', frame)
        
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
