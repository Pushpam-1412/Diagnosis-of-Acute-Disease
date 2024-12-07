from transformers import BertTokenizer, BertForMaskedLM
import whisper

# Load Whisper model for speech-to-text
whisper_model = whisper.load_model("large")  # 'large' offers better accuracy for Indian languages

# Load mBERT model and tokenizer for text translation
bert_model_name = "bert-base-multilingual-cased"  # mBERT multilingual model
bert_model = BertForMaskedLM.from_pretrained(bert_model_name)
bert_tokenizer = BertTokenizer.from_pretrained(bert_model_name)

# Function to translate text using mBERT
def translate_text(input_text, source_lang, target_lang):
    # (Placeholder function - mBERT typically used for embeddings or masked predictions)
    # For translation, consider using mBART instead, as mBERT isn't specialized for direct translation.
    return f"Translated ({source_lang} to {target_lang}): {input_text}"

# Function to transcribe and translate speech using Whisper
def process_speech(audio_path, target_lang="en"):
    result = whisper_model.transcribe(audio_path, task="translate")
    return result["text"]

# Main function to handle user input
def process_input(input_type, content, source_lang=None, target_lang="en"):
    if input_type == "text":
        # Text translation using mBERT (or replace with mBART for translation)
        translated = translate_text(content, source_lang, target_lang)
        print("Translated Text:", translated)
    elif input_type == "audio":
        # Speech-to-text and translation using Whisper
        translated = process_speech(content, target_lang)
        print("Translated Speech:", translated)
    else:
        print("Invalid input type! Use 'text' or 'audio'.")