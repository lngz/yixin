
# -*- encoding: utf-8 -*-

import cookielib, urllib2
import urllib
import json
import hashlib
import re
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

DEBUG = False

class yixin :

	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

	opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.11) Gecko/20101012 Firefox/3.6.11'), ]
	opener.addheaders += [('Referer', 'https://plus.yixin.im/'), ]

	Token = ""

	def login(self, username, password) :
		
		values = {'account' : username,
				'password' : hashlib.md5(password).hexdigest(),
				'loginType':'YiXinUserId'
				 }
		data = urllib.urlencode(values)
		try:
			search = self.opener.open('https://plus.yixin.im/rest/login',data)
			logined = search.read()
			loginmsg = json.loads(logined)
			if loginmsg['code'] != 200 :
				raise
		except :
			print "login failed"
			return
		
		if DEBUG :
			print values
			print logined
			print self.cj
		
		search = self.opener.open('https://plus.yixin.im/index')
		

	def loginMD5(self, username, password) :
		
		values = {'account' : username,
				'password' : password,
				'loginType':'YiXinUserId'
				 }
		data = urllib.urlencode(values)
		try:
			search = self.opener.open('https://plus.yixin.im/rest/login',data)
			logined = search.read()
			loginmsg = json.loads(logined)
			if loginmsg['code'] != 200 :
				raise
		except :
			print "login failed"
			return
		
		if DEBUG :
			print values
			print logined
			print self.cj
		
		search = self.opener.open('https://plus.yixin.im/index')
	def sendmsg(self,fakeid,textmsg) :
		
		values = {
		    'contactId':fakeid,
		    'message':textmsg,
		}
		data = json.dumps(values)
		request = urllib2.Request('https://plus.yixin.im/rest/messages/', data=data)
		request.get_method = lambda: 'PUT' # or 'DELETE'
		request.add_header('Content-Type', 'application/json')
		request.add_header('Accept', 'application/json')

		response = self.opener.open(request)

		return response.read()


	def getfriend(self) :
		

		search = self.opener.open('https://plus.yixin.im/rest/contacts/?groupId=0&offset=0&limit=1000')
		jsonstring = search.read()
		friendslist = json.loads(jsonstring)['result']['list']
		for friend in friendslist:
			print friend['uid'],friend['userInfo']['nick']

		


		




if __name__ == '__main__':
	w = wechat()
	username = raw_input("username:")
	password = raw_input("password:")
	w.login(username,password)
	#w.sendmsg('2377600462',"hello weixin")
	w.getfriend()
	print w.friends['contacts']
	# for info in w.friends['contacts']:
	# 	    w.sendmsg( str(info['id']), info['nick_name'])
