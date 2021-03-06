from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


from anbardari.staff import *


logger = logging.getLogger(__name__)


@csrf_exempt
def base_page(request):
    template = loader.get_template('base_page.html')
    return HttpResponse(template.render({}, request))


@csrf_exempt
def register_staff_page(request):
    template = loader.get_template('register_staff_page.html')
    return HttpResponse(template.render({}, request))


def _sign_in_staff(personnel_code, request):
    logger.info('_sign_in_member')
    if check_exists('staff', 'personnel_code', personnel_code):
        logger.info('staff exists')
        template = loader.get_template('home_staff_page.html')
        staff_type = "other"
        if check_exists('transferee', 'personnel_code', personnel_code):
            staff_type = "transferee"
        elif check_exists('dischargerer', 'personnel_code', personnel_code):
            staff_type = "dischargerer"
        elif check_exists('keeper', 'personnel_code', personnel_code):
            staff_type = "keeper"
        return HttpResponse(template.render(
            {'personnel_code': personnel_code,
             'staff_type': staff_type}, request))
    else:
        return HttpResponse('staff not exists.')


@csrf_exempt
def sign_in_staff(request):
    personnel_code = request.POST['personnel_code']
    return _sign_in_staff(personnel_code, request)


@csrf_exempt
def sign_up_staff(request):
    personnel_code = request.POST['new_personnel_code']
    if check_exists('staff', 'personnel_code', personnel_code):
        return HttpResponse('staff already exists')
    staff_type = request.POST['staff_type']
    national_code = request.POST['national_code']
    name = request.POST['name']
    phone_number = request.POST['phone_number']
    work_hours = request.POST['work_hours']
    insert('staff', [national_code, name, personnel_code, phone_number, work_hours])
    if staff_type == 'transferee':
        insert('transferee', [personnel_code])
    if staff_type == 'dischargerer':
        insert('dischargerer', [personnel_code])
    if staff_type == 'transferer':
        insert('transferer', [personnel_code])
    if staff_type == 'keeper':
        insert('keeper', [personnel_code])
    return _sign_in_staff(personnel_code, request)


@csrf_exempt
def staff_add_goods(request):
    code = len(get_items('SELECT * FROM goods')) + 1
    if add_goods(request.POST['barcode'], code, request.POST['name'],
                                  request.POST['group_title'], request.POST['base_price'], request.POST['price'],
                                  request.POST['maintenance'], request.POST['production_date'],
                                  request.POST['entry_date'], request.POST['exit_date'], request.POST['producer']):
        return HttpResponse('goods has been added')
    else:
        return HttpResponse('there is no group named %s' % request.POST['group_title'])


@csrf_exempt
def staff_add_exit_date(request):
    if add_exit_date(request.POST['goods_barcode'], request.POST['exit_date']):
        return HttpResponse('the exit date of goods with barcode %s has set to %s' % (request.POST['goods_barcode'], request.POST['exit_date']))
    else:
        return HttpResponse('the exit date could not set')


@csrf_exempt
def staff_add_caring(request):
    if add_caring(request.POST['personnel_code'], request.POST['goods_barcode']):
        return HttpResponse('the keeper with personnel code %s care good with %s barcode' % (request.POST['personnel_code'], request.POST['goods_barcode']))
    else:
        return HttpResponse('The keeper could not keep this item. Maybe this item or this personnel code doesn\'t exist.')


@csrf_exempt
def staff_get_salary(request):
    return HttpResponse(get_salary(request.POST['personnel_code']))


@csrf_exempt
def staff_add_group(request):
    insert('team', [request.POST['title'], request.POST['maintenance'], request.POST['base_price']])
    return HttpResponse('group has been made')

