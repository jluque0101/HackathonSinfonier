"""
A simple example script to get all posts on a user's timeline.
Originally created by Mitchell Stewart.
<https://gist.github.com/mylsb/10294040>
"""
import facebook
import requests


def print_userinfo(post):
    print(post['created_time'])
    print(post['message'])


# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
access_token = 'CAAH26FZBvJ6cBALlsUJEzSe5mr2LlMf7I6cA4UkfZAFJo1tTN2oIsT0tX938Ipt4xbJguIycYZBRYapWQyEzAJCjZA8nLJPeqgcU0c8sUPesTn4K63LLHeBItYAkqDXncZA9W53SIZCi0ZCFdhGENWACbuBU42FhDlH3ZBwCDVJVzXMsTeZAFhdq7FQhwmVTHiVcZD'
graph = facebook.GraphAPI(access_token)
# Look at Bill Gates's profile for this example by using his Facebook id.


user = 'LeoMessi'
#

profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'posts')

# Wrap this block in a while loop so we can keep paginating requests until
# finished.

while True:
    try:
        # Perform some action on each post in the collection we receive from
        # Facebook.
        [print_userinfo(post=post) for post in posts['data']]
        # Attempt to make a request to the next page of data, if it exists.
        posts = requests.get(posts['paging']['next']).json()
    except KeyError:
        # When there are no more pages (['paging']['next']), break from the
        # loop and end the script.
        break

#####
