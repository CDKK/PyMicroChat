from microchat import client_tornado

def main():
    usrname = "getomgid"
    passwd = "qwerdfb123"
    client_tornado.start(usrname, passwd)


if __name__ == '__main__':
    main()