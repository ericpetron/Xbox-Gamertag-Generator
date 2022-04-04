import random


def gamertag():
    final_list_adj = [] # Empty Lists
    final_list_noun = []
    temp_var_adj = open('adjective.txt')
    adj_list = temp_var_adj.readlines() # Creating a list of file IO
    temp_var_adj.close()
    for ele in adj_list:
        ele = ele.strip('\n')
        ele = ele.capitalize()
        final_list_adj.append(ele)
    
    
    
    
    # For the nouns
    temp_var_noun = open('nouns.txt')
    noun_list = temp_var_noun.readlines()    # File IO
    temp_var_noun.close()
    for ele in noun_list:
        ele = ele.split()
        for word in ele:
            word = word.strip('\n')
            word = word.capitalize()
            final_list_noun.append(word)
    
    
    
    
    
    num = random.randint(0, 1000) # Random 3 digit number
    noun_num = random.randint(0, len(final_list_noun)) # Indexing num
    adj_num = random.randint(0, len(final_list_adj)) # Indexing num
    return final_list_adj[adj_num] + final_list_noun[noun_num] + str(num)

print(gamertag())
