from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages #can use messaages to create a one time alert displayed if form data is valid
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

from django.contrib.auth.decorators import login_required

# Create your views here.

##
## implement Crispyforms to make unvalidated form error messages look better
##

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) #instantiate a form with the post request's data
        if form.is_valid():
            form.save() #automatically saves the data from the form including hashing the password
                        #data is correctly handled by django
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account was successfully created for {username}') #create the success alert
            return redirect('login') #redirect to home page after submitting form
    else:
        form = UserRegisterForm() #just instantiate an empty form
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)

@login_required #decorator to ensure that the user is logged in before calling profile function to view profile page
def profile(request):
    if request.method == 'POST':
        userupdateform = UserUpdateForm(request.POST, instance=request.user)
        profileupdateform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if userupdateform.is_valid() and profileupdateform.is_valid():
            userupdateform.save()
            profileupdateform.save() 
            messages.success(request, f'Account successfully updated')
            return redirect('profile') 
            
    else:
        userupdateform = UserUpdateForm(instance=request.user)
        profileupdateform = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'userupdateform': userupdateform,
        'profileupdateform': profileupdateform
    }

    return render(request, 'users/profile.html', context)
