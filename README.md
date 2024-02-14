<img src="https://github.com/fabiomatricardi/HowSmalltoChatYouCanGo/raw/main/QuyenChat-github.png" width=800>

# The Future in Your Hands: Build Your Custom AI Conversation Partner - Quyen Chat 4 ALL
### Don’t just read about AI, build your own! A step-by-step guide awaits… Start Your Bot adventure with Quyen-Mini Now!

Repo of the code from the Medium article

Here the Streamilt Python app to run Quyen Mini that has 1.8 Billion parameters<br>
I am using here the quantized version that runs on CPU with llama-cpp-python

### Tested with Python 3.10

filename of the model: Quyen-Mini-v0.1.Q4_K_M.gguf

- HF repo: [https://huggingface.co/vilm/Quyen-Mini-v0.1-GGUF](https://huggingface.co/vilm/Quyen-Mini-v0.1-GGUF)
- HF GGUF file Url: [Quyen-Mini-v0.1.Q4_K_M.gguf](https://huggingface.co/vilm/Quyen-Mini-v0.1-GGUF/resolve/main/Quyen-Mini-v0.1.Q4_K_M.gguf)

1. Create a new directory
2. Create a virtual environment and activate it

```
mkdir QuyenMini
cd QuyenMini
python -m venv venv
venv\Scripts\activate
pip install llama-cpp-python
pip install streamlit
```

Download the follwing files in the Project directory
- qMini_chatALL.py
- assistant.png
- user.png

create a subfolder where to pu the GGUF file called:
```
GGUFs
```

download the GGUF file there

Open the terminal and with the venv activated run this command:
```
streamlit run qMini_chatALL.py
```

The interface will be like this one
<img src="https://github.com/fabiomatricardi/HowSmalltoChatYouCanGo/raw/main/qMini_ChatInterface000.png" width=800>

<img src="https://github.com/fabiomatricardi/HowSmalltoChatYouCanGo/raw/main/qMini_ChatInterface.png" width=700>

<img src="https://github.com/fabiomatricardi/HowSmalltoChatYouCanGo/raw/main/qMini_ChatInterface2.png" width=700>
