from smbus import SMBus

addr = 0x8
BUS = SMBus(1) //using the 1st SMBus connection

num = 1

print("Enter 1 for ON or 0 for OFF")
while num == 1:
    
    ledstate = input(">>>>   ")
    
    if ledstate == "1":
        BUS.write_byte(addr, 0x1) //turning the LED on
    elif ledstate == "0":
        BUS.write_byte(addr, 0x0) //turning the LED off
    else:
        numb = 0
