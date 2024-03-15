from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name']="Devendra"
    # request.session.set_expiry(6)
    # request.session.set_expiry(0)
    return render(request,"sets.html")

def getsession(request):
    name = request.session['name']
    request.session.modified=True
    # name=request.session.get('name',default="Guest")
    msg={'m':'Data is present','n':name}
    return  render(request,'gets.html',msg)
def delsession(request):
    if 'name' in request.session:

        # del request.session['name']
        request.session.flush()
    request.session.clear_expired()
    
    return render(request,"sets.html")