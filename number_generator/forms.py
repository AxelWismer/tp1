from django import forms
from crispy_forms.helper import FormHelper
from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ('x', 'c', 'a', 'm', 'k', 'g', 'method')

    def __init__(self, *args, **kwargs):
        super(DataForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_show_labels = False
        self.helper.form_tag = False

class ChiForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ('number_amount', 'interval_amount')

    def __init__(self, *args, **kwargs):
        super(ChiForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_show_labels = False
        self.helper.form_tag = False