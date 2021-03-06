from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from. forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth import get_user_model
from .decorators import unauthenticated_user,allowed_users
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta
from accounts.utils import *
import json
from django.db.models import Count, Q, F
import xlwt
from django.contrib.auth.models import User
from xlutils.copy import copy # http://pypi.python.org/pypi/xlutils
from xlrd import open_workbook # http://pypi.python.org/pypi/xlrd
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
import os
import csv
from .filters import *
from accounts.models import Company
 





# Create your views here.
##FUNCTIONS TO GENERATE IDs###########
def get_companyCode():
    company_code=Company.objects.all().order_by('company_code')[0:1]
    for i in company_code:
        if i.company_code is not None:
            return str(i.company_code)
get_companyCode()

def IP_no():
   return str(get_companyCode()+"-IP-Q-"+(date.today()).strftime("%d%m%Y"))+str(randint(0, 999))

def Issue_no():
    return str(get_companyCode()+"-CT-Q-"+(date.today()).strftime("%d%m%Y"))+str(randint(0, 999))

def Regulatory_no():
    return str(get_companyCode()+"-IP-LRO-Q-"+(date.today()).strftime("%d%m%Y"))+str(randint(0, 999))

def Risk_no():
    return str(get_companyCode()+"-RA-"+(date.today()).strftime("%d%m%Y"))+str(randint(0, 999))

def opportunity_no():
    return str(get_companyCode()+"-OPP-"+(date.today()).strftime("%d%m%Y"))+str(randint(0, 999))






###########################post back views#############################################








def load_cities(request):
    country_id = request.GET.get('country')
    print("country_id", country_id)
    cities = City.objects.filter(country_id=country_id).order_by('name')
    print("cities", cities)
    
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})

def load_ids(request):
    context_id = request.GET.get('contextid')
    
    #ids = mod9001_risks.objects.filter(contextdetails_id=context_id)
    #ids = mod9001_issues.objects.all()
    if context_id=="1":
        #print("context_id issues", context_id)
        ids=mod9001_issues.objects.all()
    else:
        #print("context_id pi", context_id)
        ids=mod9001_interestedParties.objects.values(issue_number=F('ip_number'))

    
    return render(request, 'id_dropdown_list_options.html', {'ids': ids})




def load_contextdesc(request):

    context_id = request.GET.get('contextid')
    context = request.GET.get('context')
    #print("context_id description", context_id)
    #print("context", context)
    if context=="1":
        contextdescription = mod9001_issues.objects.values(contextdescription=F('description')).filter(issue_number=context_id)
        #print("contextdescription issue", contextdescription)
    
    else:
        contextdescription = mod9001_interestedParties.objects.values(contextdescription=F('description')).filter(ip_number=context_id)
        #print("contextdescription ip", contextdescription)

    return render(request, 'context_descripton.html', {'contextdescription': contextdescription})



##########################end#############################################
##################### ISSUES VIEWS###########################################
@login_required(login_url='login')
@allowed_users(allowed_roles=['ManagementRepresentative'])
def issues(request):
    form=IssuesForm(initial={'issue_number': Issue_no()})
    
    if request.method=="POST":
        request.POST=request.POST.copy()
        request.POST['entered_by'] = request.user
        request.POST['date_today']=date.today()
        request.POST['status'] = 5
        request.POST['record_group']=my_data_group(request.user) #flaging status as pending car
        #print("issue description", request.POST['issue_description'])
        form=IssuesForm(request.POST)

        
               
        #print("PRINTING CONTEXT",form.date_today, form.added_by, form.responsibility)
        if form.is_valid():
            
            form.save()
            form=IssuesForm(initial={'issue_number': Issue_no()})
            context={'form':form}
            return render(request,'issues.html',context)
            #return redirect('/')
            
            
        form=IssuesForm(request.POST)
        context={'form':form}
        
        return render(request,'issues.html',context)
           
        
    context={'form':form}
    return render(request,'issues.html',context)

@login_required(login_url='login')
def issues_report(request):
    
    issues=mod9001_issues.objects.all() #get all issues in database 
    myFilter=context_issuesFilter(request.GET, queryset=issues)
    issues=myFilter.qs
    if request.method=="POST":
        issues_list = mod9001_issues.objects.all()
        myFilter=context_issuesFilter(request.GET, queryset=issues_list)
        issues=myFilter.qs
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Issues_Register.csv"'

        writer = csv.writer(response)
        writer.writerow(['Id ', 'LeadAnalyst','DateCreated', 'Context','Process','ProcessIssue','Issue Description','Other Issues','Status','ApprovalComment'])

    
        for i in issues:
            if i.process_StrengthWeakness is not None:
                writer.writerow([i.issue_number, i.analyst,i.analysis_date, i.get_context_display(),i.get_process_desc_display(),i.get_process_issues_display(),i.process_StrengthWeakness,i.otherIssue, i.status,i.rejected])
            else:
                writer.writerow([i.issue_number, i.analyst,i.analysis_date, i.get_context_display(),i.get_process_desc_display(),i.get_process_issues_display(),i.process_OpportunitiesThreats,i.otherIssue, i.status,i.rejected])
    

        return response
        
    else:
        return render(request,'issues_report.html',{'issues':issues,'myFilter':myFilter})

