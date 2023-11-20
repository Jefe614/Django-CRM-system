from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record
from .forms import AddRecordForm
# Create your views here.
def home(request):
    records = Record.objects.all
    #logging in
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

    #authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in!')
            return redirect('home')
        else:
            messages.success(request, 'Error logging in...')
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records} )



def logout_user(request):
    logout(request)
    messages.success(request, 'Logout succesful')
    return redirect('home')




def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})

    else:
        messages.success(request, "You must be logged in...!")
        return redirect('home')



def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        return redirect('home')
    
    else:
        return redirect('home')
    


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        return redirect('home')