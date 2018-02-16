import Sentiment_mod as s

#print(s.sentiment("This movie was awesome! The acting was wonderful"))
#print(s.sentiment("This movie was utter junk.Horrible movie, 0/10"))
#print(s.sentiment("This movie was utter junk. But some parts were good and amazing."))

f=open("data.txt","r")
str=f.read()
print(s.sentiment(str))