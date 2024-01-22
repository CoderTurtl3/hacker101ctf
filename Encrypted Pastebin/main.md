

AES cbc encryption
blocksize 128 bits or 16 bytes

Seems like the /?post= is followed by a url-friendly b64 encoded string which length as hex is always 320 bytes or 1280 bits.
So there are 10 blocks of encrypted data.

Padding oracle attack.

Sample
b64 m5xIfb2Ya+r/Y4p+MHqN9t9+byaiQnS3mHfeGK95QgYDrM/d5PtLGgaIqAJPF3itI75OxLpl+nPziGSqlY5OyRttTua4iBw886nbwoGkSGKRxS+0YYTc+X7kn1RGvMt6h7MKgZZXC+5PkO5OjCjjThDlncYooudmFqbaCMYgoHe/lQNCOs4CL5vl6l+LbReT760eClynnHbcE2GD0dPkoQ==
