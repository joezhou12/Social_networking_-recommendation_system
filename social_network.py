# Name: Yichun Zhou
# NYU ID: yz6176 
# Homework 4

import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter

###
### Problem 1a
###

practice_graph = nx.Graph()

practice_graph.add_edge("A", "B")
practice_graph.add_edge("A", "C")
practice_graph.add_edge("B", "C")
# TODO: Add more here...
#add edge for each node
practice_graph.add_edge("B", "D")
practice_graph.add_edge("C", "D")
practice_graph.add_edge("C", "F")
practice_graph.add_edge("D", "F")
practice_graph.add_edge("D", "E")

assert len(practice_graph.nodes()) == 6
assert len(practice_graph.edges()) == 8

# Test shape of practice graph
assert set(practice_graph.neighbors("A")) == set(["B", "C"])
assert set(practice_graph.neighbors("B")) == set(["A", "D", "C"])
assert set(practice_graph.neighbors("C")) == set(["A", "B", "D", "F"])
assert set(practice_graph.neighbors("D")) == set(["B", "C", "E", "F"])
assert set(practice_graph.neighbors("E")) == set(["D"])
assert set(practice_graph.neighbors("F")) == set(["C", "D"])

def draw_practice_graph():
    """Draw practice_graph to the screen.
    """
    nx.draw_networkx(practice_graph)
    plt.show()

# Comment out this line after you have visually verified your practice graph.
# Otherwise, the picture will pop up every time that you run your program.
#draw_practice_graph()

###
### Problem 1b
###

# (Your code for Problem 1b goes here.)
#a new graph called rj
rj = nx.Graph()
#add edge for each node
rj.add_edge("Juliet","Nurse")
rj.add_edge("Juliet","Tybalt")
rj.add_edge("Juliet","Capulet")
rj.add_edge("Juliet","Friar Laurence")
rj.add_edge("Juliet","Romeo")
rj.add_edge("Tybalt", "Capulet")
rj.add_edge("Capulet","Paris")
rj.add_edge("Capulet","Escalus")
rj.add_edge("Escalus","Paris")
rj.add_edge("Escalus","Montague")
rj.add_edge("Escalus","Mercutio")
rj.add_edge("Paris","Mercutio")
rj.add_edge("Romeo","Montague")
rj.add_edge("Romeo","Mercutio")
rj.add_edge("Romeo","Friar Laurence")
rj.add_edge("Romeo","Benvolio")
rj.add_edge("Benvolio","Montague")

assert len(rj.nodes()) == 11
assert len(rj.edges()) == 17

# Test shape of Romeo-and-Juliet graph
assert set(rj.neighbors("Nurse")) == set(["Juliet"])
assert set(rj.neighbors("Friar Laurence")) == set(["Juliet", "Romeo"])
assert set(rj.neighbors("Tybalt")) == set(["Juliet", "Capulet"])
assert set(rj.neighbors("Benvolio")) == set(["Romeo", "Montague"])
assert set(rj.neighbors("Paris")) == set(["Escalus", "Capulet", "Mercutio"])
assert set(rj.neighbors("Mercutio")) == set(["Paris", "Escalus", "Romeo"])
assert set(rj.neighbors("Montague")) == set(["Escalus", "Romeo", "Benvolio"])
assert set(rj.neighbors("Capulet")) == \
    set(["Juliet", "Tybalt", "Paris", "Escalus"])
assert set(rj.neighbors("Escalus")) == \
    set(["Paris", "Mercutio", "Montague", "Capulet"])
assert set(rj.neighbors("Juliet")) == \
    set(["Nurse", "Tybalt", "Capulet", "Friar Laurence", "Romeo"])
assert set(rj.neighbors("Romeo")) == \
    set(["Juliet", "Friar Laurence", "Benvolio", "Montague", "Mercutio"])

def draw_rj():
    """Draw the rj graph to the screen and to a file.
    """
    nx.draw_networkx(rj)
    plt.savefig("romeo-and-juliet.pdf")
    plt.show()

# Comment out this line after you have visually verified your rj graph and
# created your PDF file.
# Otherwise, the picture will pop up every time that you run your program.
#draw_rj()

###
### Problem 2
###

