#!/bin/bash
PORT="${1:-1234}"
# Explanation of options
#  Fork:
#    Start a new process for each connection so we can play
#    multiple copies of the video to different clients independently.
#  Nodelay:
#    Force packets to send every time the player flushes its buffer
#    Necessary for smooth playback, otherwise frames get batched & jittery 
socat tcp-l:$PORT,fork,nodelay system:./apple.py

