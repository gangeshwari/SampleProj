from django.shortcuts import render, redirect
from .forms import RegisterForm

def go_to_home_page(request):
    return render(request, 'home_page.html')

def go_to_register(request):
    print("*****************")
    if request.method == "POST":
        print (request.POST)
        form = RegisterForm(request.POST)
        if form.is_valid:
            print("valid form ----------------------")
            form.save()
            return redirect('/login')
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form':form} )



