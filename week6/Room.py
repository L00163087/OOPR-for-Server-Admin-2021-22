"""
# 
# File          : __init__.py.py
# Created       : 27-09-2021 02:24 PM
# Author        : Varnit Rohilla
# Version       : v1.0.0
# Licensing     : (c) 2021 Varn R., LYIT
#                  Avaialable under GNU license Policy
#             
"""

import Module

module = Module.Module()

module_room_number_list = [{'module': 'OOPR', 'room_number': '2049'}]


class Room(Module.Module):
    def get_room_number(self, module_room_number: list):
        for i in module_room_number:
            if Room().module_name == i['module']:
                return [Module.Module().name, Module.Module().module_name, i['room_number']]


room = Room()
print(room.get_room_number(module_room_number_list))
