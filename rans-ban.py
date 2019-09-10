#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from inotify import adapters
import requests, json

requis = requests.get('https://fsrm.experiant.ca/api/v1/combined')
arqlog ='/home/mauricio/tmp/teste.conf'

def main():
    i = adapters.Inotify()
    i.add_watch(arqlog)

    for evento in i.event_gen(yield_nones=False):
        if evento[1] == ['IN_MODIFY']:
            print(evento[1])
        

if __name__ == '__main__':
    main()