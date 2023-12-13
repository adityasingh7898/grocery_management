from django import forms
from customer_app.models import customer_model
from django.contrib.auth.hashers import make_password
import re
from customer_app.validators import clean_enter_new_password

class customer_register_form(forms.ModelForm):
    repassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = customer_model
        fields = ['username','first_name','last_name','email','phone','gender','dob','password']

    def clean_username(self):
        username = self.cleaned_data['username']
        if not(username[0].isupper()):
            raise forms.ValidationError('Username starts with uppercase')
        if len(username) < 3:
            raise forms.ValidationError('Username should be min 3 characters')
        if len(username) > 15:
            raise forms.ValidationError('Username should be max 15 characters')
        return username

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(str(phone)) != 10:
            raise forms.ValidationError('Phone number should be 10 digits')
        if str(phone)[0] not in '9876':
            raise forms.ValidationError('Phone numbers start with either 9,8,7,6')
        return phone
    
    def clean_password(self):
        pwd = self.cleaned_data['password']
        if not (pwd[0].isupper()):
            raise forms.ValidationError('password starts with uppercase')
        if len(pwd) < 3:
            raise forms.ValidationError('password should be min 3 characters')
        if len(pwd) > 15:
            raise forms.ValidationError('password should be max 15 characters')
        if len(re.findall('[0-9]',pwd)) == 0:
            raise forms.ValidationError('password atleast 1 numeric character')
        if len(re.findall('[^0-9a-zA-Z]',pwd)) == 0:
            raise forms.ValidationError('password atleast 1 special character')
        if len(re.findall('[a-z]',pwd)) == 0:
            raise forms.ValidationError('password atleast 1 lowercase character')
        return pwd
    
    def clean_repassword(self):
        pwd = self.cleaned_data['repassword']
        if not (pwd[0].isupper()):
            raise forms.ValidationError('repassword starts with uppercase')
        if len(pwd) < 3:
            raise forms.ValidationError('repassword should be min 3 characters')
        if len(pwd) > 15:
            raise forms.ValidationError('repassword should be max 15 characters')
        if len(re.findall('[0-9]',pwd)) == 0:
            raise forms.ValidationError('repassword atleast 1 numeric character')
        if len(re.findall('[^0-9a-zA-Z]',pwd)) == 0:
            raise forms.ValidationError('repassword atleast 1 special character')
        if len(re.findall('[a-z]',pwd)) == 0:
            raise forms.ValidationError('repassword atleast 1 lowercase character')
        return pwd
    
    def save(self,commit = True):
        user = super().save(commit=False)
        if self.cleaned_data['password'] == self.cleaned_data['repassword']:
            user.password = make_password(self.cleaned_data['password'])
            if commit:
                user.save()
            return user
        
    
class customer_login_form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if not (username[0].isupper()):
            raise forms.ValidationError('Username starts with uppercase')
        if len(username) < 3:
            raise forms.ValidationError('Username should be min 3 characters')
        if len(username) > 15:
            raise forms.ValidationError('Username should be max 15 characters')
        return username

        
    def clean_password(self):
        pwd = self.cleaned_data['password']
        if not (pwd[0].isupper()):
            raise forms.ValidationError('password starts with uppercase')
        if len(pwd) < 3:
            raise forms.ValidationError('password should be min 3 characters')
        if len(pwd) > 15:
            raise forms.ValidationError('password should be max 15 characters')
        if len(re.findall('[0-9]',pwd)) == 0:
            raise forms.ValidationError('password atleast 1 numeric character')
        if len(re.findall('[^0-9a-zA-Z]',pwd)) == 0:
            raise forms.ValidationError('password atleast 1 special character')
        if len(re.findall('[a-z]',pwd)) == 0:
            raise forms.ValidationError('password atleast 1 lowercase character')
        return pwd
    
    def clean_repassword(self):
        pwd = self.cleaned_data['repassword']
        if not (pwd[0].isupper()):
            raise forms.ValidationError('repassword starts with uppercase')
        if len(pwd) < 3:
            raise forms.ValidationError('repassword should be min 3 characters')
        if len(pwd) > 15:
            raise forms.ValidationError('repassword should be max 15 characters')
        if len(re.findall('[0-9]',pwd)) == 0:
            raise forms.ValidationError('repassword atleast 1 numeric character')
        if len(re.findall('[^0-9a-zA-Z]',pwd)) == 0:
            raise forms.ValidationError('repassword atleast 1 special character')
        if len(re.findall('[a-z]',pwd)) == 0:
            raise forms.ValidationError('repassword atleast 1 lowercase character')
        return pwd   


class change_pwd_form(forms.Form):
    enter_new_password=forms.CharField(widget=forms.PasswordInput,validators=[clean_enter_new_password])
    re_enter_password=forms.CharField(widget=forms.PasswordInput)

    def clean_re_enter_password(self):
        password = self.cleaned_data['re_enter_password']
        if not (password[0].isupper()):
            raise forms.ValidationError('re entered password starts with uppercase')
        if len(password) < 3:
            raise forms.ValidationError('re entered password should be min 3 characters')
        if len(password) > 15:
            raise forms.ValidationError('re entered password should be max 15 characters')
        if len(re.findall('[0-9]',password)) == 0:
            raise forms.ValidationError('re entered password atleast 1 numeric character')
        if len(re.findall('[^0-9a-zA-Z]',password)) == 0:
            raise forms.ValidationError('re entered password atleast 1 special character')
        if len(re.findall('[a-z]',password)) == 0:
            raise forms.ValidationError('re entered password atleast 1 lowercase character')
        if self.cleaned_data['enter_new_password']!=password:
            raise forms.ValidationError('New password and re-entered password should be same as password')
        return password   