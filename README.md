# code_2xploer_60day_challenge
60 days challenge
# Smart Playlist Intelligence System

## Student Details
Name: Vishnu Mattakoyya  
Register Number: AP24110011648  
Course: CSE205 – Hands on Python  
Department: Computer Science and Engineering  

---

## Project Description

This program analyzes a playlist represented as a list of song durations in seconds. The objective is to understand the listening pattern and categorize the playlist based on duration and repetition rules.

The system checks whether the playlist is balanced, repetitive, too short, too long, irregular, or invalid.

---

## Working Logic

First, the program checks for invalid entries.  
If any song duration is less than or equal to zero, the playlist is marked as invalid and analysis stops.

If the playlist is valid, the program calculates:

- Total duration of the playlist  
- Number of songs  

Then it applies the following checks:

- If total duration is less than 300 seconds → Too Short  
- If total duration is greater than 3600 seconds → Too Long  
- If any duration repeats → Repetitive  
- If durations are reasonable and no repetition exists → Balanced  
- Otherwise → Irregular  

---

## Output

The program displays:

- Total Duration  
- Number of Songs  
- Category of Playlist  
- Recommendation message  

---

## Learning Outcome

Through this challenge, I understood how to use lists, built-in functions like `len()` and `sum()`, and logical conditions to analyze real-world data. I also learned how to structure decision-based classification systems in Python.
