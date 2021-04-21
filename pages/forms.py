from django import forms


class ContactusForm(forms.Form):

	First_Name = forms.CharField(max_length= 100)
	Last_Name = forms.CharField(max_length = 100)
	Subject = forms.CharField(widget = forms.Textarea, max_length = 1000)
	email = forms.EmailField(max_length=150)
	Message = forms.CharField(widget = forms.Textarea)

