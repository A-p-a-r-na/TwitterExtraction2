import tweepy

consumer_key = "6iLoRCO2rgatvYVK9sRemHeqd"
consumer_secret = "qIjZGEjUaJ2p0ULuxCaemaOnwh4AkUhkCC2aZwc3rQ4FU4J1CH"
access_key = "1592966656011083776-FirtW5HCmlN30d5KuuT72EqIGkY5C6"
access_secret = "O1uOPGRlZ2Mqa7nuq6xGpFMISMy7cXYwIUEYXbYkEw3mg"

# Function to extract tweets
def get_tweets(username):
		
		# Authorization to consumer key and consumer secret
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

		# Access to user's access key and access secret
		auth.set_access_token(access_key, access_secret)

		# Calling api
		api = tweepy.API(auth)

		# 200 tweets to be extracted
		number_of_tweets=200
		tweets = api.user_timeline(screen_name=username)

		# Empty Array
		tmp=[]

		# create array of tweet information: username,
		# tweet id, date/time, text
		tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created
		for j in tweets_for_csv:

			# Appending tweets to the empty array tmp
			tmp.append(j)

		# Printing the tweets
		print(tmp)


# Driver code
if __name__ == '__main__':

	# Here goes the twitter handle for the user
	# whose tweets are to be extracted.
	get_tweets("twitter-handle")
