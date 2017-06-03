from django import forms
from rango.models import Page, Category
from django import forms
from django.contrib.auth.models import User
from rango.models import Category, Page, UserProfile,SignUpForEmail

class CategoryForm(forms.ModelForm):
    my_default_errors = {
        'required': 'Sorry that is incorrect',
        'invalid': 'Enter a valid value plz'
    }
    name = forms.CharField(max_length=128, help_text="Please Enter The Category Name.", error_messages=my_default_errors)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)



    class Meta:
        model=Category
        fields=('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://' add 'http://' to the beginning
        if url and not url.startswith('http://'):
            url = 'http://' + url

            cleaned_data['url'] = url
        return cleaned_data

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign keys
        fields = ('title', 'url', 'views')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

class EmailForm(forms.ModelForm):
    my_default_errors = {
        'required': 'Sorry that is incorrect',
        'invalid': 'Please Enter a New Email Address'
    }
    email = forms.CharField(max_length=128, help_text="Please Enter A New Email Address", error_messages=my_default_errors)

    class Meta:
        model = SignUpForEmail
        fields=('email',)