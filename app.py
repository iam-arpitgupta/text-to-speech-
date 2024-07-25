import numpy as np
import torch
import torchaudio
import ChatTTS
from IPython.display import audio
import openai
import requests

ollama_api_key = 'llama3'
ollama_client = openai.OpenAI(api_key=ollama_api_key,base_url=)

def ollama_chat(user_query):
    response = ollama.client.chat.completions.create(
        model = 'llama3',
        messages = [
            {'role':'user','content':user_query}
        ],
        temperature = 1,
        max_tokens = 2000,
    )
    return response.choice[0],message.content

def generate_control_prompt(text):
    prompt = f"""
you are an AI assistant and add more natural emotions to the text for text to speech synthesis
Given the following text:
{text}
please add the suitable emotions tokens [uv_break] and [laugh][uv_break] wherer it is suitable to specch more natural and 
expressive.

You can ONLY use : [uv_break] and [laugh]

examples:
1. "i sucked a big [uv_break]banana, [laugh][uv_break] yeah i said it 

"""
    return prompt

chat = ChatTTS.chat()
chat.load_models(compile=False) #true for better performance
inputs_en = ollama_chat("say hello to everyone and make fun of you developer")

answer = generate_control_prompt(input_en)
answer1 = ollama_chat(answer)

print(answer1)

params_refine_text = {
    'prompt':'[oral_2][laugh_7][break_4]'
}

modified_text = answer1
texts = [modified_text]

wavs = chat.infer(texts,params_refine_text=params_refine_text)
torchaudio.save("output",torch.from_numpy(wavs[0],24000))


