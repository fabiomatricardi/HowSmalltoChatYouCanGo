# Quyen Chat 4 ALL
### Aka, how SMALL can you go to build a GOOD Chatbot?

Repo of the code from the Medium article

Here the Streamilt Python app to run Quyen Mini that has 1.8 Billion parameters<br>
I am using here the quantized version that runs on CPU with llama-cpp-python

filename of the model: Quyen-Mini-v0.1.Q4_K_M.gguf

- HF repo: [https://huggingface.co/vilm/Quyen-Mini-v0.1-GGUF](https://huggingface.co/vilm/Quyen-Mini-v0.1-GGUF)
- HF GGUF file Url: [Quyen-Mini-v0.1.Q4_K_M.gguf](https://huggingface.co/vilm/Quyen-Mini-v0.1-GGUF/resolve/main/Quyen-Mini-v0.1.Q4_K_M.gguf)

Download the follwing files in the Project directory
- qMini_chat.py
- assistant.png
- user.png

create a subfolder where to pu the GGUF file called:
```
GGUFs
```

download the GGUF file there

Open the terminal and with the venv activated run this command:
```
streamlit run qMini_chat.py
```
