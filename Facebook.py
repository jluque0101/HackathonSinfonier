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

token = 'CAAHNOVctwEQBAKygzdgUjZA8JCnrihkZAbsWPPk1WsIHZCC8ZCJWXsDjr2pL4zjH4ztMxXjuHSErrd9999bimd2DPGIUFbptFOYzuBvIJ3fzGtEV37juiJNzTks6bECi5833gy8vX8HM1ccjhyhBfFPrmkfqBTR7DrBizp2eF7KbRVhTS8ghLuNDtdiJLCkZD'

graph = facebook.GraphAPI(token)
profile = graph.get_object("me")

# He corregido lo de las tildes de una manera mas simple
name = profile['name'].encode('utf-8')
id_f = profile['id']

# Info usu
print id_f, name

# Lista amigos

# con esta url hace falta permiso del token http://graph.facebook.com/v2.5/10206814498535741/friendlists

# de esta otra forma saca los taggable_friends que son menos de los que tienes en amigos
friends = graph.get_object("/me/taggable_friends")

for friend in friends['data']:
    print friend['name'].encode('utf-8')
