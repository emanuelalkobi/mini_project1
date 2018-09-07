import tweepy
import os,sys
import wget

consumer_key='r18ZDSbis8VbamUKkaxN7qL1q'
consumer_secret='v8du6LkynyqU9ft9VQeJk9sMPa0E8xGSX1BiaU6HPfk0TnCVJH'
access_token='616177906-wH4yvRqIHlPiifb9o1Q2QxCwIOzCPxlsU6pfIKrH'
access_token_secret='WhX3x7aCZ15OF1IaExlG2GkX60WJ7hZT9C7VP3bo2NNvF'


def get_images_from_user(auth,screen_name):
	api = tweepy.API(auth)

	tweets = api.user_timeline(screen_name,count=200, include_rts=False,exclude_replies=True)
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

	directory=os.getcwd() +"/"+screen_name
	try:
		if not os.path.exists(directory):
        		os.makedirs(directory)
		else:
			print "already exsist"
	except OSError:
		print ('Error: Creating directory. ' +  directory)

	for index,media_file in enumerate(media_files):
		media_num=str(index).zfill(5)
		image_name=directory+"/"+media_num+".jpg"
    		wget.download(media_file,out=image_name)

def main(screen_name):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	get_images_from_user(auth,screen_name)


