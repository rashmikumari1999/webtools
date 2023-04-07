from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from googletrans import Translator
import pyttsx3
import uuid
from .models import Url
import requests
import bs4
import pyttsx3

def index(request):
   return render(request, 'index.html')

def analyzed(request):
    return render(request, 'analyzed.html')

    # return HttpResponse("Home")


def ex1(request):
    sites = ['''<h1>For Entertainment  </h1> <a href="https://www.youtube.com/"> Youtube Videos</a> ''',
             '''<h1>For Interaction  </h1> <a href="https://www.facebook.com/"> Facebook</a> ''',
             '''<h1>For Insight  </h1> <a href="https://www.ted.com/talks"> Ted Talks</a> ''',
             '''<h1>For Internship  </h1> <a href="https://www.internshala.com">Internship</a> ''']
    return HttpResponse((sites))

def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")


def translator(request):
    return render(request, 'translator.html')

def translated(request):
    text= request.GET.get('text')
    lang= request.GET.get('lang')
    print('text:',text,'lang:', lang)
    translator= Translator()
    dt= translator.detect(text)
    dt2=dt.lang
    translated=translator.translate(text, lang)
    tr=translated.text
    return render(request, 'translated.html', {'translated':tr, 'u_lang':dt2, 't_lang':lang})
def base(request):
     return render(request, 'base.html')
def counter(request):
     mess=request.GET['message']
     w1=mess.split()
     return render(request,'counter.html',{'msg':mess,"length": len(w1)})
def home(request):
    return render(request, 'one.html')
def some(request):
    value=request.GET['inp']
    obj=pyttsx3.init()
    obj.say(value)
    obj.runAndWait()
    return redirect('/')
def short(request):
    return render(request, 'short.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect('https://'+url_details.link)
 
 

def scrab(request):
	value = []
	if request.method == 'POST':
		form = request.POST['your_url']
		resp = requests.get(form)
		scrapval = bs4.BeautifulSoup(resp.text,"html.parser")
		for data in scrapval.find_all('img'):
			srcval = data.get('src')
			print(srcval)
			value.append(srcval)

	return render(request,'scrab.html',{'value':value})

