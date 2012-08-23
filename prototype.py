# coding=utf-8
'''
Created on Aug 9, 2012

@author: CongNT3
'''

#import ldap
import active_directory
user = active_directory.find_user ("congnt3")
#user.com_object.SetPassword("NewPassword");


print user.distinguishedName

#destination_ou = active_directory.find_ou("Thang 08")
#destination_ou.com_object.MoveHere(str(user.as_string()), str(user.Name))
#print destination_ou

#destination_ou = active_directory.AD_object("LDAP://OU=Thang 08,OU=Nam 2012,OU=Hanoi,OU=NghiViec,DC=HO,DC=FPT,DC=VN")
destination_ou = active_directory.AD_object("LDAP://OU=RAD,OU=FTEL HO,OU=FTEL,DC=HO,DC=FPT,DC=VN")
destination_ou.com_object.MoveHere(str(user.as_string()), str(user.Name))
#print destination_ou.dSCorePropagationData