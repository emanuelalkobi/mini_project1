import sys
import get_images as get_images
import create_video as create_video
import analyze_video as analyze_video
def main():
	if len(sys.argv) < 2:
    		print("Please  call me with one parameter")
    		sys.exit()
        screen_name =sys.argv[1]
	print screen_name
        print "-------------------------------------"
	print "downloading image from tweeter feed " + screen_name
	print "-------------------------------------"
	get_images.get_images_from_user(screen_name)
        print "-------------------------------------"
	print "creating video from images"
	print "-------------------------------------"
        create_video.create(screen_name)	
        print "-------------------------------------"
	print "analyzing video"
	print "-------------------------------------"
	analyze_video.analyze(screen_name+".mp4") 

main()
