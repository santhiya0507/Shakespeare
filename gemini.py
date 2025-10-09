import json
import logging
import os

from google import genai
from google.genai import types
from pydantic import BaseModel


# IMPORTANT: KEEP THIS COMMENT
# Follow these instructions when using this blueprint:
# - Note that the newest Gemini model series is "gemini-2.5-flash" or gemini-2.5-pro"
#   - do not change this unless explicitly requested by the user
# - Sometimes the google genai SDK has occasional type errors. You might need to run to validate, at time.  
# The SDK was recently renamed from google-generativeai to google-genai. This file reflects the new name and the new APIs.

# This API key is from Gemini Developer API Key, not vertex AI API Key
client = genai.Client(api_key="AIzaSyB32kRLOKH9QaJtv-Obg0TXIO1lRZD3UoE")


def summarize_article(text: str) -> str:
    prompt = f"Please summarize the following text concisely while maintaining key points:\n\n{text}"

    response = client.models.generate_content(model="gemini-2.5-flash",
                                              contents=prompt)

    return response.text or "SOMETHING WENT WRONG"


class Sentiment(BaseModel):
    rating: int
    confidence: float


def analyze_sentiment(text: str) -> Sentiment:
    try:
        system_prompt = (
            "You are a communication analysis expert for the Shakespeare Club Communication App. "
            "Analyze the communication quality of the text and provide a rating "
            "from 1 to 5 stars and a confidence score between 0 and 1. "
            "Consider clarity, grammar, expression, and communication effectiveness. "
            "Respond with JSON in this format: "
            "{'rating': number, 'confidence': number}")

        response = client.models.generate_content(
            model="gemini-2.5-pro",
            contents=[
                types.Content(role="user", parts=[types.Part(text=text)])
            ],
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                response_mime_type="application/json",
                response_schema=Sentiment,
            ),
        )

        raw_json = response.text
        logging.info(f"Raw JSON: {raw_json}")

        if raw_json:
            data = json.loads(raw_json)
            return Sentiment(**data)
        else:
            raise ValueError("Empty response from model")

    except Exception as e:
        raise Exception(f"Failed to analyze sentiment: {e}")


def analyze_communication_practice(text: str, practice_type: str) -> str:
    """Analyze communication practice submission using Gemini AI"""
    try:
        prompt = f"""
        As an expert in communication analysis for the Shakespeare Club Communication App,
        analyze this {practice_type} practice submission:

        {text}

        Provide detailed feedback focusing on:
        1. Communication clarity and effectiveness
        2. Grammar and language usage
        3. Expression and articulation
        4. Specific areas for improvement
        5. Strengths demonstrated

        Give a comprehensive analysis that will help the student improve their communication skills.
        """

        response = client.models.generate_content(model="gemini-2.5-flash",
                                                  contents=prompt)

        return response.text or "Analysis could not be completed"

    except Exception as e:
        return f"Error in communication analysis: {str(e)}"


class AnswerEvaluation(BaseModel):
    score: int  # 0-100
    feedback: str
    is_correct: bool


def verify_observation_answer(question: str, student_answer: str, correct_answer: str) -> AnswerEvaluation:
    """
    Use Gemini AI to verify and score observation module answers
    Compares student answer with correct answer and provides detailed feedback
    """
    try:
        system_prompt = (
            "You are an English teacher evaluating student answers for the Shakespeare Club app. "
            "Compare the student's answer with the correct answer and evaluate it. "
            "Consider semantic similarity, not just exact matching. "
            "Score from 0-100 where: "
            "100 = Perfect answer with complete understanding, "
            "80-99 = Excellent answer with minor issues, "
            "60-79 = Good answer with some mistakes, "
            "40-59 = Average answer needing improvement, "
            "0-39 = Poor answer with incorrect understanding. "
            "Provide brief, encouraging feedback (1-2 sentences)."
        )

        prompt = f"""
Question: {question}
Expected Answer: {correct_answer}
Student's Answer: {student_answer}

Evaluate the student's answer and provide:
1. score: 0-100 based on accuracy and understanding
2. feedback: Brief, constructive feedback (1-2 sentences)
3. is_correct: true if score >= 60, false otherwise
"""

        response = client.models.generate_content(
            model="gemini-2.5-pro",
            contents=[types.Content(role="user", parts=[types.Part(text=prompt)])],
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                response_mime_type="application/json",
                response_schema=AnswerEvaluation,
            ),
        )

        raw_json = response.text
        if raw_json:
            data = json.loads(raw_json)
            return AnswerEvaluation(**data)
        else:
            raise ValueError("Empty response from model")

    except Exception as e:
        # Fallback: simple string matching
        student_lower = student_answer.lower().strip()
        correct_lower = correct_answer.lower().strip()
        
        if student_lower == correct_lower:
            return AnswerEvaluation(score=100, feedback="Correct answer!", is_correct=True)
        elif correct_lower in student_lower or student_lower in correct_lower:
            return AnswerEvaluation(score=70, feedback="Good answer with minor differences.", is_correct=True)
        else:
            return AnswerEvaluation(score=30, feedback="Please review the content and try again.", is_correct=False)


class WritingEvaluation(BaseModel):
    score: int  # 1-5 stars
    feedback: str
    strengths: str
    improvements: str


def evaluate_writing_quality(text: str, topic: str = "") -> WritingEvaluation:
    """
    Use Gemini AI to evaluate writing quality for the writing module
    Returns score (1-5), feedback, strengths, and areas for improvement
    """
    try:
        system_prompt = (
            "You are an English teacher evaluating student writing for the Shakespeare Club app. "
            "Evaluate the writing quality on a scale of 1-5 stars where: "
            "5 = Exceptional writing (excellent grammar, creativity, structure, depth), "
            "4 = Very good writing (strong quality with minor issues), "
            "3 = Good writing (acceptable quality, some improvements needed), "
            "2 = Fair writing (needs significant improvement), "
            "1 = Poor writing (major issues with grammar, structure, or content). "
            "Provide encouraging, constructive feedback."
        )

        topic_text = f"Topic: {topic}\n\n" if topic else ""
        prompt = f"""
{topic_text}Student's Writing:
{text}

Evaluate this writing and provide:
1. score: 1-5 stars based on overall quality
2. feedback: Brief overall assessment (2-3 sentences)
3. strengths: What the student did well (1-2 sentences)
4. improvements: Specific areas to improve (1-2 sentences)
"""

        response = client.models.generate_content(
            model="gemini-2.5-pro",
            contents=[types.Content(role="user", parts=[types.Part(text=prompt)])],
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                response_mime_type="application/json",
                response_schema=WritingEvaluation,
            ),
        )

        raw_json = response.text
        if raw_json:
            data = json.loads(raw_json)
            return WritingEvaluation(**data)
        else:
            raise ValueError("Empty response from model")

    except Exception as e:
        # Fallback: basic evaluation
        word_count = len(text.split())
        if word_count >= 100:
            score = 4
            feedback = "Good effort with substantial content."
        elif word_count >= 50:
            score = 3
            feedback = "Acceptable writing, could be more detailed."
        else:
            score = 2
            feedback = "Try to write more to fully express your ideas."
        
        return WritingEvaluation(
            score=score,
            feedback=feedback,
            strengths="You completed the assignment.",
            improvements="Consider adding more detail and examples."
        )