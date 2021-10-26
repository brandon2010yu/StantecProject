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
def display_usrd_info(request):
    if request.method == 'POST':
        result_fromyear = request.POST.get('fromyear')
        result_toyear = request.POST.get('toyear')
        result_sorting = request.POST.get('sorting')
        if result_sorting == None:
                return render(request, 'usrd.html')
        try:
           
            
            if result_sorting == 'Distributed Cred - Statistics by BC':

                uniqueBC = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0).values('bc').distinct()
                numberN = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0).values('bc').order_by('bc').annotate(the_count=Count('bc'))
                sumcreditTax = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0).annotate(sum_creditTax=Sum('creditTax'))
                sumallNumber = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0).aggregate(the_count=Count('bc'))
                sumallcreditTax = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0).aggregate(sum_creditTax=Sum('creditTax'))
              
                return render(request,'credit_by_bc.html',{'uniqueBC': uniqueBC,'numberN': numberN,'sumcreditTax': sumcreditTax,'sumallNumber': sumallNumber, 'sumallcreditTax': sumallcreditTax})
                
            if result_sorting == 'Detailed List of Project by BC':
                showProjects = project_list.objects.filter(year__gte=result_fromyear, year__lte=result_toyear) 
            
                return render(request,'detail_list_project.html',{'showProjects': showProjects})
            
            if result_sorting == 'Qualified Research Expenses - Statistics by BC':

                uniqueBC = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0).values('bc').distinct()
                numberN = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0).values('bc').order_by('bc').annotate(the_count=Count('bc'))
                sumcreditTax = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0).annotate(sum_creditTax=Sum('qreTax'))
                sumallNumber = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0).aggregate(the_count=Count('bc'))
                sumallcreditTax = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0).aggregate(sum_creditTax=Sum('qreTax'))
                return render(request,'qre_by_bc.html',{'uniqueBC': uniqueBC,'numberN': numberN,'sumcreditTax': sumcreditTax,'sumallNumber': sumallNumber, 'sumallcreditTax': sumallcreditTax})

            if result_sorting == 'Distributed Credit - Statistics by BL':
                numberWater = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0,bl__iexact='Water').count()
                numberTransportation = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0,bl__iexact='Transportation').count()
                numberBuildings = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0,bl__iexact='Buildings').count()
                numberEnvironmentalServices = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0,bl__iexact='Environmental Services').count()
                numberCommunityDevelopment = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0,bl__iexact='Community Development').count()
                numberMining = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0,bl__iexact='Mining').count()
                numberOilandGas = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0,bl__iexact='Oil & Gas').count()
                numberPowerandDams = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0,bl__iexact='Power & Dams').count()
                numberBusinessLineServices = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0,bl__iexact='Business Line Services-US').count()
                numberInnovationOffice = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0,bl__iexact='Innovation Office').count()
                numberFederalProgram = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0,bl__iexact='Federal Program').count()
                numberPracticeServices = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0,bl__iexact='Practice Services').count()
                
                sumWaterTax = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0,bl__icontains='Water').aggregate(total=Sum('creditTax'))
                sumTransportationTax = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0,bl__icontains='Transportation').aggregate(total=Sum('creditTax'))
                sumBuildingsTax = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0,bl__icontains='Buildings').aggregate(total=Sum('creditTax'))
                sumEnvironmentalServicesTax = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0,bl__icontains='Environmental Services').aggregate(total=Sum('creditTax'))
                sumCommunityDevelopmentTax = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0,bl__icontains='Community Development').aggregate(total=Sum('creditTax'))
                sumMiningTax = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0,bl__icontains='Mining').aggregate(total=Sum('creditTax'))
                sumOilandGasTax = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0,bl__icontains='Oil & Gas').aggregate(total=Sum('creditTax'))
                sumPowerandDamsTax = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0,bl__icontains='Power & Dams').aggregate(total=Sum('creditTax'))
                sumBusinessLineServicesTax = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0,bl__icontains='Business Line Services-US').aggregate(total=Sum('creditTax'))
                sumInnovationOfficeTax = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0,bl__icontains='Innovation Office').aggregate(total=Sum('creditTax'))
                sumFederalProgramTax = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0,bl__icontains='Federal Program').aggregate(total=Sum('creditTax'))
                sumPracticeServicesTax = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0,bl__icontains='Practice Services').aggregate(total=Sum('creditTax'))
                
                sumBLnumber = (numberWater + numberTransportation + numberBuildings + numberEnvironmentalServices + numberCommunityDevelopment + numberMining + numberOilandGas
                + numberPowerandDams + numberBusinessLineServices + numberInnovationOffice + numberFederalProgram + numberPracticeServices)
                sumBLtax = credit.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,creditTax__gt=0).aggregate(sum_BLtax=Sum('creditTax'))
                
                return render(request, 'credit_by_bl.html',{'numberWater': numberWater,'numberTransportation': numberTransportation,
                'numberBuildings': numberBuildings,'numberEnvironmentalServices': numberEnvironmentalServices,'numberCommunityDevelopment': numberCommunityDevelopment,
                'numberMining': numberMining,'numberOilandGas': numberOilandGas,'numberPowerandDams': numberPowerandDams
                ,'numberBusinessLineServices': numberBusinessLineServices,'numberInnovationOffice': numberInnovationOffice,'numberFederalProgram': numberFederalProgram
                ,'numberPracticeServices': numberPracticeServices, 'sumWaterTax': sumWaterTax, 'sumTransportationTax': sumTransportationTax,
                'sumBuildingsTax': sumBuildingsTax, 'sumEnvironmentalServicesTax': sumEnvironmentalServicesTax,'sumCommunityDevelopmentTax': sumCommunityDevelopmentTax,
                'sumMiningTax': sumMiningTax,'sumOilandGasTax': sumOilandGasTax
                ,'sumPowerandDamsTax': sumPowerandDamsTax,'sumBusinessLineServicesTax': sumBusinessLineServicesTax,'sumInnovationOfficeTax': sumInnovationOfficeTax,
                'sumFederalProgramTax': sumFederalProgramTax,'sumPracticeServicesTax': sumPracticeServicesTax,
                'sumBLnumber': sumBLnumber,'sumBLtax': sumBLtax})

            if result_sorting == 'Qualified Research Expenses - Statistics by BL':
                numberWater = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0,bl__icontains='Water').count()
                numberTransportation = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0,bl__icontains='Transportation').count()
                numberBuildings = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0,bl__icontains='Buildings').count()
                numberEnvironmentalServices = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0,bl__icontains='Environmental Services').count()
                numberCommunityDevelopment = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0,bl__icontains='Community Development').count()
                numberMining = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0,bl__icontains='Mining').count()
                numberOilandGas = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0,bl__icontains='Oil & Gas').count()
                numberPowerandDams = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0,bl__icontains='Power & Dams').count()
                numberBusinessLineServices = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0,bl__icontains='Business Line Services-US').count()
                numberInnovationOffice = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0,bl__icontains='Innovation Office').count()
                numberFederalProgram = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0,bl__icontains='Federal Program').count()
                numberPracticeServices = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0,bl__icontains='Practice Services').count()
                
                sumWaterTax = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0,bl__icontains='Water').aggregate(total=Sum('qreTax'))
                sumTransportationTax = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0,bl__icontains='Transportation').aggregate(total=Sum('qreTax'))
                sumBuildingsTax = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0,bl__icontains='Buildings').aggregate(total=Sum('qreTax'))
                sumEnvironmentalServicesTax = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0,bl__icontains='Environmental Services').aggregate(total=Sum('qreTax'))
                sumCommunityDevelopmentTax = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0,bl__icontains='Community Development').aggregate(total=Sum('qreTax'))
                sumMiningnTax = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0,bl__icontains='Mining').aggregate(total=Sum('qreTax'))
                sumOilandGasTax = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0,bl__icontains='Oil & Gas').aggregate(total=Sum('qreTax'))
                sumPowerandDamsTax = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0,bl__icontains='Power & Dams').aggregate(total=Sum('qreTax'))
                sumBusinessLineServicesTax = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0,bl__icontains='Business Line Services-US').aggregate(total=Sum('qreTax'))
                sumInnovationOfficeTax = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0,bl__icontains='Innovation Office').aggregate(total=Sum('qreTax'))
                sumFederalProgramTax = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0,bl__icontains='Federal Program').aggregate(total=Sum('qreTax'))
                sumPracticeServicesTax = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0,bl__icontains='Practice Services').aggregate(total=Sum('qreTax'))
                sumBLnumber = (numberWater + numberTransportation + numberBuildings + numberEnvironmentalServices + numberCommunityDevelopment + numberMining + numberOilandGas
                + numberPowerandDams + numberBusinessLineServices + numberInnovationOffice + numberFederalProgram + numberPracticeServices)
                sumBLtax = qre.objects.filter(year__gte=result_fromyear, year__lte=result_toyear,qreTax__gt=0).aggregate(sum_BLtax=Sum('qreTax'))
                
                return render(request, 'qre_by_bl.html',{'numberWater': numberWater,'numberTransportation': numberTransportation,
                'numberBuildings': numberBuildings,'numberEnvironmentalServices': numberEnvironmentalServices,'numberCommunityDevelopment': numberCommunityDevelopment,
                'numberMining': numberMining,'numberOilandGas': numberOilandGas,'numberPowerandDams': numberPowerandDams
                ,'numberBusinessLineServices': numberBusinessLineServices,'numberInnovationOffice': numberInnovationOffice,'numberFederalProgram': numberFederalProgram
                ,'numberPracticeServices': numberPracticeServices, 'sumWaterTax': sumWaterTax, 'sumTransportationTax': sumTransportationTax,
                'sumBuildingsTax': sumBuildingsTax, 'sumEnvironmentalServicesTax': sumEnvironmentalServicesTax,'sumCommunityDevelopmentTax': sumCommunityDevelopmentTax,
                'sumMiningTax': sumMiningnTax,'sumOilandGasTax': sumOilandGasTax
                ,'sumPowerandDamsTax': sumPowerandDamsTax,'sumBusinessLineServicesTax': sumBusinessLineServicesTax,'sumInnovationOfficeTax': sumInnovationOfficeTax,
                'sumFederalProgramTax': sumFederalProgramTax,'sumPracticeServicesTax': sumPracticeServicesTax,
                'sumBLnumber': sumBLnumber,'sumBLtax': sumBLtax})

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
