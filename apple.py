#!/usr/bin/env python3
import time
import sys

HEIGHT=25
WIDTH=60
CLEAR="\033[2J"
FRAMERATE=30
INTERVAL=1.0/FRAMERATE

with open('apple.txt', 'r') as f:
    while screen:=f.readlines(WIDTH*HEIGHT):
        sys.stdout.write(CLEAR + "".join(screen))
        sys.stdout.flush()
        time.sleep(INTERVAL)
