from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include



urlpatterns = [

######post back urls###########
  
    
    
    
    path('ajax/load-ids/', views.load_ids, name='ajax_load_ids'),
    path('ajax/load-contextdesc/', views.load_contextdesc, name='ajax_load_contextdesc'),

###########end#############


    ##########issues urs####################
    path('issues/', views.issues, name='issues'),
    path('issue_editing/',views.issue_editing,name="issue_editing"),
    path('issues_report/',views.issues_report,name="issues_report"),
    path('edit_issue/<str:pk_test>/',views.edit_issue,name="edit_issue"),
    path('delete_issue/<str:pk_test>/',views.deleteissue,name="deleteissue"),
    path('issues_pending/',views.issues_pending,name="issues_pending"),
    path('issues_rejected/',views.issues_rejected,name="issues_rejected"),
    path('approve_issue/<str:pk_test>/',views.approve_issue,name="approve_issue"),
    ####END############################

    #############INTERESTED PARTIES URL#######################
    path('interested_parties/', views.interested_parties, name='interested_parties'),
    path('ip_editing/',views.ip_editing,name="ip_editing"),
    path('ip_report/',views.ip_report,name="ip_report"),
    path('edit_ip/<str:pk_test>/',views.edit_ip,name="edit_ip"),
    path('delete_ip/<str:pk_test>/',views.deleteip,name="deleteip"),
    path('ip_pending/',views.ip_pending,name="ip_pending"),
    path('ip_rejected/',views.ip_rejected,name="ip_rejected"),
    path('approve_ip/<str:pk_test>/',views.approve_ip,name="approve_ip"),

    ############REGULATORY REQUIRMENT########################

    path('regulatory_requirement/', views.regulatory_requirement, name='regulatory_requirement'),
    path('regulatory_editing/',views.regulatory_editing,name="regulatory_editing"),
    path('regulatory_report/',views.regulatory_report,name="regulatory_report"),
    path('edit_regulatoryreq/<str:pk_test>/',views.edit_regulatoryreq,name="edit_regulatoryreq"),
    path('deleteregulatory/<str:pk_test>/',views.deleteregulatory,name="deleteregulatory"),
    path('requirement_pending/',views.requirement_pending,name="requirement_pending"),
    path('requirement_rejected/',views.requirement_rejected,name="requirement_rejected"),
    path('approve_requirement/<str:pk_test>/',views.approve_requirement,name="approve_requirement"),
###################### RISKS ##############################
    path('ajax/context_description/', views.load_issue_description, name='context_description'),
    path('risks/<str:issue_number>',views.risks,name="risks"),
    path('risk_assessed/',views.risk_assessed,name="risk_assessed"),
    path('issues_pending_risk_assesment/',views.issues_pending_risk_assesment,name="issues_pending_risk_assesment"),
    path('opportunity/<str:issue_number>',views.opportunity,name="opportunity"),
    path('opportunity_assessed/',views.opportunity_assessed,name="opportunity_assessed"),    
    path('issues_pending_opp_assesment/',views.issues_pending_opp_assesment,name="issues_pending_opp_assesment"),
    path('risks_report/',views.risks_report,name="risks_report"),
    path('opportunity_report/',views.opportunity_report,name="opportunity_report"),
    path('risk_pending/',views.risk_pending,name="risk_pending"),
    path('opp_pending/',views.opp_pending,name="opp_pending"),

    path('approve_risk/<str:pk_test>/',views.approve_risk,name="approve_risk"),
    path('risks_due/',views.risks_due,name="risks_due"), 
    path('risks_7daysToExpiryview/<str:pk_test>/',views.risks_7daysToExpiryview,name="risks_7daysToExpiryview"),
    path('verify_risk/<str:pk_test>/',views.verify_risk,name="verify_risk"),

    path('opp_due/',views.opp_due,name="opp_due"), 
    path('opp_7daysToExpiryview/<str:pk_test>/',views.opp_7daysToExpiryview,name="opp_7daysToExpiryview"),
    path('verify_opp/<str:pk_test>/',views.verify_opp,name="verify_opp"),
    path('approve_opp/<str:pk_test>/',views.approve_opp,name="approve_opp"),







    
    
]
