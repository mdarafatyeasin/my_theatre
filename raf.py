seats = {}

for i in range(5):
    seats[i] = [0] * 5

seats[2][2] = 1
seats[2][3] = 1

for i in seats:
    print (seats[i])
# print(seats)