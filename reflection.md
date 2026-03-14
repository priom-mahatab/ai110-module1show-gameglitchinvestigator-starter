# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

- The New Game button was not functional. When I click New Game, the session does not reset.

### Broken Logic
- The hint would always tell to go lower no matter what. If the correct number was 50 and I guessed 32, it would tell me to go lower. Probably the hint is just a hardcoded print statement.

- The Score calculation seems off. I am not entirely sure how it is being calculated at the moment. It seems like it is deducting points even for quick wins. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - Copilot

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - Suggestion for fixing the hint when it is an incorrect guess. The AI suggested to change the conditionals and fix how it was coded. If the guess is < correct number, hint -> "Should be higher", else "Should be lower".

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - One misleading thing was how it was rendering the developer console. Even after entering a guess, the console would not immediately update. It would only update once another guess was entered. The AI initially suggested that the logic of the console was sound. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - I did a mix of manual testing and pytesting. For example, for the developer console fix, I just ran different numbers and observed the state of the console .
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - I ran pytests for the new win logic score counter. This test specifically checked the corrected formula for win points (100 - 10*(attempt_number - 1)), verifying that a 1st-attempt win gives 100 points, a 2nd gives 90, and so on. It passed, showing that the fix worked and the scoring is now fairer. 
- Did AI help you design or understand any tests? How?
  - Yes, Copilot helped me design the test_update_score_win test by suggesting the structure and assertions based on the fixed formula. It also guided me on how to verify edge cases, which improved my understanding of unit testing for scoring logic.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  - Honestly, looking back, the secret number shouldn't have kept changing in the original app—it was supposed to stay the same once generated, stored in session state, and only reset when you hit "New Game." But the app had all these intentional glitches (like converting the secret to a string on even attempts for comparison), which probably made the whole game feel unpredictable and buggy. Maybe it seemed like the secret was changing because the hints were wrong, or the scoring was weird, or the logic broke down in confusing ways, tricking you into thinking the number itself was shifting. 

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Streamlit is all about rerunning your entire Python script from top to bottom every time the user interacts with the app—like clicking a button or typing in a field. This means the order of your code is super important because anything that happens later in the script (like updating variables) won't affect the UI elements that were already "drawn" earlier. Session state is like a special persistent storage that sticks around between these reruns, so you can keep track of things like scores or game progress without losing them. I learned that if you update session state after displaying UI elements, those updates won't show up until the next rerun, which can make the app feel laggy or inconsistent. To fix that, you have to structure your code so logic runs before the displays that depend on it.

- What change did you make that finally gave the game a stable secret number?
  - he key change I made was removing the glitchy code that converted the secret to a string on even attempts for comparison. This ensured the guess-checking always used the correct integer secret consistently. I also fixed the attempt counter to start at 0 (instead of 1) and moved the UI updates (like the developer console) to happen after the logic runs, so changes show up immediately. This made the whole app feel more reliable, with the secret staying put as intended.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
  - I would spend more time manually fixing the code. Sometimes, AI can overfix and it would take me more time going over the changes than just fixing it myself. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - This project showed me that AI-generated code, while a great starting point, often contains subtle bugs or glitches that require human debugging and testing to make it reliable. It made me more cautious about trusting AI suggestions blindly and emphasized the importance of understanding the code myself before deploying it.

