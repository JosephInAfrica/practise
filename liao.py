import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('www.sina.cn',80))

s.send('GET /HTTP/1.1\r\nHost:www.sina.cn\r\nConnection: close\r\n\r\n')

buffer=[]
while True:
	d=s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data=''.join(buffer)
s.close()
header,html=data.split('\r\n\r\n',1)
print header

with open('sina.html','wb') as f:
	f.write(html)

# here comes the server code

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind('127.0.0.1',9999)
s.listen(5)
print 'Waiting for connection...'

while True:
	sock,addr=s.accept()
	t=treading.Thread(target=tcplink,args=(sock,addr))
	t.start()

def tcplink(sock,addr):
	print 'Accept new connections from %s:%s...'%addr
	socket.send('welcome!')
	while True:
		data=sock.recv(1024)
		time.sleep(1)
		if data=='exit' or not data:
			break
		socket.send('Hello.,%s!'%data)
	sock.close()
	print 'connections from %s:%s closed.'%addr

