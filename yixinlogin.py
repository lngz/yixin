
#!/usr/bin/python
# -*-  coding: UTF-8 -*-

from yixin import yixin
import password 


if __name__ == '__main__':
    w = yixin()
    username = password.username
    password = password.password
    w.login(username,password)
    


    print w.sendmsg('2311590',"hello yixin")
    w.getfriend()

    # for info in w.friends['contacts']:
    #     print info['id'], info['nick_name']

    # touser = raw_input("input user id:")
    # textmsg = raw_input("input text message:")
    # print w.sendmsg(touser, textmsg)

    # for info in w.friends['contacts']:
    #       w.sendmsg( str(info['id']), info['nick_name'])
