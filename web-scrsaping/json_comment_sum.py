import urllib.request
import json

url = input('Enter location: ')
if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/comments_2254978.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')

info = json.loads(data)

num_list = []
for item in info['comments']:
    num_list.append(int(item['count']))
print('Count:', len(num_list))
print('Sum:', sum(num_list))