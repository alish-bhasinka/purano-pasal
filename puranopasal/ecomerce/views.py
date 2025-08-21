
# Create your views here.
from django.shortcuts import render
from electronic.models import Account  
from electronic.models import Product  

##from .models import destination
# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404


# Secret key for the eSewa API (Use your actual secret key here)
SECRET_KEY = b"8gBm/:&EnhH.1/q"  # This is your UAT secret key

def home(request):
    if 'phonenumber' not in request.session:
        return render(request, "home02.html")
    account = Account.objects.get(phonenumber=request.session['phonenumber'])


    return render(request, "home02.html", {'name': account})



def payment(request):
   ## amt = request.POST['amt']
    url ="https://uat.esewa.com.np/epay/transrec"
    ##data = {
            ##'amt': amt,
            ##'scd': 'EPAYTEST',
        ##}
    ##response = requests.post(url, data=data)
    ##json_response =xmltodict.parse(response.content)
    ##status = json_response["response"]["response_code"]


    # Do this in production (EXPLAINED BELOW IN DETAIL )
    # Esewa test allows price upto Rs. 100 only 
    # if order.total_price != int(amt):
    #     return redirect("payment_failed")
    id = request.GET.get('id')
    prdt = Product.objects.get(product_id=id)

    return render(request,"payment02.html",{'pp':prdt})

def payment_failed(request):
    return render(request,'payment02.html')

