#!/usr/bin/python3


# Funktion String nach Integer
def string_to_int(my_string):
    try:
        return True, int(my_string)
    except:
        return False, my_string


# Funktion String nach Float
def string_to_float(my_string):
    try:
        return True, float(my_string)
    except:
        return False, my_string


# Funtion String nach IPv4
def string_to_ipv4(ip):
    oktetts = ip.split('.')
    if len(oktetts) != 4:
        return False, ip

    for oktett in oktetts:
        try:
            oktett = int(oktett)
            if oktett > 255 or oktett < 0:
                return False, ip
        except:
            return False, ip
    return True, ip

