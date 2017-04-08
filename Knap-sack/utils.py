class utils:
    # general Messages
    WELCOME_MESS = '''
                      //////////////////////////////////////////////////////
                      //////     welcome to Knap-Sack simulation     ///////
                      //////////////////////////////////////////////////////
                      '''

    # input messages
    GET_MULTIPLIER_MESS = 'please insert a multiplier value ...'
    GET_MULTIPLIER_MESS_ERROR = 'please insert a valid multiplier value ...'

    GET_INVERSE_MULTIPLIER_MESS = 'please insert a inverse multiplier value ...'
    GET_INVERSE_MULTIPLIER_MESS_ERROR = 'please insert a valid inverse multiplier value ...'

    GET_MODULUS_MESS = 'please insert a modulus value whish is prime relative to your multiplier ...'
    GET_MODULUS_MESS_ERROR = 'please insert a valid modulus value ...'

    GET_BINARY_MESSAGE_MESS = 'please insert your binary message ..'
    GET_BINARY_MESSAGE_MESS_ERROR = 'please insert a valid binary message ..'

    GET_SIMPLE_KNAPSACK_MESS = 'please insert your simple knapsack comma separated ...'
    GET_SIMPLE_KNAPSACK_MESS_ERROR = 'please insert your a valid simple knapsack comma separated ...'

    # encryption messages
    ENCRYPTION_START_MESS = 'Starting encryption process .....'

    ENCRYPTION_ILLUSTRATION_MESS = '''
            Now , For a start we need to convert simple knapsack to a general knapsack which is hard to
            break by using the idea of "Modular Arithmetic" theory so to achieve that ,
            we are going to use both multiplier and modulus which are available for both end-users
    '''
    GENERAL_KNAPSACK_MESS = '''
            The Following is the general knapsack which is hard to break as the modular arithmetic
            problem
    '''
    DATA_BLOCK_LIST_MESS = "Data blocks will be used to encrypt message :"
    DATA_BLOCK_NUMBER_MESS = "so number of data blocks (message length / general knapsack length ) = "
    ENCRYPTED_MESSAGE_MESS = "### Encrypted message is :  "

    # decryption messages
    DECRYPTION_START_MESS = 'Starting Decryption process .....'

    DECRYPTION_ILLUSTRATION_MESS = '''
            So far we've a public encrypted message , that any one can intercept , but only
            users with the modulus and multiplier are only people who are able to decrypt the message
    '''

    ORIGINAL_MESSAGE_MESS = "### Original message is :  "
    DECRYPTION_MESS = """
                    ### Decoded Message is :
                    """
    FINAL_DECRYPTION_MESS='''
                    By converting each element of the decoded message to its binary represntation using the simple knapsack ,
                    starting from most significant bit,
                    the highest value till the sum matches the element , this will lead to the original message itself
    '''
    FINAL_OUTPUT_MESS = 'Final output is = '