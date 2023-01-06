from django.shortcuts import render,redirect,HttpResponse
from .models import *
from authenticationapp.models import Customer

# Create your views here.

def product(request):
    featuredproduct=Product.objects.filter(catagory='f')
    latestproduct=Product.objects.filter(catagory='l')
    offerproduct=Product.objects.filter(catagory='o')
    context={
        'featuredproduct':featuredproduct,
        'latestproduct':latestproduct,
        'offerproduct':offerproduct
    }

    return render(request,'productapp/e-commerce.html',context)

def productview(request,id):
    a=Product.objects.get(id=id)
    context={
        'a':a
    }
    return render(request,'productapp/productview.html',context)

def addcart(request):
    if request.method=="POST":
        user=request.user
        product_id=request.POST['prod_id']
        prod=Product.objects.get(id=product_id)
        cart=Cart(user=user,product=prod)
        cart.save()
    return redirect('/showcart')


def showcart(request):
    user=request.user
    showcart=Cart.objects.filter(user=user)
    context={
        'showcart':showcart
    }

    amount=0.0
    total_amount=0.0
    tax=70.0
    
    cart_product=[p for p in Cart.objects.all() if p.user==user]
    if cart_product:
        for p in cart_product:
            # print(p.product.price,'ye proce hain')
            print(p,'ye only p hain')
            teampamount=p.product.price
            print('teampamount',teampamount)
            amount=amount+teampamount
            print('amount =',amount)
            total_amount=amount+tax
            print('This is total amoutn',total_amount)
            context={
                'amount':amount,
                'total_amount':total_amount,
                'showcart':showcart
            }
            return render(request,'productapp/cart.html',context)
    else:
        return render(request,'productapp/emptycart.html',context)
    print(cart_product)


    
    # return render(request,'productapp/cart.html',context)

    




def checkout(request):
    user=request.user
    a=Cart.objects.filter(user=user)
    b=Customer.objects.filter(user=user)
    print(a)
    print(b)
    context={
        'a':a,
        'b':b
    }

    return render(request,'productapp/checkout.html',context)


def paymentdone(request):
    usr=request.user
    customer=Customer.objects.filter(user=usr)
    print(customer)
    cart=Cart.objects.filter(user=usr)

    for c in cart:
        Orderplaced(user=usr,customer=customer,product=c.product,quantity=c.quantity)
        c.delete()
    return HttpResponse("Your order successfully ordered")


def header(request):
    return render(request,'productapp/headerandfooter.html')


def men(request):
    return render(request,'productapp/men.html')

def women(request):
    return render(request,'productapp/women.html')

def kids(request):
    return render(request,'productapp/kids.html')

def productdelete(request,id):
    # product=Cart.objects.all()
    # print(product)
    # for i in product:
    #     print(i.id)
    product=Cart.objects.get(id=id)
    print(product)
    product.delete()

    return redirect("/showcart/")
    # return render(request,'productapp/kids.html')