"""
use a python dictionary to translate to morse code

Author: J. Knerr
Date: fall 2010

The hardcoded variable key uses the standard Morse Code as follows:

    A *-        I **        Q --*-      Y -*--
    B -***      J *---      R *-*       Z --**
    C -*-*      K -*-       S ***
    D -**       L *-**      T -
    E *         M --        U **-
    F **-*      N -*        V ***-
    G --*       O ---       W *--
    H ****      P *--*      X -**-

"""
# ---------------------------------------------------------- #

def main():

 morse = {
   'a': '.-',
   'b': '-...',
   'c': '-.-.',
   'd': '-..',
   'e': '.',
   'f': '..-.',
   'g': '--.',
   'h': '....',
   'i': '..',
   'j': '.---',
   'k': '-.-',
   'l': '.-..',
   'm': '--',
   'n': '-.',
   'o': '---',
   'p': '.--.',
   'q': '--.-',
   'r': '.-.',
   's': '...',
   't': '-',
   'u': '..-',
   'v': '...-',
   'w': '.--',
   'x': '-..-',
   'y': '-.--',
   'z': '--..' }

  # print(morse)
  
 word = input("word? ").lower()
 for ch in word:
    print(ch, morse[ch])

 for ch in "sos":
   print(morse[ch])

 print(morse)


# ---------------------------------------------------------- #

main()
