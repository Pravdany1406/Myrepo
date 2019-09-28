from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

hex_to_rgb("#ffffff")              # ==> (255, 255, 255)
hex_to_rgb("#ffffffffffff")        # ==> (65535, 65535, 65535)
rgb_to_hex((255, 255, 255))        # ==> '#ffffff'
rgb_to_hex((65535, 65535, 65535))  # ==> '#ffffffffffff'

print('Please enter your colour hex')

h = input('Enter hex: ').lstrip('#')
print('RGB =', tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))

