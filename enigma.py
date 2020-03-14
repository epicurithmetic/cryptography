# Arthur Scherbius' Enigma Machine (Invented: 1918 by Scherbius & Ritter).

# The enigma machine is, in essence, an interwoven series of subsitution
# ciphers; that is, ciphers which use permutations on the letters of an
# alphabet. The machines did not use any of the special German characters
# so the alphabet involved is identical to the English alphabet.


# Nazi Germany employed eight different rotors throughout 1930 - 1942. These
# are the rotors that we will use for this code.
I = list('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
II = list('AJDKSIRUXBLHWTMCQGZNPYFVOE')
III = list('BDFHJLCPRTXVZNYEIWGAKMUSQO')
IV = list('ESOVPZJAYQUIRHXLNFTGKDCMWB')
V = list('VZBRGITYUPSDNHLXAWMJQOFECK')
VI = list('JPGVOUMFYQBENHZRDKASXLICTW')
VII = list('NZJHGRCXMYSWBOUFAIVLPEKQDT')
VIII = list('FKQHTLXOCBJSPDZRAMEWNIUYGV')

class Rotor:

    """
        To specify a rotor one must state:
            * permutation of the alphabet
            * the turn over notch (ton)

    """

    def __init__(self,permutation,ton):
        #self.count = 0
        self.permutation = permutation
        self.ton = ton

    def rotate(self):

        """
        This method rotates the rotor. Moving all elements to the right
        by one space. Now 'A' gets mapped to the entry that we previously
        at the end of the list.
        """

        self.permutation = [self.permutation[-1]] + self.permutation[0:25]

    def update_input(self, X):
        alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        i = alphabet.index(X)
        X = self.permutation[i]
        self.rotate()
        return X

# Rotors produced by Nazi-Germany
rotor_one = Rotor(I, ['R'])
rotor_two = Rotor(II, ['F'])               # "Engima 1"
rotor_three = Rotor(III, ['W'])

rotor_four = Rotor(IV, ['K'])              # "M3 Army"
rotor_five = Rotor(V, ['A'])

rotor_six = Rotor(VI, ['A','N'])
rotor_seven = Rotor(VII, ['A','N'])        # "M3 and M4 Naval"
rotor_eight = Rotor(VIII, ['A','N'])

class EnigmaMachine:

    def __init__(self,rotors,iv):

        self.rotors = rotors
        self.iv = iv
        self.rotor_count = len(self.rotors)
        self.initialize()

    def initialize(self):

        for i in range(0, self.rotor_count):
            while not (self.iv[i] == self.rotors[i].permutation[0]):
                (self.rotors[i]).rotate()

machine = EnigmaMachine([rotor_three,rotor_two,rotor_one],['B','A','E'])

def enigma_encryption(machine,plaintext):


    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    plaintext = list(plaintext)
    ciphertext = ''

    # Pass each character through the enigma machine
    for x in plaintext:
        print(x)

        # Pass character through the rotors
        for rotor in machine.rotors:
            x = rotor.update_input(x)           # Make adjustments for turnover
            print(x)                            # of the other rotors.
        # Apply later stages of the machine


        ciphertext += x

    return ciphertext

print(enigma_encryption(machine, 'G'))
