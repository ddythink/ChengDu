# -*- coding:utf-8 _*_

from django.forms import ModelForm
from .models import Report

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        from django.forms.widgets import HiddenInput
        super(ReportForm, self).__init__(*args, **kwargs)
        self.fields['pids'].widget = HiddenInput()
        #self.fields['rname'].widget = HiddenInput()
        self.fields['control'].widget = HiddenInput()
        self.fields['report_type'].widget = HiddenInput()