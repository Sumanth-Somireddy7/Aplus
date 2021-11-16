from django.shortcuts import render
from .methods import *

# Create your views here.
def speed_convert(request):
    try:
        num1 = request.POST['num1']
        em = request.POST['em']
        ea = request.POST['ea']
    except:
        res = 'Please Enter a Valid Numerical Value'
        cas = False
        x = ''
        y = ''
        z = ''
        em = ''
        ea = ''
        num1 = ''
    else:
        try:
            x = float(num1)
            y = str(em)
            z = str(ea)
        except:
            res = 'Please Enter Valid Numerical Value'
            cas = False
            x = ''
            y = ''
            z = ''
            em = ''
            ea = ''
            num1 = ''
        else:
            res = conv(x,y,z)
            cas = True
    return render(request,"speedconversion.html",{'num1':num1,'result':res[0],'from':em,'to':ea,'eq':'=','converted_speed_m_s':res[1],'cas':cas,'converted_speed':res[0]})
def kineticfriction(request):
    try:
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        num3 = request.POST['num3']
    except:
        res = 'Please Enter an Valid Numerical value'
        strg1 = ''
        strg2 = ''
        stru = ''
        g1 = ''
        g2 = ''
        x = ''
        eq = ''
        unit = ''
        st = ''
        fr = ''
        mu = ''
        nf = ''
        cas = False
    else:
        if num1=='x':
            try:
                mu = float(num3)
                nf = float(num2)
            except:
                res = 'Please Enter valid Numerical Value'
                strg1 = ''
                strg2 = ''
                stru = ''
                g1 = ''
                g2 = ''
                x = ''
                eq = ''
                unit = ''
                st = ''
                mu = ''
                nf = ''
                fr = ''
                cas = False
            else:
                res = fricf(mu,nf)
                fr = res
                strg1 = 'Coefficient of friction'
                strg2 = 'Normal Force'
                g1 = mu
                g2 = nf
                stru = 'Friction Value'
                x = 'x ='
                eq = '='
                unit = 'N'
                st = 'Here in this case, it is'
                cas = True
        elif num3=='x':
            try:
                fr = float(num1)
                nf = float(num2)
            except:
                res = 'Please Enter an Valid Numerical value'
                strg1 = ''
                strg2 = ''
                stru = ''
                g1 = ''
                g2 = ''
                x = ''
                eq = ''
                unit = ''
                st = ''
                fr = ''
                mu = ''
                nf = ''
                cas = False
            else:
                res = fricm(fr,nf)
                mu = res
                strg1 = 'Friction Value'
                strg2 = 'Normal Force'
                g1 = fr
                g2 = nf
                stru = 'Coefficient of Friction'
                x = 'x ='
                eq = '='
                unit = 'N'
                st = 'Here in this case, it is'
                cas = True
        else:
            try:
                fr = float(num1)
                mu = float(num3)
            except:
                res = 'Please Enter an Valid Numerical value'
                strg1 = ''
                strg2 = ''
                stru = ''
                g1 = ''
                g2 = ''
                x = ''
                eq = ''
                unit = ''
                st = ''
                fr = ''
                mu = ''
                nf = ''
                cas = False
            else:
                res = fricn(fr,mu)
                nf = res
                strg1 = 'Friction Value'
                strg2 = 'Coefficient of Friction'
                g1 = fr
                g2 = mu
                stru = 'Normal Force'
                x = 'x ='
                eq = '='
                unit = 'N'
                st = 'Here in this case, it is'
                cas = True
    return render(request,"kineticfriction.html",{'result':res,'fr':fr,'mu':mu,'nf':nf, 'strg1':strg1,'strg2':strg2,
	'stru':stru,'g1':g1,'g2':g2,'x':x,'eq':eq,'unit':unit,'st':st,'cas':cas})
