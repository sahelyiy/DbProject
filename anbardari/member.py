from anbardari.database_communication import *


def order(code, good_code, member_code, dischargerer_personnel_code, date):
    if check_exists('dischargerer', 'personnel_code', dischargerer_personnel_code):
        insert('instruction', [code, good_code, member_code, dischargerer_personnel_code, date])
        return True
    else:
        return False


def deliver(code, good_code, member_code, transferee_personnel_code, date):#tahvil dadan
    if check_exists('transferee', 'personnel_code', transferee_personnel_code):
        insert('transfer', [code, good_code, member_code, transferee_personnel_code, date])
        return True
    else:
        return False


def take_delivery(code, good_code, member_code, transferer_personnel_code, date, cost):#tahvil gereftan
    if check_exists('transferer', 'personnel_code', transferer_personnel_code):
        insert('recieve', [code, good_code, member_code, transferer_personnel_code, date, cost])
        return True
    else:
        return False


def edit_name(member_code, new_name):
    try:
        c.execute('UPDATE member SET name = ? WHERE code = ?', (new_name, member_code))
        conn.commit()
        return True
    except:
        return False


def get_goods(member_code):
    first_query = 'SELECT member_goods_code FROM member_basket Where member_code = %s' % member_code
    second_query = 'SELECT name FROM goods Where code = ?'
    return get_items_by_fk(first_query, second_query)


def add_good(member_code, good_name):
    try:
        good_code = get_items('SELECT code FROM goods Where name=?', (good_name,))[0]
        insert('member_basket', (member_code, good_code))
        return True
    except:
        return False


def remove_good(member_code, good_name):
    try:
        good_code = get_items('SELECT code FROM goods Where name=?', (good_name,))[0]
        delete('member_basket', ['member_code', 'member_goods_code'], [member_code, good_code])
        return True
    except Exception as e:
        return False


def calculate_keep_price(member_code):
    sum_price = 0.0
    first_query = 'SELECT member_goods_code FROM member_basket Where member_code = %s' % member_code
    second_query = 'SELECT name, base_price FROM goods Where code = ?'
    goods = get_items_by_fk(first_query, second_query)
    for name, price in goods:
        sum_price += price
    return sum_price, goods
