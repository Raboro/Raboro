def decodeMorse(morse_code):
    decode = { '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
              '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',     
              '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z'     
    }
    for e in range(0, len(morse_code)):
      # if morse_code[e] == "   "
        morse_code.replace(e, decode[e])
    for e in range(0, len(morse_code)):
        print(morse_code[e])
    return morse_code.replace('.', '.').replace('-','-').replace(' ', '')

decodeMorse('') # enter your morse code
