from django.contrib import admin
from .models import Raf, Urun, RafUrun, Alis, Satis

class RafUrunInline(admin.TabularInline):    #TabularInlına bir modelin diğer modelle olan ilişkisini ana modelde tablo şeklinde gösterir.
    model = RafUrun #ilişkili model
    extra = 0   #ekstra satır yok
    readonly_fields = ('adet',)   #adet alanı admin panelinde sadece okunulur değişmez.
    can_delete = False #kayıtlar admin panelinden silinemez.

@admin.register(Raf)   #raf modeli admin paneline kaydedilir
class RafAdmin(admin.ModelAdmin): 
    list_display = ('raf_ad', 'raf_tekil_barkod', 'raf_id')   #admin listesinde bu sütunlar gösterilir.
    inlines = [RafUrunInline]    #Raf detay sayfasında ilgili ürünleri (RafUrun modeli üzerinden) tablolarda gösterir.

@admin.register(Urun)
class UrunAdmin(admin.ModelAdmin):
    list_display = ('urun_ad', 'urun_barkod', 'urun_id', 'urun_adet')

@admin.register(Alis)
class AlisAdmin(admin.ModelAdmin):
    list_display = ('urun', 'raf', 'adet', 'tarih')

@admin.register(Satis)
class SatisAdmin(admin.ModelAdmin):
    list_display = ('urun', 'raf', 'adet', 'tarih')
