from django.shortcuts import render
from electronic.models import Account  # Adjust according to your app name
from django.contrib.postgres.search import SearchVector, SearchQuery
from django.db.models import Q

# Create your views here.

# Create your views here.
from django.shortcuts import render
##from .models import destination
# Create your views here.
from electronic.models import Product
from datetime import date
import re;


def elect(request):
        if 'phonenumber' not in request.session:
                sl=Product.objects.all()
                today_date = date.today()
                return render(request, 'allproductelect.html',{'prdsl':sl,'today_date':today_date})

        else:
                account = Account.objects.get(phonenumber=request.session['phonenumber'])
                sl=Product.objects.all()
                today_date = date.today()
                return render(request, 'allproductelect.html',{'name': account,'prdsl':sl,'today_date':today_date})



def laptop_list(request):
        try:
                account = Account.objects.get(phonenumber=request.session['phonenumber'])
                sl=Product.objects.all()
                today_date = date.today()
                return render(request, 'laptop_list.html',{'name': account,'prdsl':sl,'today_date':today_date})
        except:
                sl=Product.objects.all()
                today_date = date.today()
                return render(request, 'laptop_list.html',{'prdsl':sl,'today_date':today_date})

def mobile_list(request):
        try:
                account = Account.objects.get(phonenumber=request.session['phonenumber'])
                sl=Product.objects.all()
                today_date = date.today()

                return render(request, 'mobile_list.html',{'name': account,'prdsl':sl,'today_date':today_date})
        except:
                sl=Product.objects.all()
                today_date = date.today()

                return render(request, 'mobile_list.html',{'prdsl':sl,'today_date':today_date})
def speaker_list(request):
         try:
                 account = Account.objects.get(phonenumber=request.session['phonenumber'])
                 sl=Product.objects.all()
                 today_date = date.today()

                 return render(request, 'speaker_list.html',{'name': account,'prdsl':sl,'today_date':today_date})
         except:
                 sl=Product.objects.all()
                 today_date = date.today()

                 return render(request, 'speaker_list.html',{'prdsl':sl,'today_date':today_date})
def headphone_list(request):
        try:
                account = Account.objects.get(phonenumber=request.session['phonenumber'])
                sl=Product.objects.all()
                today_date = date.today()

                return render(request, 'headphone_list.html',{'name': account,'prdsl':sl,'today_date':today_date})
        except:
                sl=Product.objects.all()
                today_date = date.today()
                return render(request, 'headphone_list.html',{'prdsl':sl,'today_date':today_date})
def tv_list(request):
         try:
                 account = Account.objects.get(phonenumber=request.session['phonenumber'])
                 sl=Product.objects.all()
                 today_date = date.today()

                 return render(request, 'tv_list.html',{'name': account,'prdsl':sl,'today_date':today_date})
         except:
                 sl=Product.objects.all()
                 today_date = date.today()

                 return render(request, 'tv_list.html',{'prdsl':sl,'today_date':today_date})
        
def refrigerator_list(request):
        try:
                account = Account.objects.get(phonenumber=request.session['phonenumber'])
                sl=Product.objects.all()
                today_date = date.today()

                return render(request, 'refrigerator_list.html',{'name': account,'prdsl':sl,'today_date':today_date})
        except:
                sl=Product.objects.all()
                today_date = date.today()

                return render(request, 'refrigerator_list.html',{'prdsl':sl,'today_date':today_date})
def microoven_list(request):
         try:
                 account = Account.objects.get(phonenumber=request.session['phonenumber'])
                 sl=Product.objects.all()
                 today_date = date.today()

                 return render(request, 'microoven_list.html',{'name': account,'prdsl':sl,'today_date':today_date})
         except:
                 sl=Product.objects.all()
                 today_date = date.today()

                 return render(request, 'microoven_list.html',{'prdsl':sl,'today_date':today_date})
        
def vaccum_list(request):
        try:
                account = Account.objects.get(phonenumber=request.session['phonenumber'])
                sl=Product.objects.all()
                today_date = date.today()

                return render(request, 'vaccum_list.html',{'name': account,'prdsl':sl,'today_date':today_date})
        except:
                sl=Product.objects.all()
                today_date = date.today()

                return render(request, 'vaccum_list.html',{'prdsl':sl,'today_date':today_date})
def iron_list(request):
        try:
                account = Account.objects.get(phonenumber=request.session['phonenumber'])
                sl=Product.objects.all()
                today_date = date.today()

                return render(request, 'iron_list.html',{'name': account,'prdsl':sl,'today_date':today_date})
        except:
                sl=Product.objects.all()
                today_date = date.today()

                return render(request, 'iron_list.html',{'prdsl':sl,'today_date':today_date})
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        middle_name = request.POST['middlename']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirmpassword']
        phone_number = request.POST['phonenumber']  # Ensure this field is in your form
        location = request.POST['location']  # Ensure this field is in your form
        image = request.FILES.get('image')  # Handle file upload

        if password == confirm_password:
            account = Account(
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                phone_number=phone_number,
                password=password,  # Consider hashing this password
                location=location,
                image=image
            )
            account.save()
            messages.success(request, "Account created successfully!")
            return redirect('success_page')  # Change this to your actual redirect
        else:
            messages.error(request, "Passwords do not match.")

    return render(request, 'signup01.html')  # Make sure to adjust the template name


