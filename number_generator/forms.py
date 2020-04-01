from django import forms
from crispy_forms.helper import FormHelper
from .models import Data

class DataForm(forms.ModelForm):

    class Meta:
        model = Data
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DataForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_show_labels = False
        self.helper.form_tag = False