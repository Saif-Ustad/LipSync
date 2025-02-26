from google.cloud import texttospeech
import os

# Ensure the environment variable is set (for Windows users)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your-key.json"

def text_to_speech_google(text, output_audio_path="output_audio.mp3", language_code="en-IN", voice_name="en-IN-Wavenet-D"):
    """
    Convert text to speech using Google Wavenet with an Indian accent.

    Args:
        text (str): The input text.
        output_audio_path (str): The output file path.
        language_code (str): Language for speech synthesis (default: Indian English).
        voice_name (str): Voice model (default: Wavenet D for Indian accent).
    """
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code,
        name=voice_name,
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    with open(output_audio_path, "wb") as out:
        out.write(response.audio_content)
        print(f"✅ Audio saved as {output_audio_path}")

# Example Usage
text = """Namaste Mathangi! My name is Anika, and I’m here to guide you through managing your credit card dues..."""
text_to_speech_google(text, "test_audio_google.mp3")
