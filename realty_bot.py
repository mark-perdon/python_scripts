from bs4 import BeautifulSoup as bs
import requests
r=requests.get('http://realtymlp.com/dashboard',auth=('znex07@gmail.com','123'))
r2=requests.get('http://realtymlp.com/dashboard')
res=r2.content
#soup=bs(res,features="lxml")
#for link in soup.find_all('a'):
#	print(link.get('href'))
print(res)
