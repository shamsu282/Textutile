from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')

    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    numberremover = request.POST.get('numberremover','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyze=""
        for char in djtext:
            if char not in punctuations:
                analyze =  analyze + char

        params = {'purpose':'Removed Punctuations','analyzed_text':analyze}
        djtext = analyze
    
    if (fullcaps=="on"):
        analyze = ""
        for char in djtext:
            analyze = analyze + char.upper()
        params = {'purpose':'Changed to Uppercase','analyzed_text':analyze}
        djtext = analyze
    
    if (newlineremover=="on"):
        analyze = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyze = analyze + char
        
        params = {'purpose':'Removed Newline','analyzed_text':analyze}
    
    if (numberremover=="on"):
        analyze = ""
        numbers = '0123456789'
        for char in djtext:
            if char not in numbers:
                analyze = analyze + char

        params = {'purpose':'Removed Number','analyzed_text':analyze}
        djtext = analyze

    if (extraspaceremover=="on"):
        analyze = ""
        for index,char in enumerate(djtext):
            if char == djtext[-1]:
                if not(djtext[index]== " "):
                    analyze = analyze + char
            elif not (djtext[index]== " " and djtext[index+1]==" "):
                analyze = analyze + char

        params = {'purpose':'Removed ExtraSpace','analyzed_text':analyze}   

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover!="on" and numberremover!="on" and fullcaps!="on"):
        return HttpResponse("Please Select Any Operation And Try Again")     

    return render(request,'analyze.html',params)


        

