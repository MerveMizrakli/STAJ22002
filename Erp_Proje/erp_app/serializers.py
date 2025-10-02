from rest_framework import serializers
from .models import Raf, Urun, RafUrun, Alis, Satis

class RafSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raf
        fields = '__all__'

class UrunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urun
        fields = '__all__'

class RafUrunSerializer(serializers.ModelSerializer):
    raf = RafSerializer(read_only=True)    #Bu iki bilgi nested (iç içe) JSON olarak gösterilir, ama API üzerinden değiştirilmez (sadece okunur).
    urun = UrunSerializer(read_only=True)
    class Meta:
        model = RafUrun
        fields = '__all__'

class AlisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alis
        fields = '__all__'

class SatisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Satis
        fields = '__all__'



   #Serializer’lar, veritabanı modellerini JSON formatına çevirip API üzerinden göndermeyi veya API’den gelen JSON verilerini modele dönüştürmeyi sağlar.
   #Crud işlemleri sırasında django rest framework bu serializerleri kullanır.