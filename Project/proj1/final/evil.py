#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = '''
           y��H�����^��A���7�A�

�Q2���ŭ�X>A�����e 2��	�����HN�PG��p3%�)�W�XC(���&6��������]����=�"YW��y.�˯M9$�80]�Ù�\W'''
from hashlib import sha256
if sha256(blob).hexdigest() == '7528e233c6b4e46726efa837f21aa7200ca17e168e00d71d8cec6f37f0fc49e8':
	print "I come in peace."
else:
	print "Prepare to be destroyed!"
