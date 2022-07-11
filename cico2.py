import ipaddress
valid=[]
invalid=[]
ans=[]
def check(address):
    try:
      ip=ipaddress.IPv4Address(address)
      valid.append(address)
    except ipaddress.AddressValueError:
        invalid.append(address)
def convert_func(valid):
    for i in valid:
            no = int(valid.index(i))
            #print(no)
            bin='{:#_b}'.format(ipaddress.IPv4Address(i))
            #print("binary format:", bin)
            oct='_'.join(["%04o" % int(x) for x in str(i).split('.')])
            #print("octal format:", oct)
            hex='{:#_X}'.format(ipaddress.IPv4Address(i))
            #print("hexadecimal format:", hex)
            ans.append("  "+str(i)+",")
            ans.append("  "+str(bin)+",")
            ans.append("  "+str(oct)+",")
            ans.append("  "+str(hex)+'/')        
def enter_input():
    for i in range(10):
           address=input("enter ipv4 address:")
           check(address)
def output():

    enter_input()
    convert_func(valid)
    file1 = open("myfile.txt","w+")
    file1.writelines(ans)
    file1.close()
    with open("myfile.txt", 'r+') as f:
            for line in f:
                li=line.split('/')
            #print("lendgth          ",len(li))
            #print(li)
            for i in range(len(li)-1):   
                print("the ",i+1,"th IP address in Decimal, Binary, Octal and hexadecimal format is <",str(li[i]).strip()+ ">\n")
                
    f.close()
        
        
    
        

output()
#print(valid)
#print(invalid) 
#print(ans)      