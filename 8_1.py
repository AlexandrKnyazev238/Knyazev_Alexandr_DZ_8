# Task_1

import re


def email_parse(email_address):
    re_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not re_email.match(email_address):
        raise ValueError(f'Wrong email: {email_address}')
    print(re_email.match(email_address).groupdict())


for i in ['someone@geekbrains.ru', 'som&eone@geekbrainsru', 'someone@geekbrainsru']:
    try:
        email_parse(i)
    except ValueError as err:
        print(err)


# import re
#
#
# def email_parse(email_address):
#     re_email = re.findall(r'(^[^@&][a-z0-9_\.-]*)@([a-z0-9_-]*\.[a-z]{2,})$', email_address)
#     if not re_email:
#         raise ValueError(f'Неправильный адрес E-mail: {email_address}')
#     return dict(zip(['username', 'domain'], re_email[0]))
#
#
# try:
#     print(email_parse(input('Введите E-mail: ').lower()))
# except ValueError as err:
#     print(err)
