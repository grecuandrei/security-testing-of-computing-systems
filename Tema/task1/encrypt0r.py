#!/usr/bin/env python3

import base64
import binascii
from encodings import utf_8
import json
import gmpy2
from random import randint
import os
import libnum

def str_to_number(text):
    """ Encodes a text to a long number representation (big endian). """
    return int.from_bytes(text.encode("latin1"), 'big')

def number_to_str(num):
    """ Decodes a text to a long number representation (big endian). """
    num = int(num)
    return num.to_bytes((num.bit_length() + 7) // 8, byteorder='big').decode('latin1')

def encrypt(pub_k, msg_num):
    """ We only managed to steal this function... """
    cipher_num = gmpy2.powmod(msg_num, pub_k["e"], pub_k["n"])
    # note: gmpy's to_binary uses a custom format (little endian + special GMPY header)!
    cipher_b64 = base64.b64encode(gmpy2.to_binary(cipher_num))
    return cipher_b64

def decrypt(priv_k, cipher):
    """ We don't have the privary key, anyway :( """
    # you'll never get it!
    pass

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

if __name__ == "__main__":
    # example public key
    pub_k = {"e": 17, "n": 1221540932698357538969048008476734604937734436157953593060163}

    s = "eyJuIjogMTMyMTgxMzY5NjQxNDMwMzY1OTg1ODY4NjI5MjQxNTI1MTE3NzIzMTM0Mzg5OTgxNjMxMTU1MDM0MjQzMDAzODYyOTA5MTAwMDcwMTE5ODE3Mjg5NzMzNzk0NjIyOTQzODY5MjMzOTA1MTcxMzE5MjYwMjY1MzkyMTE2NDYwNDc2MjM4NjA5MDU3NzYwODUwOTgwNjEzMzY5NjY2NjEyNDgxMTU5OTYzNzg0MDk4ODcyNzc1MDQxMjYzOTQ1NTQ3ODg4MzM2MzMyNjM4NDAxNDQ5ODg5MDkwNTc3OTA2Mzc4NTYwOTgzODI4NTgwNDIwODYzODkxNzAwMDkwMzQzMzgxODUzMjIxMDYzMDY2Nzk5OTEzMzY1NTcwMzQ3OTE0ODIxMTg2NjczODIzNzYxMDUzMTgyNDYzMTIyMjM5MTE2MTM5ODQ3OTExODI2ODk4MjQ4ODIyNDQzMzY5MjA1NjA2MjI3NTA5NzIxNTc1MzQ3ODczMDIyOTkyMjA5NDQxMTY4ODgwOTMwNzMwMzU3NTczNTc4MjQ0OTAwOTc2NzUwOTMzOTE0MjYyNDA3NjIzMjE0NjA0ODY1MjE5NDk4OTAzNjg3ODczMzY1Njk5Nzk3NzQ2MTA0MjU1OTUyMTkyMjg0MzQ0NTUyMTYzOTYzMTUyMTQyOTUxODAzODM2Mjk5MjEzMTMwMTk2MzQxMDIxNzcwNTUzMjE1MTM5MDI0NTY4NDA1NzIyNDIxNzI0MTc0OTY1MTMwMDQ2NjcxOTc4MjY0MDY0MDc0NTQwMzg5OTEzMzgzMDgwNTcyMDM0NzY0ODk2MDA0NTMsICJlIjogMjI0ODU3LCAiZmxhZyI6ICJBUUZSVXBuYng1YzFjVDBMTUJEL3I5eHJ0K0xDNDZRQ0RtZjJYa2hQME9wRXhSUUFGQTJmNEs5c1hpOGFhMEljL1padHBpeE5kL1hSS013WHBtdlRvdVJBSVB2S1ZDSmkzdFdiWWo2QkQxZ3BQWldvS0UyK21EV01mQk83c0gxbG5DaWFCREF2WmtTc1BJWms0eGpwWUdkRktxNnFrcElMSnFnWW1udVJ0VmI0RnVRNjJsQk45allEcWhFeTRZQ2RTVjF3UVJ3S0ZMNUJvcE9XTjh5UTRqZXBBSlBGWGNFNmI3QnNYMlZWSWVub2pQVEttaWNjZ25qZ01TOU96VkhNOUdtcXRpelFKcjhjMnpxRUc0VDg3ZkFFN1JDZ3ExNnNRL2FRVE5nVjZHZTh5UE9yajNpbW1Pay8wU1RJTFBSREthTFJJeXFzdkhtVWZUaFltZlFPZU5BNSJ9"
    
    r = 3
    print("The random number")
    print(r)
    print()

    a = json.loads(base64.b64decode(s))
    print(a)

    cypher_dash = (gmpy2.from_binary(base64.b64decode(a['flag'])) * (gmpy2.powmod(r ,a['e'], a['n']))) % a['n']
    
    msg = {
        "n": 13218136964143036598586862924152511772313438998163115503424300386290910007011981728973379462294386923390517131926026539211646047623860905776085098061336966661248115996378409887277504126394554788833633263840144988909057790637856098382858042086389170009034338185322106306679991336557034791482118667382376105318246312223911613984791182689824882244336920560622750972157534787302299220944116888093073035757357824490097675093391426240762321460486521949890368787336569979774610425595219228434455216396315214295180383629921313019634102177055321513902456840572242172417496513004667197826406407454038991338308057203476489600453,
        "e": 224857,
        "flag": base64.b64encode(gmpy2.to_binary(cypher_dash)).decode('utf-8')}

    print(msg)
    
    send_this = base64.b64encode(json.dumps(msg).encode())
    print("This needs to be sent")
    print(send_this)
    print()

    # os.system('netcat isc2022.1337.cx 11063')
    
    d_uni = b'\xfaQ0<Z8\xd3E$6q\xcc\xca\x00`9)\x91\x05\xfa8\xd5\xa2\xab\xcf\x90\xd8\xa6A\xd2\xa3\x02\x96\xe4\xdch\xe5_\xa5\xed\x976<w'

    d_dec = d_uni.decode("unicode_escape")
    
    print("D decoded")
    print(d_dec)
    print()

    d = str_to_number(d_dec)
    print("D as number")
    print(d)
    print()
    
    res = d // r
    print("Response as number")
    print(res)
    print()

    print(number_to_str(res))
    