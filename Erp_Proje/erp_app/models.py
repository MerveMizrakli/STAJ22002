from django.db import models

class Raf(models.Model):
    raf_ad = models.CharField(max_length=10)
    raf_tekil_barkod = models.CharField(max_length=10)
    raf_id = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.raf_ad} ({self.raf_tekil_barkod})"


class Urun(models.Model):
    urun_ad = models.CharField(max_length=100)
    urun_barkod = models.IntegerField(default=0)
    urun_id = models.IntegerField(default=0)
    urun_adet = models.IntegerField(default=0)
    
    def __str__(self):
        return self.urun_ad
    

class RafUrun(models.Model):
    raf = models.ForeignKey(Raf, on_delete=models.CASCADE, related_name="raf_urunleri")
    urun = models.ForeignKey(Urun, on_delete=models.CASCADE, related_name="urun_raflari")
    adet = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('raf', 'urun')   #aynı ürün aynı rafta birden fazla kayıt olamayacak demek.

    def __str__(self):
        return f"{self.raf.raf_ad} - {self.urun.urun_ad} ({self.adet} adet)"


class Alis(models.Model):
    urun = models.ForeignKey(Urun, on_delete=models.CASCADE)
    raf = models.ForeignKey(Raf, on_delete=models.CASCADE)
    adet = models.PositiveIntegerField()
    tarih = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):     #stok güncelleme işlemleri
        raf_urun, created = RafUrun.objects.get_or_create(     #ürün raftaysa stoğu güncelle değilse olutşurrr.
            raf=self.raf, urun=self.urun, defaults={'adet': 0}   #raftaki ürün adedini arttır.
        )
        raf_urun.adet += self.adet
        raf_urun.save()
        super().save(*args, **kwargs)    #alış kaydı veritabanına kaydediliyor.
 

class Satis(models.Model):
    urun = models.ForeignKey(Urun, on_delete=models.CASCADE)
    raf = models.ForeignKey(Raf, on_delete=models.CASCADE)
    adet = models.PositiveIntegerField()
    tarih = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        try:
            raf_urun = RafUrun.objects.get(raf=self.raf, urun=self.urun)
        except RafUrun.DoesNotExist:
            raise ValueError("Bu rafta ürün bulunmamaktadır.")     #ürünün raf ve stok kaydı kontrol edilir eksiltme işlemi yapılcağı için.
  
        if raf_urun.adet < self.adet:
            raise ValueError("Yeterli stok yok!")

        raf_urun.adet -= self.adet
        raf_urun.save()
        super().save(*args, **kwargs)
    



    #buradaki save metodları sayesinde stoklar oto güncellenir.Böylece aapi üzerinden gelen tüm istekler veritabanına yansıyor.