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
        QLearning.load()
    elif mode == 2:
        import QLearning
        QLearning.train()
    else:
        import chromedino