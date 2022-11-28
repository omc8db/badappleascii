#!/bin/bash
# Re-renders the ascii version of bad apple from its video source. Tweak output size or framerate here
tmpdir="$(mktemp -d)"
curl https://ia802905.us.archive.org/19/items/TouhouBadApple/Touhou%20-%20Bad%20Apple.mp4 > $tmpdir/BadApple.mp4
ffmpeg -i $tmpdir/BadApple.mp4 $tmpdir/$filename%05d.png
jp2a $tmpdir/*.png --height=24 > apple.txt
rm -rf $tmpdir
