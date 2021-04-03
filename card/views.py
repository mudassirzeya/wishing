from django.shortcuts import render, redirect
from .forms import Createform
from .models import Create_card
import random
import string

# Create your views here.


def wishing_card(request, pk=''):
    if pk == '':
        context = {}
        return render(request, 'card/wishing.html/', context)
    else:
        user = Create_card.objects.filter(random_str=pk).first()
        context = {'user': user}
        return render(request, 'card/wishing.html/', context)


def create_card(request):
    form = Createform()
    random_string = ''.join(random.choice(
        string.ascii_uppercase + string.digits) for _ in range(8))
    if request.method == 'POST':
        print("request.POST: ", request.POST)
        userform = Createform(request.POST, request.FILES)
        if userform.is_valid():
            print("form valid")
            userObj = userform.save(commit=False)
            userObj.random_str = random_string
            userObj.save()
            return redirect('wishing', pk=userObj.random_str)
        else:
            print("form not valid")
        return redirect('create')
    context = {'form': form}
    return render(request, 'card/create.html/', context)
