# Create your views here.
from django.shortcuts import render, redirect
from .forms import SignupForm

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # ou onde quiser redirecionar
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})
