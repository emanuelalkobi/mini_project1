import subprocess as sp
import os

def create(screen_name):
	command="ffmpeg -r 1/1 -i "+screen_name+"/%05d.jpg -vcodec mpeg4 -y "+screen_name+".mp4"
	os.system(command)

