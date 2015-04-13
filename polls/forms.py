from django import forms

class ResponseForm(forms.Form):
	response = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'autofocus'}), label='Your Glorious Answer', max_length=150, error_messages={'required': 'Hmm...that doesn\'t look quite right. Try a different answer.'})
