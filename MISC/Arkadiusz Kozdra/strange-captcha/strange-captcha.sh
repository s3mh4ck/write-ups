#!/bin/bash

#xdotool set_desktop 0 search --class firefox sleep 1 windowactivate windowfocus
#import -window root -crop 500x200+100+300 pic.png
#import -window root -crop 90x60+105+340 pic1.png
#import -window root -crop 90x60+245+340 pic2.png
#import -window root -crop 95x60+385+340 pic3.png
#import -window root -crop 95x60+385+400 pic4.png
#import -window root -crop 90x60+245+400 pic5.png
#import -window root -crop 90x60+105+400 pic6.png
#import -window root -crop 90x100+500+340 pic7.png
#gocr='gocr -C 0-9AVΩ -a 0'
#$gocr pic1.png |tr -d _  >rec
#$gocr pic2.png |tr -d _ >>rec
#$gocr pic3.png |tr -d _ >>rec
#$gocr pic4.png |tr -d _ >>rec
#$gocr pic5.png |tr -d _ >>rec
#$gocr pic6.png |tr -d _ >>rec
#$gocr pic7.png |tr -d _ >>rec
#
#grep -v '  1' rec >rec2

curl -s -o cap.svg -b session=c2dae962-bec8-42ec-8362-cefb06aa5196 https://strange-captcha.ecsc18.hack.cert.pl/schematic

grep Deja cap.svg |grep -o '#DejaVuSans-[0-9a-f]\+' |grep -o -- '-.*' |python3 -c 'import sys;print("".join(chr(-int(x,16))for x in sys.stdin.read().split()))' |grep -o '[0-9]\+.' >rec

head -1 rec|tail -1  >rec2
head -3 rec|tail -1 >>rec2
head -6 rec|tail -1 >>rec2
head -5 rec|tail -1 >>rec2
head -4 rec|tail -1 >>rec2
head -2 rec|tail -1 >>rec2
head -7 rec|tail -1 >>rec2

mv rec2 rec

# detect arrow pointing upwards
amp=($(grep -A9 patch_2 cap.svg |grep -o '[ML] [0-9. ]\+'|cut -f3 -d\ |sort -nu))
[ $(python3 -c "print((${amp[0]}+${amp[2]})/2>${amp[1]})") == True ] && sed -i 's/^\([0-9]\+A\)$/-\1/' rec

# detect minus over plus
mp=($(grep -2 '^L [0-9. ]\+$' cap.svg |grep -A4 line2d_|grep -B4 /g |grep -o '[LM] [0-9. ]\+$'|cut -f3 -d\ |sort -nu))
[ $(python3 -c "print((${mp[0]}+${mp[3]})/2<${mp[2]})") == True ] && sed -i 's/^\([0-9]\+V\)$/-\1/' rec

#display cap.svg &
#vi rec
#xdotool search --name cap.svg windowclose

xdotool set_desktop 0 search --class firefox sleep 0.1 click 1 sleep 0.1 type -- "$(python3 strange-captcha.py <rec | tail -1)"$'\r'
sleep 1

