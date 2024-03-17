from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import PatientSignUpForm, DoctorSignUpForm

def patient_signup(request):
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_patient = True
            user.save()
            return redirect('patient_dashboard')
    else:
        form = PatientSignUpForm()
    return render(request, 'signup.html', {'form': form})

def doctor_signup(request):
    if request.method == 'POST':
        form = DoctorSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_doctor = True
            user.save()
            return redirect('doctor_dashboard')
    else:
        form = DoctorSignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_patient:
                return redirect('patient_dashboard')
            elif user.is_doctor:
                return redirect('doctor_dashboard')
    return render(request, 'login.html')
