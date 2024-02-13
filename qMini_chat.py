# source  https://github.com/lalanikarim/ai-chatbot/blob/main/main.py
# for the avatar and streaming my repo
# https://github.com/fabiomatricardi/LaminiChat/blob/main/stapp.py
# Not STREAMING the output
# Not having a Conversation Buffer
# How to use a login -> https://blog.streamlit.io/how-to-build-an-llm-powered-chatbot-with-streamlit/
# https://medium.com/p/1499c062b1b9  for tuning hyperparameters
# Using Chat_Completion from llamaCPPpython
# https://llama-cpp-python.readthedocs.io/en/latest/#chat-completion



import streamlit as st
#from langchain.llms import LlamaCpp
from llama_cpp import Llama
from langchain.prompts import PromptTemplate
#from huggingface_hub import hf_hub_download
from time import  sleep
import datetime
import tiktoken



def writehistory(filename,text):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        f.write('\n')
    f.close()

encoding = tiktoken.get_encoding("r50k_base")
#AVATARS  👷🐦
av_us = 'user.png'  #"🦖"  #A single emoji, e.g. "🧑‍💻", "🤖", "🦖". Shortcodes are not supported.
av_ass = 'assistant.png'



@st.cache_resource
def create_chain():   
    mp = "GGUFs\Quyen-Mini-v0.1.Q4_K_M.gguf"
    # initialize LlamaCpp LLM model
    # n_gpu_layers, n_batch, are for GPU support.
    # When not set, CPU will be used.
    # n_ctx is the context window the model can support
    llm = Llama(
            model_path=mp,
            n_gpu_layers=0,
            temperature=0.1,
            top_p = 0.5,
            n_ctx=5000,
            max_tokens=350,
            # n_gpu_layers=1,
            # n_batch=512,
            repeat_penalty=1.7,
            stop=["<|im_end|>","Instruction:","### Instruction:","###<user>","</user>"],
            verbose=False,
            streaming=True,
            chat_format="chatml",
            )

    return llm


# Set the webpage title
st.set_page_config(
    page_title="Your own LocalGPT with Quyen-Mini 🐦",
    page_icon="🐦")

# Create a header element
st.header("Your own LocalGPT with Quyen-Mini 🐦")
st.markdown("#### :green[*Quyen-Mini-v0.1.Q4_K_M.gguf - the best 1.8B  English/Chinese small model?*]")

if "logfilename" not in st.session_state:
## Logger file
    tstamp = datetime.datetime.now()
    tstamp = str(tstamp).replace(' ','_')
    tstamp = str(tstamp).replace(':','_')
    logfile = f'{tstamp[:-7]}_log.txt'
    st.session_state.logfilename = logfile
    #Write in the history the first 2 sessions
    writehistory(st.session_state.logfilename,f'🧠🫡: You are a helpful assistant.')    
    writehistory(st.session_state.logfilename,f'🐦: How may I help you today?')

if "big_context" not in st.session_state:
    st.session_state.big_context = ""

if "len_context" not in st.session_state:
    st.session_state.len_context = 0

if "bufstatus" not in st.session_state:
    st.session_state.bufstatus = "### :green[Good]"

with st.sidebar:
    st.markdown("""### Missing features:
- <s>ConversationBuffer</s>
- Real streaming output
- HyperParameters
- <s>Buffer limiter</s>
- CSS for streamlit""", unsafe_allow_html=True)
    mytokens = st.markdown(f"""**Context turns**
{st.session_state.len_context}""")
    system_prompt = st.text_area(
                        label="System Prompt",
                        value="You are a helpful assistant.",
                        key="system_prompt",
                        height=20)
    st.markdown("### Buffer status")
    st.markdown(st.session_state.bufstatus)
    st.markdown("### Logfile")
    st.markdown(st.session_state.logfilename)

# Create LLM chain to use for our chatbot.
llm_chain = create_chain()

# We store the conversation in the session state.
# This will be used to render the chat conversation.
# We initialize it with the first message we want to be greeted with.
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant.",},
        {"role": "assistant", "content": "How may I help you today?"}
    ]


if "current_response" not in st.session_state:
    st.session_state.current_response = ""

# We loop through each message in the session state and render it as
# a chat message.
for message in st.session_state.messages[1:]:
    if message["role"] == "user":
        with st.chat_message(message["role"],avatar=av_us):
            st.markdown(message["content"])
    else:
        with st.chat_message(message["role"],avatar=av_ass):
            st.markdown(message["content"])

# We take questions/instructions from the chat input to pass to the LLM
if user_prompt := st.chat_input("Your message here", key="user_input"):

    # Add our input to the session state
    st.session_state.messages.append(
        {"role": "user", "content": user_prompt}
    )

    # Add our input to the chat window
    with st.chat_message("user", avatar=av_us):
        st.markdown(user_prompt)
        writehistory(st.session_state.logfilename,f'👷: {user_prompt}')

    
    with st.chat_message("assistant",avatar=av_ass):
        with st.spinner("Thinking..."):
            full_response = ''
            placeholder = st.empty()
            conv_messages = []
            st.session_state.len_context = len(st.session_state.messages) 
            # Checking context window for the LLM, not for the chat history to be displayed
            if st.session_state.len_context > 13:
                st.session_state.bufstatus = "### :red[Overflow]"
                # this will keep 5 full turns into consideration
                x=9
                conv_messages.append(st.session_state.messages[0])
                for i in range(0,x):
                    conv_messages.append(st.session_state.messages[-x+i])
                print(len(conv_messages))
                for item in llm_chain.create_chat_completion(messages=conv_messages)["choices"][0]["message"]["content"]:
                    full_response += item
                    placeholder.markdown(full_response + "▌")
                    sleep(0.01)
                placeholder.markdown(full_response)
                writehistory(st.session_state.logfilename,f'🐦: {full_response}') 
            else:
                st.session_state.bufstatus = "### :green[Good]"
                for item in llm_chain.create_chat_completion(messages=st.session_state.messages)["choices"][0]["message"]["content"]:
                    full_response += item
                    placeholder.markdown(full_response + "▌")
                    sleep(0.01)
                placeholder.markdown(full_response)
                writehistory(st.session_state.logfilename,f'🐦: {full_response}') 
            
    # Add the response to the session state
    st.session_state.messages.append(
        {"role": "assistant", "content": full_response}
    )
