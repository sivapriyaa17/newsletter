from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.tokenizers import Tokenizer
def summarize(text,count=5):
    try:
        parser=PlaintextParser.from_string(text,Tokenizer("english"))
        s=LsaSummarizer()
        ss=s(parser.document,count)
        return " ".join([str(i) for i in ss])
    except Exception as e:
        print(e)