from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from TaxCreditDatabaseApp.models import Book

# Create your views here.
def home(request):
    return render(request,'home.html')
def searchfromYear(request):
    if request.method == 'POST':
        result_fromyear = request.POST.get('fromyear')
        result_toyear = request.POST.get('toyear')
        try:
            fromyear = Book.objects.values(result_fromyear)[0]
            toyear = Book.objects.values(result_toyear)[0]
            html = ("<H1>Result of Years</H1>", fromyear , toyear)
            return HttpResponse(html)
            # return render(request,'usrd_DLPbyBC.html',html)
        except Book.DoesNotExist:
            return HttpResponse("no such data")
    else:
        return render(request, 'usrd.html')
    # resultsDisplay=Book.objects.all()
    # return render(request,'usrd_DLPbyBC.html',{'Book':resultsDisplay})
 
def usrd_DLPbyBC(request):
    return render(request, 'usrd_DLPbyBC.html')
def usrd(request):
    return render(request,'usrd.html')
def sred(request):
    return render(request,'sred.html')
def one79d(request):
    return render(request,'179d.html')
