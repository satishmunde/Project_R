from django.http import HttpResponse
from django.shortcuts import render,redirect
from Items.models import Item
from Cart.models import UserCart
from Developer.models import Developer
from contact.models import ContactUs
from User_Details.models import UserDtl
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password, check_password
import random
def home(request):

    if request.user.is_anonymous:
        return redirect('/signin')
    
    items = Item.objects.all()
    context={'items':items}


    if request.method == "POST":
        p_id=request.POST["p_id"]
    

        cart = UserCart.objects.create(user = request.user , orderid = "123 ", itemid = p_id,status = "Pending")
        cart.save()


    return render(request,'index.html',context)


    
   
    
    # try :
    #     product =Item.objects.get(pk=p_id)
    #     print("Product found")
    #     #print(quantity*float(product.price))
    #     order = Order(
    #         customerName = str(request.user),
    #         totalPrice   = float((str)(quantity)* (float)((str)(product).price)),
    #         status       ='Pending'

    #     )
    #     order.save()
    #     orderItems =OrderItem(order=order,
    #                           productId    =(str)(product)).save()
    #     messages.success(request,"Added to Cart Successfully!!!")
    #     return HttpResponseRedirect('/')
    # except:
    #     messages.error(request,"Error in adding Product To Cart.")
    #     return HttpResponseRedirect("/")
    

def logoutUser(request):

    logout(request)
    return redirect('/signin')

def aboutus(request):
    return render(request,'team.html')

def cart(request):
    item = UserCart.objects.filter(user = request.user)
    data={
        'product':item
    }
    


    return render(request,'cart.html',data)

def checkout(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address1 = request.POST.get('address1')
        address2= request.POST.get('address2')
        country = request.POST.get('country')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')

        data=UserDtl(fname=fname,lname = lname, phoneNo=phone,email=email, addressLine1=address1, addressLine2=address2, state=state, country=country,zipCode=zipcode)
        data.save()
    return render(request,'checkoutfrom.html')

def team(request):

    dev = Developer.objects.all()
    data={
        'data':dev
    }
    return render(request,'team.html',data)

def contactus(request):

    return render(request,'contactus.html')


def makepayment(request):

    return render(request,'payment.html')

def ordhist(request):

    return render(request,'ordhist.html')

def forgetpass(request):
    print("satish munde")
    if request.method == "POST":
        mailid = request.POST['mail']
        print(mailid)
        print("Hellos")
        if User.email == mailid:
            print("Hello your Email is same")
    return render(request,"forgetpass.html")


def saveEnq(request):
    if request.method == "POST":
        name=request.POST.get('Name')
        phone =request.POST.get('number')
        email  =request.POST.get('Email')
        message =request.POST.get('Message')
        
        cn = ContactUs(name=name,phone=phone,email=email,message=message)
        cn.save()


    return render(request,'contactus.html')


def signin(request):
    if request.method == "POST":
        username = request.POST.get("email")
        pwd = request.POST.get("password")

        user = authenticate(username = username,password=pwd)
        if user is not None:
            login(request,user)
            return redirect("/")
        
        else:
            return redirect('/signin')
        

    return render(request,'signin.html')



def signup(request):
    if request.method=='POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
      
        email=request.POST.get('email')
        pass1=request.POST['pass']
        pass2=request.POST['re-pass']
        # pass1=request.POST.get('pass')
        # pass2=request.POST.get('re-pass')
    
        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            pass1=make_password(request.POST['pass'])

            # return HttpResponse("SucessFull")
            user = User(first_name=fname ,last_name = lname, username= email,email=email,password=pass1)
            user.save()
            return redirect('/')
        



    return render (request,'signup.html')


def new_Arrivals(request):
    return render(request,'items.html')