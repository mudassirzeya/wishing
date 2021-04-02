from django.shortcuts import render, redirect
from .forms import Createform
from .models import Create_card

# Create your views here.


def wishing_card(request, pk=''):
    if pk == '':
        context = {}
        return render(request, 'card/wishing.html/', context)
    else:
        user = Create_card.objects.get(id=pk)
        context = {'user': user}
        return render(request, 'card/wishing.html/', context)


def create_card(request):
    form = Createform()
    if request.method == 'POST':
        print("request.POST: ", request.POST)
        userform = Createform(request.POST, request.FILES)
        if userform.is_valid():
            print("form valid")
            userObj = userform.save()
            return redirect('wishing', pk=userObj.id)
        else:
            print("form not valid")
        return redirect('create')
    context = {'form': form}
    return render(request, 'card/create.html/', context)
