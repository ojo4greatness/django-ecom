from django.shortcuts import render

# Create your views here.
def new_conversation(request):

    return render(request, "conversation/home.html")