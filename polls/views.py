from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .db_controller import exist


@csrf_exempt
def index(request):
    return render(request, 'polls/index.html')


@csrf_exempt
def login(request):
    msg = 'Login Failed.'
    if request.POST:
        id = request.POST['id']
        pw = request.POST['pw']
        print(id, pw)
        if exist(id, pw):
            msg = 'Login Success!'
    return render(request, 'polls/alert.html', {'msg': msg})
