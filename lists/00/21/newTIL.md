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

If you finished the [previous project](http://www.reddit.com/r/beginnerprojects/comments/1i951e/project_compare_recent_karma/) which compared the karma of two new comments, hopefully you learned a thing or two about receiving data from Reddit's API.  Now you're going to take this a step further, and even have the opportunity to make a basic twitter bot.

**Goal**

Create a program that receives data from the /r/todayilearned subreddit, and looks for new facts that have been posted.  Each time the program comes across a new fact, the fact should be printed into the command line.  However, phrases like "TIL ", "TIL that", etc should be removed so the only thing that is printed is the fact.

[>>New TIL API data here<<](http://www.reddit.com/r/todayilearned/new/.json)

There are a couple things to note about this since you'll more than likely be using a loop to check for new posts.  According to [Reddit's API Access Rules Page](https://github.com/reddit/reddit/wiki/API), the API pages are only updated once every thirty seconds, so you'll have to have your code pause for at least thirty seconds before it tries to find more posts.  Secondly, if for some reason you decide to try to get data sooner than every thirty seconds, make sure to not send more than thirty requests per minute.  That is the maximum you are allowed to do.

**Subgoal Ideas**

There is actually a lot you can do once your program starts receiving facts.  Instead of simply printing the facts, here are some ideas for what you can do with them.  If you currently do not feel like you can accomplish these ideas, feel free to come back later when you have more experience.

* Print the link to the source of the fact too.

* Try to further clean up the fact by adding punctuation to the end if it is missing, capitalize the first word, etc.

* Write the facts to a separate text file so you end up with a giant compilation of random facts.

* Create a bot that posts the facts to twitter.  This may sound hard, but it's actually pretty simple by using the "[Python Twitter Tools](https://pypi.python.org/pypi/twitter)" module and following the guide [posted here](http://wilsonericn.wordpress.com/2011/08/22/tweeting-in-python-the-easy-way/).  Remember, the maximum amount of characters you can use in a tweet is only 140, so you'll have to filter out facts that are longer than that.

By now you should be pretty familiar with python, so if you get ideas for improving your program, go for it!)
