from django.shortcuts import render

# Create your views here.
def chattingView(request):
    return render(request, 'chatbot/index.html')