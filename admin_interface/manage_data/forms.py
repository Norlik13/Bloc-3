from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False, label='Nouveau mot de passe')

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_staff']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            return self.instance.password
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')

        if password:
            user.set_password(password)

        if commit:
            user.save()
        return user