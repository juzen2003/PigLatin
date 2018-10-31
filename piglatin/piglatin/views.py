from django.http import HttpResponse
#  this is for showing html as response
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def translate(request):
    # request.GET['originaltext'] -> originaltext inputed from form is passed to translate page from request
    originaltext = request.GET['originaltext']
    tranlationtext = ''
    for word in originaltext.lower().split():
        tranlation_word = translation(word)
        tranlationtext += tranlation_word + ' '
    return HttpResponse(tranlationtext)

# translate a word into pig latin
def translation(word):
    vowel = ['a', 'e', 'i', 'o', 'u']
    translation_word = ''

    while word[0] not in vowel:
        word = word[1:] + word[0]

    word = word + 'ay'
    return word
