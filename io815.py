try:
    f=open('815metaclass.py','r')
    # print f.read()
    for line in f.readlines():
        print line
finally:
    if f:
        f.close()

# with open('815metaclass.py','r') as f:
    # print f.read()