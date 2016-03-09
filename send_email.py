#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests


def send_simple_message(mailto, subject, message):
    return requests.post(
        "", # set api url endpoint
        auth=("api", ""), # set api key
        data={"from": "", # set from address
              "to": [mailto],
              "subject": subject,
              "text": message})
