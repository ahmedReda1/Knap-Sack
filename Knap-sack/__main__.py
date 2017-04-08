import sys
import KnapsackView
import Encryptor
import Decryptor


def main():
    # getting Inputs
    inputs = KnapsackView.inputs()

    # Encryption Part
    encryptor = Encryptor.Encryptor(inputs.multiplier,inputs.inverse_multiplier,inputs.modulus,inputs.simpleKnapsack,inputs.message)
    encrypted_message = encryptor.encrypt()

    #Decryption Part
    decryptor = Decryptor.Decryptor(inputs.inverse_multiplier,inputs.modulus,encrypted_message,inputs.simpleKnapsack)
    encrypted_message = decryptor.decrypt()


if __name__ == '__main__':
    sys.exit(main())