@login_required(login_url='login')
def issue_editing(request):
    
    all_issues=mod9001_issues.objects.all() #get all issues in database 
   
    
    context={'all_issues':all_issues} 

    return render(request,'issue editing.html',context)

@login_required(login_url='login')
def deleteissue(request,pk_test):
    deleteissue=mod9001_issues.objects.get(issue_number=pk_test)
    if request.method=="POST":
        deleteissue.delete()
        return redirect('/')

    context={'item':deleteissue}
  
    return render(request,'deleteissue.html',context)


@login_required(login_url='login')
def edit_issue(request,pk_test):
    issue=mod9001_issues.objects.get(issue_number=pk_test)
    form=IssuesEdit(instance=issue)

    if request.method=="POST":
            
            form=IssuesEdit(request.POST, instance=issue)
            if form.is_valid():
                form.save()
                return redirect('/')

    context={'form':form}  


    return render(request,'issues_update.html',context)

@login_required(login_url='login')
def issues_pending(request):
    pendingcar={}
    context={}
    if is_Auditor(request.user):
        #pendingcar=mod9001_qmsplanner.objects.all().filter(status='5').filter(~Q(verification_status='Closed')) #get all qms pending approval    
        #pendingcar=mod9001_changeRegister.objects.filter(status='5').filter(~Q(verification_status='Closed')) #get all planning  pending approval    
        #pendingcar=mod9001_issues.objects.filter(risk_assessment_flag='No').filter(status='1') #get all ip pending approval    
        pendingcar=mod9001_issues.objects.filter(status='5') #get all issues pending approval    
        
    
    if is_Executive(request.user):
        #pendingcar=mod9001_qmsplanner.objects.filter(status='5').filter(planner_user_title=20)     
        #pendingcar=mod9001_changeRegister.objects.filter(status='5') #get all planning  pending approval    
        #pendingcar=mod9001_issues.objects.filter(risk_assessment_flag='No').filter(status='1')#get all ip pending approval    
        pendingcar=mod9001_issues.objects.filter(status='5') #get all issues pending approval    
       
    
    
    
    
    #pendingcar=mod9001_issues.objects.filter(status='5').filter(record_group=my_data_group(request.user)) #get all issues pending approval    
    context={'pendingcar':pendingcar} 
    return render(request,'issues_pending.html',context)

@login_required(login_url='login')
def issues_rejected(request):
    pendingcar=mod9001_issues.objects.all().filter(date_today__gte=datetime.now() - timedelta(days=7)).filter(status='4') #get all issues rejected    
    context={'pendingcar':pendingcar} 
    return render(request,'issues_rejected.html',context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['TopManager'])
def approve_issue(request,pk_test):
    pending_issue=mod9001_issues.objects.get(issue_number=pk_test)
    form=ApproveIssue(instance=pending_issue)

    if request.method=="POST":

            
            
                      
            request.POST=request.POST.copy()
            request.POST['approved_by']=request.user
            request.POST['approval_date']=date.today()
            form=ApproveIssue(request.POST, instance=pending_issue)
            #print("TESTING FORM",request.POST)
            if form.is_valid():
                form.save()
                return redirect('/issues_pending/')

    context={'form':form,'pk_test':pk_test}  


    return render(request,'issue_approve.html',context)

    ########################END OF ISSUES VIEWS#########################################

#############INTERESTED PARTIES VIEWS##########################################

@login_required(login_url='login')
@allowed_users(allowed_roles=['ManagementRepresentative'])
def interested_parties(request):
    form=interestedPartiesFORM(initial={'ip_number': IP_no()})
   
    if request.method=="POST":
        request.POST=request.POST.copy()
        request.POST['entered_by'] = request.user
        request.POST['date_today']=date.today()
        request.POST['status'] = 5 #flaging status as pending car
        request.POST['record_group']=my_data_group(request.user)
        form=interestedPartiesFORM(request.POST)
        #print("PRINTING GROUP",my_data_group(request.POST['responsibility']))
               
        
        if form.is_valid():
            
            form.save()
            #return redirect('/')
            form=interestedPartiesFORM(initial={'ip_number': IP_no()})
            context={'form':form}
            return render(request,'interestedparties.html',context)
            
            
        form=interestedPartiesFORM(request.POST)
        context={'form':form}
        
        return render(request,'interestedparties.html',context)
           
        
    context={'form':form}
    return render(request,'interestedparties.html',context)

