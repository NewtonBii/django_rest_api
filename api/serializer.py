from rest_framework import serializers
from .models import UserInformation

class UserInformationSerializer(serializers.ModelSerializer):
    class Meta:
        models = UserInformation
        fields = ('name', 'date_of_birth', 'blood_group', 'gender', 'race')
