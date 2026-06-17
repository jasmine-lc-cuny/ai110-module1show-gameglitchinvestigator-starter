# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**
I asked GitHub Copilot (inside the Codespace) to analyze the full `app.py` file, identify all logic bugs, and explain why the hints were showing the wrong direction when a player guessed too high or too low.

**What did the agent do?**
Copilot read through the `check_guess` function and correctly identified that the hint messages were swapped - the `Too High` branch returned `Go HIGHER!` and the `Too Low` branch returned `Go LOWER!`, which is backwards. It also traced through the even-attempt string conversion issue where `secret = str(st.session_state.secret)` caused integer-to-string comparison failures, explaining that `42 != "42"` in Python.

**What did you have to verify or fix manually?**
I had to manually compare the three difficulty range values (`Easy: 1-20`, `Normal: 1-100`, `Hard: 1-50`) to catch that Hard mode was actually easier than Normal mode. Copilot did not flag this automatically because it only saw each branch in isolation, not the relative comparison between them.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Guess exactly equals secret on an even-numbered attempt (string conversion bug) | "Write a pytest test for check_guess where the guess equals the secret but secret is passed as a string instead of an integer" | `assert check_guess(42, "42") == ("Win", "Correct!")` | No - returned `Too Low` instead of Win | This confirmed the type mismatch bug. When secret is a string, `42 == "42"` is False in Python, so the win condition is never triggered on even attempts |
| Guess is higher than secret but hint says Go Higher (backwards hint bug) | "Write a test to check that when guess is greater than secret, the hint tells the player to go lower" | `assert check_guess(60, 42)[1] == "Go LOWER!"` | No - returned `Go HIGHER!` | This proved the hint logic is reversed. The `if guess > secret` branch incorrectly returns the Go HIGHER message |
| Hard difficulty range is harder than Normal | "Write a test that verifies get_range_for_difficulty returns a wider range for Hard than for Normal" | `assert get_range_for_difficulty("Hard")[1] > get_range_for_difficulty("Normal")[1]` | No - Hard returns 50, Normal returns 100 | Hard mode (1-50) has a smaller range than Normal (1-100), making it easier, not harder |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**
```
Review this Python code for style issues, unused variables, and any PEP8 violations. Suggest improvements to make it cleaner and more Pythonic.
```

**Linting output before:**
```
W0611: Unused import (random imported but used only in one branch)
C0301: Line too long (83 > 79 characters) in check_guess function
R1705: Unnecessary elif after return in get_range_for_difficulty
W0612: Unused variable 'g' assigned but only used in one branch of except block
```

**Changes applied:**
Copilot suggested replacing the chained `if/elif` in `get_range_for_difficulty` with a dictionary lookup for cleaner code. It also suggested combining the `try/except` branches in `check_guess` into a single comparison using `int()` conversion upfront rather than catching `TypeError` after the fact. I reviewed both suggestions and agreed the dictionary approach was cleaner, but kept the try/except for now since changing it could introduce new bugs.

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:** "Look at this Python function `check_guess(guess, secret)`. The hints are backwards - when guess is too high it says Go HIGHER, and when guess is too low it says Go LOWER. Explain why this is happening and suggest a fix."

| | Model A | Model B |
|---|---|---|
| **Model name** | GitHub Copilot (GPT-4o) | ChatGPT (GPT-4o mini) |
| **Response summary** | Immediately identified that the return values in the `if guess > secret` and `else` branches were swapped. Provided a corrected version of the function with the messages switched and explained that `Too High` should tell the player to go lower, not higher. | Identified the same bug but spent more time re-explaining the game logic before getting to the fix. Also suggested adding input validation to make sure the guess is always an integer before comparing. |
| **More Pythonic?** | Yes - suggested using a match/case statement (Python 3.10+) for cleaner branching | No - kept the same if/else structure but added type hints |
| **Clearer explanation?** | Yes - got straight to the point with a concise before/after code block | Less concise - gave a longer narrative explanation before showing the fix |

**Which did you prefer and why?**
I preferred GitHub Copilot because it was faster and more direct - it showed me the exact lines to change without unnecessary explanation. However, ChatGPT's suggestion to add input validation upfront (converting guess to int before the comparison) was actually a better long-term fix that would prevent the type mismatch bug on even attempts as well. In the future I would use both: Copilot for quick fixes and ChatGPT for thinking through edge cases.
