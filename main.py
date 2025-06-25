from rss import fetch
from scraper import full_text
from summarizer import summarize
from engine import render_newsletter
print("welcome NEWSLETTER")
art=fetch()
print("articles ")
l=[]
for a in art:
    print("the articles are: ")
    print(a["title"])
    t=full_text(a["link"])
    summary=summarize(t)
    l1={"title":a["title"],"summary":summary,"link":a["link"]}
    l.append(l1)
print("NEWSLETTER")
print("length of :",len(l))
render_newsletter(l)
for j in l:
    print(j)
print("open html file in the directory")
    