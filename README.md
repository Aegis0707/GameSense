## GameSense
A project meant to enhance a gamer's intuition and improve their gameplay. Uses a mix of OpenCV, a trained computer vision model, and an LLM to show mistakes and suggest improvement. Currently not working on this until I better understand computer vision.

**Goals:**

* Analyze clips using a custom OpenCV Model that can detect enemies, current position, and anything specific to the game. (i.e THE FINALS with elemental barrels, Battlefield with openings caused by destrution, or Hero Shooters with ability charge.
* Uses pre-trained clips that can determine right/wrong plays. For example, if they correctly use cover, then it will be highlighted as a good play. If they run out of cover recklessly, it's labelled as a bad play.
* At the end of the clip, use an LLM to generate a summary on what the user has done right, done wrong, and any recommendations for improvement (i.e: use cover more often, pick less battles when in a survival shooter, etc.)

**Advanced Goals:**

* Analyze audio to get directional input on enemies attempting to flank or anything out of view.
* Get the user's input on their playstyle and factor that in when reviewing their gameplay.
* Add support for a variety of FPS games.
* Add Support for fighting games like Street Fighter 6 or Tekken, which would review different parts of gameplay such as spacing and aggression.


**Note: Temporarlily Not Working On This.**
Due to not knowing much about the code behind how these advanced programs like OpenCV work, I decided to put off on this project until I learn enough about such modules so that I can confidently go back.
