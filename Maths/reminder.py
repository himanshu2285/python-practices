def ask_ok(prompt, retries=4, reminder="Please try again!"):
    while True:
        reply=input(prompt)
        if reply in {'yes', 'y', 'ye'}:
            return True
        if reply in {'no', 'n','not', 'nope'}:
            return False
        retries -= 1
        if retries < 0:
            raise ValueError("invalid user response")  

        print(reminder)