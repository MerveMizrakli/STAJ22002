from rest_framework import serializers
from .models import UrunOzellik

class UrunOzellikSerializer(serializers.ModelSerializer):
    class Meta:    #Serializer’ın hangi model ile çalışacağını ve hangi alanları kullanacağını tanımlayan iç sınıf (Meta class)
        model = UrunOzellik
        fields = '__all__'

        #serializer modeldeki veriyi jsona çevirir.Bu sayede api daha doğru çalışır.