#!/usr/bin/env python3
"""Quick test to verify Gemini API is working."""

import os
from dotenv import load_dotenv

load_dotenv()

try:
    import google.generativeai as genai
    
    api_key = os.getenv("GEMINI_API_KEY")
    print(f"API Key found: {bool(api_key)}")
    print(f"API Key (first 10 chars): {api_key[:10] if api_key else 'N/A'}")
    
    if api_key:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        response = model.generate_content("Write a one-sentence argument for banning cars in cities.")
        print(f"\nResponse: {response.text}")
        print("\n✅ Gemini API is working!")
    else:
        print("\n❌ No API key found")
        
except Exception as e:
    print(f"\n❌ Error: {e}")
