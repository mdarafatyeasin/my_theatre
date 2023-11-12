class Star_Cinema:
    hall_list = []

    def entry_hall(self, row, col, hall_no):
        hall_instance = Hall(row, col, hall_no)
        return hall_instance 

class Hall:
    def __init__(self, row, col, hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.hall_row = row
        self.hall_col = col
        self.hall_no = hall_no

        Star_Cinema.hall_list.append(self)


    # entry show
    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.__show_list.append(show)

        totalSeat = {}
        for i in range(0, self.hall_row):
            totalSeat[i] = [0] * self.hall_col
        self.__seats[id] = totalSeat

    # book seats
    def book_seats(self, id, row, col):
        maxRow = self.hall_row
        maxCol = self.hall_col
        if 1 <= row <= maxRow and 1 <= col <= maxCol:
            if id in self.__seats:
                if self.__seats[id][row -1 ][col - 1] == 0:
                    print(f"Booking seat success.")
                    self.__seats[id][row - 1][col - 1] = 1
                else:
                    print(f"\nSeat is already booked.")
            else:
                print('\nWrong ID')
        else:
            print('\nInvalid Set position')
    # view show list
    def view_show_list(self):
        print('================================================')
        for show in self.__show_list:
            print(f'ID : {show[0]} | Movie Name : {show[1]} | Time : {show[2]}')
        print('================================================')

    # print all the seat
    def view_available_seats(self, id):
        print("\nAvailable Seats:")
        # print(self.seats)

        if id in self.__seats:
            seatAvl = self.__seats[id]
            # print(seatAvl)
            for i in seatAvl:
                print(seatAvl[i])
        else:
            print('Wrong show ID')



# Create an instance of Star_Cinema
booth = Star_Cinema()

# Call entry_hall method to add a hall to the hall_list
hall1 = booth.entry_hall(5, 5, 1)

# Set a show for the hall
hall1.entry_show(1, "Movie 1", "12:00 PM")
hall1.entry_show(5, "Movie 2", "3:00 PM")


while True:
    print('\n1. VIEW ALL SHOW TODY')
    print('2. VIEW AVAILABLE SEATS')
    print('3. BOOK TICKET')
    print('4. EXIT\n')

    op = int(input('ENTER OPTION: '))

    if op == 1:
        hall1.view_show_list()
    elif op == 2:
        id = int(input('ENTER SHOW ID: '))
        hall1.view_available_seats(id)
    elif op == 3:
        id = int(input('ENTER SHOW ID: '))
        row = int(input('ENTER ROW ID: '))
        col = int(input('ENTER COLUM ID: '))
        hall1.book_seats(id,row,col)
    elif op == 4:
        break




