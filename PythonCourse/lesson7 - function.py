def motivation():
    print("Never give up!")
    print("Every bug teaches you something.")
    print("Keep coding!")

motivation()
motivation()

def menu():
    print("======== MENU ========")
    print("")
    print("1. Play Game")
    print("")
    print("2. Settings")
    print("")
    print("3. Exit")
    print("")
    print("======================")

menu()

def introduce(name):
    print(f"Hello!, {name}!")
    print("Welcome to python!")

introduce("ross")

def dream(job):
    print("Your dream job is", job)
    print("Keep working toward it!")
    
dream("Cybersecurity Engineer")


def show_win(secret, attempts):
    print("====================")
    print("🎉 YOU WIN!")
    print("Secret Number:", secret)
    print("attempts: ",attempts)
    print("====================")

show_win(2,4)