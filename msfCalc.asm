00000000  FC                cld
00000001  E88200            call 0x86
00000004  0000              add [bx+si],al
00000006  60                pusha
00000007  89E5              mov bp,sp
00000009  31C0              xor ax,ax
0000000B  648B5030          mov dx,[fs:bx+si+0x30]
0000000F  8B520C            mov dx,[bp+si+0xc]
00000012  8B5214            mov dx,[bp+si+0x14]
00000015  8B7228            mov si,[bp+si+0x28]
00000018  0F                db 0x0f
00000019  B74A              mov bh,0x4a
0000001B  2631FF            es xor di,di
0000001E  AC                lodsb
0000001F  3C61              cmp al,0x61
00000021  7C02              jl 0x25
00000023  2C20              sub al,0x20
00000025  C1CF0D            ror di,byte 0xd
00000028  01C7              add di,ax
0000002A  E2F2              loop 0x1e
0000002C  52                push dx
0000002D  57                push di
0000002E  8B5210            mov dx,[bp+si+0x10]
00000031  8B4A3C            mov cx,[bp+si+0x3c]
00000034  8B4C11            mov cx,[si+0x11]
00000037  78E3              js 0x1c
00000039  48                dec ax
0000003A  01D1              add cx,dx
0000003C  51                push cx
0000003D  8B5920            mov bx,[bx+di+0x20]
00000040  01D3              add bx,dx
00000042  8B4918            mov cx,[bx+di+0x18]
00000045  E33A              jcxz 0x81
00000047  49                dec cx
00000048  8B34              mov si,[si]
0000004A  8B01              mov ax,[bx+di]
0000004C  D6                salc
0000004D  31FF              xor di,di
0000004F  AC                lodsb
00000050  C1CF0D            ror di,byte 0xd
00000053  01C7              add di,ax
00000055  38E0              cmp al,ah
00000057  75F6              jnz 0x4f
00000059  037DF8            add di,[di-0x8]
0000005C  3B7D24            cmp di,[di+0x24]
0000005F  75E4              jnz 0x45
00000061  58                pop ax
00000062  8B5824            mov bx,[bx+si+0x24]
00000065  01D3              add bx,dx
00000067  668B0C            mov ecx,[si]
0000006A  4B                dec bx
0000006B  8B581C            mov bx,[bx+si+0x1c]
0000006E  01D3              add bx,dx
00000070  8B04              mov ax,[si]
00000072  8B01              mov ax,[bx+di]
00000074  D0894424          ror byte [bx+di+0x2444],1
00000078  245B              and al,0x5b
0000007A  5B                pop bx
0000007B  61                popa
0000007C  59                pop cx
0000007D  5A                pop dx
0000007E  51                push cx
0000007F  FFE0              jmp ax
00000081  5F                pop di
00000082  5F                pop di
00000083  5A                pop dx
00000084  8B12              mov dx,[bp+si]
00000086  EB8D              jmp short 0x15
00000088  5D                pop bp
00000089  6A01              push byte +0x1
0000008B  8D85B200          lea ax,[di+0xb2]
0000008F  0000              add [bx+si],al
00000091  50                push ax
00000092  68318B            push word 0x8b31
00000095  6F                outsw
00000096  87FF              xchg di,di
00000098  D5BB              aad 0xbb
0000009A  F0B5A2            lock mov ch,0xa2
0000009D  56                push si
0000009E  68A695            push word 0x95a6
000000A1  BD9DFF            mov bp,0xff9d
000000A4  D53C              aad 0x3c
000000A6  06                push es
000000A7  7C0A              jl 0xb3
000000A9  80FBE0            cmp bl,0xe0
000000AC  7505              jnz 0xb3
000000AE  BB4713            mov bx,0x1347
000000B1  726F              jc 0x122
000000B3  6A00              push byte +0x0
000000B5  53                push bx
000000B6  FFD5              call bp
000000B8  63616C            arpl [bx+di+0x6c],sp
000000BB  6300              arpl [bx+si],ax
