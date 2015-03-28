# Simple qcm program

import random
import sys

choice = None

# Questions du qcm
questions = [('What is the average latency with OVP?', '10us'),
             ('What is the maximum throughput we can reach with AVP?', 'Line rate'),
             ('In OpenStack, what is Nova in charge of?','Compute'),
             ('In OpenStack, Horizon is for the...?', 'gui'),
             ('Most famous cloud solution is?', 'Amazon')]

# List of already asked questions
# We will store the question's id
qcache = [] 

NB_QUESTIONS = len(questions)
NB_WORDS = len(questions[0]) - 1

#
# Query yes or no
#
def query_yes_no(question, default="yes"):
    """ Ask a yes/no question via input() and return the answer.
    "Question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning an answer
        is required of the user)
    The "answer" return value is one of "y":"yes", "ye":"yes", "no":None)
    """
    valid = {"yes":"yes", "y":"yes", "ye":"yes",
            "no":"no", "n":"no"}
    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("Invalid default answer: '%s'" % default)
        
    while 1:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return default
        elif choice in valid.keys():
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "\
                             "(or 'y' or 'n').\n")


#
# Pick the question at random 
#
def select_question_id():
    """Will pick a question at random"""
    # generate random numbers 1 - 6
    question_nb = random.randint(1, NB_QUESTIONS-1)
    return question_nb

#
# Ask the question once chosen
#
def ask_question(question_id):
    """Ask the question to the student"""
    print("What is the correct answer?")
    for i in range(0, NB_WORDS):
        print(i, ") ", questions[question_id][i])
    return None

#
# Main meny
#
while choice != "0":
    print(
    """
    Q&A
    
    0 - Exit
    1 - Start the test
    2 - Create a test
    """
    )
    
    choice = input("What is your choice? ")
    print()
    
    # Quit
    if choice == "0":
        print("Bye!")
    # Start a new test     
    elif choice == "1":
        print("We start the test\n")
        score = 0
        nb_of_questions = int(input("How many questions do you want? "))
 
        for i in range(0, nb_of_questions):
            # Pick a question...
            question_id = select_question_id()
            while question_id in qcache:
                question_id = select_question_id()
            qcache.append(question_id)
            print("Cache content: ", qcache)
            
            # Ask the question
            print("Here is question #", question_id)
            ask_question(question_id)
            
            # Wait for the user's answer
            answer = input("What is your answer? ")
            print("The right answer is ", questions[question_id][1])
            
            # Rate the answer
            answer = query_yes_no("Do you consider the answer is correct?")
            print("You answered %s" % answer)
            if answer == "yes":
                score += 1
        
        print("You final score is %d/%d" % (score,nb_of_questions))
                         
    # Créer un qcm
    elif choice == "2":
        print("Créer un qcm : pas encore implémenté")
    # Choix inconnu
    else:
        print("Désolé mais le choix ", choice, "n'est pas disponible.")
        
input("\n\nAppuyer sur la toucher entrer pour quitter.")


#
# TODO
#
# 1) Get rid of the questions in the program and store them in an XML file
#