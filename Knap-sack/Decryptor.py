import sys
import utils


class Decryptor:
    def __init__(self, inverse_multiplier, modulus, encrypted_message, simpleKnapsack):
        self.inverse_multiplier = inverse_multiplier
        self.modulus = modulus
        self.encrypted_message = encrypted_message
        self.simple_Knapsack = simpleKnapsack

    def decrypt(self):
        print utils.utils.DECRYPTION_ILLUSTRATION_MESS
        decrypted_message = ''
        binary_message = ''
        decrypted_arr = []
        for element in self.encrypted_message:
            decrypted_block = (element * self.inverse_multiplier) % self.modulus
            decrypted_message += ' ' + str(decrypted_block)
            decrypted_arr.append(decrypted_block)
            binary_message += ' ' + self.getFinalValue(decrypted_block)
            print str(element) + ' X ' + str(self.inverse_multiplier) + ' mod ' + str(self.modulus) + ' = ' + str(
                decrypted_block)

        print utils.utils.DECRYPTION_MESS + decrypted_message
        print utils.utils.FINAL_DECRYPTION_MESS
        print utils.utils.FINAL_OUTPUT_MESS + binary_message

    # this function converts decrypted block into binary representation as the knapsack itself
    def getFinalValue(self, decrypted_block):
        output = [0] * len(self.simple_Knapsack)
        sum = 0
        flag = True
        while (flag):
            for index, i in enumerate(reversed(self.simple_Knapsack)):
                if ((sum + i) > decrypted_block):
                    output[index] = 0
                elif ((sum + i) <= decrypted_block):
                    output[index] = 1
                    sum += i
            break

        return ''.join(map(str, list(reversed(output))))
