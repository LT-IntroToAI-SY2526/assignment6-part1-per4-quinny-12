# Assignment 6 Part 1 - Writeup

**Name:** Quinn Downey  
**Date:** 11/21/25

---

## Part 1: Understanding Your Model

### Question 1: R² Score Interpretation
What does the R² score tell you about your model? What does it mean if R² is close to 1? What if it's close to 0?

**YOUR ANSWER:**
R² measures how well the model explains the variance in the data, where close to 1 means strong predictive power and close to 0 means the model barely explains the relationship.

---

### Question 2: Mean Squared Error (MSE)
What does the MSE (Mean Squared Error) mean in plain English? Why do you think we square the errors instead of just taking the average of the errors?

**YOUR ANSWER:**
MSE is the average of squared differences between predicted and actual values; we square errors to penalize larger errors more heavily and eliminate negative values that would cancel out.

---

### Question 3: Model Reliability
Would you trust this model to predict a score for a student who studied 10 hours? Why or why not? Consider:
- What's the maximum hours in your dataset?
- What happens when you make predictions outside the range of your training data?

**YOUR ANSWER:**
I would be somewhat cautious since the maximum hours in the dataset is 9.6, and extrapolating beyond the training data range can produce unreliable predictions that don't follow the actual relationship.

---

## Part 2: Data Analysis

### Question 4: Relationship Description
Looking at your scatter plot, describe the relationship between hours studied and test scores. Is it:
- Strong or weak?
- Linear or non-linear?
- Positive or negative?

**YOUR ANSWER:**
The relationship is strong, linear, and positive, showing that more study hours consistently correlate with higher test scores.

---

### Question 5: Real-World Limitations
What are some real-world factors that could affect test scores that this model doesn't account for? List at least 3 factors.

**YOUR ANSWER:**
1. Prior knowledge or natural aptitude in the subject
2. Quality of study methods and learning environment/motivation
3. Sleep quality, stress levels, and overall health on test day

---

## Part 3: Code Reflection

### Question 6: Train/Test Split
Why do we split our data into training and testing sets? What would happen if we trained and tested on the same data?

**YOUR ANSWER:**
We split data to evaluate how well the model generalizes to new data; testing on training data would give artificially high performance metrics that don't reflect real-world accuracy.

---

### Question 7: Most Challenging Part
What was the most challenging part of this assignment for you? How did you overcome it (or what help do you still need)?

**YOUR ANSWER:**
The most challenging part was understanding all the functions from libraries such as pandas, since I was unfamiliar with these libraries.

---

## Part 4: Extending Your Learning

### Question 8: Future Applications
Describe one real-world problem you could solve with linear regression. What would be your:
- **Feature (X):** 
- **Target (Y):** 
- **Why this relationship might be linear:**

**YOUR ANSWER:**
I could predict a pitcher's ERA based on their strikeout rate (K/9), where higher strikeout rates linearly correlate with lower ERAs since preventing batters from putting the ball in play reduces runs scored.

---

## Grading Checklist (for your reference)

Before submitting, make sure you have:
- [x] Completed all functions in `a6_part1.py`
- [x] Generated and saved `scatter_plot.png`
- [x] Generated and saved `predictions_plot.png`
- [x] Answered all questions in this writeup with thoughtful responses
- [ ] Pushed all files to GitHub (code, plots, and this writeup)
