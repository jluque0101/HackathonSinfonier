import requests

token = "CAAH26FZBvJ6cBABPmImKXGPU3W9xsuneZCi9ZBOY5kbZAIDM8K66qKwMdmF3lDl70pwhAnHu7bmePeCiRX5bnmegMkhaJXB55UdZCncSYZBKDDMYA4CEFqwL8xFXZAek7EjdAMBybfsuGcZBBeIGGeijNu08IdzyKPRc91D8V16SLAlprfZCha5WZB"
groupname = "oficialgrupopalomo"

groupinfoquery = "https://graph.facebook.com/v2.5/"+groupname+"?fields=id&access_token="+token
groupinforesp = requests.get(groupinfoquery)
groupid = groupinforesp.json()['id']

grouppostquery = "https://graph.facebook.com/v2.5/"+groupid+"?fields=posts&access_token="+token
grouppostresp = requests.get(grouppostquery)
grouppost = grouppostresp.json()

gp = grouppost['posts']
dg = gp['data']

for i in dg:
    print "Created time: " + i["created_time"]
    if "story" in i.keys():
        print "Story: " + i["story"]
    if "message" in i.keys():
        print "Message: " + i["message"]
