# Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences.

## 1. What was broken when you started?

When I first ran the game, it looked like a normal number guessing game but was nearly impossible to win. The hints were completely backwards: when my guess was too high, the game said Go HIGHER instead of Go LOWER. The secret number also seemed to change between guesses because on even-numbered attempts the code converted the secret to a string, causing type mismatches. Additionally, Hard mode returned a range of 1-50, which was actually easier than Normal mode range of 1-100.

### Bug Reproduction Log

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess 60, secret is 42 (attempt 1) | Hint says Go LOWER | Hint says Go HIGHER (backwards) | Go HIGHER displayed |
| Guess 42, secret is 42 (attempt 2, even) | Win | No win, secret is converted to string so 42 != "42" | Game continues |
| Select Hard difficulty | Harder range than Normal | Range is 1-50, easier than Normal 1-100 | Sidebar shows Range: 1 to 50 |

## 2. How did you use AI as a teammate?

I used Perplexity AI, GitHub Copilot, and Codex as teammates at different stages. I also wanted to try Claude AI because CodePath offers access to it, but I did not understand the difference between Opus and Sonnet at first. While working on my CodePath CYB101 project, I used Opus too much and ran through my credits because I later learned it is the highest-usage option. For this project, Perplexity helped me understand the assignment flow and identify the first set of bugs, Copilot helped explain the `check_guess` logic inside the Codespace, and Codex helped finish the repair by comparing the documentation to the real code, moving the logic into `logic_utils.py`, and expanding the pytest tests. One misleading AI result I had to correct was documentation that claimed tests had been generated even though the saved test output still showed failures.

## 3. Debugging and testing your fixes

To verify each bug, I traced through the code manually with specific inputs and compared expected versus actual behavior. For the hints bug, I simulated: secret=42, guess=60, so guess > secret is True, and the fixed code now returns `Too High` with `Go LOWER!`. I added tests for the win case, high/low hints, string secret conversion, Hard difficulty range, decimal input, and score behavior. I ran `python -m pytest` and confirmed that all 7 tests passed.

## 4. What did you learn about Streamlit and state?

I learned that Streamlit re-runs the entire script from top to bottom on every user interaction, which is very different from traditional web apps. This means regular Python variables reset on every interaction, so you must use st.session_state to persist data like the secret number, attempts, and score across clicks. The bug where the secret appeared to change was caused by intentional code that converted the secret to a string on even attempts, exploiting this re-run behavior. Understanding session state is essential to building any Streamlit app that tracks progress across multiple steps.

## 5. What would you do differently next time?

Next time I would read the full code carefully before running the app to form a mental model and spot logic errors before playing. I would also write a quick test script that calls check_guess with known inputs to immediately confirm whether hints are correct. I learned that AI tools like Copilot are great for explaining code, but you still need to think critically about whether the explanation matches expected behavior. Finally, I would check all edge cases like difficulty ranges and boundary conditions more systematically from the start.
