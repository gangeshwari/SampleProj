from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.shortcuts import redirect
from users.forms import RegisterForm
from products.models import CellPhones
from django.contrib import auth

from django.contrib.auth import authenticate


def go_to_home(request):
    print("--------------------")
    return render(request, 'home_page.html', context={})

def go_to_index(request):
    return render(request, 'base.html', context={})


def go_to_register(request):
    if request.method == "POST":
        print (request.POST)
        form = RegisterForm(request.POST)
        if form.is_valid:
            print("valid form ----------------------")
            form.save()
            return redirect('/login')
        else:
            msg = "invalid form"
            return render(request, 'register.html', locals() )
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form':form} )


def go_to_login(request):
    if request.method == "POST":
        context = RequestContext(request)
        print (request.POST, "================================================")
        products = CellPhones.objects.all()
        user = authenticate(username=request.POST['usernme'], password=request.POST['pass1'])
        if user is not None:
            print("tttttttttttttttttt")
            auth.login(request, user)
            return render(request, 'home_page.html', locals())
        else:
            print("=====fffffffffffffff")
            msg = "user doesnt exixts"
            return render(request, 'login.html', locals())
        # form = CellPoneForm(request.POST)
        # if form.is_valid:
        #     print("valid form ----------------------")
        #     form.save()
        #     # return redirect('home_page.html')
        #     cells = CellPhones.objects.all()
            # return render(request, 'home_page.html', {'products': cells})
    else:
        context = RequestContext(request)
        context_dict = {}
        # context_dict.update(csrf(request))
        # return render_to_response("login.html", context_dict, context)
        return render(request, 'login.html', context_dict)


def go_to_loginin_in(request):
    print("------------------111")
    import pdb; pdb.set_trace()
    un = request.data.get('uname')
    pasw = request.data.get('passw')
    user = authenticate(username=un, password=pasw)

    if user is not None:
        print("success")
    else:
        pass
    # No backend authenticated the credentials
    # return render(request, 'login.html', context={})


def show_models(request):
    cells = CellPhones.objects.all()
    return render(request, 'home_page.html', {'products': cells})