# Hangman Game
This is a simple hangman game for beginners trying to learn python. I have tried to keep
it as simply as possible.
# Sample output
Here is some sample output from my game.
```
__ ____ ___________ 

 you have 10 guesses left
guess a letter> W
your guess was correct
w_ ____ ___________ 

 you have 10 guesses left
guess a letter> e
your guess was correct
we ___e ___________ 

 you have 10 guesses left
guess a letter> m
your guess was correct
we ___e ______mm___ 

 you have 10 guesses left
guess a letter> ^CTraceback (most recent call last):
  File "/home/eulerthedestroyer/coding/hangman/main.py", line 46, in <module>
    main()
  File "/home/eulerthedestroyer/coding/hangman/main.py", line 22, in main
    userGuess = input("guess a letter> ").lower()
KeyboardInterrupt
eulerthedestroyer@penguin:~/coding/hangman$ ^C
eulerthedestroyer@penguin:~/coding/hangman$ ^C
eulerthedestroyer@penguin:~/coding/hangman$ ^C
eulerthedestroyer@penguin:~/coding/hangman$ ^C
eulerthedestroyer@penguin:~/coding/hangman$ ^C
eulerthedestroyer@penguin:~/coding/hangman$ ^C
eulerthedestroyer@penguin:~/coding/hangman$ ^C
eulerthedestroyer@penguin:~/coding/hangman$ ^C
eulerthedestroyer@penguin:~/coding/hangman$ ^C
eulerthedestroyer@penguin:~/coding/hangman$ ^C
eulerthedestroyer@penguin:~/coding/hangman$ ^C
eulerthedestroyer@penguin:~/coding/hangman$ ^C
eulerthedestroyer@penguin:~/coding/hangman$ /usr/bin/python3 /home/eulerthedestroyer/coding/hangman/main.py
__ ____ ___________ 

 you have 10 guesses left
guess a letter> g
your guess was correct
__ ____ ___g______g 

 you have 10 guesses left
guess a letter> e
your guess was correct
_e ___e ___g______g 

 you have 10 guesses left
guess a letter> d
your guess was incorrect
_e ___e ___g______g 

 you have 9 guesses left
guess a letter> f
your guess was incorrect
_e ___e ___g______g 

 you have 8 guesses left
guess a letter> v
your guess was correct
_e __ve ___g______g 

 you have 8 guesses left
guess a letter> g
you already guessed that letter
_e __ve ___g______g 

 you have 8 guesses left
guess a letter> a
your guess was correct
_e __ve ___g_a____g 

 you have 8 guesses left
guess a letter> w
your guess was correct
we __ve ___g_a____g 

 you have 8 guesses left
guess a letter> l
your guess was correct
we l_ve ___g_a____g 

 you have 8 guesses left
guess a letter> y
your guess was incorrect
we l_ve ___g_a____g 

 you have 7 guesses left
guess a letter> h
your guess was incorrect
we l_ve ___g_a____g 

 you have 6 guesses left
guess a letter> o
your guess was correct
we love __og_a____g 

 you have 6 guesses left
guess a letter> p
your guess was correct
we love p_og_a____g 

 you have 6 guesses left
guess a letter> r
your guess was correct
we love progra____g 

 you have 6 guesses left
guess a letter> x
your guess was incorrect
we love progra____g 

 you have 5 guesses left
guess a letter> b
your guess was incorrect
we love progra____g 

 you have 4 guesses left
guess a letter> n
your guess was correct
we love progra___ng 

 you have 4 guesses left
guess a letter> m
your guess was correct
we love programm_ng 

 you have 4 guesses left
guess a letter> i
your guess was correct
you won
```