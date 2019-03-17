from django import forms

from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

STATES = (
    ('', 'Choose...'),
    ('MH', 'Maharashtra'),
    ('KA', 'Karnataka'),
    ('TN', 'Tamilanadu')
)

class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('password', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'address_1',
            'address_2',
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('state', css_class='form-group col-md-4 mb-0'),
                Column('zip_code', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            'check_me_out',
            Submit('submit', 'Sign in')
        )

class UserProfileForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last name'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Set password'}))
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6'),
                Column('last_name', css_class='form-group col-md-6'),
            ),
            'email',
            'password',
            Submit('submit','Register')
        )

