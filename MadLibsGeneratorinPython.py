def mad_libs():
    print("Let's play Mad Libs! Fill in the blanks below:")

    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")

    story = f"One day, a {adjective} {noun} decided to {verb} {adverb}. It was an unforgettable moment!"

    print("\nHere is your Mad Libs story:\n")
    print(story)

if __name__ == "__main__":
    mad_libs()
