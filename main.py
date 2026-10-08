def calculate_sum(scores):
    return sum(scores)


def calculate_average(scores):
    return sum(scores) / len(scores)


def calculate_maximum(scores):
    return max(scores)


def calculate_minimum(scores):
    return min(scores)


def main():
    scores_input = input("Enter scores separated by spaces: ")

    try:
        scores = [float(score) for score in scores_input.split()]
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    if len(scores) == 0:
        print("No scores entered.")
        return

    total = calculate_sum(scores)
    average = calculate_average(scores)
    maximum = calculate_maximum(scores)
    minimum = calculate_minimum(scores)

    print("\n--- Score Results ---")
    print(f"Scores: {scores}")
    print(f"Sum: {total:g}")
    print(f"Average: {average:.2f}")
    print(f"Maximum: {maximum:g}")
    print(f"Minimum: {minimum:g}")


if __name__ == "__main__":
    main()