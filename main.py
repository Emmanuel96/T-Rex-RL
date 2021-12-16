if __name__ == "__main__":
    # Mode selection
    print("Possible modes:\n1. Watch a pre-trained model\n2. Watch a new model train\n3. Play the game yourself")
    try:
        mode = int(input("What mode would you like to choose? "))
    except:
        raise Exception("Not a valid mode, please try again")
    if 1 > mode or 3 < mode:
        raise Exception("Not a valid mode, please try again")
    
    if mode == 1:
        import QLearning
        try:
            n = int(input("How many episodes would you like to see? "))
        except:
            raise Exception("Must be a positive integer, please try again")
        if 1 > n:
            raise Exception("Must be a positive integer, please try again")
        QLearning.load(n)
    elif mode == 2:
        try:
            n = int(input("How many steps of training would you like the model to take (minimum recommendation: 100000)? "))
        except:
            raise Exception("Must be a positive integer, please try again")
        if 1 > n:
            raise Exception("Must be a positive integer, please try again")
        import QLearning
        QLearning.train()
    else:
        import chromedino