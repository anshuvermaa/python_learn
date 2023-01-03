import tweepy

import itertools

import time 

auth = tweepy.OAuth1UserHandler(
   'wjhd528cR6jqKDdCRkoVaOrV0', 'ghrg9y0aRwyBtLjgD5G83i5Yia8PBvqcFvLqyBouEwdBVxMYoC', '977935202759700480-ofi8tOZgB5HfXqNZLOupuV06sCF6wVv', 'WLm34m5nU2kigzvsIvHQtMxy5fMAWP2o1hY259UJrG7Dd'
)

api = tweepy.API(auth)


user = api.get_user(screen_name='anshuverma')     #screen_name-> username
print(user.screen_name)                       #username which is on twitter
print(user.name)                            #real name which is on twitter
print(user.followers_count)
print(user.status.source )
print(user.description )
print(user.profile_banner_url )
for friend in user.friends():
   print(friend.screen_name)          #print followings


# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text) 





# print("this is my followers")
# def limit_handled(cursor):
#     try:
#         while True:
#          yield cursor.next()
#     except tweepy.RateLimitError:
#             time.sleep(1000)




# for follower in limit_handled(tweepy.Cursor(user.friends()).items()):
#    print(follower.screen_name)







# like bot

search_string ='BITCOIN'
n=2

for tweet in tweepy.cursor(api.search_tweets('BITCOIN')).items(n):
    try:
        # tweet.favorite()
        print('tweet')
        print('i liked that tweet')
    except  tweepy.tweepError as e:
        print(e.reason)
    except StopIteration:
        break

