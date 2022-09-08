from rest_framework import serializers
from rest_framework.validators import UniqueValidator


from .models import City 

class CitySerializer(serializers.ModelSerializer):
    class Meta: 
        model = City 
        fields = ('city_name', )
        extra_kwargs = {
        'city_name': {
            'validators': [
                UniqueValidator(
                    queryset=City.objects.all()
                )
            ]
        }
    }

    