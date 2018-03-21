# import serializers module from the rest_framework package
from rest_framework import serializers

# import UserInformation class from the models module
from .models import UserInformation

# create a UserInformationSerializer class that will inhertit form the ModelSerializer class
class UserInformationSerializer(serializers.ModelSerializer):
    class Meta:
        models = UserInformation
        fields = ('name', 'date_of_birth', 'blood_group', 'gender', 'race')
