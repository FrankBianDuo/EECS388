'''
imports required classes and methods to this
'''

from pymd5 import md5, padding

h = md5(state="3ecc68efa1871751ea9b0b1a5b25004d".decode("hex"), count=512)
x = "Good advice"
h.update(x)
print h.hexdigest()

m = "Use HMAC, not hashes"
h1 = md5()
h1.update( m + padding(len(m)*8) + x)
print h1.hexdigest()