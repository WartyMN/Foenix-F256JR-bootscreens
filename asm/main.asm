!source "inc/macros.asm"

; macro to create the basic program to start code
+start_at $0900

  lda #00   
  sta $d020  ; border colour
  sta $d021  ; background colour
loop
  inc $d021    ; increase background colour
  jmp loop     ; loop forever
