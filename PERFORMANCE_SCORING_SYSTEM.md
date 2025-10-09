# 🎯 Performance-Based Scoring System

## Overview

The app now awards points based on **performance quality**, not just completion. Students earn more points for impressive, accurate answers.

---

## 📊 Scoring System by Module

### 1. Speaking Module (Current Implementation)

**Points Range:** 5-15 points

**Scoring Logic:**
```python
# Excellent Performance (15 points)
- Similarity >= 80% AND Sentiment rating >= 4
- Clear pronunciation, good pace, natural expression

# Good Performance (12 points)  
- Similarity >= 60% OR Sentiment rating >= 3
- Decent pronunciation, acceptable pace

# Basic Performance (10 points)
- Similarity >= 50%
- Completed the task

# Poor Performance (5-8 points)
- Similarity < 50%
- Needs improvement
```

**AI Analysis:**
- ✅ Speech-to-text accuracy
- ✅ Sentiment analysis (emotion, confidence)
- ✅ Word matching with original text
- ✅ Pronunciation quality

---

### 2. Listening Module (NEEDS UPDATE)

**Current:** Fixed 10 points
**New:** 3-10 points based on answer accuracy

**Proposed Scoring:**
```python
# Perfect Answer (10 points)
- All questions answered correctly
- 100% accuracy

# Good Answer (7-9 points)
- 70-99% questions correct
- Minor mistakes

# Average Answer (5-6 points)
- 50-69% questions correct
- Several mistakes

# Poor Answer (3-4 points)
- < 50% questions correct
- Needs improvement
```

**Implementation Needed:**
```python
def calculate_listening_points(total_questions, correct_answers):
    accuracy = (correct_answers / total_questions) * 100
    
    if accuracy == 100:
        return 10  # Perfect!
    elif accuracy >= 90:
        return 9   # Excellent
    elif accuracy >= 80:
        return 8   # Very Good
    elif accuracy >= 70:
        return 7   # Good
    elif accuracy >= 60:
        return 6   # Above Average
    elif accuracy >= 50:
        return 5   # Average
    else:
        return max(3, int(accuracy / 10))  # Minimum 3 points
```

---

### 3. Writing Module (NEEDS UPDATE)

**Current:** 10-15 points (first poster bonus)
**New:** 5-15 points based on quality + AI analysis

**Proposed Scoring:**
```python
# Exceptional Writing (15 points)
- First poster from department (bonus)
- OR AI rates content as excellent
- Clear, well-structured, meaningful

# Excellent Writing (12-14 points)
- AI rates as very good
- Good grammar, structure, creativity

# Good Writing (9-11 points)
- AI rates as good
- Acceptable quality

# Basic Writing (6-8 points)
- AI rates as average
- Meets minimum requirements

# Poor Writing (5 points)
- AI rates as needs improvement
- Minimal effort
```

**AI Analysis Needed:**
```python
def analyze_writing_quality(text):
    # Use Gemini AI to analyze:
    # 1. Grammar and spelling
    # 2. Creativity and originality
    # 3. Coherence and structure
    # 4. Relevance to topic
    # 5. Length and depth
    
    # Return score: 1-5
    # Convert to points: score * 3 = 3-15 points
```

---

### 4. Observation Module (NEEDS MAJOR UPDATE)

**Current:** Fixed 10 points
**New:** 3-15 points based on answer quality + AI verification

**Proposed Scoring:**
```python
# Outstanding Answers (15 points)
- All answers correct AND detailed
- AI verifies high quality responses
- Shows deep understanding

# Excellent Answers (12-14 points)
- All answers correct
- Good detail and explanation
- AI verifies accuracy

# Good Answers (9-11 points)
- 80-99% correct
- Adequate explanation
- Minor issues

# Average Answers (6-8 points)
- 60-79% correct
- Basic understanding shown

# Poor Answers (3-5 points)
- < 60% correct
- Needs improvement
```

**AI Verification Needed:**
```python
def verify_observation_answer(question, student_answer, correct_answer):
    """
    Use Gemini AI to:
    1. Compare student answer with correct answer
    2. Check for semantic similarity (not just exact match)
    3. Evaluate explanation quality
    4. Rate answer: 0-100%
    """
    
    prompt = f"""
    Question: {question}
    Correct Answer: {correct_answer}
    Student Answer: {student_answer}
    
    Evaluate the student's answer:
    1. Is it factually correct?
    2. Does it show understanding?
    3. Is it well-explained?
    
    Rate 0-100 and provide brief feedback.
    """
    
    # Get AI response
    # Return: score (0-100), feedback (string)
```

---

## 🎯 Implementation Plan

### Step 1: Update Speaking Module (DONE ✅)
- Already has performance-based scoring
- Uses AI sentiment analysis
- Awards 5-15 points based on quality

### Step 2: Update Listening Module
**File:** `app.py` - listening submission route

**Changes Needed:**
```python
@app.route('/listening/<int:content_id>/submit', methods=['POST'])
def submit_listening(content_id):
    # Get answers
    student_answers = request.form.getlist('answers')
    correct_answers = get_correct_answers(content_id)
    
    # Calculate accuracy
    correct_count = sum(1 for s, c in zip(student_answers, correct_answers) if s == c)
    total_questions = len(correct_answers)
    accuracy = (correct_count / total_questions) * 100
    
    # Award points based on accuracy
    points_earned = calculate_listening_points(total_questions, correct_count)
    
    # Save with score
    save_completion('listening', content_id, accuracy, points_earned)
```

