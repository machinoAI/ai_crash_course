
# use second hand in analog clock to print between 1 to 12 (only digits)
# Stop the clock by pressing keyboard if it stopped at:
# [1,5,7,11] give 30 points
# [2,4,8,10] give 20 points
# [3,6,9,12] give 10 points
# Maximum three turns
# Enter player name, N players ca be added.
# To exist the game press n and continue y

from time import sleep

def clock_game():
    print("Press `Enter` to continue and `Ctrl+C` to stop the second hand")

    points_table = {}
    name = input("Enter the player name: ")

    attempts = 1
    points = 0

    while True:

        for digit in range(1, 13):
            try:
                print(digit)
                sleep(0.2)

            except KeyboardInterrupt:

                if digit in [1, 5, 7, 11]:
                    points += 30
                elif digit in [2, 4, 8, 10]:
                    points += 20
                else:
                    points += 10

                attempts += 1
                print(f"{name} has scored: {points}")

                if attempts == 4:
                    print(f"{name} has scored: {points}")
                    points_table[name] = points

                    ans = input("Is there any other player (y/n)? ").lower()

                    if ans == "y":
                        name = input("Enter the player name: ")
                        attempts = 1
                        points = 0
                        continue
                    else:
                        print("\nFinal Scores:")
                        print(points_table)
                        return

clock_game()