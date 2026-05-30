import requests


# ==========================================
# REAL LLM ANALYSIS
# ==========================================

def ask_llm(question, df):

    try:

        # LIMIT DATA FOR AI
        sample_data = df.head(20).to_string()

        prompt = f"""
        You are an expert business analyst.

        Analyze the following business dataset.

        DATA:
        {sample_data}

        QUESTION:
        {question}

        Give:
        - direct answer
        - business explanation
        - recommendations
        """

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        result = response.json()

        return result["response"]

    except Exception as e:

        return f"LLM Error: {str(e)}"