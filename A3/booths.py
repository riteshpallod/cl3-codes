'''
booths algorithm for 8 bit numbers
start reading from booths_multiply
imp: numbers (here) are arrays!
'''

'''
'number' is number. int
we return array which is binary representation of 'number'
'''
def decimal_to_binary(number):
    #create a 8 binary_number array
    binary_number = [0]*8
    print ("binary_number initially:\t", binary_number)
    
    index = 7
    while number and index >= 0:
        quotient = int(number/2)
        remainder = number%2
        
        #print(quotient,"\t\t", remainder)
        binary_number[index] = remainder
        
        index = index -1
        number = quotient

    print ("binary_number now:\t\t", binary_number)
    return binary_number

def add(a, b):
    result = [0]*len(a)
    carry = 0
    index = len(a)-1

    while index >= 0:
        temp_sum = a[index]+b[index]+carry
        carry = temp_sum/2
        result[index] = temp_sum%2
        index -= 1
    return result

def right_shift(number_array):
    #inserting A[0] at initial position and shifting it
    number_array.insert(0, number_array[0]) 

    #shifting matlab poping it
    number_array.pop()
    return number_array


def binary_to_decimal(number_array):
    flag = 1 #for positive numbers
    '''
    if number is negative (msb or number_array[0] is 1),
    we need to convert this negative number back to positive

    if number is negative then the number is in 2s complement form
    we take 1s complement and add 1.
    '''
    length = len(number_array)
    
    #if number is negative
    if number_array[0] == 1:
        flag = -1
        #take ones complement
        for i in range(length): #16 bit number
            number_array[i] = 1 - number_array[i]

        #add one 
        one = [0]*(length-1) + [1]
        number_array = add(number_array, one)
        print("number is now: ", number_array)
    
    #normal conversion
    power = 0
    number_decimal = 0
    index = length-1
    
    while index >= 0:
        if number_array[index] == 1:
            number_decimal += 2**power
        power += 1 
        index -= 1
    print("decimal calculated: ", number_decimal)
    
    return flag*number_decimal

def booths_multiply(a,b):
    # a, b are decimal
    # we need to convert them to decimal
    binary_a = decimal_to_binary(a)
    binary_b = decimal_to_binary(b)

    print("binary a: ", binary_a)
    print("binary b: ", binary_b)

    #now let binary_a be Q, and binary_b be M
    Q = binary_a
    Q_minus_1 = 0
    
    M = binary_b

    #Minus_M = twos_complement(binary_b) ABHI KE LIYE WE DO THE FOLLOWING
    Minus_M = decimal_to_binary(-b)

    # A is array of 0s, size = 8
    A = [0]*8 
    
    #let ALL17 be A+Q+Q_minus_1
    ALL17 = []
    ALL17.extend(A)
    ALL17.extend(Q)
    ALL17.append(Q_minus_1)

    print(ALL17)

    #Abhi we add M (or Minus_M) to A
    '''
    A = ALL17[0:8]
    Q = ALL17[8:16]
    Q_minus_1 = ALL17[16]

    so when we add M to A, we are actually adding M (8bit) to ALL17(17it)'s first 8 bit
    easier way would be to append 9 zeroes at the end of M (naya waala ko bol M') 
    which makes our actual M the first 8 bits of M'
    example:
    ALL17 = 0000 0000 1111 0101 0
    M     = 1010 0010
    M'    = 1010 0010 0000 0000 0
    
    
    same logic is applied everywhere


    so adding M to A is same as adding M' to ALL17
    '''
    M = M + [0]*9
    Minus_M = Minus_M + [0]*9

    #8bit booths so 8 baar do things
    for i in range(8):
        #check the last two bits (last bit is Q_minus_1, second last is Q ka last)
        if (ALL17[-2] == 0 and ALL17[-1] == 1):
            #do A+M
            ALL17 = add(ALL17, M)
            print(ALL17[0:8],"\t",ALL17[8:16],"\t", ALL17[-1], "\t adding M. ")
             
        elif (ALL17[-2] == 1 and ALL17[-1] == 0):
            #do A-M 
            ALL17 = add(ALL17, Minus_M)
            print(ALL17[0:8],"\t",ALL17[8:16],"\t", ALL17[-1], "\t adding -M. ")
               
        #right shift
        ALL17 = right_shift(ALL17)
        print(ALL17[0:8],"\t",ALL17[8:16],"\t", ALL17[-1],"\t right shift\n")
    
    '''
    now our answer is AQ. We don't need the last bit
    so pop it
    '''
    ALL17.pop()
    #ALL17 is actually 16 bits now. Yay!
    #return the decimal version of ALL17 (16waala)
    return binary_to_decimal(ALL17)

if __name__ == "__main__":
    '''
    while True:    
        x = int(input())
        print(x)
        x = decimal_to_binary(x)
        print(x)
        x = binary_to_decimal(x)
        print(x)
    '''
    while True:
        a = int(input())
        b = int(input())

        print("booths multiplication: ", booths_multiply(a,b))