def instantaneous_velocity(request):
    try:
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        num3 = request.POST['num3']
        num4 = request.POST['num4']
        num5 = request.POST['num5']
    except:
        res = 'Please Enter a Valid Numerical Value'
        cas = False
        eq = ''
        x = ''
        x1 = ''
        x2 = ''
        t2 = ''
        t1 = ''
        v = ''
        g1 = ''
        g2 = ''
        g3 = ''
        g4 = ''
        uk = ''
        gn1 = ''
        gn2 = ''
        gn3 = ''
        gn4 = ''
        u1 = ''
        u2 = ''
        u3 = ''
        u4 = ''
        uu = ''
    else:
        if num1 == 'x':
            try:
                x1 = float(num2)
                t2 = float(num3)
                t1 = float(num4)
                v = float(num5)
            except:
                res = 'Please Enter a valid numerical value'
                cas = False
                eq = ''
                x = ''
                x1 = ''
                x2 = ''
                t2 = ''
                t1 = ''
                v = ''
                g1 = ''
                g2 = ''
                g3 = ''
                g4 = ''
                uk = ''
                gn1 = ''
                gn2 = ''
                gn3 = ''
                gn4 = ''
                u1 = ''
                u2 = ''
                u3 = ''
                u4 = ''
                uu = ''
            else:
                res = fx2(x1,t2,t1,v)
                x2 = res
                eq = '='
                x = 'x ='
                g1 = 'Initial Position'
                g2 = 'Final Time'
                g3 = 'Initial Time'
                g4 = 'Instantaneous Velocity'
                uk = 'Final Position'
                gn1 = x1
                gn2 = t2
                gn3 = t1
                gn4 = v
                u1 = 'm'
                u2 = 'sec'
                u3 = 'sec'
                u4 = 'm/s'
                uu = 'm'
                cas = True

        elif num2 == 'x':
            try:
                x2 = float(num1)
                t2 = float(num3)
                t1 = float(num4)
                v = float(num5)
            except:
                res = 'Please Enter a valid numerical value'
                cas = False
                eq = ''
                x = ''
                x1 = ''
                x2 = ''
                t2 = ''
                t1 = ''
                v = ''
                g1 = ''
                g2 = ''
                g3 = ''
                g4 = ''
                uk = ''
                gn1 = ''
                gn2 = ''
                gn3 = ''
                gn4 = ''
                u1 = ''
                u2 = ''
                u3 = ''
                u4 = ''
                uu = ''
            else:
                res = fx1(x2,t2,t1,v)
                x1 = res
                eq = '='
                x = 'x ='
                g1 = 'Final Position'
                g2 = 'Final Time'
                g3 = 'Initial Time'
                g4 = 'Instantaneous Velocity'
                uk = 'Initial Position'
                gn1 = x2
                gn2 = t2
                gn3 = t1
                gn4 = v
                u1 = 'm'
                u2 = 'sec'
                u3 = 'sec'
                u4 = 'm/s'
                uu = 'm'
                cas = True
        elif num3 == 'x':
            try:
                x2 = float(num1)
                x1 = float(num2)
                t1 = float(num4)
                v = float(num5)
            except:
                res = 'Please Enter a valid numerical value'
                cas = False
                eq = ''
                x = ''
                x1 = ''
                x2 = ''
                t2 = ''
                t1 = ''
                v = ''
                g1 = ''
                g2 = ''
                g3 = ''
                g4 = ''
                uk = ''
                gn1 = ''
                gn2 = ''
                gn3 = ''
                gn4 = ''
                u1 = ''
                u2 = ''
                u3 = ''
                u4 = ''
                uu = ''
            else:
                res = ft2(x2,x1,t1,v)
                x = 'x ='
                eq = '='
                t2 = res
                g1 = 'Final Position'
                g2 = 'Initial Position'
                g3 = 'Initial Time'
                g4 = 'Instantaneous Velocity'
                uk = 'Final Time'
                cas = True
                gn1 = x2
                gn2 = x1
                gn3 = t1
                gn4 = v
                u1 = 'm'
                u2 = 'm'
                u3 = 'sec'
                u4 = 'm/s'
                uu = 'sec'
        elif num4 == 'x':
            try:
                x2 = float(num1)
                x1 = float(num2)
                t2 = float(num3)
                v = float(num5)
            except:
                res = 'Please Enter a valid numerical value'
                cas = False
                eq = ''
                x = ''
                x1 = ''
                x2 = ''
                t2 = ''
                t1 = ''
                v = ''
                g1 = ''
                g2 = ''
                g3 = ''
                g4 = ''
                uk = ''
                gn1 = ''
                gn2 = ''
                gn3 = ''
                gn4 = ''
                u1 = ''
                u2 = ''
                u3 = ''
                u4 = ''
                uu = ''

            else:
                res = ft1(x2,x1,t2,v)
                t1 = res
                eq = '='
                x = 'x ='
                g1 = 'Final Position'
                g2 = 'Initial Position'
                g3 = 'Final Time'
                g4 = 'Instantaneous Velocity'
                uk = 'Initial Time'
                cas = True
                gn1 = x2
                gn2 = x1
                gn3 = t2
                gn4 = v
                u1 = 'm'
                u2 = 'm'
                u3 = 'sec'
                u4 = 'm/s'
                uu = 'sec'
        else:
            try:
                x2 = float(num1)
                x1 = float(num2)
                t2 = float(num3)
                t1 = float(num4)
            except:
                res = 'Please Enter a valid numerical value'
                cas = False
                eq = ''
                x = ''
                x1 = ''
                x2 = ''
                t2 = ''
                t1 = ''
                v = ''
                g1 = ''
                g2 = ''
                g3 = ''
                g4 = ''
                uk = ''
                gn1 = ''
                gn2 = ''
                gn3 = ''
                gn4 = ''
                u1 = ''
                u2 = ''
                u3 = ''
                u4 = ''
                uu = ''
            else:
                res = fv(x2,x1,t2,t1)
                v = res
                eq = '='
                x = 'x ='
                g1 = 'Final Position'
                g2 = 'Initial Position'
                g3 = 'Final Time'
                g4 = 'Initial Time'
                uk = 'Instantaneous Velocity'
                cas = True
                gn1 = x2 
                gn2 = x1
                gn3 = t2
                gn4 = t1
                u1 = 'm'
                u2 = 'm'
                u3 = 'sec'
                u4 = 'sec'
                uu = 'm/s'
    return render(request,"instantaneousvelocity.html",
    {'result':res,'x2':x2,'x1':x1,'t2':t2,'t1':t1,'v':v,'cas':cas,'g1':g1,'g2':g2,'g3':g3,'g4':g4,'uk':uk,'gn1':gn1,'gn2':gn2,'gn3':gn3,
    'gn4':gn4,'x':x,'eq':eq,'u1':u1,'u2':u2,'u3':u3,'u4':u4,'uu':uu})

def horsepower(request):
    try:
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        num3 = request.POST['num3']
        num4 = request.POST['num4']
    except:
        res = 'Please Enter an Valid Numerical value'
        strg1 = ''
        strg2 = ''
        strg3 = ''
        stru = ''
        g1 = ''
        g2 = ''
        g3 = ''
        x = ''
        eq = ''
        unit = ''
        p = ''
        d = ''
        t = ''
        f = ''
        u1 = ''
        u2 = ''
        u3 = ''
        cas = False
    else:
        if num1=='x':
            try:
                d = float(num2)
                t = float(num3)
                f = float(num4)

            except:
                res = 'Please Enter valid Numerical Value'
                strg1 = ''
                strg2 = ''
                strg3 = ''
                stru = ''
                g1 = ''
                g2 = ''
                g3 = ''
                x = ''
                eq = ''
                unit = ''
                p = ''
                d = ''
                t = ''
                f = ''
                u1 = ''
                u2 = ''
                u3 = ''
                cas = False
            else:
                res = hpp(d,t,f)
                p = res
                strg1 = 'Distance'
                strg2 = 'Time'
                strg3 = 'Force'
                g1 = d
                g2 = t
                g3 = f
                u1 = 'm'
                u2 = 's'
                u3 = 'N'
                stru = 'Horsepower'
                x = 'x ='
                eq = '='
                unit = 'hp'
                cas = True
        elif num2=='x':
            try:
                p = float(num1)
                t = float(num3)
                f = float(num4)
            except:
                res = 'Please Enter valid Numerical Value'
                strg1 = ''
                strg2 = ''
                strg3 = ''
                stru = ''
                g1 = ''
                g2 = ''
                g3 = ''
                x = ''
                eq = ''
                unit = ''
                p = ''
                d = ''
                t = ''
                f = ''
                u1 = ''
                u2 = ''
                u3 = ''
                cas = False
            else:
                res = hpd(p,t,f)
                d = res
                strg1 = 'Horsepower'
                strg2 = 'Time'
                strg3 = 'Force'
                g1 = p
                g2 = t
                g3 = f
                u1 = 'hp'
                u2 = 's'
                u3 = 'N'
                stru = 'Distance'
                x = 'x ='
                eq = '='
                unit = 'm'
                cas = True
        elif num3=='x':
            try:
                p = float(num1)
                d = float(num2)
                f = float(num4)
            except:
                res = 'Please Enter valid Numerical Value'
                strg1 = ''
                strg2 = ''
                strg3 = ''
                stru = ''
                g1 = ''
                g2 = ''
                g3 = ''
                x = ''
                eq = ''
                unit = ''
                p = ''
                d = ''
                t = ''
                f = ''
                u1 = ''
                u2 = ''
                u3 = ''
                cas = False
            else:
                res = hpt(p,d,f)
                t = res
                strg1 = 'Horsepower'
                strg2 = 'Distance'
                strg3 = 'Force'
                g1 = p
                g2 = d
                g3 = f
                u1 = 'hp'
                u2 = 'm'
                u3 = 'N'
                stru = 'Time'
                x = 'x ='
                eq = '='
                unit = 'sec'
                cas = True
        else:
            try:
                p = float(num1)
                d = float(num2)
                t = float(num3)
            except:
                res = 'Please Enter valid Numerical Value'
                strg1 = ''
                strg2 = ''
                strg3 = ''
                stru = ''
                g1 = ''
                g2 = ''
                g3 = ''
                x = ''
                eq = ''
                unit = ''
                p = ''
                d = ''
                t = ''
                f = ''
                u1 = ''
                u2 = ''
                u3 = ''
                cas = False
            else:
                res = hpf(p,d,t)
                f = res
                strg1 = 'Horsepower'
                strg2 = 'Distance'
                strg3 = 'Time'
                g1 = p
                g2 = d
                g3 = t
                u1 = 'hp'
                u2 = 'm'
                u3 = 's'
                stru = 'Force'
                x = 'x ='
                eq = '='
                unit = 'N'
                cas = True
    return render(request,"horsepower.html",{'result':res,'p':p,'d':d,'t':t,'f':f ,'strg1':strg1,'strg2':strg2,'stru':stru,'g1':g1,'g2':g2,'x':x,'eq':eq,'unit':unit,'cas':cas,
    'strg3':strg3,'g3':g3,'u1':u1,'u2':u2,'u3':u3})

