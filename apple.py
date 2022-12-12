#!/usr/bin/env python3
import time
import sys
HEIGHT=25
WIDTH=60
# This clear code actually moves the cursor to the top left and overwrites
# in-place instead of adding each frame to scrollback history
CLEAR="\033[H\033J"
FRAMERATE=30
INTERVAL=1.0/FRAMERATE

# Push scrollback out of the way so we don't nuke the terminal history
sys.stdout.write('\033[H\033[2J')
try:
    with open('apple.txt', 'r') as f:
        while screen:=f.readlines(WIDTH*HEIGHT):
            # Omit the final newline to avoid blank line at the bottom
            sys.stdout.write(CLEAR + "".join(screen)[:-2])
            sys.stdout.flush()
            time.sleep(INTERVAL)
except KeyboardInterrupt:
    pass
sys.stdout.write('\n')