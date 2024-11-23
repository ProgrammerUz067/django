def add_son(x,y):
    return x+y


def min_num(x,y):
    return x-y




def toq_juft(x):
    return x%2 == 0





def yosh(yosh):
    if 0<yosh<=9:
        return "bola"
    elif 9<yosh<=18:
        return "O'smir"
    elif 18<yosh<=30:
        return "Yigit"
    else:
        return "Katta yoshli"








"""
 1Kiritilgan satrning birinchi, o'rta va oxirgi belgilaridan tuzilgan yangi satr yaratish dasturini yozing.
str1 = "James”
Natija: Jms
"""



def orta(soz):
    bosh=soz[0]
    oxir=soz[-1]
    orta_index=len(soz)//2
    orta=soz[orta_index]
    yangisoz=bosh+orta+oxir
    return yangisoz





def karra(x,y):
    return x*y








def ism(ism):
    teskari=ism[:-1]
    return teskari






def sonlar_ortaarifmetigi(x,y,z):
    return x*y*z









def Kattakkichikharflar(soz):
    k_harf=''
    ka_harf=''
    for harf in soz:
        if harf.islower:
            k_harf.islower()
        elif harf.isupper:
            ka_harf+=harf
    natija=ka_harf+ka_harf
    return natija






# def belgi_sonni_ajratish(kod):
#     soz=''
#     son=''
#     belgi=''
#     for x in kod:
#         if x.isnumeric:
#             son.isnumeric()
#         elif x.isalpha:
#             soz.isalpha()
#         elif x.isprintable:
#             belgi.isprintable()
#     natija=soz+son+belgi
#     return natija




def absyxs(x,y):
    natija=x[0]+y[0]+x[1]+y[1]+x[2]+y[2]
    return natija




def otaarifmetigi(x):
    natija=''
    uzunlik=len(natija)
    teng=sum(natija)/uzunlik
    for son in x:
        if son.isnum:
            natija.isalnum()
    return teng





def sanash(satr):
    natija = {}
    for belgi in satr:
        if belgi in natija:
            natija[belgi] += 1
        else:
            natija[belgi] = 1

    return natija