def impulse(request):
    try:
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        num3 = request.POST['num3']
    except:
        res = 'Please Enter an Valid Numerical value'
        strg1 = ''
        strg2 = ''
        stru = ''
        g1 = ''
        g2 = ''
        x = ''
        eq = ''
        unit = ''
        j = ''
        f = ''
        t = ''
        u1 = ''
        u2 = ''
        cas = False
    else:
        if num1=='x':
            try:
                f = float(num2)
                t = float(num3)
            except:
                res = 'Please Enter valid Numerical Value'
                strg1 = ''
                strg2 = ''
                stru = ''
                g1 = ''
                g2 = ''
                x = ''
                eq = ''
                unit = ''
                j = ''
                f = ''
                t = ''
                u1 = ''
                u2 = ''
                cas = False
            else:
                res = imj(f,t)
                j = res
                strg1 = 'Force'
                strg2 = 'Time'
                g1 = f
                g2 = t
                u1 = 'N'
                u2 = 's'
                stru = 'Impulse'
                x = 'x ='
                eq = '='
                unit = 'N sec'
                cas = True
        elif num2=='x':
            try:
                j = float(num1)
                t = float(num3)
            except:
                res = 'Please Enter an Valid Numerical value'
                strg1 = ''
                strg2 = ''
                stru = ''
                g1 = ''
                g2 = ''
                x = ''
                eq = ''
                unit = ''
                j = ''
                f = ''
                t = ''
                u1 = ''
                u2 = ''
                u3 = ''
                cas = False
            else:
                res = imf(j,t)
                f = res
                strg1 = 'Impulse'
                strg2 = 'Time'
                g1 = j
                g2 = t
                u1 = 'N sec'
                u2 = 's'
                stru = 'Force'
                x = 'x ='
                eq = '='
                unit = 'N'
                cas = True
        else:
            try:
                j = float(num1)
                f = float(num2)
            except:
                res = 'Please Enter an Valid Numerical value'
                strg1 = ''
                strg2 = ''
                stru = ''
                g1 = ''
                g2 = ''
                x = ''
                eq = ''
                unit = ''
                j = ''
                f = ''
                t = ''
                u1 = ''
                u2 = ''
                cas = False
            else:
                res = imt(j,f)
                t = res
                strg1 = 'Impulse'
                strg2 = 'Force'
                g1 = j
                g2 = f
                u1 = 'N sec'
                u2 = 'N'
                stru = 'Time'
                x = 'x ='
                eq = '='
                unit = 's'
                cas = True
    return render(request,"impulse.html",{'result':res,'j':j,'f':f,'t':t, 'strg1':strg1,'strg2':strg2,'stru':stru,'g1':g1,'g2':g2,'x':x,'eq':eq,'unit':unit
    ,'cas':cas,'u1':u1,'u2':u2})

def inductivereactance(request):
    try:
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        num3 = request.POST['num3']
    except:
        res = 'Please Enter a Valid Numerical value'
        u1 = ''
        u2 = ''
        strg1 = ''
        strg2 = ''
        stru = ''
        x = ''
        g1 = ''
        g2 = ''
        eq = ''
        unit = ''
        i = ''
        f = ''
        xl = ''
        cas = False
    else:
        if num1=='x':
            try:
                i = float(num2)
                f = float(num3)
            except:
                res = 'Please Enter valid Numerical Value'
                strg1 = ''
                strg2 = ''
                u1 = ''
                u2 = ''
                stru = ''
                x = ''
                g1 = ''
                g2 = ''
                x = ''
                eq = ''
                unit = ''
                i = ''
                f = ''
                xl = ''
                cas = False
            else:
                res = irxl(i,f)
                xl = res
                strg1 = 'Inductance'
                strg2 = 'Frequency'
                u1 = 'H'
                u2 = 'Hz'
                g1 = i
                g2 = f
                stru = 'Inductive Reactance'
                x = 'x ='
                eq = '='
                unit = 'ohm'
                cas = True
        elif num2=='x':
            try:
                xl = float(num1)
                f = float(num3)
            except:
                res = 'Please Enter a Valid Numerical value'
                strg1 = ''
                u1 = ''
                u2 = ''
                strg2 = ''
                stru = ''
                g1 = ''
                g2 = ''
                x = ''
                eq = ''
                unit = ''
                i = ''
                f = ''
                xl = ''
                cas = False
            else:
                res = iri(xl,f)
                i = res
                strg1 = 'Inductive Reactance'
                strg2 = 'Frequency'
                g1 = xl
                u1 = 'ohm'
                u2 = 'Hz'
                g2 = f
                stru = 'Inductance'
                x = 'x ='
                eq = '='
                unit = 'H'
                cas = True
        else:
            try:
                xl = float(num1)
                i = float(num2)
            except:
                res = 'Please Enter a Valid Numerical value'
                strg1 = ''
                u1 = ''
                u2 = ''
                strg2 = ''
                stru = ''
                g1 = ''
                g2 = ''
                x = ''
                eq = ''
                unit = ''
                i = ''
                xl = ''
                f = ''
                cas = False
            else:
                res = irf(xl,i)
                f = res
                strg1 = 'Inductive Reactance'
                strg2 = 'Inductance'
                u1 = 'ohm'
                u2 = 'H'
                g1 = xl
                g2 = i
                stru = 'Frequency'
                x = 'x ='
                eq = '='
                unit = 'Hz'
                cas = True
    return render(request,"inductivereactance.html",{'result':res,'fr':i,'mu':f,'nf':xl, 'strg1':strg1,
    'strg2':strg2,'stru':stru,'g1':g1,'u1':u1,'u2':u2,
    'g2':g2,'x':x,'eq':eq,'unit':unit,'cas':cas})

