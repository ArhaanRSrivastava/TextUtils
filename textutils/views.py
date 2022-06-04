from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    purpose = ""

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\\,<>./?@#$%^&*_`'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
        purpose += "|Removed Punctuations"
        params = {'purpose': purpose, 'analyzed_text': analyzed}

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed
        purpose += "|Capitalized"
        params = {'purpose': purpose, 'analyzed_text': analyzed}

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        purpose += "|Removed New lines"
        djtext = analyzed
        params = {'purpose': purpose, 'analyzed_text': analyzed}

    if extraspaceremover == "on":
        analyzed = ""
        for num, char in enumerate(djtext):
            if not (djtext[num] == " " and djtext[num + 1] == " "):
                analyzed = analyzed + char
        djtext = analyzed
        purpose += "|Removed extra spaces"
        params = {'purpose': purpose, 'analyzed_text': analyzed}

    if charcount == "on":
        analyzed = ""
        djtext = djtext.replace(" ", "")
        counted_text = "The number of character in your text is " + str(len(djtext))
        purpose += "|Character counted"
        params = {'purpose': purpose, 'analyzed_text': analyzed, "counted_text": counted_text}

    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on":
        return HttpResponse("<h1>please select any operation</h1>")

    return render(request, 'analyze.html', params)
