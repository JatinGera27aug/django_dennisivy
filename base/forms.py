from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model =  Room
        fields = '__all__'     # ye sare form inputs ko ek strcutre dedega
        