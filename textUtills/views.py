'''created by me'''
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
def about(request):
    return HttpResponse("Hello about")
def analyze(request):
    # get the text
    getText=request.POST.get('text', 'default')
    getRemovepunc=request.POST.get('removepunc', 'off')
    getFullcaps=request.POST.get('fullcaps', 'off')
    getNewlineremover=request.POST.get('newlineremover', 'off')
    getExtraspace=request.POST.get('extraspaceremover', 'off')
    purpose=""
    if getRemovepunc == "on":
        punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
        analyzed = ""
        for char in getText:
            if char not in  punc:
                analyzed += char
        params = {"purpose":"Removed punc", "analyzed_text":analyzed}
        getText=analyzed
        purpose+="Remove Punctuation"
        # analyze the text
        # return render(request, 'analyze.html', params)
    if getFullcaps == "on":
        analyzed = ""
        for char in getText:
            analyzed += char.upper()
        params = {"purpose": "Changed to uppercase", "analyzed_text": analyzed}
        getText = analyzed
        purpose += "|Uppercase|"
        # analyze the text
        # return render(request, 'analyze.html', params)
    if getNewlineremover == "on":
        analyzed = ""
        for char in getText:
            if char != "\n" and char !="\r":
                analyzed += char
        params = {"purpose": "New line remover", "analyzed_text": analyzed}
        getText = analyzed
        purpose += "|New line removed|"
        # analyze the text
        # return render(request, 'analyze.html', params)
    if getExtraspace == "on":
        analyzed = ""
        for index, char in enumerate(getText):
            if not(getText[index]==" " and getText[index+1]==" "):
                analyzed+=char
        params = {"purpose": "Extra Space Remover", "analyzed_text": analyzed}
        purpose += "|Removed extra spoaces|"
        # analyze the text
        # return render(request, 'analyze.html', params)
    if getRemovepunc!="on" and getFullcaps!="on" and getExtraspace!="on" and getNewlineremover!="on":
        return HttpResponse("Please select any operation and try again!")
    params = {"purpose": purpose, "analyzed_text": analyzed}
    return render(request, 'analyze.html', params)