import tweepy
import os,sys
import wget

#please insert your own twitter credentials in order to run the script
consumer_key=''
consumer_secret=''
access_token='616177906-'
access_token_secret=''


def get_images_from_user(screen_name):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
        try:
		tweets = api.user_timeline(screen_name,count=200, include_rts=False,exclude_replies=True)
	except tweepy.TweepError as e:
		print e.args[0][0]['message']
		exit() 
	last_id = tweets[-1].id 
	while (True):
		more_tweets = api.user_timeline(screen_name,count=200,include_rts=False,exclude_replies=True,max_id=last_id-1)
	# There are no more tweets
		if (len(more_tweets) == 0):
      			break
		else:
      			last_id = more_tweets[-1].id-1
      			tweets = tweets + more_tweets

	media_files = set()
	for status in tweets:
    		media = status.entities.get('media', [])
    		if(len(media) > 0):
      	 		url =  media[0]['media_url']
        		file_type = url.split(".")[-1]
	 		if (file_type=="jpg"):
         			media_files.add(media[0]['media_url'])
	if (len(media_files)==0):      
		print "There are no jpg images in the user that you insert.\nCan't create video."
		exit()

	directory=os.getcwd() +"/"+screen_name
	try:
		if not os.path.exists(directory):
        		os.makedirs(directory)
		else:
			print "already exsist"
	except OSError:
		print ('Error: Creating directory. ' +  directory)
	deleted=0
	
	#remove error images with size equals to 0
	for index,media_file in enumerate(media_files):
		media_num=str(index-deleted).zfill(5)
		image_name=directory+"/"+media_num+".jpg"
    		wget.download(media_file,out=image_name)
	        file_st=os.stat(image_name)
                if (file_st.st_size==0):
 	               os.remove(image_name)
		       deleted=deleted+1

