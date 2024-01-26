import operator

def person_lister(f):
    def inner(people):

        from operator import itemgetter

        from itertools import groupby
        

        people.sort(key=operator.itemgetter(2, -1))

        y = groupby(people, itemgetter(2))

        # print(y)
        # for items in people:
        #     print(items)
        
        return (f(i) for i in people)
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')