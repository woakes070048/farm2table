from django import forms


class RegistrationForm(forms.Form):
    user_type = (
        ('F', 'Farmer'),
        ('R', 'Restaurant'),
        ('I', 'Individual'),
    )

    username = forms.CharField()
    email = forms.CharField()
    type = forms.ChoiceField(choices=user_type)
    password = forms.CharField(widget=forms.PasswordInput)
