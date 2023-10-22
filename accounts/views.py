from django.shortcuts import render

# Create your views here.
def loginView(request):
    return render(request, 'accounts/login.html')

def registerView(request):
    return render(request, 'accounts/register.html')