import utils

class userInputs:

    def getMultiplier(self):
        error = False
        while error != True:
            print utils.utils.GET_MULTIPLIER_MESS
            try:
                multiplier = int(raw_input())
                error = True
            except ValueError:
                print utils.utils.GET_MULTIPLIER_MESS_ERROR

        return multiplier


    def getInverseMultiplier(self):
        error = False
        while error != True:
            print utils.utils.GET_INVERSE_MULTIPLIER_MESS
            try:
                inverse_multiplier = int(raw_input())
                error = True
            except ValueError:
                print utils.utils.GET_INVERSE_MULTIPLIER_MESS_ERROR

        return inverse_multiplier



    def getModulus(self):
        error = False
        while error != True:
            print utils.utils.GET_MODULUS_MESS
            try:
                modulus = int(raw_input())
                error = True
            except ValueError:
                print utils.utils.GET_MODULUS_MESS_ERROR

        return modulus



    def getBinaryMessage(self):
        error = False
        while error != True:
            print utils.utils.GET_BINARY_MESSAGE_MESS
            try:
                message = bin(int(raw_input(),2))
                error = True
            except ValueError:
                print utils.utils.GET_BINARY_MESSAGE_MESS_ERROR

        return message



    def getSimpleKnapsack(self):
        error = False
        while error != True:
            print utils.utils.GET_SIMPLE_KNAPSACK_MESS
            try:
                simpleKnapsack = map(int,raw_input().split(','))
                error = True
            except ValueError:
                print utils.utils.GET_SIMPLE_KNAPSACK_MESS_ERROR

        return simpleKnapsack
