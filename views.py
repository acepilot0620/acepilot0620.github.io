from django.shortcuts import render
from .models import InputText

def main(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    word = text.split()
    word_dictionary = {}
    for i in word:
        if i in word_dictionary:
            word_dictionary[i]+=1
        else:
            word_dictionary[i]=1
    return render(request,'result.html', {'full':text, 'total': len(word), 'dictionary':word_dictionary.items()})
