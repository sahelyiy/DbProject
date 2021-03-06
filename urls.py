from django.conf.urls import url

from anbardari.views import *

urlpatterns = {
    url(r'^/?$', base_page),
    url(r'^helloworld/?$', helloworld),
    url(r'^register_member_page/?$', register_member_page),
    url(r'^sign_in_member/?$', sign_in_member),
    url(r'^sign_up_member/?$', sign_up_member),
    url(r'^member_get_goods/?$', member_get_goods),
    url(r'^member_edit_name/?$', member_edit_name),
    url(r'^member_cal_price/?$', member_cal_price),
    url(r'^member_take_delivery/?$', member_take_delivery),
    url(r'^member_take_delivery_list/?$', member_take_delivery_list),
    url(r'^member_deliver/?$', member_deliver),
    url(r'^member_deliver_list/?$', member_deliver_list),
    url(r'^member_order/?$', member_order),
    url(r'^show_all_goods/?$', show_all_goods),
    url(r'^member_order_list/?$', member_order_list),
    url(r'^show_all_goods/?$', show_all_goods),
    url(r'^add_to_basket/?$', add_to_basket),
    url(r'^remove_from_basket/?$', remove_from_basket),
    url(r'^show_dischargerers/?$', show_dischargerers),
    url(r'^show_transferees/?$', show_transferees),
    url(r'^show_transferers/?$', show_transferers),
    url(r'^register_staff_page/?$', register_staff_page),
    url(r'^sign_up_staff/?$', sign_up_staff),
    url(r'^sign_in_staff/?$', sign_in_staff),
    url(r'^staff_add_goods/?$', staff_add_goods),
    url(r'^staff_add_exit_date/?$', staff_add_exit_date),
    url(r'^staff_add_caring/?$', staff_add_caring),
    url(r'^staff_get_salary/?$', staff_get_salary),
    url(r'^staff_add_group/?$', staff_add_group),
    url(r'^register_admin_page/?$', register_admin_page),
    url(r'^sign_up_admin/?$', sign_up_admin),
    url(r'^sign_in_admin/?$', sign_in_admin),
    url(r'^admin_add_goods/?$', staff_add_goods),
    url(r'^admin_add_group/?$', staff_add_group),
    url(r'^admin_monitor_goods/?$', admin_monitor_goods),
    url(r'^admin_monitor_staffs/?$', admin_monitor_staffs),
    url(r'^admin_monitor_members/?$', admin_monitor_members),
    url(r'^admin_cal_keep_price/?$', admin_cal_keep_price),
    url(r'^admin_add_staff/?$', admin_add_staff),
    url(r'^admin_add_member/?$', admin_add_member),
    url(r'^admin_monitor_keeping_goods/?$', admin_monitor_keeping_goods),
    url(r'^admin_cal_staff/?$', admin_cal_staff),
    url(r'^admin_cal_all/?$', admin_cal_all),

}
