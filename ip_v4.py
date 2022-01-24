#!/usr/bin/python3

def string_to_ipv4(ip):
    oktetts = ip.split('.')
    if len(oktetts) != 4:
        return False, ip

    for oktett in oktetts:
        try:
            oktett = int(oktett)
            if oktett > 256 or oktett <  0: 
                return False, ip
        except:
            return False, ip
    return True, ip
