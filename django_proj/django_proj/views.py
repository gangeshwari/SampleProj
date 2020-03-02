from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.template import RequestContext
# from django.shortcuts import render_to_response
from django.shortcuts import redirect
from users.forms import RegisterForm
from products.models import CellPhones

from django.contrib.auth import authenticate


def go_to_home(request):
    print("--------------------")
    return render(request, 'home_page.html', context={})


def go_to_register(request):
    form = RegisterForm()
    return render(request, 'register.html', {'form':form} )


def go_to_login(request):
    return render(request, 'login.html', context={})


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