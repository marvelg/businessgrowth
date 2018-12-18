from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    
            
