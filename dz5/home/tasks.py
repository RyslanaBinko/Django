import requests
from celery import chain, shared_task
from home.models import Currency


@shared_task
def exchange_rates(*args):
    currencies = requests.get(
        'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    )
    currencies_json = currencies.json()
    return currencies_json


@shared_task
def save_currency(currencies):
    for currency in currencies:
        currency_instance = Currency()
        currency_instance.ccy = currency.get('ccy')
        currency_instance.base_ccy = currency.get('base_ccy')
        currency_instance.buy = currency.get('buy')
        currency_instance.sale = currency.get('sale')
        currency_instance.save()


@shared_task
def compile_task():
    chain(
        exchange_rates.si(),
        save_currency.s()
    )()
