#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           ��q(�%��m�ܨ.+�� ���Z��p>=�+���=(S���ǔ��1+�����MV�������	���d�5nt$�^l�/����_]EAt��n����:�}�k�c��GG4T����"""
from hashlib import sha256
print sha256(blob).hexdigest()
