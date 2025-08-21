from django.shortcuts import render, redirect
from django.contrib import messages
from electronic.models import Account  
from electronic.models import Product  
import time
import random
import string
import re
from datetime import date

from django.contrib.auth.hashers import make_password, check_password 

def product_cost(request):

    if request.method == 'POST':

            model_name = request.POST['modelname']
            brand_name = request.POST['brandname']
            category=request.POST['category']
            delivery=request.POST['delivery']
            negotiable=request.POST['negotiable']
            date=request.POST['date']
            expiredate=request.POST['expiredate']
            price=request.POST['price']
            processor=request.POST['processor']
            ram=request.POST['ram']
            HDD=request.POST['HDD']
            screensize=request.POST['screensize']
            battery=request.POST['battery']
            img=request.FILES.get('div_picture')
            idnumber=request.POST['numberid']
            des=request.POST['description']
            numdes=len(des) 
           
            random_suffix = ''.join(random.choices( string.digits, k=4))
            unique_id = f"{random_suffix}"
      
            
            pattern=r"^[a-zA-Z0-9']"
            pattnnum = r'^[0-9]+$'

            if not model_name or not brand_name or not processor or not price or not ram or not screensize or not battery:
                account = Account.objects.get(phonenumber=request.session['phonenumber'])
                return render(request, 'userads.html',{'prderr':'please fill all box','acct':account}) 

            if not idnumber:
                if re.match(pattern,model_name):
                    if re.match(pattern,brand_name):
                        if re.match(pattern,processor):
                            if re.match(pattnnum,price):
                                if re.match(pattern,ram):
                                    if re.match(pattern,HDD):
                                        if re.match(pattern,screensize):
                                            if re.match(pattern,battery):
                                                if numdes<=150:

                                                    prdt = Product(
                                                    model_name = model_name,
                                                    brand_name = brand_name,
                                                    category_name_id = category,
                                                    delivery = delivery,
                                                    negotiable = negotiable,
                                                    date = date,
                                                    expiredate = expiredate,
                                                    price = price,
                                                    processor = processor,
                                                    ram = ram,
                                                    HDD = HDD,
                                                    screensize = screensize,
                                                    battery = battery,
                                                    product_id=unique_id,
                                                    image=img,
                                                    description=des,
                                                    phonenumber=request.session['phonenumber']
                                                    )
                                                    prdt.save()
                                                    try:
                                                        prdt = Product.objects.all( )
                                                        account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                                        return render(request, 'userads.html',{'acct':account,'prdsl':prdt})
                                                    except:
                                                        account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                                        return render(request, 'userads.html',{'acct':account})
                                                else:
                                                    try:
                                                        prdt = Product.objects.all( )
                                                        account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                                        return render(request, 'userads.html',{'prderr':'description:word is more than 20','acct':account,'prdsl':prdt}) 
                                                    except:
                                                        account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                                        return render(request, 'userads.html',{'prderr':'description:word is more than 20','acct':account})      
                                                    
                                            else:
                                               try: 
                                                   prdt = Product.objects.all( )
                                                   account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                                   return render(request, 'userads.html',{'prderr':'battery:please enter word','acct':account,'prdsl':prdt}) 
                                               except:
                                                   account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                                   return render(request, 'userads.html',{'prderr':'battery:please enter word','acct':account}) 


                                        else:
                                            try: 
                                                prdt = Product.objects.all( )
                                                account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                                return render(request, 'userads.html',{'prderr':'screensize:please enter word','acct':account,'prdsl':prdt}) 
                                            except:
                                                account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                                return render(request, 'userads.html',{'prderr':'screensize:please enter word','acct':account}) 
                                    else:
                                        try: 
                                            prdt = Product.objects.all( )
                                            account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                            return render(request, 'userads.html',{'prderr':'HDD:please enter word','acct':account,'prdsl':prdt}) 
                                        except:
                                            account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                            return render(request, 'userads.html',{'prderr':'HDD:please enter word','acct':account}) 
                                else:
                                    try: 
                                        prdt = Product.objects.all( )
                                        account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                        return render(request, 'userads.html',{'prderr':'ram:please enter word','acct':account,'prdsl':prdt}) 
                                    except:
                                        account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                        return render(request, 'userads.html',{'ram:prderr':'ram:please enter word','acct':account})                                 
                            else:
                                try: 
                                    prdt = Product.objects.all( )
                                    account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                    return render(request, 'userads.html',{'prderr':'price:please enter number','acct':account,'prdsl':prdt}) 
                                except:
                                    account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                    return render(request, 'userads.html',{'prderr':'price:please enter number','acct':account})                                 
                        else:
                            try: 
                                prdt = Product.objects.all( )
                                account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                return render(request, 'userads.html',{'prderr':'processor:please enter word','acct':account,'prdsl':prdt}) 
                            except:
                                account = Account.objects.get(phonenumber=request.session['phonenumber'])
                                return render(request, 'userads.html',{'prderr':'processor:please enter word','acct':account}) 

                    else:
                        try:
                           prdt = Product.objects.all( )
                           account = Account.objects.get(phonenumber=request.session['phonenumber'])

                           return render(request, 'userads.html',{'prderr':'brandname:please enter word','acct':account,'prdsl':prdt}) 
                        except:
                            account = Account.objects.get(phonenumber=request.session['phonenumber'])

                            return render(request, 'userads.html',{'prderr':'brandname:please enter word','acct':account})                            
                else:
                    try:
                        prdt = Product.objects.all( )
                        account = Account.objects.get(phonenumber=request.session['phonenumber'])

                        return render(request, 'userads.html',{'prderr':'modelname:please enter word','acct':account,'prdsl':prdt}) 
                    except:
                        account = Account.objects.get(phonenumber=request.session['phonenumber'])

                        return render(request, 'userads.html',{'prderr':'modelname:please enter word','acct':account})         

                
            if idnumber is not None:
                model_name = request.POST['modelname']
                brand_name = request.POST['brandname']
                category=request.POST['category']
                delivery=request.POST['delivery']
                negotiable=request.POST['negotiable']
                date=request.POST['date']
                expiredate=request.POST['expiredate']
                price=request.POST['price']
                processor=request.POST['processor']
                ram=request.POST['ram']
                HDD=request.POST['HDD']
                screensize=request.POST['screensize']
                battery=request.POST['battery']
                img=request.FILES.get('div_picture')  
                des=request.POST['description']
                numdes=len(des)

                random_suffix = ''.join(random.choices( string.digits, k=4))
                unique_id = f"{random_suffix}"

                
                pattern=r"^[a-zA-Z0-9']"
                pattnnum = r'^[0-9]+$'

 


                if re.match(pattern,model_name):
                    if re.match(pattern,brand_name):
                        if re.match(pattern,processor):
                            if re.match(pattnnum,price):
                                if re.match(pattern,ram):
                                    if re.match(pattern,HDD):
                                        if re.match(pattern,screensize):
                                            if re.match(pattern,battery):
                                                if numdes<=150:
                                                    prdt = Product.objects.get(product_id=idnumber)
                                                    prdt.model_name = model_name
                                                    prdt.brand_name = brand_name
                                                    prdt.category_name_id = category
                                                    prdt.delivery = delivery
                                                    prdt.negotiable = negotiable
                                                    prdt.date = date
                                                    prdt.expiredate = expiredate
                                                    prdt.price = price
                                                    prdt.processor = processor
                                                    prdt.ram = ram
                                                    prdt.HDD = HDD
                                                    prdt.screensize = screensize
                                                    prdt.battery = battery
                                                    prdt.image=img
                                                    prdt.description=des
                                                    
                                                    prdt.save()
                                                    try:
                                                        prdt = Product.objects.all( )
                                                        account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                                        return render(request, 'userads.html',{'acct':account,'prdsl':prdt}) 
                                                    except:
                                                        account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                                        return render(request, 'userads.html',{'acct':account}) 
                                                else:
                                                    try:
                                                        prdt = Product.objects.all( )
                                                        account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                                        return render(request, 'userads.html',{'prderr':'description:word is more than 20','acct':account,'prdsl':prdt}) 
                                                    except:
                                                        account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                                        return render(request, 'userads.html',{'prderr':'description:word is more than 20','acct':account})    
                                                    
                                                    
                                                    

                                            else:
                                                try:
                                                    prdt = Product.objects.all( )
                                                    account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                                    return render(request, 'userads.html',{'prderr':'battery:please enter word','acct':account,'prdsl':prdt}) 
                                                except:
                                                    account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                                    return render(request, 'userads.html',{'prderr':'battery:please enter word','acct':account})
                                        else:
                                            try:
                                                prdt = Product.objects.all( )
                                                account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                                return render(request, 'userads.html',{'prderr':'screensize:please enter word','acct':account,'prdsl':prdt}) 
                                            except:
                                                account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                                return render(request, 'userads.html',{'prderr':'screensize:please enter word','acct':account})
                                    else:
                                        try:
                                            prdt = Product.objects.all( )
                                            account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                            return render(request, 'userads.html',{'prderr':'HDD:please enter word','acct':account,'prdsl':prdt}) 
                                        except:
                                            account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                            return render(request, 'userads.html',{'prderr':'HDD:please enter word','acct':account})                                    
                                    
                                    
                                else:
                                    try:
                                        prdt = Product.objects.all( )
                                        account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                        return render(request, 'userads.html',{'prderr':'ram:please enter word','acct':account,'prdsl':prdt}) 
                                    except:
                                        account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                        return render(request, 'userads.html',{'prderr':'ram:please enter word','acct':account})
                                
                                
                                
                                
                                
                            else:
                                try:
                                    prdt = Product.objects.get(phonenumber=request.session['phonenumber'])
                                    account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                    return render(request, 'userads.html',{'prderr':'price:please enter number','acct':account,'prdsl':prdt}) 
                                except:
                                    account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                    return render(request, 'userads.html',{'prderr':'price:please enter number','acct':account})                            
                                                        
                                
                        else:
                            try:
                                prdt = Product.objects.get(phonenumber=request.session['phonenumber'])
                                account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                return render(request, 'userads.html',{'prderr':'processor:please enter word','acct':account,'prdsl':prdt}) 
                            except:
                                account = Account.objects.get(phonenumber=request.session['phonenumber'])

                                return render(request, 'userads.html',{'prderr':'processor:please enter word','acct':account})                        
                        
                        
                    else:
                        try:
                            prdt = Product.objects.get(phonenumber=request.session['phonenumber'])
                            account = Account.objects.get(phonenumber=request.session['phonenumber'])

                            return render(request, 'userads.html',{'prderr':'brandname:please enter word','acct':account,'prdsl':prdt}) 
                        except:
                            account = Account.objects.get(phonenumber=request.session['phonenumber'])

                            return render(request, 'userads.html',{'prderr':'brandname:please enter word','acct':account})                    
                    
                    
                else:
                    try:
                        prdt = Product.objects.get(phonenumber=request.session['phonenumber'])
                        account = Account.objects.get(phonenumber=request.session['phonenumber'])

                        return render(request, 'userads.html',{'prderr':'modelname:please enter word','acct':account,'prdsl':prdt}) 
                    except:
                        account = Account.objects.get(phonenumber=request.session['phonenumber'])

                        return render(request, 'userads.html',{'prderr':'modelname:please enter word','acct':account})                
                
                
                
            else:
                try:
                    prdt = Product.objects.get(phonenumber=request.session['phonenumber'])
                    account = Account.objects.get(phonenumber=request.session['phonenumber'])

                    return render(request, 'userads.html',{'prderr':'please enter word','acct':account,'prdsl':prdt}) 
                except:
                    account = Account.objects.get(phonenumber=request.session['phonenumber'])

                    return render(request, 'userads.html',{'prderr':'please enter word','acct':account})  
            
            
                                    


    else:
        try:
            prdt = Product.objects.get(phonenumber=request.session['phonenumber'])
            account = Account.objects.get(phonenumber=request.session['phonenumber'])

            return render(request, 'userads.html',{'prderr':'please enter word','acct':account,'prdsl':prdt})
        except:
            account = Account.objects.get(phonenumber=request.session['phonenumber'])

            return render(request, 'userads.html',{'prderr':'please enter word','acct':account})                    
                            
                            
