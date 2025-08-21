from django.shortcuts import render, redirect
from django.contrib import messages
from electronic.models import Account  # Adjust according to your app name
import re
from django.contrib.auth.hashers import make_password, check_password  # Import for password hashing

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        middle_name = request.POST['middlename']
        last_name = request.POST['lastname']
        password = request.POST['password']
        confirm_password = request.POST['confirmpassword']
        phone_number = request.POST['phonenumber']
        hashed_password = make_password(password)

        pattern=r"^[a-zA-Z']"
        pattnnum = r'^[0-9]+$'
        act = Account.objects.filter(phonenumber=phone_number).first()
        if not first_name:
            if not last_name:
                if not password:
                    if not confirm_password:
                        if not phone_number:
                            return render(request, 'signup01.html',{'err':'fill all box'})  


        if not first_name:
            return render(request, 'signup01.html',{'err':'fill all box'})
        if not last_name:
            return render(request, 'signup01.html',{'err':'fill all box'})
        if not password:
            return render(request, 'signup01.html',{'err':'fill all box'})
        if not confirm_password:
            return render(request, 'signup01.html',{'err':'fill all box'})
        if not phone_number:
            return render(request, 'signup01.html',{'err':'fill all box'})

   

        if re.match(pattern,first_name):
            if re.match(pattern,middle_name) or not middle_name:
                if re.match(pattern,last_name):
                    if re.match(pattnnum,phone_number):
                        if len(phone_number)==10:

                            if password == confirm_password:
                                if act:
                                    return render(request, 'signup01.html',{'err':'phonenumber is already exist'}) 
  
                                else:
                                    account = Account(
                                        first_name=first_name,
                                        middle_name=middle_name,
                                        last_name=last_name,
                                        phonenumber=phone_number,
                                        password=hashed_password,  # Consider hashing this password
                                    )
                                    account.save()
                                    messages.success(request, "Account created successfully!")
                                    return redirect('success_page')  # Change this to your actual redirect
                                
                            else:
                                messages.error(request, "Passwords do not match.")
                                return render(request, 'signup01.html',{'err':'password is not correct'})  # Make sure to adjust the template name
                    
                        else:
                            return render(request, 'signup01.html',{'err':'please enter 10 digit phonenumber'}) 
            
                    else:
                        return render(request, 'signup01.html',{'err':'please enter number'}) 

                else:
                    return render(request, 'signup01.html',{'err':'please enter lastname in word'}) 
      
                
            else:
                return render(request, 'signup01.html',{'err':'please enter middlename in word'}) 

        
        else:
            return render(request, 'signup01.html',{'err':'please enter firstname in word'}) 
    if 'phonenumber' not in request.session:
        return render(request, "signup01.html")
    account = Account.objects.get(phonenumber=request.session['phonenumber'])

    return render(request, "signup01.html", {'name': account})

        

def success_view(request):
    return render(request,"signup01.html")
