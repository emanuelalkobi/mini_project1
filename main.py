import sys
import get_images as get_images
def main():
	if len(sys.argv) < 2:
    		print("Please  call me with one parameter")
    		sys.exit()
        screen_name =sys.argv[1]
	print screen_name
	get_images.main(screen_name)	 

main()
