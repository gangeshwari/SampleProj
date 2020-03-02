from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from .forms import CellPoneForm
from .models import CellPhones
# from django.shortcuts import render_to_response


def go_to_function(request):
    print("--------------------")
    cells = CellPhones.objects.all()
    # form = CellPoneForm
    return render(request, 'home_page.html', {'products': cells})

def add_cellphones(request):
    if request.method == "POST":
        print (request.POST)
        form = CellPoneForm(request.POST)
        if form.is_valid:
            print("valid form ----------------------")
            form.save()
            # return redirect('home_page.html')
            cells = CellPhones.objects.all()
            return render(request, 'home_page.html', {'products': cells})
    else:
        form = CellPoneForm
        return render(request, 'add_product.html', {'form':form} )

def get_cell_details(request):
    print("*****-------------------**", request.GET['cell_id'])
    c_id = request.GET['cell_id']
    cell = CellPhones.objects.filter(id=c_id)
    print(cell[0].model, "============================")
    return render(request, 'prod_details_page.html', {'product': cell[0]})


def go_to_loginin_in(request):
    print("------------------111")
    # import pdb; pdb.set_trace()
    un = request.data.get('uname')
    pasw = request.data.get('passw')
    user = authenticate(username=un, password=pasw)

    if user is not None:
        print("success")
    else:
        pass


def show_models(request):
    cells = CellPhones.objects.all()
    return render(request, 'home_page.html', {'products': cells})


