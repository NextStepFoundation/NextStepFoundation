from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def enroll(request):

    return render(request, 'enroll.html')

def about(request):
    return render(request, 'about.html')

def success(request):
    return render(request, 'success.html')

def successreg(request):
    return render(request, 'successreg.html')

def successvs(request):
    return render(request, 'successvs.html')
    

def contactus(request):
    return render(request, 'contactus.html')


def terms(request):
    return render(request, 'terms.html')

def privacy(request):
    return render(request, 'privacy.html')

def requestinfo(request):
    if request.method == 'POST':
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        recipient_list = ['konfydentz@gmail.com']
        subject = 'great'
        full_message = f'Name :{name}\nEmail :{email}\n Message :{message}'

        send_mail(
            subject,
            full_message,
            email,
            recipient_list,
            ['konfydentz@gmail.com'],  
        )

        return redirect('success')

    return render(request, 'requestinfo.html')


def register(request):
    if request.method == 'POST':
            occupation = request.POST.get('occupation')
            name = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            pemail = request.POST.get('pname')
            cpemail = request.POST.get('cpname')
            country = request.POST.get('country')
            state = request.POST.get('state')
            zip = request.POST.get('zip')
            phone = request.POST.get('phone')
            program = request.POST.get('program')
            message = request.POST.get('message')
            recipient_list = ['konfydentz@gmail.com']
            subject = 'great'
            full_message = f'Name :{name}\nLname :{lname}\nOccupation :{occupation}\nEmail :{email}\nPemail :{pemail}\nCpemail :{cpemail}\nCountry :{country}\nState :{state}\nZip :{zip}\nPhone :{phone}\nProgram :{program}\nMessage :{message}'

            send_mail(
                subject,
                full_message,
                email,
                recipient_list,
                ['konfydentz@gmail.com'],  
            )

            return redirect('successreg')
    return render(request, 'register.html')


def vs(request):
    if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            sv = request.POST.get('sv')
            country = request.POST.get('country')
            state = request.POST.get('state')
            zip = request.POST.get('zip')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            recipient_list = ['konfydentz@gmail.com']
            subject = 'great'
            full_message = f'Name :{name}\nEmail :{email}\nSv :{sv}\nCountry :{country}\nState :{state}\nZip :{zip}\nPhone :{phone}\nMessage :{message}'

            send_mail(
                subject,
                full_message,
                email,
                recipient_list,
                ['konfydentz@gmail.com'],  
            )
            
            return redirect('successreg')
    return render(request, 'vs.html')

def gmail(request):
    return render(request, 'gmail.html')

def custom_404(request, expection):
    return render(request, '404.html', status=404)