def heattransfer(request):
    try:
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        num3 = request.POST['num3']
        num4 = request.POST['num4']
    except:
        res = 'Please Enter a Valid Numerical value'
        u1 = ''
        u2 = ''
        u3 = ''
        strg1 = ''
        strg2 = ''
        strg3 = ''
        stru = ''
        x = ''
        g1 = ''
        g2 = ''
        g3 = ''
        eq = ''
        unit = ''
        k = ''
        dt = ''
        d = ''
        q = ''
        cas = False
    else:
        if num1=='x':
            try:
                k = float(num2)
                dt = float(num3)
                d = float(num4)
            except:
                res = 'Please Enter a Valid Numerical value'
                u1 = ''
                u2 = ''
                u3 = ''
                strg1 = ''
                strg2 = ''
                strg3 = ''
                stru = ''
                x = ''
                g1 = ''
                g2 = ''
                g3 = ''
                eq = ''
                unit = ''
                q = ''
                k = ''
                dt = ''
                d = ''
                cas = False
            else:
                res = heatq(k,dt,d)
                q = res
                strg1 = 'Thermal Conductivity Constant'
                strg2 = 'Temperature Difference'
                strg3 = 'Distance'
                u1 = 'Calorie/cm.C.s'
                u2 = 'K'
                u3 = 'm'
                g1 = k
                g2 = dt
                g3 = d
                stru = 'Heat Transfer'
                x = 'x ='
                eq = '='
                unit = 'Calorie/cm².s'
                cas = True
        elif num2=='x':
            try:
                q = float(num1)
                dt = float(num3)
                d = float(num4)
            except:
                res = 'Please Enter a Valid Numerical value'
                strg1 = ''
                u1 = ''
                u2 = ''
                u3 = ''
                strg2 = ''
                strg3 = ''
                stru = ''
                g1 = ''
                g2 = ''
                g3 = ''
                x = ''
                eq = ''
                unit = ''
                q = ''
                dt = ''
                d = ''
                k = ''
                cas = False
            else:
                res = heatk(q,dt,d)
                k = res
                strg1 = 'Heat Transfer'
                strg2 = 'Temperature Difference'
                strg3 = 'Distance'
                g1 = q
                u1 = 'Calorie/cm².s'
                u2 = 'K'
                u3 = 'm'
                g2 = dt
                g3 = d
                stru = 'Thermal Conductivity Constant'
                x = 'x ='
                eq = '='
                unit = 'Calorie/cm.C.s'
                cas = True
        elif num3=='x':
            try:
                q = float(num1)
                k = float(num2)
                d = float(num4)
            except:
                res = 'Please Enter a Valid Numerical value'
                strg1 = ''
                u1 = ''
                u2 = ''
                u3 = ''
                strg2 = ''
                strg3 = ''
                stru = ''
                g1 = ''
                g2 = ''
                g3 = ''
                x = ''
                eq = ''
                unit = ''
                q = ''
                dt = ''
                d = ''
                k = ''
                cas = False
            else:
                res = heatdt(q,k,d)
                dt = res
                strg1 = 'Heat Transfer'
                strg2 = 'Thermal Conductivity Constant'
                strg3 = 'Distance'
                g1 = q
                u1 = 'Calorie/cm².s'
                u2 = 'Calorie/cm.C.s'
                u3 = 'm'
                g2 = k
                g3 = d
                stru = 'Temperature Difference'
                x = 'x ='
                eq = '='
                unit = 'K'
                cas = True
        else:
            try:
                q = float(num1)
                k = float(num2)
                dt = float(num3)
            except:
                res = 'Please Enter a Valid Numerical value'
                strg1 = ''
                u1 = ''
                u2 = ''
                u3 = ''
                strg2 = ''
                strg3 = ''
                stru = ''
                g1 = ''
                g2 = ''
                g3 = ''
                x = ''
                eq = ''
                unit = ''
                q = ''
                k = ''
                dt = ''
                d = ''
                cas = False
            else:
                res = heatd(q,k,dt)
                d = res
                strg1 = 'Heat Transfer'
                strg2 = 'Thermal Conductivity Constant'
                strg3 = 'Temperature Difference'
                u1 = 'Calorie/cm².s'
                u2 = 'Calorie/cm.C.s'
                u3 = 'K'
                g1 = q
                g2 = k
                g3 = dt
                stru = 'Distance'
                x = 'x ='
                eq = '='
                unit = 'm'
                cas = True
    return render(request,"heattransfer.html",{'result':res,'q':q,'dt':dt,'d':d,'k':k, 'strg1':strg1,
    'strg2':strg2,'stru':stru,'g1':g1,'u1':u1,'u2':u2,'g3':g3,'u3':u3,'strg3':strg3,
    'g2':g2,'x':x,'eq':eq,'unit':unit,'cas':cas})

