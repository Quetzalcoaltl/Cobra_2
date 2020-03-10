INICIO: IN R16, DDRB
        ORI R16,0x20
        OUT DDRB,R16
LOOP:   SBI PORTB,PB5
        RCALL ATRASO
        CBI PORTB, PB5
        RCALL ATRASO
        RJMP LOOP
ATRASO: LDI R16,X   //1
L1:     DEC R16     //1
        BRNE L1     //1-2
        RET         //4
        DEX R16

