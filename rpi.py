from smbus import SMBus

addr = 0x8
BUS = SMBus(1) 

num = 1

print("Enter 1 for ON or 0 for OFF")
while num == 1:
    
    ledstate = input(">>>>   ")
    
    if ledstate == "1":
        BUS.write_byte(addr, 0x1) 
    elif ledstate == "0":
        BUS.write_byte(addr, 0x0) 
    else:
        numb = 0
