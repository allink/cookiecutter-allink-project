# -*- coding: utf-8 -*-
# from django.conf import settings

# from celery import shared_task


# Example Celery Task


# @shared_task(ignore_result=True)
# def invoice_overdue_task(self):
#     overdue_orders = Order.objects.filter(status__in=("Versandt", "Gemahnt", "falscher Betrag"), invoice_payable__lt=datetime.date.today()).exclude(conflict_type__in=(settings.CONFLICT_STATI['TO_MUCH'][0], settings.CONFLICT_STATI['LITTLE_TO_MUCH'][0]))
#     for order in overdue_orders:
#         EventHandler().handle_order_status_change(order, u"Überfällig", 'Die Zahlung für diese Bestellung ist überfällig.')
