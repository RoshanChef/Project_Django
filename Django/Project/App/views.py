from django.shortcuts import render , HttpResponse , redirect
from .models import register , author , feedback

# Create your views here.

#to show messages  
def first(request):
    return HttpResponse('<h1>this is first page using html and css</h1')

# to show html pages
def second(request): 
    return render(request , 'demo.html')

def table(request):
    a = register.objects.all()
    b = author.objects.all()

    # all the row
    # for i in a:
        # print(i.number)
    return render(request,'table.html' , {'dataFetch':a , 'dataFetch2':b})

def nav(request):
    if 'email' in request.session:
        return render(request,'nav.html' , {'session0':True})
    return render(request,'nav.html' , {'session0':False})

def auth(request):
    if (request.method == 'POST'):
        # table
        a = author()
                    # name attribute value
        a.name = request.POST['name']
                    # for image
        a.post  = request.FILES['img']
        a.save()
        print(request.method)
        return render(request,'auth.html')
    else :
        print(request.method)
        print('error')
        return render(request,'auth.html')


def reg(request):
    if request.method == 'POST':
        b = register()
        # store the data
        b.name = request.POST['name']
        b.number = request.POST['number']
        b.confirm = request.POST['cpass']
        b.password = request.POST['pass']
        b.email = request.POST['email']
        b.address = request.POST['address']

        print(request.method)
        c = register.objects.filter(name=b.name)
        error_msg = None
        if b.email:
            if c : 
                return render(request,'reg.html' , {'save':'Data already exists ... '})
            else:
                if (len(b.number) == 10):
                    if (b.password == b.confirm):
                        b.save()
                        return render(request,'reg.html' , {'save':'Data stored successfully ... '})
                    else:
                        return render(request, 'reg.html',{'save':'Password is not matching'})
                else:
                    error_msg = 'Contact length should be 10 digits'
                    return render(request, 'reg.html',{'error':error_msg})        
        else:
            error_msg = 'Please insert email '
            return render(request,'reg.html',{'error':error_msg})
    else:
        return render(request,'reg.html')
    
def feed(request):
    a = register.objects.get(name='Roshan Kalmathe')
    if request.method == 'POST':
        c = feedback()
        c.name = request.POST['name']
        c.email = request.POST['email']
        c.message = request.POST['mes']
        c.save()
        return render(request,'feed.html',{'feed':a})
    else:
        return render(request,'feed.html',{"feed":a})


def login(request):
    if request.method == 'POST':
        a =  register.objects.get(email = request.POST['email'])
        if a.password == request.POST['pass'] :
            # return render(request, 'nav.html')
                    # see the change in url 
                    # redirect('na me of path in url.py')
            request.session['email'] = a.email
            return redirect('nav')
        else:
            return render(request ,'login.html', {'mes' : "password is incorrect"})
    else:
        return render(request, 'login.html')



        
