#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, time
from datetime import datetime
from pytz import timezone

# set email to send notification
mailto = ['email@email.com']
mail_message = []


def log(logmessage):
    agora = datetime.now(timezone('America/Sao_Paulo'))
    data = agora.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    mail_message.append('{} - {}'.format(data, logmessage))
    print('{} - {}'.format(data, logmessage))


dir1 = '' # diretory with control file

lista1 = []
lista2 = []

with open(arq1, 'r') as f:
    lista1[:] = f.read().splitlines()

print(50 * '-')
log('Starting cleanup ...')

for root, directories, filenames in os.walk(os.path.join(dir1, 'site_data')):
    for filename in filenames:
        if filename.endswith('.php'):
            lista2.append(os.path.join(root,filename))

dif = list(set(lista2) - set(lista1))

if len(dif) > 0:
    log('Found {} file(s) to remove !!!'.format(len(dif)))
else:
    log('Nothing to remove !!!')
    sys.exit(0)

for i in dif:
    log('Removing {}'.format(i))
    os.remove(i)

log('Files removed !!!')

from send_email import send_simple_message
for i in mailto:
    send_simple_message(i, 'Check File Just Removed File(s)', '\n'.join(mail_message))
