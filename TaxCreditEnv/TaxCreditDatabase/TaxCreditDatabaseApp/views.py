from django.db.models.expressions import OrderBy
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from TaxCreditDatabaseApp.models import qre
from TaxCreditDatabaseApp.models import credit
from TaxCreditDatabaseApp.models import project_list
from django.db.models import Subquery
from django.db.models import Count
from django.db.models import Sum
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request,'home.html')
def display_credit_by_bc(request):
    if request.method == 'POST':
        result_fromyear = request.POST.get('fromyear')
        result_toyear = request.POST.get('toyear')
        result_sorting = request.POST.get('sorting')
        try:
            if result_sorting == 'select':
                return render(request,'usrd.html')
            
            if result_sorting == 'Distributed Cred - Statistics by BC':

                uniqueBC = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gte=0).values('bc').distinct()
                numberN = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gte=0).values('bc').order_by('bc').annotate(the_count=Count('bc'))
                sumcreditTax = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gte=0).annotate(sum_creditTax=Sum('creditTax'))
                sumallNumber = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gte=0).aggregate(the_count=Count('bc'))
                sumallcreditTax = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gte=0).aggregate(sum_creditTax=Sum('creditTax'))
                return render(request,'credit_by_bc.html',{'uniqueBC': uniqueBC,'numberN': numberN,'sumcreditTax': sumcreditTax,'sumallNumber': sumallNumber, 'sumallcreditTax': sumallcreditTax})
                
            if result_sorting == 'Detailed List of Project by BC':
                showProjects = project_list.objects.filter(year__gte=result_fromyear, year__lte=result_toyear) 
            
                return render(request,'detail_list_project.html',{'showProjects': showProjects})
            
            if result_sorting == 'Qualified Research Expenses - Statistics by BC':

                uniqueBC = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gte=0).values('bc').distinct()
                numberN = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gte=0).values('bc').order_by('bc').annotate(the_count=Count('bc'))
                sumcreditTax = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gte=0).annotate(sum_creditTax=Sum('qreTax'))
                sumallNumber = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gte=0).aggregate(the_count=Count('bc'))
                sumallcreditTax = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gte=0).aggregate(sum_creditTax=Sum('qreTax'))
                return render(request,'qre_by_bc.html',{'uniqueBC': uniqueBC,'numberN': numberN,'sumcreditTax': sumcreditTax,'sumallNumber': sumallNumber, 'sumallcreditTax': sumallcreditTax})

            if result_sorting == 'Distributed Credit - Statistics by BL':
                numberWater = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gte=0,bc__icontains='Water').count()
                numberTransportation = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gte=0,bc__icontains='Transportation').count()
                numberBuildings = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gte=0,bc__icontains='Buildings').count()
                numberEnergyandResources = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gte=0,bc__icontains='Power').count()
                numberEnvironmentalServices = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gte=0,bc__icontains='Environmental Services').count()
                
                sumWaterTax = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gte=0,bc__icontains='Water').aggregate(total=Sum('creditTax'))
                sumTransportationTax = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gte=0,bc__icontains='Transportation').aggregate(total=Sum('creditTax'))
                sumBuildingsTax = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gte=0,bc__icontains='Buildings').aggregate(total=Sum('creditTax'))
                sumEnergyandResourcesTax = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gte=0,bc__icontains='Power').aggregate(total=Sum('creditTax'))
                sumEnvironmentalServicesTax = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gte=0,bc__icontains='Environmental Services').aggregate(total=Sum('creditTax'))
                sumBLnumber = numberWater + numberTransportation + numberBuildings + numberEnergyandResources + numberEnvironmentalServices
                sumBLtax = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gte=0).aggregate(sum_BLtax=Sum('creditTax'))
                return render(request, 'credit_by_bl.html',{'numberWater': numberWater,'numberTransportation': numberTransportation,
                'numberBuildings': numberBuildings,'numberEnergyandResources': numberEnergyandResources, 
                'numberEnvironmentalServices': numberEnvironmentalServices, 'sumWaterTax': sumWaterTax, 'sumTransportationTax': sumTransportationTax,
                'sumBuildingsTax': sumBuildingsTax,'sumEnergyandResourcesTax': sumEnergyandResourcesTax, 'sumEnvironmentalServicesTax': sumEnvironmentalServicesTax,
                'sumBLnumber': sumBLnumber,'sumBLtax': sumBLtax})

            if result_sorting == 'Qualified Research Expenses - Statistics by BL':
                numberWater = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gte=0,bc__icontains='Water').count()
                numberTransportation = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gte=0,bc__icontains='Transportation').count()
                numberBuildings = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gte=0,bc__icontains='Buildings').count()
                numberEnergyandResources = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gte=0,bc__icontains='Power').count()
                numberEnvironmentalServices = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gte=0,bc__icontains='Environmental Services').count()
                
                sumWaterTax = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gte=0,bc__icontains='Water').aggregate(total=Sum('qreTax'))
                sumTransportationTax = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gte=0,bc__icontains='Transportation').aggregate(total=Sum('qreTax'))
                sumBuildingsTax = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gte=0,bc__icontains='Buildings').aggregate(total=Sum('qreTax'))
                sumEnergyandResourcesTax = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gte=0,bc__icontains='Power').aggregate(total=Sum('qreTax'))
                sumEnvironmentalServicesTax = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gte=0,bc__icontains='Environmental Services').aggregate(total=Sum('qreTax'))
                sumBLnumber = numberWater + numberTransportation + numberBuildings + numberEnergyandResources + numberEnvironmentalServices
                sumBLtax = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gte=0).aggregate(sum_BLtax=Sum('qreTax'))
                return render(request, 'qre_by_bl.html',{'numberWater': numberWater,'numberTransportation': numberTransportation,
                'numberBuildings': numberBuildings,'numberEnergyandResources': numberEnergyandResources, 
                'numberEnvironmentalServices': numberEnvironmentalServices, 'sumWaterTax': sumWaterTax, 'sumTransportationTax': sumTransportationTax,
                'sumBuildingsTax': sumBuildingsTax,'sumEnergyandResourcesTax': sumEnergyandResourcesTax, 'sumEnvironmentalServicesTax': sumEnvironmentalServicesTax,
                'sumBLnumber': sumBLnumber,'sumBLtax': sumBLtax})

              






            if result_sorting == 'Qualified Research Expenses - Statistics by BL':
                return render(request, 'qre_by_bl.html' )

           
        except credit.DoesNotExist:
            return HttpResponse("no such data")
    else:
        return render(request, 'usrd.html')
          
    # resultsDisplay = credit.objects.all()
    # return render(request,'credit_by_bc.html',{'credit':resultsDisplay})
 
def usrd_DLPbyBC(request):
    return render(request, 'usrd_DLPbyBC.html')
def usrd(request):
    return render(request,'usrd.html')
def sred(request):
    return render(request,'sred.html')
def one79d(request):
    return render(request,'179d.html')
