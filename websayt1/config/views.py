from django.http import HttpResponse

def home(request):
    return HttpResponse("Bugun Aziz ko'p xato qildi aziz bugun trendda")


def bosh_sahifa(request):
    return HttpResponse("saytimizga xush kelibsiz")

def yangilik(request):
    return HttpResponse("Иқлим муаммолари – барқарор ривожланиш йўлида жаҳондаги энг асосий таҳдид, деди президент глобал иқлим саммитидаги нутқида. Унинг сўзларига кўра, Марказий Осиёда ҳаво ҳароратининг ошиши жаҳондаги ўртача кўрсаткичдан икки баравар кўп. Минтақада сўнгги йилларда фавқулодда иссиқ кунлар сони икки баробар кўпайиб, музликларнинг учдан бир қисми эриб кетган.")


def sozdal(request):
    return HttpResponse("Bu sayt Ramizjon Ziyodullayev tomonidan yaratilgan")














