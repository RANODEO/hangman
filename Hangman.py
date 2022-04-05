def hangman(word):
    wrong=0
    stages=["",
	"　　　ミ~￣￣￣＼ ",
	"　　　/ ＿＿＿＿亅",
	"　　 / ＞ ⌒　⌒｜",
	"　　｜/　(･) (･)｜",
	"　　(6――○-○-｜",
	"　　｜　　　つ　｜",
	"　　｜　　＿＿_)/ ",
	"　　 ＼　(＿／ /  ",
	"　　 ／＼＿＿／   ",
	"　　/　 ＼><∧    ",
	"　 / /”          ",	
            ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess 1 character!"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print(" You Won!!")
            print(" ".join(board))
            win = True
            break

    if not win:
            print("\n".join(stages[0:wrong+1]))
            print("You lost... Correct word is {}.".format(word))

hangman("cat")
