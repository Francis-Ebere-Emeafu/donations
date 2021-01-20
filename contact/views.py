from django.shortcuts import render, redirect
from django.contrib import messages

from contact.forms import ContactForm


def message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your message has been saved!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
