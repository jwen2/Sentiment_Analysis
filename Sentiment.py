
import tweepy
from textblob import TextBlob
import datetime

#Change Keys to useable Twitter API key

consumer_key = 'AczBVcVl7W1kIqoEwKjZa34jO'
consumer_secret = 'sjWqaeCKqBghkxqYLOYKZWKMz8LM6i3K0YMn5Lhw6Zn1KRySqy'

access_token = '1873709048-bsx9JjSvNQv7vEtZLcufaHEMzjLUJLIvc7BwOkQ'
access_token_secret = 'aIpz3h7axzJhLobZjfhLrXchdvhQZOyyXgBk9WX0smcSY'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Authenticates API
api = tweepy.API(auth)

#public_tweets_sox = api.search('Red Sox')
#public_tweets_celtics = api.search('Celtics')
#public_tweets_bruins = api.search('Bruins')


#Function that returns the average polarity of a tweet
def avg_sentiment(api):
    counter = 0
    total_polarity = 0
    for tweet in api:
        analysis = TextBlob(tweet.text)
        counter = counter + 1
        total_polarity = total_polarity + analysis.sentiment[0]
        return total_polarity/counter

#Function that compares the average sentiment of the teams
def compare_sentiment(t):
    big_polarity = 0
    winning_team = ""
    for i in t:
        public_tweets = api.search(i)
        avg_team_sent = avg_sentiment(public_tweets)
        print(i, avg_team_sent)
        if (avg_team_sent > big_polarity):
            big_polarity = max(avg_team_sent, big_polarity)
            winning_team = i
    return "The team with the highest polarity is:", winning_team,"with an average polarity of:", big_polarity

teams = ['Red Sox', 'Celtics', 'Bruins']
print(compare_sentiment(teams))

#Ask the user to enter three team/topic and tell the user which team/topic has the highest average polarity

new_list = [input("What is your first topic:  "),input("What is your second topic:  "),input("What is your third topic:  ")]
print(big_function(new_list))


#Return the tweet with the highest polarity given an user input

def high_pol():
    wt = input("What is your tweet word be?")
    public_tweets = api.search(wt)
    highest_sent = 0
    good_tweet = ""
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        if analysis.sentiment[0] > highest_sent:
            highest_sent = analysis.sentiment[0]
            good_tweet = tweet.text
    return "The most positive tweet in your subject is", good_tweet, "with a sentiment of", highest_sent

print(high_pol())
