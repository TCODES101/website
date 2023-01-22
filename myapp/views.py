from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import property
from .models import money
from .models import bedsitter
from .models import oneBedroom
import re
from django.db.models import FloatField
from django.db.models.functions import Cast


from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

#lnm
import requests
from . import keys
from datetime import datetime
import base64
from requests.auth import HTTPBasicAuth



def index(request):
    properties = property.objects.all()
    
    bs= bedsitter.objects.annotate( rooms=Cast('available', output_field=FloatField()),).get()

    oneB= oneBedroom.objects.annotate( rooms=Cast('available', output_field=FloatField()),).get()

    
    
    #context={
        #'bsNumber':bs.rooms,
        #'obNumber':oneB.rooms
       # }
    return render(request, 'index.html',{'bsNumber':bs.rooms,'obNumber':oneB.rooms, 'properties':properties})
    
    
    

    


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request,'user.html')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        pl = len(password)
        subject = 'Welcome to JFLATS'
        message = 'we are pleased to have you as our client'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        reg=re.compile('[@_!#$%^&*()~:/\|]')

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('signup')
            elif(pl < 8):
                messages.info(request, 'password must be 8 or more characters')
                return redirect('signup')
            elif reg.search(password)==None:
                messages.info(request, 'password must contain special characters eg. @ # $')
                return redirect('signup')

            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                send_mail(subject, message, from_email,
                          recipient_list, fail_silently=False)
                return redirect('login')

        else:
            messages.info(request, 'Password not the same')
            return redirect('signup')

    else:
        return render(request, 'signUp.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

my_access_token=''
x=''
def user(request):
    global amount
    global date
    
    if request.method == "POST":
        
        global my_access_token 
        global amount
        global phone
        amount = request.POST['amount']
        phone=request.POST['phone']
        date=request.POST['date']
    
        #print(datetime.now())
        #2022-11-07 13:25:15.789877
        #unformatted_time=datetime.now()
        #formatted_time=unformatted_time.strftime('%Y%m%d%H%M%S')
        #print(formatted_time) 
        #20221107133140

       # data_to_encode= keys.business_short_code + keys.lipa_na_mpesa_passkey + formatted_time
        #encoded_string = base64.b64encode(data_to_encode.encode())
        #print(encoded_string)
        #b'MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjIxMTA3MTM0MTE3'
        #decoded_password=encoded_string.decode('utf-8')
        #print(decoded_password)

       # consumer_key =keys.consumer_key
       # consumer_secret=keys.consumer_secret
       # api_URL=(' https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials')
       # r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key,consumer_secret))
        #print(r.json())

        #json_response=r.json()#{'access_token': 'jQPawD8Q6uxkRrQOVHxTK2AVTh7V', 'expires_in': '3599'}

        #my_access_token=json_response['access_token']

        
        characters=len(phone)
        value=int(amount)
        if characters>=3:
            check=phone[0] + phone[1] + phone[2]
            if check!='254':
                messages.info(request,'your phone number must start with 254 and have 12 characters')
                return render(request, 'user.html')
            elif characters>12:
                messages.info(request,'your phone number should not have more than twelve characters')
                return render(request, 'user.html')
            elif characters<12:
                messages.info(request,'your phone number should not have less than twelve characters')
                return render(request, 'user.html')
            elif value<1:
                messages.info(request,'Amount can not be less than zero')
                return render(request, 'user.html')

            else:

            

                def lipa_na_mpesa():
                    global x
                    

                    api_url='https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
                    access_token=my_access_token

                    headers = {
                        'Content-Type': 'application/json',
                        'Authorization': 'Bearer %s' % access_token
                    } 

                    request = {
                        "BusinessShortCode": keys.business_short_code,
                        "Password": decoded_password,
                        "Timestamp": formatted_time,
                        "TransactionType": "CustomerPayBillOnline",
                        "Amount": amount,
                        "PartyA": phone,
                        "PartyB": keys.business_short_code,
                        "PhoneNumber": phone,
                        "CallBackURL": "https://mydomain.com/path",
                        "AccountReference": "JFLATS",
                        "TransactionDesc": "Pay school fees" 
                        }

                    response = requests.post(api_url, json=request, headers=headers)
                    print(response.text)
                    data1=response.json()
                    x=data1['CheckoutRequestID']

            
                    
                    #response

                lipa_na_mpesa()

        




            messages.info(request, 'Check your phone to complete the transaction then click proceed to complete your transaction..')
            return render(request, 'user.html')
        else:
            messages.info(request, 'Phone number incorrect')
            return render(request, 'user.html')

    else:
        return render(request, 'user.html')
        


    
def complete(request):
    if my_access_token=='' and x=='':
        messages.info(request,'Make the transaction  first')
        return render(request,'user.html')
    else:

        def message():
            global y
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer %s' % my_access_token
            }

            request2 = {
                "BusinessShortCode": '174379',
                "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjIxMTEyMTE1MDU2",
                "Timestamp": "20221112115056",
                "CheckoutRequestID": x,
                }

            response = requests.post('https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query', headers = headers, json=request2)
            print(response.text)
            data=response.json()
            print(data)
            y=data['ResultDesc']
            print(y)
        message()
        if (y=="The service request is processed successfully."):
            
            from .models import money
            new_transaction=money(amount=amount,date=date, name=request.user.get_username())
            new_transaction.save()
            messages.info(request,'Transaction complete')
            
            return render(request,'user.html')
        else:
            messages.info(request,'You cancelled the Transaction')
            return render(request,'user.html')
        

def history(request):
    context={}
    transaction=money.objects.filter(name=request.user.get_username())
    context['transaction']=transaction
    return render(request,'History.html',context)
        



   

    
    