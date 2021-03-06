from django.urls import path
from . import views

urlpatterns = [
    path('speed-convert/',views.speed_convert,name = 'speed_convert'),
    path('kineticfriction/',views.kineticfriction,name = 'kineticfriction'),
    path('instantaneous-velocity/',views.instantaneous_velocity,name = 'instantaneous_velocity/'),
    path('horsepower/',views.horsepower,name= 'horsepower'),
    path('impulse/',views.impulse,name = 'impulse'),
    path('inductive-reactance/',views.inductivereactance,name = 'inductivereactance'),
    path('heat-transfer/',views.heattransfer,name = 'heattransfer'),
    path('machnumber/',views.machnumber,name = 'machnumber'),
    path('lc-resonance/',views.lcresonance,name = 'lcresonance'),
    path('zener-diode/',views.zenerdiode,name = 'zenerdiode'),
    path('centripetal-acceleration/',views.centripetal_acceleration,name='centripetal_acceleration'),
    path('resistance-frequency-capacitance/',views.resistance_frequency_capacitance,name =  'resistance_frequency_capacitance'),
    path('kinematic/',views.kinematic,name = 'kinematic'),
    path('voltage-resistance-power-current/',views.voltageresistancepowercurrent,name = 'voltageresistancepowercurrent'),
    path('specific-heat-and-density/',views.specificheatanddensity,name = 'specificheatanddensity'),
    path('roundone/',views.roundone,name = 'roundone'),
    path('roundtotwo/',views.roundtotwo,name = 'roundtotwo'),
    path('roundtothree/',views.roundtothree,name = 'roundtothree'),
    path('sigfig/',views.sigfig, name = 'sigfig'),
    path('time-clock-15-minutes/',views.time_clock_15_minutes,name = 'time_clock_15_minutes'),
    path('nearest-eighth/',views.nearest_eighth,name = 'nearest_eighth'),
    path('identifying-perfect-cube/',views.identifying_perfect_cube,name = 'identifying_perfect_cube'),
    path('cancel-out/',views.cancel_out,name = 'cancel_out'),
    path('feet-inch/',views.feet_inch,name = 'feet_inch'),
    path('nearest-feet/',views.nearest_feet,name = 'nearest_feet'),
    path('meter-centimeter/',views.meter_centimeter,name = 'meter_centimeter'),
    path('nearest-meter/',views.nearest_meter,name = 'nearest_meter'),
    path('centimeter-millimeter/',views.centimeter_millimeter,name = 'centimeter_millimeter'),
    path('nearest-centimeter/',views.nearest_centimeter,name = 'nearest_centimeter'),
    path('kilometer-meter/',views.kilometer_meter,name = 'kilometer_meter'),
    path('nearest-kilometer/',views.nearest_kilometer,name = 'nearest_kilometer'),
    path('nearest-millimeter/',views.nearest_millimeter,name = 'nearest_millimeter'),
    path('millimeter-micrometer/',views.millimeter_micrometer,name = 'millimeter_micrometer'),
    path('nearest-micrometer/',views.nearest_micrometer,name = 'nearest_micrometer'),
    path('micrometer-nanometer/',views.micrometer_nanometer,name = 'micrometer_nanometer'),
    path('nearest-nanometer/',views.nearest_nanometer,name = 'nearest_nanometer'),
    path('nearest-yard/',views.nearest_yard,name = 'nearest_yard'),
    path('nearest-mile/',views.nearest_mile,name = 'nearest_mile'),
    path('time-clock-30-minutes/',views.time_clock_30_minutes,name = 'time_clock_30_minutes'),
    path('sinx/',views.sinx,name = 'sinx'),
    path('cosx/',views.cosx,name = 'cosx'),
    path('tanx/',views.tanx,name = 'tanx'),
    path('arcsinx/',views.arcsinx,name = 'arcsinx'),
    path('arctanx/',views.arctanx,name = 'arctanx'),
    path('secx/',views.secx,name = 'secx'),
    path('radian-to-degree/',views.radian_to_degree,name = 'radian_to_degree'),
    path('degree-to-radian/',views.degree_to_radian,name = 'degree_to_radian'),
    path('rpm-to-radianspersecond/',views.rpm_to_radianspersecond,name = 'rpm_to_radianspersecond'),
    path('trig-functions-right-triangle/',views.trig_functions_right_triangle,name = 'trig_functions_right_triangle'),
    path('simplify-trigonometric-expressions/',views.simplify_trigonometric_expressions, name = 'simplify_trigonometric_expressions'),
    path('find-quadrant-of-angle/',views.find_quadrant_of_angle, name = 'find_quadrant_of_angle'),
    path('trig-value-of-angle/',views.trig_value_of_angle, name = 'trig_value_of_angle'),
    path('de-moivre/',views.de_moivre, name = 'de_moivre'),
    path('golden-ratio/',views.golden_ratio,name = 'golden_ratio'),
    path('silver-ratio/',views.silver_ratio,name = 'silver_ratio'),
    path('rule-of-72/',views.rule_of_72,name = 'rule_of_72'),
    path('savings-goal/',views.savings_goal,name = 'savings_goal'),
    path('deferred-annuity',views.deferred_annuity, name = 'deferred_annuity'),
]