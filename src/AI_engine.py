from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_document_report(document_text, document_images):

    prompt = f"""
You are an intelligent document analysis system.

Analyze the following document and generate a structured report.

Document Content:
{document_text}

Generate:

# Document Analysis Report

## 1. Document Type
Identify what type of document this is.

## 2. Summary
Provide a concise summary.

## 3. Key Sections
List and describe important sections.

## 4. Important Insights
Highlight key findings.

## 5. Actionable Information (if applicable)

## 6. Missing or Unclear Information

If images are relevant, mention them.
If not available, write "Image Not Available".
"""

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return completion.choices[0].message.content