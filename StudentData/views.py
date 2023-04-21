from django.shortcuts import render,redirect
from .forms  import StudentRegistration
from .models import User
# Create your views here.

def add_show(request):
    if request.method =="POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pw = form.cleaned_data['password']

            reg = User(name=nm, email=em, password=pw)
            reg.save()
            return redirect('/')

    else: 
        form = StudentRegistration()
        stud = User.objects.all()

    return render(request, 'add_show.html', {'form':form, 'student':stud})

def update_data(request, pk):
    if request.method =='POST':
        user = User.objects.get(id=pk)
        form = StudentRegistration(request.POST, instance=user)
        if form.is_valid():
            form.save()

    else:
        user = User.objects.get(id=pk)
        form = StudentRegistration(instance=user)

        return render(request, 'update.html',{'form':form})
    return redirect('/')


def delete_data(request, pk ):
    if request.method =='POST':
        user = User.objects.get(id=pk)
        user.delete()
        return redirect('/')
    return render(request, 'delete.html')
   