def machnumber(request):
    try:
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        num3 = request.POST['num3']
    except:
        res = 'Please Enter valid Numerical Value'
        strg1 = ''
        strg2 = ''
        stru = ''
        g1 = ''
        g2 = ''
        x = ''
        eq = ''
        unit = ''
        v = ''
        c = ''
        m = ''
        u1 = ''
        u2 = ''
        cas = False
    else:
        if num1=='x':
            try:
                c = float(num2)
                m = float(num3)
            except:
                res = 'Please Enter valid Numerical Value'
                strg1 = ''
                strg2 = ''
                stru = ''
                g1 = ''
                g2 = ''
                x = ''
                eq = ''
                unit = ''
                v = ''
                c = ''
                m = ''
                u1 = ''
                u2 = ''
                cas = False
            else:
                res = machv(c,m)
                v = res
                strg1 = 'Speed of Sound in medium'
                strg2 = 'Mach Number'
                g1 = c
                g2 = m
                stru = 'Object speed'
                x = 'x ='
                eq = '='
                unit = 'm/s'
                u1 = 'm/s'
                u2 = ''
                cas = True
        elif num2=='x':
            try:
                v = float(num1)
                m = float(num3)
            except:
                res = 'Please Enter valid Numerical Value'
                strg1 = ''
                strg2 = ''
                stru = ''
                g1 = ''
                g2 = ''
                x = ''
                eq = ''
                unit = ''
                v = ''
                c = ''
                m = ''
                u1 = ''
                u2 = ''
                cas = False
            else:
                res = machc(v,m)
                c = res
                strg1 = 'Object speed'
                strg2 = 'Mach Number'
                g1 = v
                g2 = m
                stru = 'Speed of Sound in medium'
                x = 'x ='
                eq = '='
                unit = 'm/s'
                u1 = 'm/s'
                u2 = ''
                cas = True
        else:
            try:
                v = float(num1)
                c = float(num2)
            except:
                res = 'Please Enter valid Numerical Value'
                strg1 = ''
                strg2 = ''
                stru = ''
                g1 = ''
                g2 = ''
                x = ''
                eq = ''
                unit = ''
                v = ''
                c = ''
                m = ''
                u1 = ''
                u2 = ''
                cas = False
            else:
                res = machm(v,c)
                m = res
                strg1 = 'Object Speed'
                strg2 = 'Speed of Sound in medium'
                g1 = v
                g2 = c
                stru = 'Mach Number'
                x = 'x ='
                eq = '='
                unit = ''
                u1 = 'm/s'
                u2 = 'm/s'
                cas = True
    return render(request,"machnumber.html",{'result':res,'v':v,'c':c,'m':m, 'strg1':strg1,'strg2':strg2,'stru':stru,'g1':g1,'g2':g2,'x':x,
    'eq':eq,'unit':unit,'cas':cas,'u1':u1,'u2':u2})
def lcresonance(request):
    try:
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        num3 = request.POST['num3']
    except:
        res = 'Please Enter an Valid Numerical value'
        strg1 = ''
        strg2 = ''
        stru = ''
        g1 = ''
        g2 = ''
        x = ''
        eq = ''
        unit = ''
        f = ''
        l = ''
        c = ''
        u1 = ''
        u2 = ''
        cas = False
    else:
        if num1=='x':
            try:
                c = float(num2)
                l = float(num3)
            except:
                res = 'Please Enter valid Numerical Value'
                strg1 = ''
                strg2 = ''
                stru = ''
                u1 = ''
                u2 = ''
                g1 = ''
                g2 = ''
                x = ''
                eq = ''
                unit = ''
                f = ''
                l = ''
                c = ''
                cas = False
            else:
                res = lcf(c,l)
                f = res
                strg1 = 'Capacitance'
                strg2 = 'Inductance'
                g1 = c
                g2 = l
                u1 = 'μC'
                u2 = 'H'
                stru = 'Frequency'
                x = 'x ='
                eq = '='
                unit = 'Hz'
                cas = True
        elif num2=='x':
            try:
                f = float(num1)
                l = float(num3)
            except:
                res = 'Please Enter an Valid Numerical value'
                strg1 = ''
                strg2 = ''
                stru = ''
                g1 = ''
                g2 = ''
                u1 = ''
                u2 = ''
                x = ''
                eq = ''
                unit = ''
                f = ''
                l = ''
                c = ''
                cas = False
            else:
                res = lcc(f,l)
                c = res
                strg1 = 'Frequency'
                strg2 = 'Inductance'
                g1 = f
                g2 = l
                u1 = 'Hz'
                u2 = 'H'
                stru = 'Capacitance'
                x = 'x ='
                eq = '='
                unit = 'μC'
                cas = True
        else:
            try:
                f = float(num1)
                c = float(num2)
            except:
                res = 'Please Enter an Valid Numerical value'
                strg1 = ''
                strg2 = ''
                stru = ''
                g1 = ''
                g2 = ''
                u1 = ''
                u2 = ''
                x = ''
                eq = ''
                unit = ''
                f = ''
                l = ''
                c = ''
                cas = False
            else:
                res = lcl(f,c)
                l = res
                strg1 = 'Frequency'
                strg2 = 'Capacitance'
                g1 = f
                g2 = c
                u1 = 'Hz'
                u2 = 'μC'
                stru = 'Inductance'
                x = 'x ='
                eq = '='
                unit = 'H'
                cas = True
    return render(request,"lcresonance.html",{'result':res,'f':f,'l':l,'c':c, 'strg1':strg1,'strg2':strg2,'stru':stru,'g1':g1,'g2':g2,
    'x':x,'eq':eq,'unit':unit,'cas':cas,'u1':u1,'u2':u2})

def zenerdiode(request):
    try:
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        num3 = request.POST['num3']
        num4 = request.POST['num4']
    except:
        rest = 'Please Enter a Valid Numerical Value'
        cas = False
        message = ''
        g1 = ''
        g2 = ''
        g3 = ''
        g4 = ''
        gn1 = ''
        gn2 = ''
        gn3 = ''
        gn4 = ''
        res = ''
        zp = ''
        zv = ''
        rp = ''
    else:
            try:
                vmi = float(num1)
                vmax = float(num2)
                vout = float(num3)
                il = float(num4)
            except:
                rest = 'Please Enter a valid numerical value'
                cas = False
                message = ''
                g1 = ''
                g2 = ''
                g3 = ''
                g4 = ''
                gn1 = ''
                gn2 = ''
                gn3 = ''
                gn4 = ''
                zv = ''
                zp = ''
                rp = ''
                res = ''
            else:
                if vmi<=vout:
                    rest = ''
                    cas = False
                    message = 'Minimum Input Voltage is low than Output Voltage!'
                    g1 = ''
                    g2 = ''
                    g3 = ''
                    g4 = ''
                    gn1 = ''
                    gn2 = ''
                    gn3 = ''
                    gn4 = ''
                    zv = ''
                    zp = ''
                    rp = ''
                    res = ''
                else:
                    rest = ''
                    message = ''
                    resu = calc(vmi,vmax,vout,il)
                    res = resu[0]
                    zv = resu[1]
                    zp = resu[2]
                    rp = resu[3]
                    g1 = 'Minimum Input Voltage'
                    g2 = 'Maximum Input Voltage'
                    g3 = 'Output Voltage'
                    g4 = 'Load Current'
                    gn1 = vmi
                    gn2 = vmax
                    gn3 = vout
                    gn4 = il
                    cas = True
    return render(request,"zenerdiode.html",{'rest':rest,'cas':cas,'res':res,'zv':zv,'zp':zp,'rp':rp,
    'g1':g1,'g2':g2,'g3':g3,'gn1':gn1,'gn2':gn2,'gn3':gn3,'gn4':gn4,'g4':g4,'message':message})

