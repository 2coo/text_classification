from readability2 import Readability
import urllib.request as urllib

response = urllib.urlopen('http://medee.mn/main.php?eid=116053')

article =  Readability(str(response.read().decode('utf8'))).parse()

print(article["title"])
print("-------------------------------------------------------------------------------------------------------------------------------------")
print(article["textContent"])