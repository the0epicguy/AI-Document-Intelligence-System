# AI Document Intelligence System

## Overview

This project implements an AI-powered document intelligence pipeline
capable of analyzing arbitrary PDF documents and generating structured,
human-readable reports.

The system extracts text and images, filters noise, and uses a Large
Language Model (LLM) to generate meaningful insights.

------------------------------------------------------------------------

## Key Features

-   General-purpose PDF processing (any document type)
-   Text and image extraction using PyMuPDF
-   Intelligent image filtering (size, ratio, duplicates)
-   AI-powered analysis using Groq (Llama models)
-   Structured report generation (HTML + Markdown)
-   Multi-document support

------------------------------------------------------------------------

## System Architecture

PDF(s) ↓ Text + Image Extraction ↓ Image Filtering & Deduplication ↓ AI
Analysis (LLM) ↓ Structured Report Generation

------------------------------------------------------------------------

## Project Structure

Urbanroof/ ├── data/ ├── output/ │ ├── images/ │ ├── final_report.md │
└── final_report.html ├── src/ │ ├── document_parser.py │ ├──
AI_engine.py │ └── ddr_generator.py ├── main.py ├── requirements.txt └──
README.md

------------------------------------------------------------------------

## Setup

pip install -r requirements.txt

Create a .env file:

GROQ_API_KEY=your_api_key_here

------------------------------------------------------------------------

## Run

python main.py

------------------------------------------------------------------------

## Output

output/final_report.html

------------------------------------------------------------------------

## Limitations

-   Token limits for large documents
-   Heuristic image matching
-   Complex PDFs may reduce accuracy

------------------------------------------------------------------------

## Future Improvements

-   RAG-based processing
-   Better image-text alignment
-   Web interface

------------------------------------------------------------------------

## Author

AI Document Analysis Project
