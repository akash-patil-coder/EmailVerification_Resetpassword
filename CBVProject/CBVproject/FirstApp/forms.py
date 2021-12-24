from django import forms
from .models import Laptop
from django.core import validators

class LaptopModelForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'

        #labels
        labels = {
            'lid': 'Enter ID',
            'ram': 'Enter RAM in GB :',
            'rom': 'ROM :',
            'model_name': 'Enter Model Name :',
            'company': 'Enter Company Name :',
            'processor': 'Enter Processor :',
            'price': 'Enter Price :',
            'weight': 'Enter Weight'
        }

        # placeholder
        widgets = {'company':forms.TextInput(attrs={'placeholder':'e.g : dell,lenovo'}),
                   'model_name': forms.TextInput(attrs={'placeholder': 'eg : thinkPad,lattitude'}),
                   'ram': forms.NumberInput(attrs={'placeholder': 'eg : 2GB,4GB,8GB'}),
                   'rom':forms.NumberInput(attrs={'placeholder':'eg : 1SSD'}),
                   'processor':forms.TextInput(attrs={'placeholder':'eg : core i3,Xeon'}),
                   'price':forms.NumberInput(attrs={'placeholder':'Enter the price'}),
                   'weight':forms.NumberInput(attrs={'placeholder':'eg : 2kg'})
                   }

    # Validation

    def clean_ram(self):
        ram = self.cleaned_data['ram']
        if ram < 0:
            raise forms.ValidationError("ROM always greater than zero")
        elif ram % 2 != 0:
            raise forms.ValidationError("RAM always avaliable in even number ")
        else:
            return ram


    def clean_rom(self):
        rom = self.cleaned_data['rom']
        if rom < 0:
            raise forms.ValidationError("ROM must be greater than zero")
        else:
            return rom

    def clean_weight(self):
        weight = self.cleaned_data['weight']
        if weight < 0:
            raise forms.ValidationError("Weight must be greater than zero")
        else:
            return weight
