from django.shortcuts import render,redirect
from .models import Customer,Product,Order
from .forms import CreateUserForm
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from crmapp.decorater import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractUser,User





@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
@admin_only
def home(request):
    products=Product.objects.all()
    customers=Customer.objects.all()
    all_orders=Order.objects.all()
    orders=Order.objects.all().count()
    pending=Order.objects.filter(status='pending').count()
    deliver=Order.objects.filter(status='delivered').count()
    outdel=Order.objects.filter(status='outfor delivery').count()
    context={
        'all_orders':all_orders,
        'products':products,
        'customers':customers,
        'totel_orders':orders,
        'pending':pending,
        'deliver':deliver,
        'outdel':outdel
    }
    return render(request,'accounts/dashboard.html',context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products=Product.objects.all()
    return render(request,'accounts/product.html',{'products':products})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def orders(request):
    all_orders = Order.objects.all()
    return render(request,'accounts/orders.html',{'all_orders':all_orders})





# ----------Particular Customer--------

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request,pk):
    user=Customer.objects.get(id=pk)
    orders=user.order_set.all()
    totel_orders=len(orders)
    pending = orders.filter(status='pending').count()
    deliver = orders.filter(status='delivered').count()
    outdel = orders.filter(status='outfor delivery').count()
    context = {
        'user':user,
        'orders':orders,
        'totel_orders':totel_orders,
        'pending': pending,
        'deliver': deliver,
        'outdel': outdel
    }
    return render(request,'accounts/customer.html',context)



# ----------All Customers--------

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def all_customers(request):
    all_customers=Customer.objects.all()
    context={'all_customers':all_customers}
    return render(request,'accounts/all_customers.html',context)






# --------Product Add,Update,Delete ------

@login_required(login_url='login')
def add_product(request):
    if request.method=='POST':
        name=request.POST.get('name')
        price=request.POST.get('price')
        des=request.POST.get('des')
        cat=request.POST.get('cat')
        data=Product(
            name=name,
            price=price,
            description=des,
            category=cat
        )
        data.save()
        return redirect('products')

    else:
        return render(request,'accounts/add_product.html')


@login_required(login_url='login')
def update_product(request,pk):
    if request.method=='POST':
        product=Product.objects.get(id=pk)
        product.name=request.POST.get('name')
        product.price=request.POST.get('price')
        product.description=request.POST.get('des')
        product.category=request.POST.get('cat')
        product.save()
        # data=Product(
        #     name=name,
        #     price=price,
        #     description=des,
        #     category=cat
        # )
        # data.save()
        return redirect('products')
    else:
        pro=Product.objects.get(id=pk)
        context={'product':pro}
        return render(request,'accounts/update_product.html',context)

@login_required(login_url='login')
def delete_product(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('products')








# --------Update Orders-----------

@login_required(login_url='login')
def update_order(request,pk):
    if request.method=='POST':
        order = Order.objects.get(id=pk)
        order.status=request.POST.get('status')
        order.save()
        return redirect('home')

    else:
        order = Order.objects.get(id=pk)
        return render(request,'accounts/update_order.html',{'order':order})







# --------Login,Register,Logout---------

@unauthenticated_user        #This is One possibilty of not showning login and logout pages when user logged
def register_view(request):
    form = CreateUserForm()
    context = {'form':form}
    if request.method =="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name='customer')
            user.groups.add(group)
            return redirect('login')
        else:
            return redirect('register')
    else:
        return render(request,'accounts/register.html',context)




@unauthenticated_user
def login_view(request):
    if request.method == "POST":
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        user = authenticate(username = username1, password =password1)
        if user is not None:
            login(request,user)
            messages.success(request,'Login Successfully')
            return redirect('home')
        else:
            messages.warning(request,'Username or Password is Wrong')
    return render(request,'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')








def user_page(request):
    #customer=Customer.objects.get(orders=)
    #context={"customer":customer}
    return render(request, 'accounts/user_page.html')