@login_required(login_url='login')
def ip_report(request):
    
    ips=mod9001_interestedParties.objects.all() #get all ips in database 
    myFilter=context_ipFilter(request.GET, queryset=ips)
    ips=myFilter.qs
    if request.method=="POST":
        ips_list = mod9001_interestedParties.objects.all()
        myFilter=context_ipFilter(request.GET, queryset=ips_list)
        ips=myFilter.qs
        print("PRINTING",ips)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="IPs.csv"'

       # wb = xlwt.Workbook(encoding='utf-8')
        #ws = wb.add_sheet('Users')

        #row_num = 0
        #font_style = xlwt.XFStyle()
        #font_style.font.bold = True


        writer = csv.writer(response)
        writer.writerow(['IP Number', 'LeadAnalyst','Context', 'Interested Party','Requirement','Description','Ip to Co.','Co. to IP','Priority','ActionTaken','OtherAction','Responsibility',
'ApprovalComment','When','Status'])


    
        for i in ips:
            if (i.get_internal_issues_display()) is not None :
                writer.writerow([i.ip_number, i.analyst, i.get_context_display(),i.get_internal_issues_display(),i.get_quality_needs_display(),i.description,i.get_interestedparties_display(),i.get_companyinterestedparties_display(),i.get_priority_display(),i.get_actiontaken_display(),i.actionOther,i.responsibility,i.rejected,
i.due,i.status])
            else:
                writer.writerow([i.ip_number, i.analyst, i.get_context_display(),i.get_external_issues_display(),i.get_quality_needs_display(),i.description,i.get_interestedparties_display(),i.get_companyinterestedparties_display(),i.get_priority_display(),i.get_actiontaken_display(),i.actionOther,i.responsibility,i.rejected,
i.due,i.status])
        
        
        return response
        
    else:
        return render(request,'ip_report.html',{'ips':ips,'myFilter':myFilter})

@login_required(login_url='login')
def ip_editing(request):
    
    all_ips=mod9001_interestedParties.objects.all() #get all ips in database 
   
    
    context={'all_ips':all_ips} 

    return render(request,'ip editing.html',context)

@login_required(login_url='login')
def edit_ip(request,pk_test):
    ip=mod9001_interestedParties.objects.get(ip_number=pk_test)
    form=IPEdit(instance=ip)

    if request.method=="POST":
            #print('Printing ips:', request.POST)
            form=IPEdit(request.POST, instance=ip)
            if form.is_valid():
                form.save()
                return redirect('/')

    context={'form':form}  


    return render(request,'ip_update.html',context)

@login_required(login_url='login')
def deleteip(request,pk_test):
    deleteip=mod9001_interestedParties.objects.get(ip_number=pk_test)
    if request.method=="POST":
        deleteip.delete()
        return redirect('/')

    context={'item':deleteip}
  
    return render(request,'deleteip.html',context)

@login_required(login_url='login')
def ip_pending(request):
    pendingcar={}
    context={}
    if is_Auditor(request.user):
        #pendingcar=mod9001_qmsplanner.objects.all().filter(status='5').filter(~Q(verification_status='Closed')) #get all qms pending approval    
        #pendingcar=mod9001_changeRegister.objects.filter(status='5').filter(~Q(verification_status='Closed')) #get all planning  pending approval    
        pendingcar=mod9001_interestedParties.objects.filter(status='5').filter(~Q(status=1)) #get all ip pending approval    
        
    
    if is_Executive(request.user):
        #pendingcar=mod9001_qmsplanner.objects.filter(status='5').filter(planner_user_title=20)     
        #pendingcar=mod9001_changeRegister.objects.filter(status='5') #get all planning  pending approval    
        pendingcar=mod9001_interestedParties.objects.filter(status='5')#get all ip pending approval    
  
    context={'pendingcar':pendingcar} 
    return render(request,'ip_pending.html',context)

