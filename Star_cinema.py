class Star_Cinema:
    __hall_list = []

    def entry_hall(self):
        Star_Cinema.__hall_list.append(self)


class Hall(Star_Cinema):
    def __init__(self, hall_no, rows, colm) -> None:
        self.hall_no = hall_no
        self.rows = rows
        self.colm = colm
        self.seats = {}
        self.__show_list = []
        self.entry_hall()

    def entry_show(self, id, movie_name, time):
        self.__show_list.append((id, movie_name, time))
        self.seats[id] = [[0 for i in range(self.colm)] for j in range(self.rows)]

    def book_seats(self, id, seat_list):
        for row, col in seat_list:
            self.seats[id][row][col] = 1

    def view_show_list(self):
        for id, movie_name, time in self.__show_list:
            print(f'Id: {id}, Movie name: {movie_name}, Show time: {time}')

    def view_available_seats(self, id):

        for row in range(self.rows):
            for col in range(self.colm):
                if self.seats[id][row][col] == 0:
                    print(f'seat{row,col}',end=", ")
            print()

        print()
        for val in self.seats[id]:
            print(val)


MegaHall = Hall(11, 4, 5)

MegaHall.entry_show(123, 'Fun', '10.00 am')
MegaHall.entry_show(124, 'Frustration', '02.00 pm')
MegaHall.entry_show(125, 'Fateh', '07.00 pm')

run = True

while run:

    print('\nOptions: \n')

    print('1 : View Show List')
    print('2 : View Available Seats')
    print('3 : Book Seats')
    print('4 : Exit')

    choice = int(input('\n\tEnter Option: '))
    print('\n')

    if choice == 1:
        MegaHall.view_show_list()

    elif choice == 2:
        id = None
        while True:
            id = int(input('\tEnter show id: '))
            print()
            if id in MegaHall.seats:
                MegaHall.view_available_seats(id)
                break

            print('\nPlease, Enter a valid id !')

    elif choice == 3:
        id = None
        while True:
            id = int(input('\tEnter show id: '))
            if id in MegaHall.seats:
                break
            
            print('\nPlease, Enter a valid id !')

        seat_count = int(input('\tEnter How many seats you want: '))
        seat_list = []

        for i in range(seat_count):
            row = None
            colm = None
            while True:
                row, colm = map(int, input('\tEnter row, colm: ').split())
                if 0 <= row < MegaHall.rows and 0 <= colm < MegaHall.colm:
                    if MegaHall.seats[id][row][colm] == 0:
                        seat_list.append((row, colm))
                        break

                    print('\nThe seat is Already booked !')
                    print('Please, Enter valid row, colm !')
                    
                else:
                    print('\nPlease, Enter valid row, colm !')
            
        MegaHall.book_seats(id, seat_list)

    elif choice == 4:
        break

    else:
        print('Please, Enter a Valid Option !')