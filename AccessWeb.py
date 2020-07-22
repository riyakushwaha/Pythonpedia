# ------------------------------ Traditional method to get file from server
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()


#Second Method. In this urlib library do all the socket work
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode())

# But soft what light through yonder window breaks
#
# It is the east and Juliet is the sun
#
# Arise fair sun and kill the envious moon
#
# Who is already sick and pale with grief
#


fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

# But soft what light through yonder window breaks
# It is the east and Juliet is the sun
# Arise fair sun and kill the envious moon
# Who is already sick and pale with grief

fhand1 = urllib.request.urlopen('http://data.pr4e.org/romeo.txt').read()
print(fhand1)

# b'But soft what light through yonder window breaks\nIt is the east and Juliet is the sun\nArise fair
# sun and kill the envious moon\nWho is already sick and pale with grief\n'



# ------------------------------Parse Xml
import xml.etree.ElementTree as et
data = '''<person>
    <name> Chuck </name>
    <phone type="initl"> 8903564339 >/phone>
    <email hide="yes"/>
</person>'''

tree =et.fromstring(data)
print("Name:", tree.find("name").text)
print("Attr:", tree.find("email").get("hide"))

# ------------------------------Parse HTML
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

# ------------------------------Parse json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

# Loads methods python dictionary
info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
