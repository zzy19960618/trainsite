from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Carriage, Train, RawData, CarAxle, Pressure, TrainCarriage


@admin.register(Pressure)
class PressureAdmin(admin.ModelAdmin):
    pass
    #list_display = ('num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8')
    #list_display = ('num1', 'num2', '测量3', '测量4', '测量5', '测量6', '测量7', '测量8')


admin.site.register(Carriage)
admin.site.register(Train)
admin.site.register(RawData)
admin.site.register(CarAxle)
admin.site.register(TrainCarriage)
