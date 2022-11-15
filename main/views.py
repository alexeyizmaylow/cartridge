from django.shortcuts import render, redirect
from .models import *
from .forms import AuthorForm, OrderFormset
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
import xlwt, datetime


class CartAddView(TemplateView):
    template_name = "main/order_cart.html"

    def get(self, *args, **kwargs):
        form = AuthorForm()
        formset = OrderFormset()
        return self.render_to_response({'form': form, 'formset': formset})

    def post(self, *args, **kwargs):
        form = AuthorForm(data=self.request.POST)
        if form.is_valid():
            author = form.save()
            formset = OrderFormset(data=self.request.POST, instance=author)
            if formset.is_valid():
                formset.save()
                return redirect("success/")
        return self.render_to_response({'form': form, 'formset': formset})


def success(request):
    return render(request, 'main/kek.html')


def export(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="cart.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("Все картриджи", cell_overwrite_ok=True)
    ws1 = wb.add_sheet("По отделам", cell_overwrite_ok=True)
    ws.col(0).width = 12 * 256
    ws.col(1).width = 12 * 256

    row_num = 0

    font_style = xlwt.easyxf('font: bold on, color black;\
    borders: left double, right double, top double, bottom double;\
    align: wrap on, vert centre, horiz center')


    font_style2 = xlwt.easyxf('font: bold off, color black;\
    borders: left thin, right thin, bottom thin;\
    align: wrap on, vert centre, horiz center')

    font_style3 = xlwt.easyxf('font: bold on, color black;\
    borders: left thin, right thin, bottom thin;\
    align: wrap on, vert centre, horiz center')

    row_num = 0
    ws.merge(row_num, row_num, 0, 1)
    ws.merge(row_num, row_num, 2, 3)
    ws.merge(row_num, row_num, 4, 5)
    ws.merge(row_num, row_num, 6, 7)

    for col_num in range(8):
        ws.col(col_num).width = 12 * 256
        ws.write(row_num, col_num, '', font_style)

    ws.write(row_num, 0, 'КСК-Электро', font_style)
    ws.write(row_num, 2, 'ИНОЛ', font_style)
    ws.write(row_num, 4, 'СВЕТОН', font_style)
    ws.write(row_num, 6, 'Электропроект', font_style)

    row_num = 1
    columns = ['Картридж', 'Количество']

    for col_num in range(8):
        if col_num == 0 or col_num % 2 == 0:
            ws.write(row_num, col_num, columns[0], font_style3)
        else:
            ws.write(row_num, col_num, columns[1], font_style3)

    cart_ksk = list(Listy.objects.values_list("title", 'numbers').filter(
        date__contains=datetime.datetime.now().year
    ).filter(
        date__contains=datetime.datetime.now().month
    ).exclude(
        author__depart__contains='ЭЛЕКТРОПРОЕКТ'
    ).exclude(
        author__depart__contains="СВЕТОН"
    ).exclude(
        author__depart__contains="ИНОЛ"
    ))

    cart_ep = list(Listy.objects.values_list("title", 'numbers').filter(
        date__contains=datetime.datetime.now().year, author__depart__contains="ЭЛЕКТРОПРОЕКТ"
    ).filter(
        date__contains=datetime.datetime.now().month
    ))

    cart_svtn = list(Listy.objects.values_list("title", 'numbers').filter(
        date__contains=datetime.datetime.now().year, author__depart__contains="СВЕТОН"
    ).filter(
        date__contains=datetime.datetime.now().month
    ))

    cart_inol = list(Listy.objects.values_list("title", 'numbers').filter(
        date__contains=datetime.datetime.now().year, author__depart__contains="ИНОЛ"
    ).filter(
        date__contains=datetime.datetime.now().month
    ))

    def tup_to_dict(cartlist):
        cart_dict = {}
        for tup in cartlist:
            if tup[0] in cart_dict:
                num = cart_dict.get(tup[0])
                cart_dict[tup[0]] = tup[1] + num
            else:
                cart_dict[tup[0]] = tup[1]
        return cart_dict

    for cart, num in tup_to_dict(cart_ksk).items():
        row_num += 1
        ws.write(row_num, 0, cart, font_style2)
        ws.write(row_num, 1, num, font_style2)

    row_num = 1
    for cart, num in tup_to_dict(cart_ep).items():
        row_num += 1
        ws.write(row_num, 6, cart, font_style2)
        ws.write(row_num, 7, num, font_style2)

    row_num = 1
    for cart, num in tup_to_dict(cart_svtn).items():
        row_num += 1
        ws.write(row_num, 4, cart, font_style2)
        ws.write(row_num, 5, num, font_style2)

    row_num = 1
    for cart, num in tup_to_dict(cart_inol).items():
        row_num += 1
        ws.write(row_num, 2, cart, font_style2)
        ws.write(row_num, 3, num, font_style2)

    row_num = 0
    ws1.merge(row_num, row_num, 0, 2)
    ws1.merge(row_num, row_num, 3, 5)
    ws1.merge(row_num, row_num, 6, 8)
    ws1.merge(row_num, row_num, 9, 11)
    ws1.merge(row_num, row_num, 12, 14)
    ws1.merge(row_num, row_num, 15, 17)
    ws1.merge(row_num, row_num, 18, 20)
    ws1.merge(row_num, row_num, 21, 23)
    ws1.merge(row_num, row_num, 24, 26)
    ws1.merge(row_num, row_num, 27, 29)

    for col_num in range(30):
        ws1.col(col_num).width = 12 * 256
        ws1.write(row_num, col_num, '', font_style)

    ws1.write(row_num, 0, 'МСК СКЛАД', font_style)
    ws1.write(row_num, 3, 'МСК ОФИС', font_style)
    ws1.write(row_num, 6, 'ПРОИЗВОДСТВО', font_style)
    ws1.write(row_num, 9, 'СПБ СКЛАД', font_style)
    ws1.write(row_num, 12, 'СПБ ОФИС', font_style)
    ws1.write(row_num, 15, 'БУХГАЛТЕРИЯ', font_style)
    ws1.write(row_num, 18, 'СВЕТОН', font_style)
    ws1.write(row_num, 21, 'ЭЛЕКТРОПРОЕКТ', font_style)
    ws1.write(row_num, 24, 'МАГАЗИН БЕЛОВОДСКИЙ', font_style)
    ws1.write(row_num, 27, 'МАГАЗИН ВАРШАВКА', font_style)

    def query(depart):
        response = list(
            Listy.objects.values_list(
                'title',
                'numbers',
                'author__surname'
            ).filter(
                author__depart__contains=depart,
                date__contains=datetime.datetime.now().year
            ).filter(
                date__contains=datetime.datetime.now().month
            )
        )
        return response

    msk_sklad = query('МСК СКЛАД')
    msk_off = query('МСК ОФИС')
    proiz = query('ПРОИЗВОДСТВО')
    sklad = query('СПБ СКЛАД')
    off = query('СПБ ОФИС')
    buh = query('БУХГАЛТЕРИЯ')
    svtn = query('СВЕТОН')
    ep = query('ЭЛЕКТРОПРОЕКТ')
    shop_bel = query('МАГАЗИН БЕЛОВОДСКИЙ')
    shop_varsh = query('МАГАЗИН ВАРШАВКА')

    row_num = 1
    columns = ['Картридж', 'Количество', 'Фамилия']

    for col in range(30):
        if col == 0 or col % 3 == 0:
            ws1.write(row_num, col, columns[0], font_style3)
        elif col == 1 or (col - 1) % 3 == 0:
            ws1.write(row_num, col, columns[1], font_style3)
        else:
            ws1.write(row_num, col, columns[2], font_style3)

    def tup_write(cart_list, row_num, col0, col1, col2, font_style2):
        for tup in cart_list:
            row_num += 1
            ws1.write(row_num, col0, tup[0], font_style2)
            ws1.write(row_num, col1, tup[1], font_style2)
            ws1.write(row_num, col2, tup[2], font_style2)

    tup_write(msk_sklad, 1, 0, 1, 2, font_style2)
    tup_write(msk_off, 1, 3, 4, 5, font_style2)
    tup_write(proiz, 1, 6, 7, 8, font_style2)
    tup_write(sklad, 1, 9, 10, 11, font_style2)
    tup_write(off, 1, 12, 13, 14, font_style2)
    tup_write(buh, 1, 15, 16, 17, font_style2)
    tup_write(svtn, 1, 18, 19, 20, font_style2)
    tup_write(ep, 1, 21, 22, 23, font_style2)
    tup_write(shop_bel, 1, 24, 25, 26, font_style2)
    tup_write(shop_varsh, 1, 27, 28, 29, font_style2)

    wb.save(response)

    return response