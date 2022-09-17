import random
import Levenshtein as lev


def DNA_Create():
    chars = ['A', 'G', 'T', 'C']
    string1 = ""
    for i in range(0, 6):
        string1 += random.choice(chars)
    return string1


def First_Data():
    lst = []
    for i in range(0, 30):
        lst.append(DNA_Create())
    return lst


def Print_list(lst):
    for i in lst:
        print(i)


def Print_Teams(lst):
    for i in range(len(lst)):
        print("Team : ", i+1)
        Print_list(lst[i])
        print("\n")


def Team(data):
    team = []
    for i in range(0, 10):
        team.append(random.choice(data))
    return team


def Second_Data(data):
    lst = []
    for i in range(0, 10):
        team1 = Team(data)
        lst.append(team1)
    return lst


def Levenshtein_Calculation(team):
    score = 0
    for i in range(0, (len(team) - 1)):
        for j in range(i + 1, len(team)):
            distance = (lev.distance(team[i], team[j]))
            if distance <= 1:
                score += 1
    return score


def Best_Group(lst):
    max_score = 0
    max_index = 0
    for i in range(len(lst)):
        if max_score < Levenshtein_Calculation(lst[i]):
            max_score = Levenshtein_Calculation(lst[i])
            max_index = i
    return lst[max_index]


def New_List(best_group):
    lst = []
    for i in range(10):
        lst.append(best_group[:])
    return lst


def List_Replace(lst, data):
    for i in range(len(lst)):
        Replace(lst[i], data)
    return lst


def Replace(best_team, data):
    best_team[random.randint(0, len(best_team) - 1)] = random.choice(data)
    return best_team


def Loop(lst, data):
    rounds = 0
    for i in range(100):
        rounds += 1
        best_g = Best_Group(lst)
        sum1 = Levenshtein_Calculation(best_g)
        if sum1 < 45:
            lst = New_List(best_g)
            lst = List_Replace(lst, data)
        else:
            print("Total Rounds : ", i)
            print("The Best Group : ")
            Print_list(best_g)
            break
        if rounds == 100:
            print(" We have reached 100 rounds ")


def Run():
    print("First Data :")
    data = First_Data()
    Print_list(data)
    print("\nSecond Data :  ")
    print("--------------------")
    lst = Second_Data(data)
    Print_Teams(lst)
    best_g = Best_Group(lst)
    print("-" * 30, "\nBest group:")
    Print_list(best_g)
    lst = New_List(best_g)
    print("\n")
    Loop(lst, data)


Run()