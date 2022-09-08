from rest_framework import serializers
from rest_framework.validators import UniqueValidator


from .models import City 

class CitySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    class Meta:
        model = City 
        exclude = ('id',)
        extra_kwargs = {
        'city_name': {
            'validators': [
                UniqueValidator(
                    queryset=City.objects.all()
                )
            ]
        }
    }

    