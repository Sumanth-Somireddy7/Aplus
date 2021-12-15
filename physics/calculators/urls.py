from django.urls import path
from . import views

urlpatterns = [
    path('speed_convert/',views.speed_convert,name = 'speed_convert'),
    path('kineticfriction/',views.kineticfriction,name = 'kineticfriction'),
    path('instantaneous_velocity/',views.instantaneous_velocity,name = 'instantaneous_velocity/'),
    path('horsepower/',views.horsepower,name= 'horsepower'),
    path('impulse/',views.impulse,name = 'impulse'),
    path('inductivereactance/',views.inductivereactance,name = 'inductivereactance'),
    path('heattransfer/',views.heattransfer,name = 'heattransfer'),
    path('machnumber/',views.machnumber,name = 'machnumber'),
    path('lcresonance/',views.lcresonance,name = 'lcresonance'),
    path('zenerdiode/',views.zenerdiode,name = 'zenerdiode'),
    path('centripetal_acceleration/',views.centripetal_acceleration,name='centripetal_acceleration'),
    path('resistance_frequency_capacitance/',views.resistance_frequency_capacitance,name =  'resistance_frequency_capacitance'),
    path('kinematic/',views.kinematic,name = 'kinematic'),
    path('voltageresistancepowercurrent/',views.voltageresistancepowercurrent,name = 'voltageresistancepowercurrent'),
    path('specificheatanddensity/',views.specificheatanddensity,name = 'specificheatanddensity'),
    path('roundone/',views.roundone,name = 'roundone'),
    path('roundtotwo/',views.roundtotwo,name = 'roundtotwo'),
    path('roundtothree/',views.roundtothree,name = 'roundtothree'),
    path('sigfig/',views.sigfig, name = 'sigfig'),
    path('time_clock_15_minutes/',views.time_clock_15_minutes,name = 'time_clock_15_minutes'),
    path('nearest_eighth/',views.nearest_eighth,name = 'nearest_eighth'),
    path('identifying_perfect_cube/',views.identifying_perfect_cube,name = 'identifying_perfect_cube'),
]