def search_list(request):
        seh=request.POST['search-data']
        today_date = date.today()

        if seh.lower() == "laptop":
                
                sefils = Product.objects.filter(category_name_id=1)
                return render(request,"searchelec.html",{'serlist':sefils,'today_date':today_date})
        elif seh.lower() == "mobile":
                sefil = Product.objects.filter(category_name_id=5)
                return render(request,"searchelec.html",{'serlist':sefil,'today_date':today_date})
      
     
        elif seh.lower() == "speaker":
                sefil = Product.objects.filter(category_name_id=7)
                return render(request,"searchelec.html",{'serlist':sefil,'today_date':today_date})
      
     
        elif seh.lower() == "headphone":
                sefil = Product.objects.filter(category_name_id=2)
                return render(request,"searchelec.html",{'serlist':sefil,'today_date':today_date})
      
     
        elif seh.lower() == "tv"  :
                sefil = Product.objects.filter(category_name_id=8)
                return render(request,"searchelec.html",{'serlist':sefil,'today_date':today_date})
      
     
        elif seh.lower() == "refrigerator" :
                sefil = Product.objects.filter(category_name_id=6)
                return render(request,"searchelec.html",{'serlist':sefil,'today_date':today_date})
      
     
        elif seh.lower() == "microoven"  :
                sefil = Product.objects.filter(category_name_id=4)
                return render(request,"searchelec.html",{'serlist':sefil,'today_date':today_date})
      
     
        elif seh.lower() == "vacuum cleaner" or seh.lower() == "vacuumcleaner"  :
                sefil = Product.objects.filter(category_name_id=9)
                return render(request,"searchelec.html",{'serlist':sefil,'today_date':today_date})
      
     
        elif seh.lower() == "iron" :
                sefil = Product.objects.filter(category_name_id=3)
                return render(request,"searchelec.html",{'serlist':sefil,'today_date':today_date})
      


        else:
                pattern=r"^[a-zA-Z0-9']"
                pattnnum = r'^[0-9]+$'

                if re.match(pattnnum,seh):
                        sefil = Product.objects.filter(price__gte=abs(int(seh)-1000), price__lte=abs(int(seh)+1000))
                        
                        
                        return render(request,"searchelec.html",{'serlist':sefil,'today_date':today_date})
                if re.match(pattern,seh):
                        
                        terms = re.findall(r'\d+|[a-zA-Z]+', seh)
                        numeric_terms = [term for term in terms if term.isdigit()]
                        text_terms = [term.lower() for term in terms if term.isalpha()]

                        # Step 2: Define category name to ID map
                        category_map = {
                        'laptop': 1,
                        'headphone': 2,
                        'iron': 3,
                        'microoven': 4,
                        'mobile': 5,
                        'refrigerator': 6,
                        'speaker': 7,
                        'tv': 8,
                        'vacuum': 9
                        }

                        # Step 3: Split text terms into category and model terms
                        category_ids = []
                        model_text_terms = []

                        for term in text_terms:
                                if term in category_map:
                                        category_ids.append(category_map[term])
                                else:
                                        model_text_terms.append(term)

                        # Step 4: Build query
                        query = Q()

                        # Case 1: Price + Category
                        if numeric_terms and category_ids:
                                for price in numeric_terms:
                                        for cat_id in category_ids:
                                                query |= Q(price=price, category_name_id=cat_id)

                        # Case 2: Price + Model Name
                        elif numeric_terms and model_text_terms:
                                for price in numeric_terms:
                                        for model in model_text_terms:
                                                query |= Q(price=price, model_name__icontains=model)

                        # Case 3: Only Model Name
                        elif model_text_terms:
                                for model in model_text_terms:
                                        query |= Q(model_name__icontains=model)

                        # Case 4: Only Price
                        elif numeric_terms:
                                for price in numeric_terms:
                                        query |= Q(price=price)

                        # Step 5: Execute Query
                        sefil = Product.objects.filter(query)

                                                
                        
                        
                        
                        
                        
                        
                        
                                   
                        return render(request,"searchelec.html",{'serlist':sefil,'today_date':today_date})
                else:
                        if 'phonenumber' not in request.session:
                                return render(request, "electron01.html")
                        account = Account.objects.get(phonenumber=request.session['phonenumber'])

                        return render(request, "electron01.html", {'name': account})