def product_sold(request):
    if request.method == 'POST':
        id_number = request.POST['idnumber']
        sold = request.POST['sold']
        action = request.POST.get('submit')

        pattnnum = r'^[0-9]+$'
        if action == "OK":
            if re.match(pattnnum,id_number):
                try:
                    prdt = Product.objects.get(product_id=id_number)
                    prdt.sold = sold
                    prdt.save()
                    account = Account.objects.get(phonenumber=request.session['phonenumber'])
                    return render(request, 'signinpage01.html',{'acct':account}) 
                except:
                    account = Account.objects.get(phonenumber=request.session['phonenumber'])
                    return render(request, 'userads.html',{'prddelerrd':'Does not exist number','acct':account})       

                    
            else:
                account = Account.objects.get(phonenumber=request.session['phonenumber'])

                return render(request, 'userads.html',{'prddelerr':'please enter number','acct':account}) 
            
        if action == "delete":                   
            if re.match(pattnnum,id_number):
                try:
                    prdt = Product.objects.get(product_id=id_number)
                    prdt.delete()
                    account = Account.objects.get(phonenumber=request.session['phonenumber'])
                    return render(request, 'signinpage01.html',{'acct':account})
                except:
                    account = Account.objects.get(phonenumber=request.session['phonenumber'])
                    return render(request, 'userads.html',{'prddelerr':'Does not exist number','acct':account})       

            else:
                account = Account.objects.get(phonenumber=request.session['phonenumber'])

                return render(request, 'userads.html',{'prddelerr':'please enter number','acct':account}) 
    else:
        account = Account.objects.get(phonenumber=request.session['phonenumber'])

        return render(request, 'signinpage01.html',{'acct':account}) 
                            

def product_info(request):
    try:
        account = Account.objects.get(phonenumber=request.session['phonenumber'])
        id = request.GET.get('id')
        prdt = Product.objects.get(product_id=id)
        
    
        return render(request, 'information.html',{'acct':account,'prdsl':prdt}) 
    except:

        id = request.GET.get('id')

        prdt = Product.objects.get(product_id=id)


        return render(request, 'information.html',{'prdsl':prdt}) 
    ## this for sold product##
#def product_usersold(request):
     ##sld = Product.objects.get(phonenumber=request.session['phonenumber'])
     ####account = Account.objects.get(phonenumber=request.session['phonenumber'])

    ## return render(request, 'signinpage01.html',{'acct':account,'sld':sld}) ###