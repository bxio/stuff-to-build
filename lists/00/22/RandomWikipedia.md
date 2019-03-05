[**BACKGROUND INFORMATION**

If you do not know how 21 (AKA Blackjack) is played, reading the  first couple of paragraphs of this [wikipedia article](http://en.wikipedia.org/wiki/Blackjack) may be beneficial.

**MAIN GOAL**

In this project, you will make a game similar to 21/blackjack.  Since this is not an actual game (as far as I'm aware of), here the the instructions for how to play.

> In this version, there is only one player, and there are two types of scores - the round score and the game score.  The game score will begin at 100, and the game will last for five rounds.

> At the beginning of the round, the player is given two random cards from a deck and they will be added together to make the player's round score.  From here, the player has two options - draw another card to try to get their round score closer to 21, or they can end the round.  The player can draw as many cards as they want until they end the round or their round score exceeds 21.

> At the end of the round, the difference between 21 and the round score is subtracted from the game score, and then the next round begins.  After the five rounds, the player is given their total score and the game is over.

---Other Information About The Game---

* Aces are only worth 1.

* If a player busts, 21 is subtracted from their total score.

* All face cards are worth 10.

So the point of your program is to allow the user to play the game described above.  Many of the subgoals listed below can be added to shine up the game.

**SUBGOALS**

1.  At the beginning of each round, print the round number (1 to 5).

2.  Since this is a text base game, tell the user what is happening.  For example, tell him/her when he/she draws a card, the name of the card, when they bust, etc.

3.  Create a ranking system at the end of the game and tell the user their rank.  For example, if the player finishes with 50-59 points they get an F, 60-69 is a D, 70-79 is a C, 80-89 is a B, and 90-100 is an A.

4.  At the end of each round, print out the user's total score.

5.  This may be the hardest part of the project, depending on how you wrote it.  Make sure the deck has 4 of each type of card, and then remove cards as they are drawn.  At the end of each round, make the deck have all of the cards again.
](**Background**

If you've been to Wikipedia, you may have noticed that there is a link to a random article on the left side of the screen.  While it can be fun to see what article you get taken to, sometimes it would be nice to see the name of the article so you can skip it if it sounds boring.  Luckily, Wikipedia has an API that allows us to do so ([Click here](http://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json)).

However, there is a dilemma.  Since Wikipedia has articles about topics from all over the world, some of them have special characters in the title.  For example, the article about the spanish painter [Erasto Cortés Juárez](http://en.wikipedia.org/wiki/Erasto_Cort%C3%A9s_Ju%C3%A1rez) has é and á in it.  If you look at this [specific article's API](http://en.wikipedia.org/w/api.php?action=query&prop=info&pageids=39608394&inprop=url&format=json), you will see that the title is "Erasto Cort\u00e9s Ju\u00e1rez" and that the \u00e9 and \u00e1 are replacing the two previously mentioned letters. (For information about what this is, start by checking out the first half of [this page](http://docs.python.org/2/howto/unicode.html) in the documentation).  To make your program work, you're going to have to handle this problem somehow.

**Goal**

Create a program that pulls titles from the official Wikipedia API and then asks the user one by one if he or she would like to read about that article.  So if the first title is Reddit, then the program should ask something along the lines of "Would you like to read about Reddit?"  If the user says yes, then the program should open up the article for the user to read.

HINT: Mouse over the hidden area below to see how the article's ID can be used to access the actual article.
[http://en.wikipedia.org/wiki?curid=39608394](/spoiler)

**Subgoals**

* As mentioned before, do something about the possibility of unicode appearing in the title.  Whether you want your program to simply filter out these articles or you want to actually turn the codes into readable characters, that's up to you.

* Make the program pause once the user has selected an article to read, and allow him or her to continue browsing different article titles once finished reading.

* Allow the user to simply press ENTER to be asked about a new article.)
