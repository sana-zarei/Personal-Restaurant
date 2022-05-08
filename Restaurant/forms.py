from django import forms
from .models import ContactUs,Reservation_Received

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation_Received
        fields = ('name', 'date' , 'time', 'count', 'table_number')



class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name2', 'subject', 'email', 'message')
        widgets = {
            'name2': forms.TextInput(attrs={'placeholder': 'Enter Your Name {Required}','class': 'input-control'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Enter Your Subject {Required}','class': 'input-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Your Email {Required}','class': 'input-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter Your Message {Required}','class': 'input-control'})}

