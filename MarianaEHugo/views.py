from django.shortcuts import render
from .forms import RSVPForm

def home_page_view(request):
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add a message or redirect to a thank you section on the same page
            return render(request, 'MarianaEHugo/home.html', {'form': RSVPForm(), 'success': True})
    else:
        form = RSVPForm()

    return render(request, 'MarianaEHugo/home.html', {'form': form})
