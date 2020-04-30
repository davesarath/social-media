from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import custModel,tweet


class registerForm(UserCreationForm):
    class Meta:
        model = custModel
        fields =  ['email','password1','password2','username']
        widgets={
            'username':forms.HiddenInput(),
            'email' : forms.EmailInput({"class":"form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['username'].required = False
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
    
class loginForm(forms.Form):
    email=forms.EmailField(required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(max_length=20, required=True,widget=forms.PasswordInput(attrs={"class":"form-control"}))

class tweetForm(forms.ModelForm):
    class Meta:
        model=tweet
        fields = ['content',"author"]
    
        widgets={
            "author":forms.HiddenInput()
        }



class updateForm(forms.ModelForm):
    class Meta:
        model=custModel
        fields = ["first_name","last_name","email","username","pro_pic"]
        widgets={
            "username"  :   forms.HiddenInput(),
            "first_name":   forms.TextInput(attrs={'class':'form-control'}),
            "last_name" :   forms.TextInput(attrs={'class':'form-control'}),
            "email"     :   forms.EmailInput(attrs={'class':'form-control'}),
        }   
    
