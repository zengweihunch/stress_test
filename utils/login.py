#coding:utf-8
import platform
import sqlite3
import os

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
import keyring


class Login(object):
    def __init__(self, home_url=None):
        self.home_url = home_url
        pass

    def open_browser(self, name='Chrome'):
        pass

    def __login__(self, url, name, password):

        pass

    @property
    def system(self):
        return platform.system()

    def query_cookies(self, values=['Name', 'Values', 'encrypted_value'], host_key='zenvideo.cn'):
        values_str = ','.join(values)
        print '>>>:', "select " + values_str + " from cookies where host_key=" + host_key
        with sqlite3.connect(self.cookies_file) as conn:
            result = conn.execute(
                "select " + values_str + " from cookies where host_key='%s'" % host_key).fetchall()
        return result

    @property
    def cookies_file(self):
        if self.system == 'Darwin':
            cookies_path = '/Users/zengwei/Library/Application Support/Google/Chrome/Default/Cookies'
            cookie_file = os.path.expanduser(cookies_path)
            return cookie_file
        else:
            raise Exception('other systems are not support for getting cookies for now')
            return None


def get_cookies():
    '''
    Login中的这个函数还没有调试成功
    :return:
    '''
    cookies = {
        'csrftoken': 'xXzHC9mQofZIwLjPaVS1dsNNw4evR4jSSvs7LtsKjgwg3ncdgBbyqQpwo0IDeRyd',
        'sessionid': '01plj5z020x81eobofoz1o0nq47okl1i'
    }
    my_login = Login()
    result = my_login.query_cookies(values=['name', 'encrypted_value'])
    print 'result:', result
    for node in result:
        if 'csrftoken' == node[0]:
            cookies['csrftoken'] = decrypt_session(node[1])
        if 'sessionid' == node[0]:
            cookies['sessionid'] = decrypt_session(node[1])
    return cookies

def decrypt_session(ENCRYPTED_VALUE):
    # https://github.com/n8henrie/pycookiecheat/blob/master/pycookiecheat/pycookiecheat.py
    # replace with your encrypted_value from sqlite3
    encrypted_value = ENCRYPTED_VALUE

    # Trim off the 'v10' that Chrome/ium prepends
    encrypted_value = encrypted_value[3:]

    # Default values used by both Chrome and Chromium in OSX and Linux
    salt = b'saltysalt'
    iv = b' ' * 16
    length = 16

    # On Mac, replace MY_PASS with your password from Keychain
    # On Linux, replace MY_PASS with 'peanuts'
    my_pass = keyring.get_password('Chrome Safe Storage', 'Chrome')
    my_pass = my_pass.encode('utf8')
    # print 'my_pass:', my_pass

    # 1003 on Mac, 1 on Linux
    iterations = 1003

    key = PBKDF2(my_pass, salt, length, iterations)
    cipher = AES.new(key, AES.MODE_CBC, IV=iv)

    decrypted = cipher.decrypt(encrypted_value)

    # Function to get rid of padding
    def clean(x):
        return x[:-ord(x[-1])]

    return clean(decrypted)


if __name__ == "__main__":
    print get_cookies()
    pass

