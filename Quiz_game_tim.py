print("Welcome to my Quiz game")
score = 0

playing = input(print("Want to play? >>"))

if playing.lower() != "yes":
    quit()
print("Okay, let's start the game!")

answer = input("What does SEO stands for? >>")
if answer.lower() == "search engine optimization":
    print("Right Answer")
    score += 1
else:
    print("Wrong Answer. You Failed")

answer = input("What does CPU stands for? >>")
if answer.lower() == "central processing unit":
    print("Right Answer")
    score += 1
else:
    print("Wrong Answer. You Failed")

answer = input("What does GPU stands for? >>")
if answer.lower() == "graphics processing unit":
    print("Right Answer")
    score += 1
else:
    print("Wrong Answer. You Failed")

answer = input("What does RAM stands for? >>")
if answer.lower() == "random access memory":
    print("Right Answer")
    score += 1
else:
    print("Wrong Answer. You Failed")

print(f"You got {score} cool points")
print(f"You got {(score / 4) * 100} %  ")