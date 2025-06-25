import feedparser
from config import FEEDS,Max
def fetch():
    k=[]
    for u in FEEDS:
        ff=feedparser.parse(u)
        for e in ff.entries[:Max]:
            j={"title":e.title,"link":e.link,"summary":e.get("summary",""),"published":e.get("published","")}
            k.append(j)
    return k