def print_table():
    numbers = [[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10],
               [113, 124, 135, 146, 15],
               [16, 17, 18, 19, 20],
               [211, 222, 233, 244, 255]]
    
    for row in range (5):
        #printing the top border
        if row == 0:
            print("+----+----+----+----+----+")

        separator = "|"
        #every row, it will loop 5 times
        for column in range (5):
            separator += f"{numbers[row][column]:4}|"
        print(separator)

        #printing the bottom border
        print("+----+----+----+----+----+")

print_table()