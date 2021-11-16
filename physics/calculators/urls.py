from django.urls import path
from . import views

urlpatterns = [
    path('speed_convert/',views.speed_convert),
    path('speed_convert/speed_convert',views.speed_convert),
    path('kineticfriction/',views.kineticfriction),
    path('kineticfriction/kineticfriction',views.kineticfriction),
    path('instantaneous_velocity/',views.instantaneous_velocity),
    path('instantaneous_velocity/instantaneous_velocity',views.instantaneous_velocity),
    path('horsepower/',views.horsepower),
    path('horsepower/horsepower',views.horsepower),
    path('impulse/',views.impulse),
    path('impulse/impulse',views.impulse),
    path('inductivereactance/',views.inductivereactance),
    path('inductivereactance/inductivereactance',views.inductivereactance),
    path('heattransfer/',views.heattransfer),
    path('heattransfer/heattransfer',views.heattransfer),
    path('machnumber/',views.machnumber),
    path('machnumber/machnumber',views.machnumber),
    path('lcresonance/',views.lcresonance),
    path('lcresonance/lcresonance',views.lcresonance),
    path('zenerdiode/',views.zenerdiode),
    path('zenerdiode/zenerdiode',views.zenerdiode),
    path('centripetal_acceleration/',views.centripetal_acceleration),
    path('centripetal_acceleration/centripetal_acceleration',views.centripetal_acceleration),
    path('resistance_frequency_capacitance/',views.resistance_frequency_capacitance),
    path('resistance_frequency_capacitance/resistance_frequency_capacitance',views.resistance_frequency_capacitance),
    path('kinematic/',views.kinematic),
    path('kinematic/kinematic',views.kinematic)


]