def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    """
    # This function has already been implemented for you.
    # You do not need to add any more code to this (short!) function.
    return set(graph.neighbors(user))

assert friends(rj, "Mercutio") == set(['Romeo', 'Escalus', 'Paris'])


def friends_of_friends(graph, user):
    """Returns a set of friends of friends of the given user, in the given 
    graph. The result does not include the given user nor any of that user's
    friends.
    """
    #on the pdf it says this function can be done in 4 lines
    #I tried my best and got it done in 7 lines
    #call a new empty set for future storage for friends_of_friends
    friends_of_friends_set = set()
    #iterate through the set returned by friends() function 
    for f in friends(graph,user):
        #call the friends() function again to get the friends_of_friends
        #and iterate through friends_of_friends
        for i in friends(graph,f):
            #check if the friends_of_friends is already a friend
            #also check if the friends_of_friends is user himself
            if i not in friends(graph,user) and i != user:
                #if not, add into the friends_of_friends_set
                friends_of_friends_set.add(i)
            else : pass
    return friends_of_friends_set
        
#friends_of_friends(rj, "Mercutio")
assert friends_of_friends(rj, "Mercutio") == set(['Benvolio', 'Capulet', 'Friar Laurence', 'Juliet', 'Montague'])


def common_friends(graph, user1, user2):
    """Returns the set of friends that user1 and user2 have in common.
    """
    #I did it! I completed this function in 1 line, just as the pdf described
    #I used the list function, it would join 2 set based on common values
    return set(list(friends(graph,user1) & friends(graph,user2)))
    #print ("Remove this print statement once common_friends is implemented")

assert common_friends(practice_graph,"A", "B") == set(['C'])
assert common_friends(practice_graph,"A", "D") == set(['B', 'C'])
assert common_friends(practice_graph,"A", "E") == set([])
assert common_friends(practice_graph,"A", "F") == set(['C'])
assert common_friends(rj, "Mercutio", "Nurse") == set()
assert common_friends(rj, "Mercutio", "Romeo") == set()
assert common_friends(rj, "Mercutio", "Juliet") == set(["Romeo"])
assert common_friends(rj, "Mercutio", "Capulet") == set(["Escalus", "Paris"])


def number_of_common_friends_map(graph, user):
    """Returns a map (a dictionary), mapping from each user U to the number 
    of friends U has in common with the given user. The map keys are the 
    users who have at least one friend in common with the given user, 
    and are neither the given user nor one of the given user's friends.
    Example: a graph called my_graph and user "A" 
    (Note: This is NOT the practice_graph used in the assignment writeup.)
    Here is what is relevant about my_graph:
        - "A" and "B" have two friends in common
        - "A" and "C" have one friend in common
        - "A" and "D" have one friend in common
        - "A" and "E" have no friends in common
        - "A" is friends with "D" (but not with "B" or "C")
    Here is what should be returned:
      number_of_common_friends_map(my_graph, "A")  =>   { 'B':2, 'C':1 }
    """
    #start with a new dictinary for store the number_of_common_friends
    number_of_common_friends_dict = {}
    #call the friends_of_friends function to get friends_of_friends set
    #itrerate through the friends_of_friends set
    for i in friends_of_friends(graph, user):
        #i is the one of the friends_of_friends, store as key in dict
        #common_friends function to find the common_friends
        #and used len function to get the the number_of_common_friends, store
        #as the value
        number_of_common_friends_dict.update(
            {i:len(common_friends(graph, user, i))})
    return number_of_common_friends_dict


assert number_of_common_friends_map(practice_graph, "A") == {'D': 2, 'F': 1}
assert number_of_common_friends_map(rj, "Mercutio") == \
    { 'Benvolio': 1, 'Capulet': 2, 'Friar Laurence': 1, 
      'Juliet': 1, 'Montague': 2 }


def number_map_to_sorted_list(map_with_number_vals):
    """Given map_with_number_vals, a dictionary whose values are numbers, 
    return a list of the keys in the dictionary.
    The keys are sorted by the number value they map to, from greatest
    number down to smallest number.
    When two keys map to the same number value, the keys are sorted by their
    natural sort order for whatever type the key is, from least to greatest.
    """
    #new empty list to later store list use
    s_list = []
    #new dict for later store dict use
    after_alpha_sort_dict = {}
    #sort the map_with_number_vals in alphabetical order
    sorted_list_alphabetically = sorted(map_with_number_vals.items())
    #iterate through sorted_list_alphabetically
    #store the list back into a dict
    for j in range(len(sorted_list_alphabetically)):
        after_alpha_sort_dict.update({sorted_list_alphabetically[j][0]:
                                      sorted_list_alphabetically[j][1]})
    #call the sorted function to sort the map_with_number_vals
    #in decending order by the value of the dict
    sorted_list = sorted(after_alpha_sort_dict.items(), key=lambda x: x[1],
                          reverse=True)
    #iterate through the final sorted_list, get the key and append into s_list
    for i in range(len(sorted_list)):
        s_list.append(sorted_list[i][0])
    return s_list

    
assert number_map_to_sorted_list({"a":5, "b":2, "c":7, "d":5, "e":5}) == \
    ['c', 'a', 'd', 'e', 'b']
# number_map_to_sorted_list({ 'Benvolio': 0.2, 'Capulet': 0.5833333333333333, 
#                             'Friar Laurence': 0.2, 'Juliet': 0.2, 
#                             'Montague': 0.45 })

def recommend_by_number_of_common_friends(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the number of common friends (people
    with the most common friends are listed first).  In the
    case of a tie in number of common friends, the names/IDs are
    sorted by their natural sort order, from least to greatest.
    """
    #call the number_of_common_friends_map fucntion to get the dictionary of
    #friends_of_friends and number of common friend
    number_of_common_friends_dict = number_of_common_friends_map(graph, user)
    #call the number_map_to_sorted_list get the list of sorted friend
    #recommendation
    sorted_recommend_key = number_map_to_sorted_list(number_of_common_friends_dict)
    return sorted_recommend_key

