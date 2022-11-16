'''Task
Given the names and grades for each student in a class of n students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
'''
records = [['chi', 20],['beta', 50],['alpha', 50]]

'''The ordered list of scores is [20,50], so the second lowest score is 50. 
There are two students with that score: ['beta','alpha']. Ordered alphabetically, the names are printed as: alpha beta
'''
Result =[]
scorelist = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Result+=[[name,score]]
        scorelist+=[score]
    b=sorted(list(set(scorelist)))[1]
    for a,c in sorted(Result):
        if c==b:
            print(a)