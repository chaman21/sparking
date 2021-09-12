from django.http import HttpResponse
from django.shortcuts import render
from banking.models import Customer
from banking.trans import Trans

def home(request):
	return render(request, "index.html")

def customer(request):
	cus = Customer.objects.filter(role = 'cus')
	return render(request, "customer.html", {"data" : cus})

def trans(request):
	cus = Trans.objects.all()
	return render(request, "trans.html", {"data": cus})

def transfer(request):
	a = request.GET["a"]
	name = ''
	if a=='0':
		a=False
		name = False
	else:
	    u = Customer.objects.get(account = a)
	    name = u.name	
	ad = Customer.objects.filter(role= 'admin')	
	return render(request, "transfer.html", {"a":a, "data":ad, "name":name})


def add(request):
	name = request.POST["name"]
	email = request.POST["email"]
	mobile = request.POST["mobile"]
	account = request.POST["account"]
	amount = request.POST["amount"]

	cus = Customer(account = account, name = name, email = email, mobile = mobile, balance = amount, role='cus')
	cus.save()
	return customer(request)

def send(request):
	ad =Customer.objects.get(role='admin')
	account = request.POST["acc"]
	balance = request.POST["amount"]
	cu = Customer.objects.get(account = account)
	cu.balance = str(int(balance) + int(cu.balance))
	cu.save()
	ad.balance = str(int(ad.balance) - int(balance))
	ad.save()
	tr = Trans(account = account, name=cu.name, email=cu.email, mobile=cu.mobile, balance = balance)
	tr.save()
	return trans(request)
	
def delete(request):
    dell = request.GET["del"]
    d = Trans.objects.get(account = dell)
    d.delete()
    return trans(request)  
    




