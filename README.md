# BlackJack-SpringBreak-Project
Python OOP BlackJack Game implementation

This application was a month long project to design a continuous text-based BlackJack game, that allows a dynamic number of players and deck size. Due to the short development time, current elements of software design can be improved and I will continue to improve such over time (notes below go into more detail of these design choices and required ammendements).

Notes:

1. The dealer is a simple reflex agent designed with fundamental game strategy and without stategical inference. 
2. Split hand functionality is currently unoperational with development still underway (performing a split will result in an application error)
3. A view module has been implemented for this project, however, print to console commands are called within the controller of this program. This design will require change to ensure view and controller seperatation, however, the program is still functional. 
4. Player classes should be split into their own respective python files for better program futureproofing.

Any additional feedback is appreciated :)

