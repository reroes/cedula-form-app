from .models import CedulaInfo
from django.forms import ModelForm


class CedulaInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(CedulaInfoForm, self).__init__(*args, **kwargs)
        self.fields['identificacion_user'].error_messages = {
            "required": u"Please tell us your identification.",
            "invalid": u"We're pretty sure you made that identification.",
        }
        self.fields['telefono'].error_messages = {
            "required": u"Please tell us your telefono.",
            "invalid": u"We're pretty sure you made that identification.",
        }
        self.fields['direccion'].error_messages = {
            "required": u"Please tell us your direccion.",
            "invalid": u"We're pretty sure you made that identification.",
        }
        self.fields['celular'].error_messages = {
            "required": u"Please tell us your celular.",
            "invalid": u"We're pretty sure you made that identification.",
        }




    class Meta(object):
        model = CedulaInfo
        fields = ('identificacion_user', 'telefono', 'direccion', 'celular')
