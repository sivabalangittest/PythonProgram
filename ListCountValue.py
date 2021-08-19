# Will count the True values in the list
class CountValuesInList:
    def __init__(self, input_list):
        self.input_list = input_list

    def count_values(self):
        count = 0

        for value in self.input_list:
            if value == 'True':
                count += 1

        print("The no.of True values in the list is " + str(count))


list1 = CountValuesInList(['True', 'False', 'True', 'True', 'False', 'True'])
list1.count_values()

