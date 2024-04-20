from django.shortcuts import render, redirect
from django.contrib.auth import login as visitor_login, logout as visitor_logout, authenticate
from django.contrib import messages
from .forms import *
from .models import *
from TourDash.views import *
from TourETAPP.decorators import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import requests
from django.core.mail import EmailMessage
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def contact(request):

  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data['name'] 
      email = form.cleaned_data['email']
      message = form.cleaned_data['message']
      mail = EmailMessage(
          'New contact form submission',  
          f'From: {name} <{email}>\n\n{message}',
          'TourET@email.com',
          ['amankelil36@gmail.com'],
      )
      mail.send()
      messages.success(request, 'Message sent successfully!')
      return render(request, 'contact.html')
    else:
      messages.error(request, form.errors)
  form = ContactForm()
  return render(request, 'contact.html', {'form': form})



def visit_login(request):
    form = Visitor_Login(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
         email = form.cleaned_data['email']
         password = form.cleaned_data['password']
         user = authenticate(request, email=email, password=password)
         if (user is not None and user.is_superuser):
             visitor_login(request, user)
             return redirect('Tour_admin')
         elif user is not None and user.is_visitor:
              visitor_login(request, user)
              return redirect('create_destination')
         else:
            messages.error(request, 'Invalid Password or Email')
    return render(request, 'login.html', {'form': form})

def logout(request):
    visitor_logout(request)
    return redirect('index')


def register(request):
    form = SiteRegistrationForm()
    if request.method == 'POST':
       form = SiteRegistrationForm(request.POST, request.FILES)
       if form.is_valid():
           visitor = form.save(commit=False)
           visitor.is_visitor = True
           visitor.save()
           return redirect('login')
       else:
           form = SiteRegistrationForm()

    return render(request, 'register.html', {'form': form})

@login_required
def destinations(request):
    destinations = Destination.objects.all()
    return render(request, 'destinations.html', {'destinations': destinations})

@login_required
def bookatour(request):
    return render(request, 'bookatour.html')


@login_required
def packages(request):
    search_query = request.GET.get('destination', '')
    package_list = Package.objects.filter(Q(name__icontains=search_query))
    destinations = Destination.objects.all()
    context = {'package_list': package_list, 'destinations': destinations, 'search_query': search_query}
    return render(request, 'packages.html', context)

@login_required
def create_package(request):
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES)
        if form.is_valid():
            package = form.save()
            messages.success(request, 'Package created successfully.')
            return redirect('packages')
        else:
            messages.error(request, 'Failed to create the package. Please check the form.')
            print(request.POST)  # Print the form data
            print(form.errors)
    else:
        form = PackageForm()

    return render(request, 'create_package.html', {'form': form})

@login_required
def create_destination(request):
    user_profile = UserProfile.objects.get(user=request.user)
    users = CustomUser.objects.all()
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            destination = form.save()

            destination_name = destination.name
            image_file = destination.image.path

            # Prepare the message text for Telegram
            text = f"New destination created:\nName: {destination_name}\n"

            # Telegram API configuration
            bot_token = '5832052126:AAG8nj_5pBVXiCj2YMT6_GwD3yMw8jK5h5I'
            chat_id = '-1001818226737'
            url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
            data = {
                'chat_id': chat_id,
                'text': text
            }
            files = {
                'photo': open(image_file, 'rb')
            }

            # Send the data to the Telegram channel
            response = requests.post(url, data=data, files=files)

            return redirect('destinations')
    else:
        form = DestinationForm()
    context = {
        'users': users,
        'form': form,
        'request': request,
        'user_profile': user_profile
    }

    return render(request, 'profile.html', context)


@login_required
def update_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')  # Add success message
            return redirect('create_destination')
    else:
        form = ProfileForm(instance=user_profile)

    context = {
        'form': form,
    }
    return render(request, 'update_profile.html', context)