def centripetal_acceleration(request):
    try:
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        num3 = request.POST['num3']
    except:
        res = ''
        cas = False
        ukv = ''
        uks = ''
        g1 = ''
        g2 = ''
        gn1 = ''
        gn2 = ''
        u1 = ''
        u2 = ''
        unit = ''
    else:
        if num1=='x':
            try:
                v = float(num2)
                r = float(num3)
            except:
                res = 'Please Enter a valid numerical value'
                cas = False
                ukv = ''
                uks = ''
                g1 = ''
                g2 = ''
                gn1 = ''
                gn2 = ''
                u1 = ''
                u2 = ''
                unit = ''
            else:
                res = ''
                cas = True
                ukv = ca(v,r)
                uks = 'Centripetal Acceleration'
                g1 = 'Velocity'
                g2 = 'Radius'
                gn1 = v
                gn2 = r
                u1 = 'm/s'
                u2 = 'm'
                unit = 'm/s²'
        elif num2=='x':
            try:
                a = float(num1)
                r = float(num3)
            except:
                res = 'Please Enter a valid numerical value'
                cas = False
                ukv = ''
                uks = ''
                g1 = ''
                g2 = ''
                gn1 = ''
                gn2 = ''
                u1 = ''
                u2 = ''
                unit = ''
            else:
                res = ''
                cas = True
                ukv = cv(a,r)
                uks = 'Velocity'
                g1 = 'Centripetal Acceleration'
                g2 = 'Radius'
                gn1 = a
                gn2 = r
                u1 = 'm/s²'
                u2 = 'm'
                unit = 'm/s'
        else:
            try:
                a = float(num1)
                v = float(num2)
            except:
                res = 'Please Enter a valid numerical value'
                cas = False
                ukv = ''
                uks = ''
                g1 = ''
                g2 = ''
                gn1 = ''
                gn2 = ''
                u1 = ''
                u2 = ''
                unit = ''
            else:
                res = ''
                cas = True
                ukv = cr(a,v)
                uks = 'Radius'
                g1 = 'Centripetal Acceleration'
                g2 = 'Velocity'
                gn1 = a
                gn2 = v
                u1 = 'm/s²'
                u2 = 'm/s'
                unit = 'm'
    return render(request,'centripetalacceleration.html',{'res':res,'cas':cas,'ukv':ukv,'uks':uks,'g1':g1,'g2':g2,
    'gn1':gn1,'gn2':gn2,'u1':u1,'u2':u2,'unit':unit})

def resistance_frequency_capacitance(request):
    try:
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        num3 = request.POST['num3']
    except:
        res = ''
        cas = False
        f = ''
        c = ''
        r = ''
        ukv = ''
        uks = ''
        gn1 = ''
        gn2 = ''
        g1 = ''
        g2 = ''
        u1 = ''
        u2 = ''
        unit = ''
    else:
        if num1=='x':
            try:
                f = float(num2)
                c = float(num3)
            except:
                res = 'Please Enter a valid numerical value'
                cas = False
                f = ''
                c = ''
                r = ''
                ukv = ''
                uks = ''
                gn1 = ''
                gn2 = ''
                g1 = ''
                g2 = ''
                u1 = ''
                u2 = ''
                unit = ''
            else:
                ukv = rfcr(f,c)
                uks = 'Resistance'
                gn1 = f
                gn2 = c
                g1 = 'Frequency'
                g2 = 'Capacitance'
                u1 = 'Hz'
                u2 = 'μF'
                unit = 'Ω'
                res = ''
                cas = True
                r = ''
        elif num2=='x':
            try:
                r = float(num1)
                c = float(num3)
            except:
                res = 'Please Enter a valid numerical value'
                cas = False
                f = ''
                c = ''
                r = ''
                ukv = ''
                uks = ''
                gn1 = ''
                gn2 = ''
                g1 = ''
                g2 = ''
                u1 = ''
                u2 = ''
                r = ''
                unit = ''
            else:
                ukv = rfcf(r,c)
                uks = 'Frequency'
                f = ''
                gn1 = r
                gn2 = c
                g1 = 'Resistance'
                g2 = 'Capacitance'
                u1 = 'Ω'
                u2 = 'μF'
                unit = 'Hz'
                res = ''
                cas = True
        else:
            try:
                r = float(num1)
                f = float(num2)
            except:
                res = 'Please Enter a valid numerical value'
                cas = False
                f = ''
                c = ''
                r = ''
                ukv = ''
                uks = ''
                gn1 = ''
                gn2 = ''
                g1 = ''
                g2 = ''
                u1 = ''
                u2 = ''
                r = ''
                unit = ''
            else:
                ukv = rfcc(r,f)
                uks = 'Capacitance'
                gn1 = r
                gn2 = f
                g1 = 'Resistance'
                g2 = 'Frequency'
                u1 = 'Ω'
                u2 = 'Hz'
                unit = 'μF'
                res = ''
                c = ''
                cas = True
    return render(request,'resistance-frequency-capacitance.html',{'gn1':gn1,'gn2':gn2,'g1':g1,'g2':g2,
    'r':r,'f':f,'c':c,'u1':u1,'u2':u2,'unit':unit,'cas':cas,'res':res,'ukv':ukv,'uks':uks})
