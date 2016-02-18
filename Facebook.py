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

token = 'CAACEdEose0cBAJPZCwThL8TbCA4WXkqpCfDXoqxAg4QYrAUGLu7lPsNRuw1UGZBPLu9UZBTF3hVc4WFdCGoEdbcI3e8NrQD2klzSpd8mVMujjsgYLZBImhUyBkQnIUu7F2VvRyPEOe4Cm8gSklZCEHfYYZACsYzoA7CMLWZAqpckNNrgp2DLKVQd7dkBbo0NOSAfgV322GZBPgZDZD'

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
#friends = graph.get_object("/me/taggable_friends")

#for friend in friends['data']:
#    print friend['name'].encode('utf-8')
#print "----------------"

# feed

#curl -i -X GET \
# "https://graph.facebook.com/v2.5/me?fields=feed&access_token=CAACEdEose0cBAJlEpVvJvEIigS8ZBJPfVfAHTIkERuW5niPndsrXcPHcxepQ3E7jAXOdRDIuqoohBZBQIkGaNgFSSPqn6s4QL6UhFu8EodosMC53qXA05ZA3oBragS3wKYDK00ZBTYZBb5sdZCY438wGxgSU8aWEQpDCOBWAFaUh1BsnVHTkcwxH9CnNGhxY3tdvfZBzPRXPZBmAmJw5cXhN"

response = requests.get("https://graph.facebook.com/v2.5/me/feed?access_token=CAACEdEose0cBAE46Se8aweo3IX459CA3zv7maghLAIr22X8dnakHwfZAO2Twn7DFji2ZArJFtZC6rhgM6YqxELjqsfmBoCgExF5X2YtVNbDhwGUOb1elE9XIOsBr7SBZCsgaxNmt249pcVQ9p4ZAhoPsgR0JdUYNMhytZCpwkVoCbDUxSvIZAoPrtJFvYwDbgf9NpDvhPgOggZDZD")
posts = response.json()
print posts


datos = posts['data']

for p in datos:
    print "Fecha de creacion: ",  p['created_time']
    if "story" in p.keys():
        print "Informacion: ", p['story'].encode('utf-8')
    if "message" in p.keys():
        print "Mensaje: ", p['message'].encode('utf-8')
    print "Id del post: ", p['id']
    print "-------------"





#    print ("{1} = {1}".format("story", posts[post]))
#posts = graph.get_object("/me/feed")
#print posts
#for post in posts['data']:
#    print post['name'].encode('utf-8')