assert recommend_by_number_of_common_friends(practice_graph,"A") == ['D', 'F']
assert recommend_by_number_of_common_friends(rj, "Mercutio") == ['Capulet', 'Montague', 'Benvolio', 'Friar Laurence', 'Juliet']


###
### Problem 3
###

def influence_map(graph, user):
    """Returns a map (a dictionary) mapping from each person P to their 
    influence score, with respect to the given user. The map only 
    contains people who have at least one friend in common with the given 
    user and are neither the user nor one of the users's friends. 
    See the assignment for the definition of influence scores.
    """
    #start with a new dictinary for store the influence_dict
    influence_dict = {}

    #itrerate through the friends_of_friends set
    for i in friends_of_friends(graph, user):
        #set influence_score = 0 for every i
        influence_score = 0
        #itrerate through the the result of common_friends
        for j in common_friends(graph, user, i):
            # at first I tried to use 3 conditon, but I found there is an easy
            # way by calling +=
            # if the number of common_friends is more than 1
            #if len(common_friends(graph, user, i)) > 1 :
                #influence_score will be added up
            influence_score += 1/len(friends(graph, j))
            #elif len(common_friends(graph, user, i)) == 1:
                #influence_score = 1/len(friends(graph, j))
            #else: pass
            influence_dict.update({i:influence_score})
    return influence_dict


#caculated by hand A's friend of friend are D and F
#influence score of D is 1/4 + 1/3 = 0.5833333333333333
#influence score of F is 1/4  = 0.25
#assert added by me
assert influence_map(practice_graph, "A") == {'D': 0.5833333333333333, 'F': 0.25}

assert influence_map(rj, "Mercutio") == { 'Benvolio': 0.2, 'Capulet': 0.5833333333333333, 'Friar Laurence': 0.2, 'Juliet': 0.2, 'Montague': 0.45 }


