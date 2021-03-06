# Task_2

import re

check = re.compile(r'^(\b.+\b).*\[(.+)].*\"([A-Z]+) +(/.+?)\s.*?\" (\d+) (\d+) .*$|^$')

with open('nginx_logs.txt', encoding='utf-8') as f:
    for line in f:
        print(re.findall(check, line))
