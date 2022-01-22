from django.shortcuts import render
# 123456

def home(request):
    request.session['name'] = 'User'
    username = request.session['name']

    return render(request, 'home.html', context={'username': username})