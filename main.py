print("\033[1;32;40m  \n")


#imports
import random
import time


#Variables
points = 0 
correct_answers = 0
wrong_answers = 0
rounds_played = 0
first_number = 0
second_number = 0


#functions, decoration
def question_creator():
  global first_number 
  global second_number
  if difficulty_levels == 1:
    first_number = random.randint(0,20) 
    second_number = random.randint(0,20)
  elif difficulty_levels == 2:
    first_number = random.randint(25,45)
    second_number = random.randint(25,45)
  elif difficulty_levels == 3:
    first_number = random.randint(50,100)
    second_number = random.randint(50,100)


def yes_no(question):
  valid = False
  global yes_no_answer
  while not valid:
    response = input(question).lower()
    if response == "yes" or response == "y":
      response = "yes"
      yes_no_answer = 1
      return response
    elif response == "no" or response == "n":
      response = "no"
      yes_no_answer = 0
      return response
    else:
      print("Please answer yes / no")


def statement_generator(statement, decoration):
  sides = decoration * 3
  statement = "{} {} {}".format(sides, statement,sides)
  top_bottom = decoration * len(statement)

  print(top_bottom)
  print(statement)
  print(top_bottom)

  return " "

def num_checker(question, low, high):
    error = "Please enter a whole number between 1 and 3"
    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if low <= response <= high:
                return response

            # output an error
            else:
              print(" ")
              statement_generator(error,"!")
              print(" ")

        except ValueError:
            print(" ")
            statement_generator(error,"!")
            print(" ")

def end_of_game():
  statement_generator("Final Points: {}".format(points), "◌")
  print(" ")
  time.sleep(0.5)
  statement_generator("rounds played: {}".format(rounds_played), "◌")
  print(" ")
  time.sleep(0.5)
  print("THANKS FOR PLAYING")