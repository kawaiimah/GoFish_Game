# GoFish_Game
Decided to code yet another game [Go Fish!](https://en.wikipedia.org/wiki/Go_Fish) as part of my learning journey into coding, enjoy!

## Coding Concepts
- Used a bunch of functions and lists to setup and shuffle the cards
- Also coded a bunch of functions for displaying the cards held by the player/computer, and to check for completed sets
- Managing player turn vs computer turn was a bit more complicated but applying the idea of a simple gamestate variable still works, just like my [TicTacToe_Game](https://github.com/kawaiimah/TicTacToe_Game)
- Deliberately incorporated a bit of time delay so that the computer pauses a bit instead of instanteously making decisions

## Notes
- There is a cheat (ahem, developer) code where player can see what cards the computer is holding.
- I tried out using the Secrets library rather than the Random library - it should be totally transparent for playing this casual game, but the same shuffling code should be re-usable if I have other future projects where I want to brute-force calculate probabilities by generating say billions of shuffled decks.
