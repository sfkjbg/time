from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList


def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if response.method == 'POST':
        print (response.POST)
        if response.POST.get('save'):
            for item in ls.item_set.all():
                if response.POST.get('c' + str(item.id)) == 'clicked':
                    item.complete = True
                else:
                    item.complete = False

                item.save()

        elif response.POST.get('newItem'):
            txt = response.POST.get('new')

            if len(txt) >2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print('Invalid')


    return render(response, 'main/list.html', {'ls': ls})


def home(response):
    return render(response, 'main/home.html', {})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data['name']
            t = ToDoList(name=n)
            t.save()
        return HttpResponseRedirect('/%i' %t.id)
    else:
        form = CreateNewList()
    return render(response, 'main/create.html', {'form': form})



















# def index(response, id):
#     ls = ToDoList.objects.get(id=id)
#     item = ls.item_set.get(id=1,)
#     sec = ls.item_set.get(id=2)
#     sep_item = ls.item_set.get(id=3)
    # return HttpResponse("<h1> %s </h1> <br></br> <p> </p>" %ls.name)
    # return HttpResponse("<h1> %s </h1> <br></br> <p> %s </p>"
    #                     "<br></br><p>%s</p>%s" %(ls.name, str(item.text), str(sep_item),str(sec)))