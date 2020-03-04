from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.shortcuts import redirect
from users.forms import RegisterForm
from products.models import CellPhones
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate


def go_to_home(request):
    print("--------------------")
    return render(request, 'home_page.html', context={})

def go_to_index(request):
    return render(request, 'base.html', context={})


def go_to_register(request):
    if request.method == "POST":
        # import pdb; pdb.set_trace()
        u,created = User.objects.get_or_create(username=request.POST['email'], 
            first_name=request.POST['first_name'], last_name=request.POST['last_name'],
            email=request.POST['email'] 
            )
        if created:
            u.set_password(request.POST['password1'])
            u.is_active = True
            u.is_staff = True
            u.save() 
            print("user created", u)
            return HttpResponseRedirect('/login')
        else:
            user_already_exixts = True
            form = RegisterForm()
            return render(request, 'register.html', locals() )  
            # HttpResponse("User already exists")
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form':form} )


def go_to_login(request):
    if request.method == "POST":
        context = RequestContext(request)
        
        user = authenticate(username=request.POST['usernme'], password=request.POST['pass1'])
        # if request.POST['usernme'] == 'admin':
        #     adm = User.objects.filter(username=request.POST['usernme']).first()
        #     if adm.is_superuser:
        #         auth.login(request, user)
        #         return render(request, 'admin_dashboard.html', locals())
        if user is not None :
            products = CellPhones.objects.all()
            auth.login(request, user)
            return HttpResponseRedirect('/products')
            # return render(request, 'home_page.html', locals())
        else:
            msg = "user doesnt exixts"
            return render(request, 'login.html', locals())
    else:
        context = RequestContext(request)
        context_dict = {}
        # context_dict.update(csrf(request))
        return render(request, 'login.html', context_dict)


def go_to_loginin_in(request):
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