### Step 3: Update Writing Module
**File:** `app.py` - writing submission route

**Changes Needed:**
```python
@app.route('/writing/submit', methods=['POST'])
def submit_writing():
    essay_text = request.form['essay']
    
    # AI quality analysis
    quality_score = analyze_writing_with_ai(essay_text)
    
    # Base points from quality (5-12)
    points_earned = 5 + int(quality_score * 7 / 5)
    
    # Bonus for first poster
    if is_first_today():
        points_earned += 3
    
    # Cap at 15
    points_earned = min(15, points_earned)
    
    save_completion('writing', topic_id, quality_score * 20, points_earned)
```

### Step 4: Update Observation Module
**File:** `app.py` - observation submission route

**Changes Needed:**
```python
@app.route('/observation/<int:content_id>/submit', methods=['POST'])
def submit_observation(content_id):
    # Get student answers
    answers = request.form.getlist('answers')
    questions = get_questions(content_id)
    
    total_score = 0
    feedback_list = []
    
    # AI verification for each answer
    for i, (question, student_answer) in enumerate(zip(questions, answers)):
        score, feedback = verify_answer_with_ai(
            question['text'],
            student_answer,
            question['correct_answer']
        )
        total_score += score
        feedback_list.append(feedback)
    
    # Calculate average score
    avg_score = total_score / len(questions)
    
    # Award points based on quality
    if avg_score >= 95:
        points_earned = 15  # Outstanding
    elif avg_score >= 85:
        points_earned = 13  # Excellent
    elif avg_score >= 75:
        points_earned = 11  # Good
    elif avg_score >= 65:
        points_earned = 9   # Above Average
    elif avg_score >= 50:
        points_earned = 7   # Average
    else:
        points_earned = max(3, int(avg_score / 10))
    
    save_completion('observation', content_id, avg_score, points_earned)
    
    return jsonify({
        'points': points_earned,
        'score': avg_score,
        'feedback': feedback_list
    })
```

---

## 🤖 AI Integration for Observation Module

### Gemini AI Function:
```python
from gemini import analyze_sentiment  # Existing
# Add new function:

def verify_observation_answer(question, student_answer, correct_answer):
    """
    Use Gemini AI to verify observation answers
    """
    import google.generativeai as genai
    
    try:
        model = genai.GenerativeModel('gemini-pro')
        
        prompt = f"""
You are an English teacher evaluating a student's answer.

Question: {question}
Expected Answer: {correct_answer}
Student's Answer: {student_answer}

Evaluate the student's answer on a scale of 0-100:
- 100: Perfect answer, shows complete understanding
- 80-99: Excellent answer, minor issues
- 60-79: Good answer, some mistakes
- 40-59: Average answer, needs improvement
- 0-39: Poor answer, incorrect understanding

Provide:
1. Score (0-100)
2. Brief feedback (1 sentence)

Format: SCORE|FEEDBACK
Example: 85|Excellent answer with good explanation, minor grammar issue.
"""
        
        response = model.generate_content(prompt)
        result = response.text.strip()
        
        # Parse response
        parts = result.split('|')
        score = int(parts[0])
        feedback = parts[1] if len(parts) > 1 else "Good effort!"
        
        return score, feedback
        
    except Exception as e:
        # Fallback: simple string matching
        if student_answer.lower().strip() == correct_answer.lower().strip():
            return 100, "Correct answer!"
        elif correct_answer.lower() in student_answer.lower():
            return 70, "Partially correct."
        else:
            return 30, "Please review the content."
```

---

## 📊 Points Summary Table

| Module | Min Points | Max Points | Based On |
|--------|-----------|-----------|----------|
| **Speaking** | 5 | 15 | Similarity + Sentiment (AI) |
| **Listening** | 3 | 10 | Answer accuracy |
| **Writing** | 5 | 15 | Quality (AI) + First poster bonus |
| **Observation** | 3 | 15 | Answer quality (AI verified) |

---

## 🎯 Benefits

### For Students:
✅ **Fair scoring** - Effort and quality rewarded
✅ **Motivation** - Strive for higher scores
✅ **Clear feedback** - Know what to improve
✅ **Skill development** - Focus on quality over quantity

### For Teachers:
✅ **Accurate assessment** - AI-powered evaluation
✅ **Less manual grading** - Automated scoring
✅ **Better insights** - See student performance levels
✅ **Objective grading** - Consistent standards

---

## 🚀 Next Steps

1. **Update `gemini.py`** - Add `verify_observation_answer()` function
2. **Update `app.py`** - Modify all submission routes
3. **Update templates** - Show score breakdown to students
4. **Test thoroughly** - Verify AI scoring accuracy
5. **Deploy** - Roll out to production

---

## 📝 Code Files to Modify

1. **`gemini.py`** - Add AI verification function
2. **`app.py`** - Update routes:
   - `/listening/<id>/submit`
   - `/writing/submit`
   - `/observation/<id>/submit`
3. **Templates** - Update result displays:
   - `listening_practice.html`
   - `writing.html`
   - `observation_practice.html`

---

**This performance-based system ensures students are rewarded fairly based on their actual performance and understanding!** 🎯