@login_required(login_url='login')
def ip_rejected(request):
    pendingcar= mod9001_interestedParties.objects.all().filter(date_today__gte=datetime.now() - timedelta(days=7)).filter(status='4')   
    context={'pendingcar':pendingcar} 
    return render(request,'ip_rejected.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['TopManager'])
def approve_ip(request,pk_test):
    pending_ip=mod9001_interestedParties.objects.get(ip_number=pk_test)
    
    form=ApproveIp(instance=pending_ip)
    
    
   

    if request.method=="POST":


            
            
                      

            request.POST=request.POST.copy()
            request.POST['approved_by']=request.user
            request.POST['approval_date']=date.today()
            form=ApproveIp(request.POST, instance=pending_ip)
            #print("TESTING FORM",request.POST)
            if form.is_valid():
                #print("TESTING ip_APPROVAL before")
                form.save()
                #print("TESTING ip_APPROVAL after")
                return redirect('/ip_pending/')
            #print("FAILED")
    
    context={'form':form,'pk_test':pk_test}  


    return render(request,'ip_approve.html',context,)


    ############# END IP VIEWS#################################

    ###############   REGULATORY REQUIREMENTS      ###############

@login_required(login_url='login')
@allowed_users(allowed_roles=['ManagementRepresentative'])
def regulatory_requirement(request):
    form=regulatoryRequirmentFORM(initial={'regulatory_number': Regulatory_no()})
    
    if request.method=="POST":
        request.POST=request.POST.copy()
        request.POST['entered_by'] = request.user
        request.POST['date_today']=date.today()
        request.POST['status'] = 5 #flaging status as pending car
        request.POST['record_group']=my_data_group(request.user)

        form=regulatoryRequirmentFORM(request.POST)
               
        
        if form.is_valid():
            
            form.save()
            form=regulatoryRequirmentFORM(initial={'regulatory_number': Regulatory_no()})
            context={'form':form}
            return render(request,'regulatoryrequirement.html',context)
            #return redirect('/')
            
            
        form=regulatoryRequirmentFORM(request.POST)
        context={'form':form}
        
        return render(request,'regulatoryrequirement.html',context)
           
        
    context={'form':form}
    return render(request,'regulatoryrequirement.html',context)

@login_required(login_url='login')
def regulatory_report(request):
    
    regulatory=mod9001_regulatoryReq.objects.all() #get all issues in database 
    myFilter=context_regulatoryFilter(request.GET, queryset=regulatory)
    regulatory=myFilter.qs
    if request.method=="POST":
        regulatory_list = mod9001_regulatoryReq.objects.all()
        myFilter=context_regulatoryFilter(request.GET, queryset=regulatory_list)
        regulatory=myFilter.qs
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="compliance_Register.csv"'

        writer = csv.writer(response)
        writer.writerow(['Reg. Id', 'Analyst', 'Requirement', 'OtherRequirement','Description','Document','InterestedParty','Details','Responsibility',
'ApprovalComment','Start Date','End Date','Status'])

    
        for i in regulatory:
            
            writer.writerow([i.regulatory_number, i.analyst,  i.cat_name,i.otherCategory,i.description,i.document,i.interestedparty,i.otherInterestedParty,i.responsibility,
i.rejected,i.registered,i.due,i.status])
        return response
        
    else:
        return render(request,'regulatory_report.html',{'issues':regulatory,'myFilter':myFilter})



@login_required(login_url='login')
def regulatory_editing(request):
    
    all_reg=mod9001_regulatoryReq.objects.all() #get all issues in database 
   
    
    context={'all_reg':all_reg} 

    return render(request,'regulatory editing.html',context)    

@login_required(login_url='login')
def edit_regulatoryreq(request,pk_test):
    id=mod9001_regulatoryReq.objects.get(regulatory_number=pk_test)
    form=regulatoryreqEdit(instance=id)

    if request.method=="POST":
            
            form=regulatoryreqEdit(request.POST, instance=id)
            if form.is_valid():
                form.save()
                return redirect('/')

    context={'form':form}  


    return render(request,'regulatory_update.html',context)


@login_required(login_url='login')
def deleteregulatory(request,pk_test):
    deleteid=mod9001_regulatoryReq.objects.get(regulatory_number=pk_test)
    if request.method=="POST":
        deleteid.delete()
        return redirect('/')

    context={'item':deleteid}
  
    return render(request,'deleteregulatory.html',context)

@login_required(login_url='login')
def requirement_pending(request):
    pendingcar={}
    context={}
    if is_Auditor(request.user):
        #pendingcar=mod9001_qmsplanner.objects.all().filter(status='5').filter(~Q(verification_status='Closed')) #get all qms pending approval    
        #pendingcar=mod9001_changeRegister.objects.filter(status='5').filter(~Q(verification_status='Closed')) #get all planning  pending approval    
        #pendingcar=mod9001_interestedParties.objects.filter(status='5').filter(~Q(status=1)) #get all ip pending approval    
        pendingcar=mod9001_regulatoryReq.objects.filter(status='5') #get all requirement pending approval    
        
    
    if is_Executive(request.user):
        pendingcar=mod9001_regulatoryReq.objects.filter(status='5')#get all requirement pending approval    
       
    
    
    
    
    #pendingcar=mod9001_regulatoryReq.objects.filter(status='5').filter(record_group=my_data_group(request.user)) #get all requirement pending approval    
    context={'pendingcar':pendingcar} 
    return render(request,'requirement_pending.html',context)


@login_required(login_url='login')
def requirement_rejected(request):
    pendingcar=mod9001_regulatoryReq.objects.filter(date_today__gte=datetime.now() - timedelta(days=7)).filter(status='4').order_by('responsibility') #get all requirement rejected    
    context={'pendingcar':pendingcar} 
    return render(request,'requirement_rejected.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['TopManager'])
def approve_requirement(request,pk_test):
    pending_requirement=mod9001_regulatoryReq.objects.get(regulatory_number=pk_test)
    form=ApproveRequirement(instance=pending_requirement)

    if request.method=="POST":

            
            
                      

            request.POST=request.POST.copy()
            request.POST['approved_by']=request.user
            request.POST['approval_date']=date.today()
            form=ApproveRequirement(request.POST, instance=pending_requirement)
            if form.is_valid():
                form.save()
                return redirect('/requirement_pending/')

    context={'form':form,'pk_test':pk_test}  


    return render(request,'requirement_approve.html',context)

    ###############   RISKS     ###############
#lookup for context description based on selected context ID
def load_issue_description(request):
    context_id = request.GET.get('issue_number')
    #print("request.GET",request.GET)
    #print("context_id",context_id)
    issue_description = mod9001_issues.objects.filter(issue_number=context_id)
    messages.success(request, 'Form submission successful')


@login_required(login_url='login')
def issues_pending_risk_assesment(request):
    pendingcar={}
    context={}
    if is_Auditor(request.user):
        #pendingcar=mod9001_qmsplanner.objects.all().filter(status='5').filter(~Q(verification_status='Closed')) #get all qms pending approval    
        #pendingcar=mod9001_changeRegister.objects.filter(status='5').filter(~Q(verification_status='Closed')) #get all planning  pending approval    
        pendingcar=mod9001_issues.objects.filter(risk_assessment_flag='No').filter(status='1') #get all ip pending approval    
        
    
    if is_Executive(request.user):
        #pendingcar=mod9001_qmsplanner.objects.filter(status='5').filter(planner_user_title=20)     
        #pendingcar=mod9001_changeRegister.objects.filter(status='5') #get all planning  pending approval    
        pendingcar=mod9001_issues.objects.filter(risk_assessment_flag='No').filter(status='1')#get all ip pending approval    
      
    
    
    
    
    
    #pendingcar=mod9001_issues.objects.filter(risk_assessment_flag='No').filter(status='1').filter(record_group=my_data_group(request.user)) #get all customer survey missing improvement plan  entries  
    context={'pendingcar':pendingcar} 
    return render(request,'issues_pending_risk_assessment.html',context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['ManagementRepresentative'])
def risks(request,issue_number):
    form=risk(initial={'risk_number': Risk_no(),'issue_number':issue_number})
    
    
    if request.method=="POST":
        request.POST=request.POST.copy()
        request.POST['entered_by'] = request.user
        request.POST['date_today']=date.today()
        request.POST['status'] = 5 #flaging status as pending risk
        request.POST['record_type'] = "RISK" #specifiing type of entry
        request.POST['record_group']=my_data_group(request.user)
        if request.POST['contextdetails']=="1":

            request.POST['ip_number']="" #set ip_number to missing

            
        else:
            request.POST['ip_number']=request.POST['issue_number'] #save ip number 
            request.POST['issue_number']="" #set issue number to missing, remember ip and issue number are selected by same dropdown combo

        if is_Marketing(request.user):#assign record to a group
            request.POST['record_group']="Marketing"
        elif is_Accounts(request.user):
            request.POST['record_group']="Accounts"
        elif is_Operations(request.user):
            request.POST['record_group']="Operations"
        elif is_Administration(request.user):
            request.POST['record_group']="Administration"
        elif is_Technical(request.user):
            request.POST['record_group']="Technical"
        else:
            request.POST['record_group']=""
           
        form = risk(request.POST)
        
         
            
        
        if form.is_valid():
           
            
            form.save()
            form=risk(initial={'risk_number': Risk_no()})
            context={'form':form}
            return render(request,'risks.html',context)
           
            #return redirect('/')
            
            
        form=risk(request.POST)
        context={'form':form}
        
        return render(request,'risks.html',context)
           
        
    context={'form':form}
    return render(request,'risks.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['ManagementRepresentative'])
def risk_assessed(request):
    form = risk()

    
    
    if request.method=="POST":
        request.POST=request.POST.copy()
        request.POST['entered_by'] = request.user
        request.POST['date_today']=date.today()
        request.POST['status'] = 5 #flaging status as pending risk
        request.POST['record_type'] = "RISK" #specifiing type of entry
        request.POST['contextdetails']="1"
        if request.POST['contextdetails']=="1":

            request.POST['ip_number']="" #set ip_number to missing

            
        else:
            request.POST['ip_number']=request.POST['issue_number'] #save ip number 
            request.POST['issue_number']="" #set issue number to missing, remember ip and issue number are selected by same dropdown combo


           
        form = risk(request.POST)
        
         
            
        
        if form.is_valid():
           
            
            form.save()
            return redirect('/issues_pending_risk_assesment/')

           
            #return redirect('/')
            
            
        form=risk(request.POST)
        context={'form':form}
        
        return render(request,'risks.html',context)
           
        
    context={'form':form}
    return render(request,'risks.html',context)



@login_required(login_url='login')
def risks_report(request):

    
    risks=mod9001_risks.objects.filter(record_type='RISK') #get all RISKS in database
  
    
    
    myFilter=planning_opportunityFilter(request.GET, queryset=risks)
    risks=myFilter.qs
    if request.method=="POST":
        risks_list = mod9001_risks.objects.filter(record_type='RISK')
        
        myFilter=planning_opportunityFilter(request.GET, queryset=risks_list)
        risks=myFilter.qs
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="RiskRegister.csv"'

        writer = csv.writer(response)
        writer.writerow(['Risk. No.', 'DateofAnalysis', 'Assessor', 'Context','ContextDescription','SWOT','IssueDesc','Details','RiskDesc.','OtherRiskDes.','LKHD','Severity','Rating','Ranking','RiskTreatment','Mitigation','MitigationDetails','RetentionDetails','Responsility','When','Approval','Verification','ResidueLKHD','ResidueSeverity','ResidueRating','ResidueRank'])

    
        for i in risks:
            if i.issue_number is not None:
                writer.writerow([i.risk_number,i.risk_date,i.assessor,i.issue_number.get_context_display(),i.issue_number.get_process_desc_display(),i.issue_number.get_process_issues_display(),i.issue_number.process_StrengthWeakness,i.issue_number.description,i.riskdescription,i.description,i.likelihood,i.severity,i.riskrating,i.riskrank,i.risktreatment,i.riskmitigation,i.mitigationdesc,i.retainreason,i.responsibility,i.due,i.status,i.verification_status,i.residuelikelihood,i.residueseverity,i.residueriskrating,i.residueriskrank])
            else:
                writer.writerow([i.risk_number,i.risk_date,i.assessor,"","","","","",i.riskdescription,i.description,i.likelihood,i.severity,i.riskrating,i.riskrank,i.risktreatment,i.riskmitigation,i.mitigationdesc,i.retainreason,i.responsibility,i.due,i.status,i.verification_status,i.residuelikelihood,i.residueseverity,i.residueriskrating,i.residueriskrank])
        
                

        return response
        
    else:
        return render(request,'risks_report.html',{'risks':risks,'myFilter':myFilter})




 ###############   OPPORTUNITY     ###############
@login_required(login_url='login')
def issues_pending_opp_assesment(request):
    pendingcar={}
    context={}
    if is_Auditor(request.user):
        pendingcar=mod9001_issues.objects.filter(status='1').filter(risk_assessment_flag='No')#get all issues that have been approved and pending risk assessment    
        
    
    if is_Executive(request.user):
        pendingcar=mod9001_issues.objects.filter(status='1').filter(risk_assessment_flag='No')#get all issues that have been approved and pending risk assessment    
            
    
    
    
    
    
    
    #pendingcar=mod9001_issues.objects.filter(status='1').filter(risk_assessment_flag='No').filter(record_group=my_data_group(request.user))#get all issues that have been approved and pending risk assessment    
    context={'pendingcar':pendingcar} 
    return render(request,'issues_pending_opp_assessment.html',context)







@login_required(login_url='login')
@allowed_users(allowed_roles=['ManagementRepresentative'])
def opportunity(request,issue_number):
    form=risk(initial={'risk_number': opportunity_no(),'issue_number':issue_number})
    
    
    if request.method=="POST":
        request.POST=request.POST.copy()
        request.POST['entered_by'] = request.user
        request.POST['status'] = 5 #flaging status as pending OPP 
        request.POST['record_type'] = "OPP" #specifiing type of entry
        request.POST['riskrank'] = request.POST['opprank'] #specifiing type of entry


        request.POST['date_today']=date.today()
        request.POST['record_group']=my_data_group(request.user)

        if request.POST['contextdetails']=="1":

            request.POST['ip_number']="" #set ip_number to missing

            
        else:
            request.POST['ip_number']=request.POST['issue_number'] #save ip number 
            request.POST['issue_number']="" #set issue number to missing, remember ip and issue number are selected by same dropdown combo


           
        form = risk(request.POST)
         
            
        
        if form.is_valid():
            
            form.save()
            #return redirect('/')
            form=risk(initial={'risk_number': opportunity_no()})
            context={'form':form}
            return render(request,'opportunity.html',context)
            
            
        form=risk(request.POST)
        context={'form':form}
        
        return render(request,'opportunity.html',context)
           
        
    context={'form':form}
    return render(request,'opportunity.html',context)


def opportunity_assessed(request):
    form=risk()
    
    
    if request.method=="POST":
        request.POST=request.POST.copy()
        request.POST['entered_by'] = request.user
        request.POST['status'] = 5 #flaging status as pending OPP 
        request.POST['record_type'] = "OPP" #specifiing type of entry
        request.POST['riskrank'] = request.POST['opprank'] #specifiing type of entry
        request.POST['contextdetails']="1"


        request.POST['date_today']=date.today()
        request.POST['record_group']=my_data_group(request.user)

        if request.POST['contextdetails']=="1":

            request.POST['ip_number']="" #set ip_number to missing

            
        else:
            request.POST['ip_number']=request.POST['issue_number'] #save ip number 
            request.POST['issue_number']="" #set issue number to missing, remember ip and issue number are selected by same dropdown combo


           
        form = risk(request.POST)
         
            
        
        if form.is_valid():
            
            form.save()
            #return redirect('/')
            return redirect('/issues_pending_opp_assesment/')
            
            
        form=risk(request.POST)
        context={'form':form}
        
        return render(request,'opportunity.html',context)
           
        
    context={'form':form}
    return render(request,'opportunity.html',context)   


@login_required(login_url='login')
def opportunity_report(request):

    
    opportunity=mod9001_risks.objects.filter(record_type='OPP') #get all opportunity planner in database
  
    
    
    myFilter=planning_opportunityFilter(request.GET, queryset=opportunity)
    opportunity=myFilter.qs
    if request.method=="POST":
        opportunity_list = mod9001_risks.objects.filter(record_type='OPP')
        
        myFilter=planning_opportunityFilter(request.GET, queryset=opportunity_list)
        opportunity=myFilter.qs
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="OpportunityRegister.csv"'

        writer = csv.writer(response)
        writer.writerow(['OPP. No.', 'DateofAnalysis', 'Assessor', 'Context','ProcessDescription','SWOT','IssueDesc','Details','OPPDescription','LKHD','BENEFIT','Rating','Ranking','PursuitAction','Responsility','When','Approval','Verification','VerificationComment'])

    
        for i in opportunity:
            if i.issue_number is not None:
                writer.writerow([i.risk_number,i.risk_date,i.assessor,i.issue_number.get_context_display(),i.issue_number.get_process_desc_display(),i.issue_number.get_process_issues_display(),i.issue_number.process_StrengthWeakness,i.issue_number.description,i.description,i.likelihood,i.severity,i.riskrating,i.riskrank,i.mitigation,i.responsibility,i.due,i.status,i.verification,i.verification_failed])
            else:
                writer.writerow([i.risk_number,i.risk_date,i.assessor,"","","","","",i.description,i.likelihood,i.severity,i.riskrating,i.riskrank,i.mitigation,i.responsibility,i.due,i.status,i.verification,i.verification_failed])


        return response
        
    else:
        return render(request,'opportunity_report.html',{'opportunity':opportunity,'myFilter':myFilter})




@login_required(login_url='login')
def risk_pending(request):
    pendingcar={}
    context={}
    if is_Auditor(request.user):
     pendingcar=mod9001_risks.objects.filter(status='5',record_type='RISK').filter(~Q(verification_status='Closed')) #get all risk pending approval    
        
    
    if is_Executive(request.user):
     pendingcar=mod9001_risks.objects.filter(status='5',record_type='RISK').filter(~Q(verification_status='Closed')) #get all risk pending approval    
     
    




    context={'pendingcar':pendingcar} 
    return render(request,'risk_pending.html',context)

@login_required(login_url='login')
def opp_pending(request):
    pendingcar={}
    context={}
    if is_Auditor(request.user):
        pendingcar=mod9001_risks.objects.filter(status='5',record_type='OPP').filter(~Q(verification_status='Closed')) #get all opportunity  pending approval    
    if is_Executive(request.user):    
        pendingcar=mod9001_risks.objects.filter(status='5',record_type='OPP').filter(~Q(verification_status='Closed')) #get all opportunity  pending approval      
    
    context={'pendingcar':pendingcar} 
    return render(request,'opp_pending.html',context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['TopManager'])
def approve_risk(request,pk_test):
    pending_risk=mod9001_risks.objects.get(risk_number=pk_test)
    form=ApproveRisk(instance=pending_risk)

    if request.method=="POST":

            
            
            request.POST=request.POST.copy()
            request.POST['approved_by']=request.user
            request.POST['approval_date']=date.today()                      

            form=ApproveRisk(request.POST, instance=pending_risk)
            if form.is_valid():
                form.save()
                return redirect('/risk_pending/')

    context={'form':form,'pk_test':pk_test}  


    return render(request,'risk_approve.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['TopManager'])
def approve_opp(request,pk_test):
    pending_opp=mod9001_risks.objects.get(risk_number=pk_test)
    form=ApproveOpp(instance=pending_opp)

    if request.method=="POST":

            
            
                      
            request.POST=request.POST.copy()
            request.POST['approved_by']=request.user
            request.POST['approval_date']=date.today()
            form=ApproveOpp(request.POST, instance=pending_opp)
            if form.is_valid():
                form.save()
                return redirect('/opp_pending/')

    context={'form':form,'pk_test':pk_test}  


    return render(request,'opp_approve.html',context)

#############################RISK AND OPPORTUNITY VERIFICATION###########################################
def CARnumbers_7days_expire(*x):
    date_str = x[0]
    date_object = datetime.strptime(date_str, '%m/%d/%Y').date()
    delta =date_object - date.today()
    return delta.days

@login_required(login_url='login')
def risks_due(request):
    carExpire7days=mod9001_risks.objects.filter(due__gte=datetime.now() - timedelta(days=7)).filter(status=1,record_type='RISK').filter(~Q(verification=1)).filter(~Q(riskrank='Low')).filter(~Q(risktreatment=2)).filter(~Q(risktreatment=4))
    #carExpire7days=mod9001_risks.objects.all().filter(due__gte=datetime.now() - timedelta(days=7)).filter(record_type='RISK').filter(status='1').filter(~Q(verification_status='Closed'))
    #thislist = []
   
    #for i in carExpire7days:
        #w=i.due
        #t=w.strftime('%m/%d/%Y')
        #if CARnumbers_7days_expire(t)<0:
    #    thislist.append(i.risk_number)
    #thisdict={}
    #i=0
    #creat a dictionary for all car numbers for display
    #for x in thislist:
    #    while i<len(thislist):
     #       y = str(i)
     ##       thisdict["risk_number"+y] = thislist[i]
    #        i+=1
    context={'products':carExpire7days}
        
    return render(request,'risks_due.html',context)



@login_required(login_url='login')
def risks_7daysToExpiryview(request,pk_test):

    products=mod9001_risks.objects.filter(risk_number=pk_test)
    return render(request,'risk_view_7_days_To_expiry.html',{'products':products})

@allowed_users(allowed_roles=['Executive'])
def verify_risk(request,pk_test):
    open_car=mod9001_risks.objects.get(risk_number=pk_test)
    
    form=VerifyRisk(instance=open_car)
    if request.method=="POST":
            
            if request.POST['verification_status'] =="Rejected":
                request.POST=request.POST.copy()
                request.POST['status'] = 5 #requires approval first before next verification
                request.POST['verification']=2 #default verifiaction to Not effective
                
                

            else:
                request.POST=request.POST.copy()
                request.POST['status'] = 1 # keep status approved
                request.POST['verification']=1 #default verifiaction to effective
                request.POST['verification_status']="Closed"

                




            form=VerifyRisk(request.POST, instance=open_car)
            if form.is_valid():
                form.save()
                #print("request saved", request.POST)
                return redirect('/risks_due/')

    context={'form':form,'open_car':open_car,'pk_test':pk_test}  


    return render(request,'risk_verify.html',context)

#################OPPORTUNITY VERIFICATION#######################
@login_required(login_url='login')
def opp_due(request):
    carExpire7days=mod9001_risks.objects.all().filter(due__gte=datetime.now() - timedelta(days=7)).filter(record_type='OPP').filter(status='1').filter(~Q(verification='1'))
    context={'products':carExpire7days}
    #thislist = []
    #for i in carExpire7days:
        #w=i.due
        #t=w.strftime('%m/%d/%Y')
        #if CARnumbers_7days_expire(t)<0:
    #    thislist.append(i.risk_number)
    #thisdict={}
    #i=0
    #creat a dictionary for all car numbers for display
    #for x in thislist:
    #    while i<len(thislist):
    #        y = str(i)
    #        thisdict["risk_number"+y] = thislist[i]
    #        i+=1

        
    return render(request,'opp_due.html',context)



@login_required(login_url='login')
def opp_7daysToExpiryview(request,pk_test):

    products=mod9001_risks.objects.filter(risk_number=pk_test)
    return render(request,'opp_view_7_days_To_expiry.html',{'products':products})

@allowed_users(allowed_roles=['Executive'])
def verify_opp(request,pk_test):
    open_car=mod9001_risks.objects.get(risk_number=pk_test)
    form=VerifyOpp(instance=open_car)
    if request.method=="POST":
                 
           
        request.POST=request.POST.copy()
        request.POST['status'] = 1 # keep status approved




        form=VerifyOpp(request.POST, instance=open_car)
        if form.is_valid():
            form.save()
            return redirect('/opp_due/')

    context={'form':form,'pk_test':pk_test}  


    return render(request,'opp_verify.html',context)


    

