import cmath
import sys
import utils
import userModel


class inputs:
    def __init__(self):
        print utils.utils.WELCOME_MESS

        # getting user inputs
        inputInstance = userModel.userInputs()

        self.multiplier = inputInstance.getMultiplier()
        self.inverse_multiplier = inputInstance.getInverseMultiplier()
        self.modulus = inputInstance.getModulus()
        self.message = inputInstance.getBinaryMessage()
        self.simpleKnapsack = inputInstance.getSimpleKnapsack()






