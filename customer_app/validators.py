from django import forms
import re

def clean_enter_new_password(newpwd):
    if not(newpwd[0].isupper()):
        raise forms.ValidationError('password should starts with uppercase')
    if len(newpwd)<5:
        raise forms.ValidationError('password should be greater than 5 characters')
    if len(newpwd)>15:
        raise forms.ValidationError('password should be less than 15 characters')
    if len(re.findall('[0-9]',newpwd))==0:
        raise forms.ValidationError('password should contain atleast one digit')
    if len(re.findall('[a-z]',newpwd))==0:
        raise forms.ValidationError('password should contain atleast one lowercase')
    if len(re.findall('[^a-z A-Z 0-9]',newpwd))==0:
        raise forms.ValidationError('password should contain atleast one special character')
    return newpwd