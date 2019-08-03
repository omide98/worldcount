from django.http import HttpResponse
from django.shortcuts  import render
import operator
def home (request):
    return render(request,'homepage.html',{'omid':'its me'})

def about (request):
    return render(request , 'about.html')

def count (request):
    text= request . GET ['text']
    print(text)
    words=text.split()
    worddic={}
    for word in words :
        if word in worddic:
            worddic[word]+=1
        else:
            worddic[word]=1
    sortworddic=sorted(worddic.items(),key=operator.itemgetter(1) , reverse=True)
    return render(request , 'count.html' , {'text': text,'words':len(words),'worddic':sortworddic})
