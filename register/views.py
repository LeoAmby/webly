from django.shortcuts import render, redirect
from register.forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form":form})


@login_required
def profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render (request, 'profile.html', context)