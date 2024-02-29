from django import forms
from apps.users.models import Author


class RegisterForm(forms.ModelForm):
    def save(self, commit: bool = True):
        user = super().save(commit)
        password = self.cleaned_data.get('password')
        user.set_password(password)
        user.save()
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'username',
                  'password', 'email', 'avatar']
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"placeholder":"Enter sername"}))
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={"placeholder":"Enter password"}))

