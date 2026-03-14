from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_ddr_report(
    inspection_text,
    thermal_text,
    inspection_images=None,
    thermal_images=None
):

    inspection_images = inspection_images or []
    thermal_images = thermal_images or []

    prompt = f"""
    You are a professional building diagnostics expert.

    You are given summarized inspection and thermal findings.

    Inspection Findings:
    {inspection_text}

    Thermal Findings:
    {thermal_text}

    Generate a structured Detailed Diagnostic Report (DDR).

    The report MUST contain:

    1. Property Issue Summary
    2. Area-wise Observations
    3. Probable Root Cause
    4. Severity Assessment (with reasoning)
    5. Recommended Actions
    6. Additional Notes
    7. Missing or Unclear Information

    Rules:
    - Do NOT invent facts.
    - If information is missing write "Not Available".
    - If an image is expected but missing write "Image Not Available".
    """

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return completion.choices[0].message.content