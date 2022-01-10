#!/usr/bin/python3

import time

zeit = time.gmtime()
wochentag = zeit[6]


if wochentag  == 0:
     print('Wochentag: Montag')
if wochentag == 1:
     print('Wochentag: Dienstag')
if wochentag == 2:
     print('Wochentag: Mittwoch')
if wochentag == 3:
     print('Wochentag: Donnerstag')
if wochentag == 4:
     print('Wochentag: Freitag')
if wochentag == 5:
     print('Wochentag: Saturday')
if wochentag == 6:
     print('Wochentag: Sonntag')
