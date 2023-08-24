from django import forms  # импортируем для создания классов формы
from models import *


class AddRecords(forms.ModelForm):
    class Meta:
        model = Records
        fields = "__all__"