def kinematic(request):
    try:
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        num3 = request.POST['num3']
        num4 = request.POST['num4']
        num5 = request.POST['num5']
    except:
        res = 'Please Enter valid Numerical value'
        u = ''
        v = ''
        t = ''
        s = ''
        a = ''
        g1 = ''
        g2 = ''
        g3 = ''
        u1 = ''
        u2 = ''
        u3 = ''
        uk1 = ''
        uk2 = ''
        unit1 = ''
        unit2 = ''
        cas = False
        tf1 = ''
        tf2 = ''
        gn1 = ''
        gn2 = ''
        gn3 = ''
        f1 = ''
        f2 = ''
    else:
        if   (num1=='x' and num2=='y') or (num1=='y' and num2 == 'x'):
            try:
                u = float(num3)
                v = float(num4)
                t = float(num5)
            except:
                res = 'Please Enter a valid Numerical value'
                u = ''
                v = ''
                t = ''
                s = ''
                a = ''
                g1 = ''
                g2 = ''
                g3 = ''
                u1 = ''
                u2 = ''
                u3 = ''
                uk1 = ''
                uk2 = ''
                unit1 = ''
                unit2 = ''
                cas = False
                tf1 = ''
                tf2 = ''
                gn1 = ''
                gn2 = ''
                gn3 = ''
                f1 = ''
                f2 = ''
            else:
                ff = kinsa(u,v,t)
                s = ff[0]
                a = ff[1]
                g1 = 'Initial Velocity'
                g2 = 'Final Velocity'
                g3 = 'Time'
                u1 = 'm/s'
                u2 = 'm/s'
                u3 = 's'
                uk1 = 'Distance'
                uk2 = 'Acceleration'
                unit1 = 'm'
                unit2 = 'm/s²'
                cas = True
                res = ''
                tf1 = s
                tf2 = a
                gn1 = u
                gn2 = v
                gn3 = t
                f1 = 'v = u+at'
                f2 = 's = ut + ½at²'
        elif (num1=='x' and num3=='y') or (num1=='y' and num3=='x'):
            try:
                a = float(num2)
                v = float(num4)
                t = float(num5)
            except:
                res = 'Please Enter a valid Numerical value'
                u = ''
                v = ''
                t = ''
                s = ''
                a = ''
                g1 = ''
                g2 = ''
                g3 = ''
                u1 = ''
                u2 = ''
                u3 = ''
                uk1 = ''
                uk2 = ''
                unit1 = ''
                unit2 = ''
                cas = False
                tf1 = ''
                tf2 = ''
                gn1 = ''
                gn2 = ''
                gn3 = ''
                f1 = ''
                f2 = ''
            else:
                ff = kinsu(a,v,t)
                s = ff[0]
                u = ff[1]
                g1 = 'Acceleration'
                g2 = 'Final Velocity'
                g3 = 'Time'
                u1 = 'm/s²'
                u2 = 'm/s'
                u3 = 's'
                uk1 = 'Distance'
                uk2 = 'Initial Velocity'
                unit1 = 'm'
                unit2 = 'm/s'
                cas = True
                res = ''
                tf1 = s
                tf2 = u
                gn1 = a
                gn2 = v
                gn3 = t
                f1 = 'v = u+at'
                f2 = 's = ut + ½at²'
        elif (num1=='x' and num4=='y') or (num1=='y' and num4=='x'):
            try:
                a = float(num2)
                u = float(num3)
                t = float(num5)
            except:
                res = 'Please Enter a valid Numerical value'
                u = ''
                v = ''
                t = ''
                s = ''
                a = ''
                g1 = ''
                g2 = ''
                g3 = ''
                u1 = ''
                u2 = ''
                u3 = ''
                uk1 = ''
                uk2 = ''
                unit1 = ''
                unit2 = ''
                cas = False
                tf1 = ''
                tf2 = ''
                gn1 = ''
                gn2 = ''
                gn3 = ''
                f1 = ''
                f2 = ''
            else:
                ff = kinsv(a,u,t)
                s = ff[0]
                v = ff[1]
                g1 = 'Acceleration'
                g2 = 'Initial Velocity'
                g3 = 'Time'
                u1 = 'm/s²'
                u2 = 'm/s'
                u3 = 's'
                uk1 = 'Distance'
                uk2 = 'Final Velocity'
                unit1 = 'm'
                unit2 = 'm/s'
                cas = True
                res = ''
                tf1 = s
                tf2 = v
                gn1 = a
                gn2 = u
                gn3 = t
                f1 = 'v = u+at'
                f2 = 's = ut + ½at²'
        elif (num1=='x' and num5=='y') or (num1=='y' and num5=='x'):
            try:
                a = float(num2)
                u = float(num3)
                v = float(num4)
            except:
                res = 'Please Enter a valid Numerical value'
                u = ''
                v = ''
                t = ''
                s = ''
                a = ''
                g1 = ''
                g2 = ''
                g3 = ''
                u1 = ''
                u2 = ''
                u3 = ''
                uk1 = ''
                uk2 = ''
                unit1 = ''
                unit2 = ''
                cas = False
                tf1 = ''
                tf2 = ''
                gn1 = ''
                gn2 = ''
                gn3 = ''
                f1 = ''
                f2 = ''
            else:
                ff = kinst(a,u,v)
                s = ff[0]
                t = ff[1]
                g1 = 'Acceleration'
                g2 = 'Initial Velocity'
                g3 = 'Final Velocity'
                u1 = 'm/s²'
                u2 = 'm/s'
                u3 = 'm/s'
                uk1 = 'Distance'
                uk2 = 'Time'
                unit1 = 'm'
                unit2 = 's'
                cas = True
                res = ''
                tf1 = s
                tf2 = t
                gn1 = a
                gn2 = u
                gn3 = v
                f1 = 'v = u+at'
                f2 = 's = ut + ½at²'
        elif (num2=='x' and num3=='y') or (num2=='y' and num3=='x'):
            try:
                s = float(num1)
                v = float(num4)
                t = float(num5)
            except:
                res = 'Please Enter a valid Numerical value'
                u = ''
                v = ''
                t = ''
                s = ''
                a = ''
                g1 = ''
                g2 = ''
                g3 = ''
                u1 = ''
                u2 = ''
                u3 = ''
                uk1 = ''
                uk2 = ''
                unit1 = ''
                unit2 = ''
                cas = False
                tf1 = ''
                tf2 = ''
                gn1 = ''
                gn2 = ''
                gn3 = ''
                f1 = ''
                f2 = ''
            else:
                ff = kinau(s,v,t)
                a = ff[0]
                u = ff[1]
                g1 = 'Distance'
                g2 = 'Final Velocity'
                g3 = 'Time'
                u1 = 'm'
                u2 = 'm/s'
                u3 = 's'
                uk1 = 'Acceleration'
                uk2 = 'Initial Velocity'
                unit1 = 'm/s²'
                unit2 = 'm/s'
                cas = True
                res = ''
                tf1 = a
                tf2 = u
                gn1 = s
                gn2 = v
                gn3 = t
                f1 = 'u = (2s/t)-v'
                f2 = 'v = u+at'
        elif (num2=='x' and num4=='y') or (num2=='y' and num4=='x'):
            try:
                s = float(num1)
                u = float(num3)
                t = float(num5)
            except:
                res = 'Please Enter a valid Numerical value'
                u = ''
                v = ''
                t = ''
                s = ''
                a = ''
                g1 = ''
                g2 = ''
                g3 = ''
                u1 = ''
                u2 = ''
                u3 = ''
                uk1 = ''
                uk2 = ''
                unit1 = ''
                unit2 = ''
                cas = False
                tf1 = ''
                tf2 = ''
                gn1 = ''
                gn2 = ''
                gn3 = ''
                f1 = ''
                f2 = ''
            else:
                ff = kinav(s,u,t)
                a = ff[0]
                v = ff[1]
                g1 = 'Distance'
                g2 = 'Initial Velocity'
                g3 = 'Time'
                u1 = 'm'
                u2 = 'm/s'
                u3 = 's'
                uk1 = 'Acceleration'
                uk2 = 'Final Velocity'
                unit1 = 'm/s²'
                unit2 = 'm/s'
                cas = True
                res = ''
                tf1 = a
                tf2 = v
                gn1 = s
                gn2 = u
                gn3 = t
                f1 = 's = ut + ½at²'
                f2 = 'v = u+at'
        elif (num2=='x' and num5=='y') or (num2=='y' and num5=='x'):
            try:
                s = float(num1)
                u = float(num3)
                v = float(num4)
            except:
                res = 'Please Enter a valid Numerical value'
                u = ''
                v = ''
                t = ''
                s = ''
                a = ''
                g1 = ''
                g2 = ''
                g3 = ''
                u1 = ''
                u2 = ''
                u3 = ''
                uk1 = ''
                uk2 = ''
                unit1 = ''
                unit2 = ''
                cas = False
                tf1 = ''
                tf2 = ''
                gn1 = ''
                gn2 = ''
                gn3 = ''
                f1 = ''
                f2 = ''
            else:
                ff = kinat(s,u,v)
                a = ff[0]
                t = ff[1]
                g1 = 'Distance'
                g2 = 'Initial Velocity'
                g3 = 'Final Velocity'
                u1 = 'm'
                u2 = 'm/s'
                u3 =  'm/s'
                uk1 = 'Acceleration'
                uk2 = 'Time'
                unit1 = 'm/s²'
                unit2 = 's'
                cas = True
                res = ''
                tf1 = a
                tf2 = t
                gn1 = s
                gn2 = u
                gn3 = v
                f1 = 'v² = u² + 2as'
                f2 = 'v = u+at'
        elif (num3=='x' and num4=='y') or (num3=='y' and num4=='x'):
            try:
                s = float(num1)
                a = float(num2)
                t = float(num5)
            except:
                res = 'Please Enter a valid Numerical value'
                u = ''
                v = ''
                t = ''
                s = ''
                a = ''
                g1 = ''
                g2 = ''
                g3 = ''
                u1 = ''
                u2 = ''
                u3 = ''
                uk1 = ''
                uk2 = ''
                unit1 = ''
                unit2 = ''
                cas = False
                tf1 = ''
                tf2 = ''
                gn1 = ''
                gn2 = ''
                gn3 = ''
                f1 = ''
                f2 = ''
            else:
                ff = kinuv(s,a,t)
                u = ff[0]
                v = ff[1]
                g1 = 'Distance'
                g2 = 'Acceleration'
                g3 = 'Time'
                u1 = 'm'
                u2 = 'm/s²'
                u3 = 's'
                uk1 = 'Initial Velocity'
                uk2 = 'Final Velocity'
                unit1 = 'm/s'
                unit2 = 'm/s'
                cas = True
                res = ''
                tf1 = u
                tf2 = v
                gn1 = s
                gn2 = a
                gn3 = t
                f1 = 's = ut + ½at²'
                f2 = 'v = u+at'
        elif (num3=='x' and num5=='y') or (num3=='y' and num5=='x'):
            try:
                s = float(num1)
                a = float(num2)
                v = float(num4)
            except:
                res = 'Please Enter a valid Numerical value'
                u = ''
                v = ''
                t = ''
                s = ''
                a = ''
                g1 = ''
                g2 = ''
                g3 = ''
                u1 = ''
                u2 = ''
                u3 = ''
                uk1 = ''
                uk2 = ''
                unit1 = ''
                unit2 = ''
                tf1 = ''
                tf2 = ''
                cas = False
                gn1 = ''
                gn2 = ''
                gn3 = ''
                f1 = ''
                f2 = ''
            else:
                ff = kinut(s,a,v)
                u = ff[0]
                t = ff[1]
                g1 = 'Distance'
                g2 = 'Acceleration'
                g3 = 'Final Velocity'
                u1 = 'm'
                u2 = 'm/s²'
                u3 = 'm/s'
                uk1 = 'Initial Velocity'
                uk2 = 'Time'
                unit1 = 'm/s'
                unit2 = 's'
                cas = True
                res = ''
                tf1 = u
                tf2 = t
                gn1 = s
                gn2 = a
                gn3 = v
                f1 = 'v² = u² + 2as'
                f2 = 'v = u+at'
        else:
            try:
                s = float(num1)
                a = float(num2)
                u = float(num3)
            except:
                res = 'Please Enter a valid Numerical value'
                u = ''
                v = ''
                t = ''
                s = ''
                a = ''
                g1 = ''
                g2 = ''
                g3 = ''
                u1 = ''
                u2 = ''
                u3 = ''
                uk1 = ''
                uk2 = ''
                unit1 = ''
                unit2 = ''
                tf1 = ''
                tf2 = ''
                gn1 = ''
                gn2 = ''
                gn3 = ''
                f1 = ''
                f2 = ''
                cas = False
            else:
                ff = kinvt(s,a,u)
                v = ff[0]
                t = ff[1]
                g1 = 'Distance'
                g2 = 'Acceleration'
                g3 = 'Initial Velocity'
                u1 = 'm/s'
                u2 = 'm/s²'
                u3 = 'm/s'
                uk1 = 'Final Velocity'
                uk2 = 'Time'
                unit1 = 'm/s'
                unit2 = 's'
                cas = True
                res = ''
                tf1 = v
                tf2 = t
                gn1 = s
                gn2 = a
                gn3 = u
                f1 = 'v² = u² + 2as'
                f2 = 'v = u+at'
    return render(request,'kinematics.html',{'s':s,'a':a,'u':u,'v':v,'t':t,'g1':g1,'g2':g2,'g3':g3,'u1':u1,'u2':u2,'u3':u3,
    'uk1':uk1,'uk2':uk2,'unit1':unit1,'unit2':unit2,'cas':cas,'res':res,'tf1':tf1,'tf2':tf2,'gn1':gn1,'gn2':gn2,'gn3':gn3,
    'f1':f1,'f2':f2})




        


