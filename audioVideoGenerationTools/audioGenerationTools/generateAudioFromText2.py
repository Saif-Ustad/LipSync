import requests

ELEVENLABS_API_KEY = "sk_9058391bbf6672838ca20d382aed511d05bdc64cec5d06c6"

def text_to_speech_elevenlabs(text, output_audio_path="test_audio_elevenlabs.mp3", voice_id="vYENaCJHl4vFKNDYPr8y"):
    """
    Convert text to speech using ElevenLabs API with an Indian female accent.

    Args:
        text (str): The input text.
        output_audio_path (str): The output file path.
        voice_id (str): The ElevenLabs voice ID for an Indian female voice.
    """
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        # "model_id": "eleven_turbo_v2.5",  # Ensure correct model is used
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.8}
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        with open(output_audio_path, "wb") as f:
            f.write(response.content)
        print(f"Audio saved as {output_audio_path}")
    else:
        print("Error:", response.json())

# Example Usage
text = """ Namaste Mathangi! My name is Anika, and I’m here to guide you through managing your credit 
card dues. Mathangi, as of today, your credit card bill shows an amount due of INR 5,053 which 
needs to be paid by 31st December 2024 
Missing this payment could lead to two significant consequences: 
First, a late fee will be added to your outstanding balance. 
Second, your credit score will be negatively impacted, which may affect your future borrowing 
ability. 
Make your payment by clicking the link here... Pay through UPI or bank transfer. Thank you! """

text_to_speech_elevenlabs(text)
