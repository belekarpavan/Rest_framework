from rest_framework import serializers
from .models import student

class studentSerializers(serializers.ModelSerializer):

    name=serializers.CharField(
        max_length=20,
        style={'placeholder': 'Your Good Name', 'autofocus': True}
    )
    address=serializers.CharField(
        max_length=50,
        style={'placeholder': 'Address'}
    )
    dob = serializers.DateField(
        style={'input_type': 'date','placeholder': 'Address'}
    )
    email = serializers.EmailField(
        max_length=30,
        style={'type':'email', 'placeholder': 'Email'}
    )
    mobile = serializers.CharField(
        style={'input_type': 'text', 'placeholder': 'Mobile No', 'maxlength':'10','minlength':'10'}
    )
    class Meta:
        model=student
        fields='__all__'

