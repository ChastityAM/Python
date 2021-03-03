#Given participants score sheet for University, find the runner up score
#You're given n scores, store them in a list and find the score of the
#runner up.
list_of_numbers = [2, 3, 6, 6, 5]
print(sorted(list(set(list_of_numbers)))[-2])

#or
list2 = [2, 3, 6, 6, 5]
def second_place(list2):
    list2.sort(reverse=True)

    first_place_score = list2[0]

    for elem in list2:
        if elem < first_place_score:
            return_string = "Congrats for second place with score of {}".format(elem)
            return return_string
print(second_place(list2))

