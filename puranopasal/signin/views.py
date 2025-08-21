from django.shortcuts import render, redirect
from django.contrib import messages
from electronic.models import Account  
from electronic.models import Product
from django.contrib.auth.hashers import make_password, check_password  # Import for password hashing
from datetime import date

import re
def signinpage_btn(request):
    if request.method == 'POST':
        today_date = date.today()
        valuebtn = request.POST.get('submit')

        try:
            account = Account.objects.get(phonenumber=request.session.get('phonenumber', None))
            prdt = Product.objects.all()

            if not valuebtn:
                print("None")
                return render(request, "userads.html", {'acct': account, 'prdsl': prdt, "today_date": today_date})

            if valuebtn == "All":
                return render(request, "userall.html", {'acct': account, 'prdsl': prdt, "today_date": today_date})

            if valuebtn == "Sold":
                return render(request, "usersold.html", {'acct': account, 'prdsl': prdt, "today_date": today_date}) 
            if valuebtn == "Expire":
                return render(request, "userexpire.html", {'acct': account, 'prdsl': prdt, "today_date": today_date}) 

        except Exception as e:
            print(f"Error: {e}")
            return render(request, "signinpage01.html", {'acct': account, 'prdsl': prdt, "today_date": today_date})
    else:
        return render(request, "signinpage01.html", {'acct': None, 'prdsl': None, "today_date": date.today()})

    
def signin(request):
    today_date = date.today() 
    if request.method == 'POST':
        phone_number= request.POST['number']
        pssd = request.POST['password']

        pattnum = r'^[0-9]+$'
        if not phone_number:
            if not pssd:
                return render(request, 'signin01.html',{'errs':'fill phonenumber and password'})

        if not phone_number:
            return render(request, 'signin01.html',{'errs':'fill phonenumber and password'})

        if not pssd:
            return render(request, 'signin01.html',{'errs':'fill phonenumber and password'})
        
        try:
            account = Account.objects.get(phonenumber=phone_number)

            if check_password(pssd, account.password):  # Validate the password
                request.session['phonenumber']=account.phonenumber
                request.session['password']=account.password
                request.session['first_name']=account.first_name
                account = Account.objects.get(phonenumber=phone_number)

                try:
                    prdt = Product.objects.all()
                    return render(request, "signinpage01.html", {'acct':account,'prdsl':prdt,"today_date": today_date})
      


                except:
                    return render(request, "signinpage01.html", {'acct':account})
                

            else:
                return render(request, 'signin01.html',{'errs':'Incorrect password'})

        except Account.DoesNotExist:
            messages.error(request, 'Phone number not found.')
            return render(request, 'signin01.html',{'errs':'Phone number not found'})

    ##return render(request, 'signin01.html')
    if 'phonenumber' not in request.session:
        return render(request, "signin01.html")

    return render(request, "signinpage01.html", {'name': request.session['first_name']})

def signinpage(request):
    today_date = date.today() 

    if 'phonenumber' not in request.session:
        return render(request, "signin01.html")
    else:
        if request.method == 'POST':

            first_name = request.POST['firstname']
            middle_name = request.POST['middlename']
            last_name = request.POST['lastname']
            location=request.POST['location']
            img=request.FILES.get('profile_picture')  


            pattern=r"^[a-zA-Z']"
            if not first_name and not last_name and not location:
                if not img :
                    account = Account.objects.get(phonenumber=request.session['phonenumber'])
                    prdt = Product.objects.all()

                    return render(request, 'signinpage01.html',{'acct':account,'prdsl':prdt,"today_date": today_date})



            if not first_name and not last_name and not location:
                if img !="":
                    account = Account.objects.get(phonenumber=request.session['phonenumber'])
                    account.image=img
                    account.save()
                    prdt = Product.objects.all()

                    return render(request, 'signinpage01.html',{'acct':account,'prdsl':prdt,"today_date": today_date})

  
            else:
 
                if first_name != "" and last_name != "" and img is not None and location!="" :
                    if re.match(pattern,first_name):                
                        if re.match(pattern,middle_name) or middle_name == "" :
                            if re.match(pattern,last_name):
                                if re.match(pattern,location):
                                    account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                    if middle_name == "":
                                        account.first_name = first_name
                                        account.last_name = last_name
                                        account.location = location
                                        account.image=img
                                        account.save()
                                        prdt = Product.objects.all()

                                        return render(request, 'signinpage01.html',{'acct':account,'prdsl':prdt,"today_date": today_date})


                                    else:
                                        account.first_name = first_name

                                        account.middle_name = middle_name
                                        account.last_name = last_name
                                        account.location = location
                                        account.image=img
                                        account.save()
                                        prdt = Product.objects.all()

                                        return render(request, 'signinpage01.html',{'acct':account,'prdsl':prdt,"today_date": today_date})



                        

                                else:
                                    account = Account.objects.get(phonenumber=request.session['phonenumber'])
                                    prdt = Product.objects.all()
                                    return render(request, 'signinpage01.html',{'accterr':'please enter word','acct':account,'prdsl':prdt,"today_date": today_date})


                            else:
                                    account = Account.objects.get(phonenumber=request.session['phonenumber'])
                                    prdt = Product.objects.all()
                                    return render(request, 'signinpage01.html',{'accterr':'please enter word','acct':account,'prdsl':prdt,"today_date": today_date})



                        else:
                            account = Account.objects.get(phonenumber=request.session['phonenumber'])
                            prdt = Product.objects.all( )
                            return render(request, 'signinpage01.html',{'accterr':'please enter word','acct':account,'prdsl':prdt,"today_date": today_date})



                    else:
                        account = Account.objects.get(phonenumber=request.session['phonenumber'])
                        prdt = Product.objects.all()
                        return render(request, 'signinpage01.html',{'accterr':'please enter word','acct':account,'prdsl':prdt,"today_date": today_date})


                else:
                    account = Account.objects.get(phonenumber=request.session['phonenumber'])
                    prdt = Product.objects.all( )

                    return render(request, 'signinpage01.html',{'accterr':'fill all','acct':account,'prdsl':prdt,"today_date": today_date})

   
             


        account = Account.objects.get(phonenumber=request.session['phonenumber'])
        prdt = Product.objects.all()

        return render(request, "signinpage01.html", {'acct':account,'prdsl':prdt,"today_date": today_date})


    
def logout(request):
    request.session.flush()  # Clear all session data
    messages.success(request, 'You have been logged out successfully.')
    return render(request, "signin01.html")

