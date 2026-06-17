# Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences.

## 1. What was broken when you started?

When I first ran the game, it looked like a normal number guessing game but was nearly impossible to win. The hints were completely backwards: when my guess was too high, the game said Go HIGHER instead of Go LOWER. The secret number also seemed to change between guesses because on even-numbered attempts the code converts the secret to a string, causing type mismatches. Additionally, Hard mode returns a range of 1-50, which is actually easier than Normal mode range of 1-100.

### Bug Reproduction Log

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess 60, secret is 42 (attempt 1) | Hint says Go LOWER | Hint says Go HIGHER (backwards) | Go HIGHER displayed |
| Guess 42, secret is 42 (attempt 2, even) | Win | No win, secret is converted to string so 42 != "42" | Game continues |
| Select Hard difficulty | Harder range than Normal | Range is 1-50, easier than Normal 1-100 | Sidebar shows Range: 1 to 50 |

## 2. How did you use AI as a teammate?

I used two AI tools throughout this project: Perplexity AI (Comet) and GitHub Copilot. I used Perplexity AI first to take control of my browser, set up the entire GitHub Codespace, read the app.py code, and identify all three bugs without me having to do anything manually. I then used GitHub Copilot inside the Codespace to get additional explanations of the check_guess function and the string conversion bug on even attempts. One thing I had to verify manually was the Hard difficulty bug, since neither AI flagged it automatically - I had to compare the three ranges myself.

## 3. Debugging and testing your fixes

To verify each bug, I traced through the code manually with specific inputs and compared expected versus actual behavior. For the hints bug, I simulated: secret=42, guess=60, so guess > secret is True, which hits the Too High branch returning Go HIGHER - but that tells the player to guess higher when they should go lower. I also reviewed the existing tests in the tests/ folder to see what was already covered. The string conversion bug was confirmed by reading the lines where secret is set to str(session_state.secret) on even attempts before passing to check_guess.

## 4. What did you learn about Streamlit and state?

I learned that Streamlit re-runs the entire script from top to bottom on every user interaction, which is very different from traditional web apps. This means regular Python variables reset on every interaction, so you must use st.session_state to persist data like the secret number, attempts, and score across clicks. The bug where the secret appeared to change was caused by intentional code that converted the secret to a string on even attempts, exploiting this re-run behavior. Understanding session state is essential to building any Streamlit app that tracks progress across multiple steps.

## 5. What would you do differently next time?

Next time I would read the full code carefully before running the app to form a mental model and spot logic errors before playing. I would also write a quick test script that calls check_guess with known inputs to immediately confirm whether hints are correct. I learned that AI tools like Copilot are great for explaining code, but you still need to think critically about whether the explanation matches expected behavior. Finally, I would check all edge cases like difficulty ranges and boundary conditions more systematically from the start.
