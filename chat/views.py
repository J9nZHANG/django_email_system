from django.conf import settings
from ModelDB import models
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.views.decorators.csrf import csrf_exempt
from ModelDB.models import User, Relationship, Sendemail
from django.core.mail import send_mail
import poplib,email,telnetlib
import datetime,time,sys,traceback
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import smtplib  #加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
import os
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
# Create your views here.

def login(request):
	return render(request, 'chat/login.html',{})


@csrf_exempt
def loginVerify(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		users= User.objects.all()
		for user in users:
			if user.username == username and user.password ==password:
				user.status =1
				request.session['username']  = username
				return render(request, 'chat/home_page.html',{'username': username})
		return render(request, 'chat/login.html', {'error':1})


def register(request):
	return render(request, 'chat/register.html',{})


@csrf_exempt	
def registerVerify(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']
		email = request.POST['email']
		users = User.objects.all()
		for user in users:
			if user.username == username:
				return render(request, 'chat/register.html', {'error':1})
			elif user.email == email:
				return render(request, 'chat/register.html', {'error':2})
		if confirm_password!= password:
			return render(request, 'chat/register.html', {'error':3})
		else:
			u1 = User()
			u1.username = username
			u1.password = password
			u1.email = email
			u1.status= 0
			u1.save()
			return render(request, 'chat/login.html', {})
	return render(request, 'chat/register.html', {}) 


def home_page(request):
	if request.method == 'POST':
		keyword = request.POST['top-search']
		sendmails =Sendemail.objects.all()
		data = models.Sendemail.objects.filter(Q(username=keyword)\
		|Q(theme=keyword)|Q(content=keyword)|Q(time=keyword)|Q(sendto=keyword)|Q(_from=keyword))
		return render(request, 'chat/search_result.html', {})
	return render(request, 'chat/home_page.html',{})


def main_page(request):
	return render(request, 'chat/main_page.html',{})

@csrf_exempt
def search_result(request):
	keyword = '大哥大'
	data = models.Sendemail.objects.filter(theme = keyword)
	return render(request, 'chat/search_result.html',{'data': data})


def change_password(request):
	username = request.session.get('username')
	users = User.objects.all()
	if request.method == 'POST':
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']
		email = request.POST['email']
		send_password = request.POST['send_password']
		for user in users:
			if user.username ==  username:
				user.email = email
				user.password = password
				user.send_password = send_password
				user.save()
				return render(request, 'chat/main_page.html',{'error':1})
	else:
		for user in users:
			if user.username ==  username:
				if user.send_password == '':
					pawd = 1
				else:
					pawd = user.send_password

				return render(request, 'chat/change_password.html',{
					'username': username,
					'password': user.password,
					'confirm_password': user.password,
					'email': user.email,
					'send_password': pawd
					})
		return render(request,'chat/change_password.html',{})


def search_friend(request):
	return render(request, 'chat/search_friend.html',{})


@csrf_exempt
def search_friendVerify(request):
	username = request.session.get('username')
	if request.method == 'POST':
		friend_name = request.POST['username']
		users = User.objects.all()
		for user in users:
			if user.name == friend_name:
				relationship =  Relationship()
				relationship.username = username
				relationship.friend_name = friend_name
				relationship.save()
				relationship.username = friend_name
				relationship.friend_name = username
				relationship.save()
				return render(request, 'chat/main_page.html',{'succeed': 1})
		return render(request, 'chat/search_friend.html',{'error': 1})
	else:
		return render(request, 'chat/search_friend.html',{'error': 2})


def write_email(request):
	return render(request, 'chat/write_email.html', {})

@csrf_exempt
def write_emailVerify(request):
	if request.method == 'POST':
		if 'submit' in request.POST:
			username = request.session.get('username')
			users = User.objects.all()
			my_sender = ''
			my_password = ''
			for user in users:
				if user.username == username:
					my_password = user.send_password
					my_sender = user.email
			write_id = request.POST['write_to_id']
			write_theme = request.POST['write_theme']
			write_content = request.POST['write_content']
			send_file = request.POST.get('send_file')
			obj = request.FILES.get('send_file')
			file_path = os.path.join('E:\\MyWeb\\mysite\\chat\\static', 'upload', obj.name)
			f = open(file_path, 'wb')
			for chunk in obj.chunks():
				f.write(chunk)
			f.close()

			sender = my_sender
			receiver = write_id
			se = Sendemail()
			se.username = username
			se.sendto = write_id
			se.theme = write_theme
			se.content = write_content
			se._from = sender
			se.time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			se.status = 1
			se.save()
			msg = MIMEMultipart()
			body = MIMEText(write_content,'plain','utf-8')
			msg.attach(body)
			attachment = MIMEBase('application', 'octet-stream')
			attachment.set_payload(open(file_path, 'rb').read())
			encoders.encode_base64(attachment)
			attachment.add_header('Content-Disposition','attachment', filename=file_path)# 前2个参数意义未深究
			msg.attach(attachment)
			msg['From'] = formataddr([username,my_sender])
			msg['To'] = formataddr(["",receiver])
			msg['Subject'] = write_theme
			#msg['Content'] = write_content
			server = smtplib.SMTP('smtp.163.com', 25)
			server.login(my_sender, my_password)
			server.sendmail(my_sender, receiver, msg.as_string())
			server.quit()
			#send_mail(write_theme, write_content, sender, receiver, fail_silently=False)
			return render(request, 'chat/main_page.html', {})
		else:
			username = request.session.get('username')
			write_id = request.POST['write_to_id']
			write_theme = request.POST['write_theme']
			write_content = request.POST['write_content']
			sender = settings.EMAIL_FROM
			receiver = [write_id]
			se = Sendemail()
			se.username = username
			se.sendto = write_id
			se.theme = write_theme
			se.content = write_content
			se._from = sender
			se.time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			se.status = 0
			se.save()
			return render(request, 'chat/main_page.html', {})


class down_email():

	def __init__(self,user,password,eamil_server):
		# 输入邮件地址, 口令和POP3服务器地址:
		self.user = user
		# 此处密码是授权码,用于登录第三方邮件客户端
		self.password = password
		self.pop3_server = eamil_server

	# 获得msg的编码
	def guess_charset(self,msg):
		charset = msg.get_charset()
		if charset is None:
			content_type = msg.get('Content-Type', '').lower()
			pos = content_type.find('charset=')
			if pos >= 0:
				charset = content_type[pos + 8:].strip()
		return charset

    #获取邮件内容
	def get_content(self,msg):
		content=''
		content_type = msg.get_content_type()
		# print('content_type:',content_type)
		if content_type == 'text/plain': # or content_type == 'text/html'
			content = msg.get_payload(decode=True)
			charset = self.guess_charset(msg)
			if charset:
				content = content.decode(charset)
		return content

	def get_att(self,msg_in):
		attachment_files = []
		for part in msg_in.walk():
			# 获取附件名称类型
			file_name = part.get_param("name")  # 如果是附件，这里就会取出附件的文件名
			# file_name = part.get_filename() #获取file_name的第2中方法
			# contType = part.get_content_type()
			if file_name:
				h = email.header.Header(file_name)
				# 对附件名称进行解码
				dh = email.header.decode_header(h)
				filename = dh[0][0]
				if dh[0][1]:
				# 将附件名称可读化
					filename = self.decode_str(str(filename, dh[0][1]))
				data = part.get_payload(decode=True)
				att_file = open('E:\\MyWeb\\mysite\\chat\\static\\download\\' + filename, 'wb')
				att_file.write(data)  # 保存附件
				att_file.close()
				attachment_files.append(filename)
		return attachment_files

    # 字符编码转换
    # @staticmethod
	def decode_str(self,str_in):
		value, charset = decode_header(str_in)[0]
		if charset:
			value = value.decode(charset)
		return value


	def run_ing(self):
        # 连接到POP3服务器,有些邮箱服务器需要ssl加密，可以使用poplib.POP3_SSL
		try:
			telnetlib.Telnet(self.pop3_server, 995)
			self.server = poplib.POP3_SSL(self.pop3_server, 995, timeout=100)
		except:
			time.sleep(5)
			self.server = poplib.POP3(self.pop3_server, 110, timeout=100)
		self.server.user(self.user)
		self.server.pass_(self.password)
        # 返回邮件数量和占用空间stat()返回的是二元组:
		Messages = self.server.stat()
		From = []
		To = []
		Content = []
		Subject = []
		Date = []
		attach_file = []
		for i in range(1, int(Messages[0]) + 1):# 顺序遍历邮件
			resp, lines, octets = self.server.retr(i)
			# lines存储了邮件的原始文本的每一行,
			# 邮件的原始文本:
			msg_content = b'\r\n'.join(lines).decode('utf-8')
			# 解析邮件:
			msg = Parser().parsestr(msg_content)
            #获取邮件的发件人，收件人， 抄送人,主题
			From.append(parseaddr(msg.get('from'))[1])
			To.append(parseaddr(msg.get('To'))[1])
			Subject.append(self.decode_str(msg.get('Subject')))
            # 获取邮件时间,格式化收件时间
			date1 = time.strptime(msg.get("Date")[0:24], '%a, %d %b %Y %H:%M:%S')
            # 邮件时间格式转换
			date2 = time.strftime("%Y-%m-%d  %H:%M:%S",date1)
			Date.append(date2)
			text = ''
			for part in msg.walk():
				text += self.get_content(part)
			Content.append(text)
			attach_file.append(self.get_att(msg))
		dict ={'from': From,'to': To, 'content': Content, 'subject': Subject, 'date': Date, 'num':int(Messages[0]), 'file':attach_file}
		return dict

def mailbox(request):
	#return render(request, 'chat/mailbox.html', {})
	username = request.session.get('username')
	users = User.objects.all()
	for user in users:
		if user.username == username:
			user_na = user.email
			password = user.send_password
	email_server = settings.EMAIL_SERVER
	email_class =down_email(user_na, password, email_server)
	dict = {}
	dict = email_class.run_ing()
	#return render(request, 'chat/mailbox.html',{ 'num': num })
	data = []
	for i in range(int(dict['num'])):
		dictx = {}
		dictx['id'] = i 
		dictx['from'] = dict['from'][i]
		dictx['subject'] = dict['subject'][i]
		dictx['date'] = dict['date'][i]
		data.append(dictx)
	return render(request, 'chat/mailbox.html', {
		'data': data
		})
	
	
def mail_detail(request, id):
	user = settings.EMAIL_HOST_USER 
	password  = settings.EMAIL_HOST_PASSWORD
	email_server = settings.EMAIL_SERVER
	email_class =down_email(user, password, email_server)
	dict = {}
	dict = email_class.run_ing()
	#return render(request, 'chat/mailbox.html',{ 'num': num })
	dictx = {}
	f_to = ''
	for i in range(int(dict['num'])):
		if i == int(id):
			dictx['id'] = i 
			dictx['content'] = dict['content'][i]
			dictx['from'] = dict['from'][i]
			dictx['subject'] = dict['subject'][i]
			dictx['date'] = dict['date'][i]
			dictx['file'] = []
			de = 0
			for x in dict['file'][i]:
				dictx['file'].append(x)
				de = de + 1
			dictx['count'] = de
			f_to = dict['from'][i]
	'''
	if request.method == 'POST':
		if request.POST == 'Delete':
			return render(request, 'chat/main_page.html',{})
		elif request.POST == 'Reply':
			return render(request, 'chat/write_email.html', {})
	'''
	return render(request, 'chat/mail_detail.html', {'dictx': dictx})	


def send_detail(request, id):
	username = request.session.get('username')
	sendemail = Sendemail.objects.all()
	dictx = {}
	t = 0
	for mail in sendemail:
		if mail.username == username:
			if mail.status == 1:
				if t == id:
					dictx['id'] = t
					dictx['sendto'] = mail.sendto
					dictx['theme'] = mail.theme
					dictx['from_'] = mail._from
					dictx['time'] = mail.time
					dictx['content'] = mail.content
				t = t +1
	return render(request, 'chat/send_detail.html',{'dictx': dictx})



def undo_detail(request, id):
	username = request.session.get('username')
	sendemail = Sendemail.objects.all()
	dictx = {}
	t = 0
	for mail in sendemail:
		if mail.username == username:
			if mail.status == 0:
				if t == id:
					dictx['id'] = t
					dictx['sendto'] = mail.sendto
					dictx['theme'] = mail.theme
					dictx['from_'] = mail._from
					dictx['time'] = mail.time
					dictx['content'] = mail.content
				t = t +1
	return render(request, 'chat/undo_detail.html',{'dictx': dictx})


def sendbox(request):
	username = request.session.get('username')
	sendemail = Sendemail.objects.all()
	data = []
	t = 0
	for mail in sendemail:
		if mail.username == username:
			if mail.status == 1:
				dictx = {}
				dictx['id'] = t
				dictx['sendto'] = mail.sendto
				dictx['theme'] = mail.theme
				dictx['from_'] = mail._from
				dictx['time'] = mail.time
				data.append(dictx)
				t = t +1
	return render(request, 'chat/sendbox.html',{'data': data})


def undobox(request):
	username = request.session.get('username')
	sendemail = Sendemail.objects.all()
	data = []
	t = 0
	for mail in sendemail:
		if mail.username == username:
			if mail.status == 0:
				dictx = {}
				dictx['id'] = t
				dictx['sendto'] = mail.sendto
				dictx['theme'] = mail.theme
				dictx['from_'] = mail._from
				dictx['time'] = mail.time
				data.append(dictx)
				t = t +1
	return render(request, 'chat/undobox.html',{'data': data})
#def show_friendlist(request):
'''
		 'from':dict['from'],
		 'to': dict['to'],
		 'content': dict['content'],
		 'subject': dict['subject'],
		 'date': dict['date'],
		 'num':dict['num'],
'''
	













