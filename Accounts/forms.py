from django import forms
from django.contrib.auth.models import User
from .models import ProfileModel
from django.contrib.auth import authenticate,login,logout,get_user_model

User = get_user_model()



class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Enter Your Username {Required}','class': 'input-round big-input'}))
    password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password {Required}','class': 'input-round big-input'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)



class ProfileRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Enter Your Username {Required}','class': 'input-round big-input'}))
    email = forms.CharField(max_length=100,widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email {Required}','class': 'input-round big-input'}))
    password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password {Required}','class': 'input-round big-input'}))

    class Meta:
        model = ProfileModel
        fields = ('username', 'email', 'password')

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        # if password1 != password2:
        #     raise forms.ValidationError("Password must match")
        username_check = User.objects.filter(username=username)
        if username_check.exists():
            raise forms.ValidationError("This username has already been registered")
        email_check = User.objects.filter(email=email)
        if email_check.exists():
            raise forms.ValidationError("This Email has already been registered")        
        return super(ProfileRegisterForm, self).clean(*args, **kwargs)
