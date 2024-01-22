# Traceback (most recent call last):
# File "./main.py", line 69, in index
post = json.loads(decryptLink(postCt).decode('utf8'))
# File "./common.py", line 48, in decryptLink
cipher = AES.new(staticKey, AES.MODE_CBC, iv)
# File "/usr/local/lib/python2.7/site-packages/Crypto/Cipher/AES.py", line 95, in new
return AESCipher(key, *args, **kwargs)
# File "/usr/local/lib/python2.7/site-packages/Crypto/Cipher/AES.py", line 59, in __init__
blockalgo.BlockAlgo.__init__(self, _AES, key, *args, **kwargs)
# File "/usr/local/lib/python2.7/site-packages/Crypto/Cipher/blockalgo.py", line 141, in __init__
self._cipher = factory.new(key, *args, **kwargs)
# ValueError: IV must be 16 bytes long


# Traceback (most recent call last):
# File "./main.py", line 69, in index
post = json.loads(decryptLink(postCt).decode('utf8'))
# File "./common.py", line 46, in decryptLink
data = b64d(data)
# File "./common.py", line 11, in <lambda>
b64d = lambda x: base64.decodestring(x.replace('~', '=').replace('!', '/').replace('-', '+'))
# File "/usr/local/lib/python2.7/base64.py", line 328, in decodestring
return binascii.a2b_base64(s)


post = json.loads(decryptLink(postCt).decode('utf8'))

cipher = AES.new(staticKey, AES.MODE_CBC, iv)

return AESCipher(key, *args, **kwargs)

blockalgo.BlockAlgo.__init__(self, _AES, key, *args, **kwargs)

self._cipher = factory.new(key, *args, **kwargs)

post = json.loads(decryptLink(postCt).decode('utf8'))

data = b64d(data)

b64d = lambda x: base64.decodestring(x.replace('~', '=').replace('!', '/').replace('-', '+'))

FDCMMv0Gu7ER7av!QK1HDc93bzAYiVyw4i4jecoVMBuC1sjqv6D9HLXvc5eXXXVbOosSQ8-MXGtY9CN4YPlyHUW!8Dt1fhf3ORFEwqHoQXksq6oRT-tHm5FnTo8jDNe-uSLgvM6TlJLV3RA1Hvm0XnwkWnCd32WTKy-VqgawWn7yitShZyZh-vq3uCMJmRLaP2iS!0QhSJFHkkksMEcqvg~~
m5xIfb2Ya-r!Y4p-MHqN9t9-byaiQnS3mHfeGK95QgYDrM!d5PtLGgaIqAJPF3itI75OxLpl-nPziGSqlY5OyRttTua4iBw886nbwoGkSGKRxS-0YYTc-X7kn1RGvMt6h7MKgZZXC-5PkO5OjCjjThDlncYooudmFqbaCMYgoHe!lQNCOs4CL5vl6l-LbReT760eClynnHbcE2GD0dPkoQ~~

FDCMMv0Gu7ER7av/QK1HDc93bzAYiVyw4i4jecoVMBuC1sjqv6D9HLXvc5eXXXVbOosSQ8+MXGtY9CN4YPlyHUW/8Dt1fhf3ORFEwqHoQXksq6oRT+tHm5FnTo8jDNe+uSLgvM6TlJLV3RA1Hvm0XnwkWnCd32WTKy+VqgawWn7yitShZyZh+vq3uCMJmRLaP2iS/0QhSJFHkkksMEcqvg==

b64 m5xIfb2Ya+r/Y4p+MHqN9t9+byaiQnS3mHfeGK95QgYDrM/d5PtLGgaIqAJPF3itI75OxLpl+nPziGSqlY5OyRttTua4iBw886nbwoGkSGKRxS+0YYTc+X7kn1RGvMt6h7MKgZZXC+5PkO5OjCjjThDlncYooudmFqbaCMYgoHe/lQNCOs4CL5vl6l+LbReT760eClynnHbcE2GD0dPkoQ==
hex 9b9c487dbd986beaff638a7e307a8df6df7e6f26a24274b79877de18af79420603accfdde4fb4b1a0688a8024f1778ad23be4ec4ba65fa73f38864aa958e4ec91b6d4ee6b8881c3cf3a9dbc281a4486291c52fb46184dcf97ee49f5446bccb7a87b30a8196570bee4f90ee4e8c28e34e10e59dc628a2e76616a6da08c620a077bf9503423ace022f9be5ea5f8b6d1793efad1e0a5ca79c76dc136183d1d3e4a1
