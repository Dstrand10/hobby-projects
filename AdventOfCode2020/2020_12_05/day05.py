class Seat:

    def __init__(self, input_data):
        self.seatID = None
        self.input_data = input_data
        self.calculate_seat_id()

    def calculate_seat_id(self):
        row_data = self.input_data[:7]
        seat_data = self.input_data[7:]

        row_id = range(0, 128)
        left_right_id = range(0, 8)
        for char in row_data:
            if char == "B":
                row_id = row_id[int(len(row_id) / 2):]
            elif char == "F":
                row_id = row_id[:int(len(row_id) / 2)]
            else:
                print("Unknown character or something else went wrong: " + char)
        for char in seat_data:
            if char == "L":
                left_right_id = left_right_id[:int(len(left_right_id) / 2)]
            elif char == "R":
                left_right_id = left_right_id[int(len(left_right_id) / 2):]
            else:
                print("Unknown character or something else went wrong: " + char)
        self.seatID = (row_id[0]) * 8 + left_right_id[0]


def sol2(seats):
    seat_ids = [seat.seatID for seat in seats]
    seat_ids.sort()
    for index, seatID in enumerate(seat_ids):
        if seat_ids[index + 1] - seatID > 1:
            return int((seat_ids[index + 1] + seatID) / 2)


def getSeats(input_data):
    seats = []
    for line in input_data:
        seat = Seat(line)
        seats.append(seat)
    return seats


def main():
    input_data = open("input.txt").read().split("\n")

    seats = getSeats(input_data)
    largest_seat_id = max([seat.seatID for seat in seats])
    print(f"Solution 1: {largest_seat_id}")

    my_seat = sol2(seats)
    print(f"Solution 2: {my_seat}")


if __name__ == "__main__":
    main()
