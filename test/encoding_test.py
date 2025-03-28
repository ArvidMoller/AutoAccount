def encode(mystring):
    mybytes = mystring.encode('utf-8')
    myint = int.from_bytes(mybytes)
    print(myint)
    return(myint)

def decode(myint):
    recoveredbytes = myint.to_bytes((myint.bit_length() + 7) // 8)
    recoveredstring = recoveredbytes.decode('utf-8')
    print(recoveredstring)
    return(recoveredstring)

enc = encode("4444")
dec = decode(enc)