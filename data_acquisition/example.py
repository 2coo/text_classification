from readability import Readability
import urllib.request as urllib

response = urllib.urlopen('https://ikon.mn/n/1hat')

article =  Readability(str(response.read().decode('utf8'))).parse()

# print(article["atype"])
for key, value in article.items():
    print(key)
    # print("#"+key+"#")
    # print("".join(["="]*50))
    # print(value)
    # print("".join(["="]*50))