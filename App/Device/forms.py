from django import forms

class DeviceForm(forms.Form):
    KEY = forms.CharField(label="KEY", max_length=64)
    MAC = forms.CharField(label="MAC", max_length=20)
    IP = forms.GenericIPAddressField(label="IP")