def recommend_by_influence(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the influence score (people
    with the biggest influence score are listed first).  In the
    case of a tie in influence score, the names/IDs are sorted
    by their natural sort order, from least to greatest.
    """
    #similar to recommend_by_number_of_common_friends
    #call the influence_map fucntion to get the dictionary of
    #friends_of_friends and number of common friend
    influence_dict = influence_map(graph, user)
    #call the number_map_to_sorted_list get the list of sorted friend
    #recommendation
    sorted_recommend_key = number_map_to_sorted_list(influence_dict)
    return sorted_recommend_key

#the recommend_by_influence for A by order would be D, F
#assert added by me
assert recommend_by_influence(practice_graph, "A") == ['D', 'F']

assert recommend_by_influence(rj, "Mercutio") == ['Capulet', 'Montague', 'Benvolio', 'Friar Laurence', 'Juliet']


###
### Problem 4
#will return True if both method return same result, vice versa
#1. Mercutio same result 
recommend_by_number_of_common_friends(rj, "Mercutio") == recommend_by_influence(rj, "Mercutio")
#2. Juliet different result 
recommend_by_number_of_common_friends(rj, "Juliet") == recommend_by_influence(rj, "Juliet")
#3. Nurse same result 
recommend_by_number_of_common_friends(rj, "Nurse") == recommend_by_influence(rj, "Nurse")
#4. Tybalt different result 
recommend_by_number_of_common_friends(rj, "Tybalt") == recommend_by_influence(rj, "Tybalt")
#5. Capulet different result 
recommend_by_number_of_common_friends(rj, "Capulet") == recommend_by_influence(rj, "Capulet")
#6. Friar Laurence same result 
recommend_by_number_of_common_friends(rj, "Friar Laurence") == recommend_by_influence(rj, "Friar Laurence")
#7. Romeo different result 
recommend_by_number_of_common_friends(rj, "Romeo") == recommend_by_influence(rj, "Romeo")
#8. Paris different result 
recommend_by_number_of_common_friends(rj, "Paris") == recommend_by_influence(rj, "Paris")
#9. Escalus same result 
recommend_by_number_of_common_friends(rj, "Escalus") == recommend_by_influence(rj, "Escalus")
#10. Montague different result 
recommend_by_number_of_common_friends(rj, "Montague") == recommend_by_influence(rj, "Montague")
#11. Benvolio same result 
recommend_by_number_of_common_friends(rj, "Benvolio") == recommend_by_influence(rj, "Benvolio")

#Use loop to find Same and Diff result
same_list = []
diff_list = []
diff_count,same_count = 0,0
for i in rj.nodes():
    if recommend_by_number_of_common_friends(rj, i) == recommend_by_influence(rj, i):
        same_count += 1
        same_list.append(i)
    else : 
        diff_count += 1
        diff_list.append(i)
print("Total Same ",same_count, "They are: ",  same_list)
print("Total Different ",diff_count, "They are: ",  diff_list)
###
### Problem 5
###

# (Your Problem 5 code goes here.)
fb = open("./facebook-links.txt","r")

f_line = []
for line_of_text in fb:
    a = line_of_text.split('\t')
    f_line.append(a)
    
# print(f_line[1000][1])

facebook = nx.Graph()

# print(len(f_line))

for i in range(len(f_line)):
    # facebook.add_node(f_line[i][0])
    # facebook.add_node(f_line[i][1])
    facebook.add_edge(int(f_line[i][0]),int(f_line[i][1]))
    
#print(len(facebook.nodes()))

assert len(facebook.nodes()) == 63731
assert len(facebook.edges()) == 817090

#recommend_by_number_of_common_friends(facebook, 28000)[0:10]
###
### Problem 6
###
# (Your Problem 6 code goes here.)
for i in facebook:
    if int(i) % 1000 == 0:
        a = recommend_by_number_of_common_friends(facebook, i)
        print("Recommandation by Number of Common Friends for "
              ,i, " is ",a[0:10])

###
### Problem 7
###
# (Your Problem 7 code goes here.)
for i in facebook:
    if int(i) % 1000 == 0:
        b = recommend_by_influence(facebook, i)
        print("Recommandation by Influence Score for ",i, " is ",b[0:10])



###
### Problem 8
###
same_count=0
diff_count=0
for i in facebook:
    if int(i) % 1000 == 0:
        a = recommend_by_number_of_common_friends(facebook, i)
        b = recommend_by_influence(facebook, i)
        if a[0:10] == b[0:10]:
            same_count += 1
        else :
            diff_count += 1
print('Same: ',same_count)
print('Different: ',diff_count)
    


# (Your Problem 8 code goes here.)

###
### Collaboration
###

# ... Write your answer here, as a comment (on lines starting with "#").


