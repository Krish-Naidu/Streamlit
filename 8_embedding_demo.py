# Import required libraries
import os
try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False
    print("google-generativeai not installed. Run: pip install google-generativeai")

def create_embedding_demo():
    """Demonstrate text embedding using Google's Gemini API"""
    
    if not GENAI_AVAILABLE:
        print("❌ google-generativeai package not available")
        return
    
    # Set up the Google API key
    try:
        # Try to get API key from environment variable first
        api_key = os.getenv('GOOGLE_API_KEY')
        
        # Configure the API
        genai.configure(api_key=api_key)
        print("✅ API configured successfully")
        
        # Text to create embedding for
        text_to_embed = "What is the meaning of life?"
        print(f"📝 Creating embedding for: '{text_to_embed}'")
        
        # Generate embedding using the correct method
        result = genai.embed_content(
            model="models/embedding-001",
            content=text_to_embed,
            task_type="retrieval_document"
        )
        
        # Display results
        print("🎉 Embedding generated successfully!")
        print(f"📊 Embedding dimensions: {len(result['embedding'])}")
        print(f"🔢 First values: {result['embedding']}")
        # print(f"🔢 Last values: {result['embedding']}")
        
        # Optional: Show some statistics about the embedding
        embedding = result['embedding']
        import statistics
        print(f"📈 Statistics:")
        print(f"   Mean: {statistics.mean(embedding):.6f}")
        print(f"   Min: {min(embedding):.6f}")
        print(f"   Max: {max(embedding):.6f}")
        
        return result['embedding']
        
    except Exception as e:
        print(f"❌ Error creating embedding: {str(e)}")
        print("\n🔧 Troubleshooting:")
        print("1. Make sure you have a valid Google API key")
        print("2. Get an API key from https://makersuite.google.com/app/apikey")
        print("3. Set GOOGLE_API_KEY environment variable or update the code")
        print("4. Make sure your API key has access to the Gemini API")
        print("5. Check your internet connection")
        return None

if __name__ == "__main__":
    print("🚀 Google Gemini Embedding Demo")
    print("=" * 40)
    
    embedding = create_embedding_demo()
    
    if embedding:
        print(f"\n✅ Success! Generated {len(embedding)}-dimensional embedding vector")
    else:
        print("\n❌ Failed to generate embedding")