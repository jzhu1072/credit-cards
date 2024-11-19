
#PART A 
def luhn_last_digit(n):
    
    lst = [] #create a empty list and add values of n
    for nums in str(n):
        lst.append(int(nums))
                
    #sum of numbers after it's doubled
    sum_of_doubled_nums = 0 

    for nums_to_double in (lst[-1::-2]):
        doubled_num = int(nums_to_double) * 2
        if doubled_num > 9: #subtract 9 if doubled num is greater than 9
            doubled_num = doubled_num - 9

        sum_of_doubled_nums += doubled_num #keeps track of sum
        
    #sum of the numbers not doubled
    sum_of_nondoubled_nums = 0 
    for nums_not_doubled in (lst[-2::-2]):
        sum_of_nondoubled_nums += int(nums_not_doubled)
 
    final_sum = sum_of_doubled_nums + sum_of_nondoubled_nums
    final_sum2 = final_sum #create a duplicate variable
    
    for digits in range(10): #0 to 9
        final_sum2 = final_sum + digits
        
        if final_sum2 % 10 == 0: #if final_sum2 is divisible by 10...
            return str(digits)
        
#example runs:        
##print(luhn_last_digit('1'))
##print(luhn_last_digit('042'))
##print(luhn_last_digit('0000'))
##print(luhn_last_digit('412345678901'))
##print(luhn_last_digit('231160563396423'))
##print(luhn_last_digit('527504685958238'))

#PART B ------------------------------------------------
import random
                         #string
def generate_card_number(card_type):

# returns a randomly generated valid credit card number
    if card_type == 'v': #when the parameter is 'v':
        visa_list = ['4'] 
        length_lst = [11, 14, 17]

        # appends the numbers (0 to 9) 11, 14, or 17 times
        for visa_length in range(1,random.choice(length_lst)+1): 
            visa_list.append(str(random.randint(0,9)))

        visa_str = (''.join(visa_list)) #convert to list
        visa_list.append(luhn_last_digit(visa_str)) #add the results to the list

        return (''.join(visa_list)) #returns visa_list as a string

    elif card_type == 'm': #when the parameter is 'm':
        rand_num = random.randint(1,2)

        if rand_num == 1: #when the card# starts with 51-55:   
            master_list = ['5']
            master_list.append(str(random.randint(1,5)))
        
            for master_length in range(1,14): #appends numbers to list
                master_list.append(str(random.randint(0,9))) 
            
            master_str = (''.join(master_list)) #convert to string
            master_list.append(luhn_last_digit(master_str)) #add the result
            return (''.join(master_list))

        if rand_num == 2: #when the card# starts with 222100-272099
            master_list2 = []
            begin_nums = str(random.randint(222100, 272099))
            
            for numbers in begin_nums: #add beginning values into the empty list
                master_list2.append(numbers)
                
            for master_length in range(1,10): #add rest of the values
                master_list2.append(str(random.randint(0,9)))
                
            master_str2 = (''.join(master_list2)) #change to string
            master_list2.append(luhn_last_digit(master_str2)) #add the result
            
            return (''.join(master_list2))
        
    elif card_type != 'v' and card_type != 'm':
        return None

#example run:  
#print(generate_card_number('v'))

#PART C ----------------------------------------

#ask for initial input
card_input = input('Enter v for a Visa number, m for MasterCard, anything else to exit: ')

while card_input == 'v' or card_input == 'm': #loops while the user enters 'v' or 'm'
    print(generate_card_number(card_input))
    card_input = input('\nEnter v for a Visa number, m for MasterCard, anything else to exit: ')

print('Bye, don’t have *too* much fun...') #prints when the loop is stopped


