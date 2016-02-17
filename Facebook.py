"""
A simple example script to get all posts on a user's timeline.
Originally created by Mitchell Stewart.
<https://gist.github.com/mylsb/10294040>
"""
import facebook
import requests
import unicodedata

# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/

token = 'CAAGmrmZAFYIkBAKhImP4CZAZA3EMUoFdh1TXdRX9gwYXZCeBZAoGqvzuZAiY5meaPPEfs2P65a4LsRYH5sZCsqinrUGe3B75OeLXfIbtWgTTZBzQaFIrbkKiHNQPzcul8pgXMpqdYZCN9iiQIAtwSUjp2pJjP5374PXnQsVa4GgSFZBvpQLji9l50ZCppRuYJ3eG5jv2tDs1hfBvG7hQzebyZBdI'

graph = facebook.GraphAPI(token)
profile = graph.get_object("me")

# He corregido lo de las tildes de una manera mas simple
name = profile['name'].encode('utf-8')
id_f = profile['id']

# Info usu
print id_f, name
print "-----------------"
# Lista amigos

# con esta url hace falta permiso del token http://graph.facebook.com/v2.5/10206814498535741/friendlists

# de esta otra forma saca los taggable_friends que son menos de los que tienes en amigos
friends = graph.get_object("/me/taggable_friends")

for friend in friends['data']:
    print friend['name'].encode('utf-8')
print "----------------"

# feed

#curl -i -X GET \
# "https://graph.facebook.com/v2.5/me?fields=feed&access_token=CAACEdEose0cBAJlEpVvJvEIigS8ZBJPfVfAHTIkERuW5niPndsrXcPHcxepQ3E7jAXOdRDIuqoohBZBQIkGaNgFSSPqn6s4QL6UhFu8EodosMC53qXA05ZA3oBragS3wKYDK00ZBTYZBb5sdZCY438wGxgSU8aWEQpDCOBWAFaUh1BsnVHTkcwxH9CnNGhxY3tdvfZBzPRXPZBmAmJw5cXhN"

response = requests.get('https://graph.facebook.com/v2.5/me?fields=feed&access_token=CAACEdEose0cBAJlEpVvJvEIigS8ZBJPfVfAHTIkERuW5niPndsrXcPHcxepQ3E7jAXOdRDIuqoohBZBQIkGaNgFSSPqn6s4QL6UhFu8EodosMC53qXA05ZA3oBragS3wKYDK00ZBTYZBb5sdZCY438wGxgSU8aWEQpDCOBWAFaUh1BsnVHTkcwxH9CnNGhxY3tdvfZBzPRXPZBmAmJw5cXhN')
posts = response.json()

for post in posts:
    print ("{1} = {1}".format("story", posts[post]))
#posts = graph.get_object("/me/feed")
#print posts
#for post in posts['data']:
#    print post['name'].encode('utf-8')
