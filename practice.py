import random


def load_verbs(filename):
    with open(filename) as file:
        lines = file.read().split("\n")
        output = []
        for line in lines:
            tenses = [tense.strip() for tense in line.split(",")]
            output.append(tenses)
        return output


def practice(verbs_matrix):
    last_input = None
    checkmark = "\033[92m\u2713\033[0m"
    while last_input != "exit":
        infinitive, imperfectum, perfectum, english = random.sample(verbs_matrix, 1)[0]
        print(f"{infinitive.upper()} ({english})\n")
        last_input = input()
        try:
            in_imperfectum, in_perfectum = [s.strip() for s in last_input.split(",")]
            imperfectum_correct = in_imperfectum == imperfectum
            perfectum_correct = in_perfectum == perfectum
            if imperfectum_correct and perfectum_correct:
                print(f"{checkmark}, {checkmark}")
            elif imperfectum_correct and not perfectum_correct:
                print(f"{checkmark}, {perfectum}")
            elif not imperfectum_correct and perfectum_correct:
                print(f"{imperfectum}, {checkmark}")
            else:
                print(f"{imperfectum}, {perfectum}")
        except Exception:
            pass
        print("\n\n")


if __name__ == "__main__":
    verbs = load_verbs("frequent_verbs.txt")
    practice(verbs)
