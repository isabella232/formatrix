#!/bin/sh

notify-send 'calculation started'
cd 1
maxima --very-quiet --batch=runme.wxm
cd ..
notify-send 'x1 calculation completed'
cd 2
maxima --very-quiet --batch=runme.wxm
cd ..
notify-send 'x2 calculation completed'
cd 3
maxima --very-quiet --batch=runme.wxm
cd ..
notify-send 'x3 calculation completed'
cd 4
maxima --very-quiet --batch=runme.wxm
cd ..
notify-send 'x4 calculation completed'
cd 5
maxima --very-quiet --batch=runme.wxm
cd ..
notify-send 'x5 calculation completed'
