from pwn import *
from pwn import p64,p32,u64,u32
from LibcSearcher import*
class Target:
    def __init__(self,target:str,port:int):
        self.target=remote(target,port) if port is None else process(target)
    
    def s(self,payload):
        self.target.send(payload)
    
    def sl(self,payload):
        self.target.sendline(payload)
    
    def sa(self,information,payload):
        self.target.sendlineafter(information,payload)
    
    def sla(self,information,payload):
        self.target.sendlineafter(information,payload)
    
    def r(self,num:int):
        return self.target.recv(num)
    
    def ru(self,information):
        return self.target.recvuntil(information)
    
    def rl(self):
        return self.target.recvline()
    
    def leak_addr_x64(self):
        try:
            return u64(self.target.recv(6).ljust(8,b'\x00'))
        except:
            return u64(self.target.recvuntil(b'\x7f')[:-6].ljust(8,b'\x00'))
    
    def inter(self):
        self.target.interactive()
        