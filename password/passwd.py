
import base64


def decrypt_password(password):
    import base64
    s = base64.decodestring(password)
    print s
    c = bytearray(str(s).encode("utf8"))
    for i in xrange(0, len(c)):
        print c[i]
    n = len(c)
    if n % 2 != 0:
        return ""
    n = n // 2
    b = bytearray(n)
    j = 0
    for i in range(0, n):
        b[i] = c[j]
        j = j+2
    return b.decode("utf8")


def gen_secret_sign(password):
    bystr = bytearray(str(password).encode('utf8'))
    lenstr = len(bystr)
    cstry = bytearray(lenstr*2)
    j = 0
    for i in range(0, lenstr):
        bystr1 = bystr[i]
        bystr2 = bystr1 ^ 11
        cstry[j] = bystr1
        cstry[j+1] = bystr2
        j = j + 2
    return base64.encodestring(cstry.decode('utf8')).replace('\r', '').replace('\n', '').strip()

if __name__ == '__main__':

    pwd = gen_secret_sign("zjn900616")
    print pwd
    print decrypt_password(pwd)
