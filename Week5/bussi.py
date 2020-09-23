"""
COMP.CS.100 Programming 1
Hang Nguyen, hang.t.nguyen@tuni.fi, student id K429778
5.6.2: Bus Time Table
"""

def main():
    bus_schedule = [630, 1015, 1415, 1620, 1720, 2000]
    user_time = int(input("Enter the time (as an integer): "))
    print("The next buses leave: ")
    length=len(bus_schedule)

    i = 0
    while bus_schedule[i] < user_time:
      i += 1
      if i == length:
          break

    for j in range (0, 3):
      print(bus_schedule[(i+j)%length])

if __name__ == "__main__":
    main()