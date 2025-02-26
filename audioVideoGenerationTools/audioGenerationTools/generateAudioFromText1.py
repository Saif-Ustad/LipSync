from gtts import gTTS
import os

def text_to_speech(text, output_audio_path="output_audio.mp3", lang="en"):
    """
    Convert text to speech and save as an audio file.

    Args:
        text (str): The input text to convert to speech.
        output_audio_path (str): The file path to save the generated audio.
        lang (str): The language for speech synthesis (default: English).
    """
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(output_audio_path)
    print(f"Audio saved as {output_audio_path}")

# Example Usage
text = """ Namaste Mathangi! My name is Anika, and I’m here to guide you through managing your credit 
card dues. Mathangi, as of today, your credit card bill shows an amount due of INR 5,053 which needs to be paid by 31st December 2024 
Missing this payment could lead to two significant consequences: 
First, a late fee will be added to your outstanding balance. 
Second, your credit score will be negatively impacted, which may affect your future borrowing 
ability. 
Make your payment by clicking the link here... Pay through UPI or bank transfer. Thank you! """

text_to_speech(text, "best_audio.mp3")

# Play the audio (optional)
# os.system("mpg321 test_audio.mp3")  # Linux/macOS
# os.system("start test_audio.mp3")  # Windows
