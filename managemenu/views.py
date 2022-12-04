from django.shortcuts import render, redirect
from .models import FnB, Menu
from .forms import FnBForm

def index(request):
    fnb = FnB.fnbs.all()
    return render(request, "managemenu.html", {"fnb": fnb})

def create(request):
    if request.method == "POST":
        form = FnBForm(request.POST)
        name = request.POST['name']

        if FnB.fnbs.filter(name=name).exists():
            error_msg = 'This item is already exist'
            return render(request, 'addfnb.html', {'msg': error_msg})
        if form.is_valid():
            try:
                form.save()
                return redirect("/managemenu")
            except:
                pass
    else:
        form = FnBForm()
        return render(request, "addfnb.html", {'form': form})

def edit(request, id):
    fnb = FnB.fnbs.get(id = id)
    return render(request, "editfnb.html", {"fnb": fnb})

def update(request, id):
    fnb = FnB.fnbs.get(id = id)
    form = FnBForm(request.POST, instance=fnb)
    print(form)
    if form.is_valid():
        form.save()
        return redirect("/managemenu")

    return render(request, "editfnb.html", {"fnb": fnb})

def delete(request, id):
    fnb = FnB.fnbs.get(id = id)
    fnb.delete()
    return redirect("/managemenu")
