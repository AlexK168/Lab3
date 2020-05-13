from django.forms import ModelForm
from .models import *


class OutletForm(ModelForm):
    class Meta:
        model = Outlet
        fields = '__all__'


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
