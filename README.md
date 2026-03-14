# AI-Powered Detailed Diagnostic Report (DDR) Generator

## Overview

This project implements an **AI-powered document analysis pipeline**
that automatically generates a **Detailed Diagnostic Report (DDR)** from
inspection and thermal imaging reports.

Inspection reports and thermal imaging reports often contain large
volumes of text, images, and observations. Manually consolidating these
documents into a structured diagnostic report can be time-consuming and
error-prone.

This system automates that process by:

-   Extracting **textual observations** from inspection and thermal
    reports
-   Extracting and filtering **relevant images**
-   Using an **LLM-based reasoning engine** to analyze findings
-   Producing a **structured client-ready DDR**

The final output is a **well-organized diagnostic report** that
summarizes property issues, observations, root causes, severity, and
recommended actions.

------------------------------------------------------------------------

# Key Features

### Automated Document Processing

The system processes **inspection reports and thermal imaging reports in
PDF format**, extracting both textual information and embedded images.

### Intelligent Image Filtering

PDFs often contain unnecessary graphical elements such as:

-   logos
-   icons
-   UI markers
-   duplicate images

The pipeline automatically removes irrelevant images using:

-   size filtering
-   aspect ratio filtering
-   file size filtering
-   duplicate detection via image hashing

This ensures that only **relevant inspection and thermal images** are
included in the final report.

### AI-Based Report Generation

The extracted information is analyzed using a **Large Language Model
(LLM)** to generate a structured **Detailed Diagnostic Report**.

The AI system:

-   merges information from multiple documents
-   avoids duplicate observations
-   highlights potential root causes
-   recommends corrective actions

### Structured Diagnostic Output

The generated report follows a professional DDR structure:

1.  Property Issue Summary\
2.  Area-wise Observations\
3.  Probable Root Cause\
4.  Severity Assessment (with reasoning)\
5.  Recommended Actions\
6.  Additional Notes\
7.  Missing or Unclear Information

Images extracted from the source documents are placed under the
**relevant observation sections** to improve clarity.

------------------------------------------------------------------------

# System Architecture

Inspection Report (PDF) Thermal Report (PDF) │ ▼ PDF Parsing (Text +
Image Extraction) │ ▼ Image Filtering (Remove logos, icons, markers,
duplicates) │ ▼ AI Analysis Engine (LLM reasoning) │ ▼ DDR Report
Generator │ ▼ Structured Diagnostic Report

------------------------------------------------------------------------

# Project Structure

    Urbanroof-DDR-AI/
    │
    ├── data/
    │   ├── inspection_report.pdf
    │   ├── thermal_report.pdf
    │
    ├── src/
    │   ├── pdf_parser.py
    │   ├── llm_analyzer.py
    │   └── ddr_generator.py
    │
    ├── output/
    │   ├── inspection_images/
    │   ├── thermal_images/
    │   └── final_ddr.html
    │
    ├── main.py
    ├── requirements.txt
    ├── README.md
    └── .gitignore

------------------------------------------------------------------------

# Technologies Used

  Technology                Purpose
  ------------------------- ------------------------------------
  Python                    Core programming language
  PyMuPDF (fitz)            PDF text and image extraction
  Groq API (Llama models)   AI reasoning and report generation
  Hashing (MD5)             Duplicate image detection
  HTML / Markdown           Report formatting

------------------------------------------------------------------------

# Image Processing Pipeline

PDF documents often contain many embedded images that are not relevant
to the diagnostic report.

The system filters images using multiple criteria:

### Size Filtering

Very small images (icons, markers) are removed.

    width < 200 OR height < 200 → discard

### File Size Filtering

Tiny embedded graphics are removed.

    file size < 15 KB → discard

### Aspect Ratio Filtering

Extreme aspect ratios (e.g., banner logos) are removed.

    ratio > 4 OR ratio < 0.25 → discard

### Duplicate Detection

Identical images embedded multiple times are removed using **MD5
hashing**.

This ensures that the final report contains **only relevant inspection
and thermal images**.

------------------------------------------------------------------------

# How to Run the Project

## 1. Install Dependencies

    pip install -r requirements.txt

## 2. Add API Key

Create a `.env` file in the root directory:

    GROQ_API_KEY=your_api_key_here

## 3. Add Input Reports

Place the following files in the `data/` folder:

    inspection_report.pdf
    thermal_report.pdf

## 4. Run the Pipeline

    python main.py

------------------------------------------------------------------------

# Output

The generated report will be saved in:

    output/final_ddr.html

The report contains:

-   structured diagnostic sections
-   relevant images
-   summarized observations
-   recommended actions

------------------------------------------------------------------------

# Limitations

-   Large documents must be truncated to stay within LLM token limits.
-   Image-to-observation matching currently relies on heuristic
    placement.
-   Complex PDF layouts may require additional preprocessing.

------------------------------------------------------------------------

# Future Improvements

Possible extensions include:

-   Vision models for **thermal image interpretation**
-   Improved **image-to-observation matching**
-   Semantic document chunking for **large reports**
-   Web interface for uploading reports
-   Automated **severity scoring models**

------------------------------------------------------------------------

# Author

Developed as part of an **AI system design assignment for an internship
opportunity**.
