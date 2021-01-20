from django.shortcuts import render, redirect
from django.contrib import messages

from convention.forms import AttendeeForm, StudentDelegateForm


def convention_page(request):
    if request.method == 'POST':
        form = AttendeeForm(request.POST)
        if form.is_valid():
            attendee = form.save(commit=False)
            attendee.save()
            messages.success(request, 'Your registration is successful')
            return redirect('convention')
    else:
        form = AttendeeForm()
    return render(request, 'convention/convention.html', {'form': form})


def student_delegate(request):
    if request.method == 'POST':
        form = StudentDelegateForm(request.POST, request.FILES or None)
        if form.is_valid():
            delegate = form.save(commit=False)
            delegate.save()
            messages.success(request, 'Your registration is successful')
            return redirect('confirmation')
    else:
        form = StudentDelegateForm()
    return render(request, 'convention/delegate.html', {'form': form})
