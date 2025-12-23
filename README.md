# PROMPT GUARD SECBERT

PROMPT GUARD SECBERT is a security-focused NLP model built on top of BERT to detect prompt injection, jailbreak attempts, and unsafe prompts in Large Language Model (LLM) applications.

It is designed for AI safety, enterprise LLM deployments, and production security pipelines.

## 🔐 Problem Overview

Modern LLM applications are vulnerable to:
- Prompt injection attacks
- Jailbreak attempts
- Unsafe or malicious user prompts

These attacks can bypass system instructions, leak sensitive information, and produce unsafe outputs.

PROMPT GUARD SECBERT provides an automated defense layer by classifying user prompts before they reach an LLM.

## 🚀 Key Features

- BERT-based text-classification model
- Detects safe vs malicious prompts
- Covers multiple attack categories
- Hugging Face–ready training & inference
- Modular, production-grade codebase
- Apache-2.0 licensed

## 🧠 Model Details

Model Name: PROMPT GUARD SECBERT  
Base Architecture: BERT (Sequence Classification)  
Pipeline Tag: text-classification  
Task: Prompt security classification  

Supported Classes:
safe, jailbreak, injection, unsafe

## 📜 License

Apache License 2.0
