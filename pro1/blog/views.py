from django.shortcuts import render,get_object_or_404,redirect
from .models  import  card,read,Category
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages
# Create your views here.
def index(request):
    cards = card.objects.all()
    return render(request, 'index.html', {'cards': cards})

def Read(request, read_id):
    read_object = read.objects.get(id=read_id)   
    related_reads = read.objects.filter(name=read_object.name)
    return render(request, 'read.html', {'read': read_object, 'related_reads': related_reads})

def category_view(request, category_id):
    category_instance = get_object_or_404(Category, id=category_id)
    cards = card.objects.filter(category=category_instance)
    return render(request, 'disp.html', {
        'category': category_instance,  # Pass the category for current page
        'cards': cards,  # Pass the related cards
    })

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Send an email (optional, can be customized)
            send_mail(
                f'New message from {name}',
                message,
                email,
                [settings.CONTACT_EMAIL],  # Ensure CONTACT_EMAIL is set in settings.py
                fail_silently=False,
            )
            
            # Flash a success message
            messages.success(request, 'Thank you for your message! We\'ll get back to you soon.')
            
            # Redirect to the index page
            return redirect('index')  # Ensure 'index' is the name of the URL pattern for your index page
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

