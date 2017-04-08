import sys
import utils


class Encryptor:
    def __init__(self, multiplier, inverse_multiplier, modulus, simpleKnapsack, message):
        self.multiplier = multiplier
        self.inverse_multiplier = inverse_multiplier
        self.modulus = modulus
        self.message = message
        self.simple_knapsack = simpleKnapsack

    # method to encrypt user data
    def encrypt(self):
        print utils.utils.ENCRYPTION_ILLUSTRATION_MESS
        general_knapsack = self.getGeneralKnapsack()
        encrypted_message = self.getEncryptedMessage(general_knapsack)
        return encrypted_message

    # getting general knapsack  as public key
    def getGeneralKnapsack(self):
        print utils.utils.GENERAL_KNAPSACK_MESS
        gns = []
        for element in self.simple_knapsack:
            gns.append((element * self.multiplier) % self.modulus)
            print str(element) + ' X ' + str(self.multiplier) + ' mod ' + str(self.modulus) + ' = ' + str(
                (element * self.multiplier) % self.modulus)
        print '\nGeneral Knapsack : '+str(gns)+"\n"
        return gns

    # function to encrypt the message by getting the general knapsack
    def getEncryptedMessage(self, general_knapsack):
        message = self.message.split('0b')[1]
        message = list(message)

        print utils.utils.DATA_BLOCK_LIST_MESS
        data_blocks = self.getDataBlocks(message, general_knapsack)

        # encrypting and getting the sum of each data block
        encrypted_message = []
        start = 0
        end = len(general_knapsack)
        for data_block in data_blocks:
            for i in range(start, end):
                sum = 0
                for index, b in enumerate(data_block):
                    if (b == '1'):
                        sum += general_knapsack[index]
            encrypted_message.append(sum)
        print "\n"+utils.utils.ENCRYPTED_MESSAGE_MESS + '  '.join(str(x) for x in encrypted_message) + " ###\n"
        return encrypted_message

    # function to split data stream to work with the general knapsack
    def getDataBlocks(self, message, general_knapsack):
        data_blocks = []
        start = 0
        end = len(general_knapsack)
        for j in range(0, len(message) / len(general_knapsack)):
            step_array = []
            for i in range(start, end):
                step_array.append(message[i])

            print step_array
            data_blocks.append(step_array)
            start = end
            end = start + len(general_knapsack)

        return data_blocks
