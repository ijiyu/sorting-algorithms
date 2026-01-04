ffmpeg -framerate 60 -start_number 0 -i frames/%d.jpg -c:v libx264 -pix_fmt yuv420p out.mp4
