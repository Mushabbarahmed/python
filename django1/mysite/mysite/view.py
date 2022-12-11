from django.http import HttpResponse
from django.shortcuts import render
def index(request):

    return HttpResponse('''<h1>assalamualikum<h1><a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">click</a>''')
def about(request):
    # djtext = request.GET.get('text', 'default')
    # print(djtext)
    return HttpResponse("walalikumsusalam")

def template1(request):
    dictionary = {"name": "ahmed",  "place": "mars"}
    return render(request,'index.html',dictionary)
def template2(request):
    # djtext=request.GET.get('text','default')
    djtext=request.POST.get('text','default')#if u use post in templates form then you have to use post heres also instead of get.get use POST.get
    removepunc=request.POST.get('remove','off')
    capitalize=request.POST.get('capitalize','off')
    charcount=request.POST.get('charcount','off')
    newline=request.POST.get('newlineremover','off')
    if removepunc=="on":
        punctuation='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyze=""
        for char in djtext:
            if char not in punctuation:
                analyze=analyze+char
        dictionary1 = {"purpose": "puctuation ", "analyzed_text":analyze}
        return render(request, 'analyze.html', dictionary1)
    elif capitalize=="on":
        analyze=""
        for char in djtext:
                analyze=analyze+char.upper()
        dictionary1 = {"purpose": "capitalize ", "analyzed_text":analyze}
        return render(request, 'analyze.html', dictionary1)
    elif newline=="on":
        analyze=""
        for char in djtext:
                #if char!="\n" :this u can use when u using get .get but if u r using post.get u have to follow below function
                 #   analyze=analyze + char
                if char!="\n" and char!="\r":
                    analyze=analyze + char
                else:
                    print("no")
        dictionary1 = {"purpose": "capitalize ", "analyzed_text":analyze}
        return render(request, 'analyze.html', dictionary1)
    elif charcount=="on":
        #analyze=""
        count=0
        for char in  djtext:
            if char==" ":
                pass
            else:
                count+=1

        dictionary1 = {"purpose": "charcount ", "number_char":count}
        return render(request, 'analyze.html', dictionary1)
        print(count)
    else:
        return HttpResponse('error')