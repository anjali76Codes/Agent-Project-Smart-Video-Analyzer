# 🤖 Normal AI Chatbot vs 🧠 AI Agent Chatbot

## 💬 Example Question:
**"What are your store hours?"**

---

## 🔹 Normal AI Chatbot

This is a basic chatbot that understands and categorizes your question — like whether it’s a general inquiry, refund, or order status — and gives a simple, direct answer.

**Response:**
> "Our store hours are from 10:00 AM to 10:00 PM."

- No memory  
- No personalization  
- No suggestions  
- Acts more like a Q&A machine

---

## 🔸 AI Agent Chatbot

This is a smart assistant that goes beyond just answering. It uses memory, personalization, and context-awareness to respond more like a human.

**Response:**
> "We’re open from 10:00 AM to 10:00 PM today!  
By the way, I noticed you ordered a Paneer Pizza last time — would you like to order it again?  
Also, it’s quite hot outside 🌞 — how about a cold drink to go with your order?"

- Suggestive, helpful, and human-like  
- Remembers past interactions  
- Connects to external data like weather, databases  
- Acts as a smart assistant, not just a responder

---


## 🧾 Summary

- A **Normal AI Chatbot** gives basic answers.
- An **AI Agent Chatbot** acts as a smart assistant:
  - It thinks ahead  
  - It remembers you  
  - It interacts like a human

 
## 🧠 Tools in AI Agent Chatbots

AI Agent Chatbots can access external **tools** to enhance intelligence and responsiveness:

- 🔌 Weather APIs  
- 🌐 Web search  
- 📚 Document databases  
- 📦 Product/order databases  
- 📊 CRM or customer history  
- 🧮 Custom Python functions & logic  

These capabilities allow AI Agents to:
- Understand **user intent**
- **Extract structured data** from natural language
- Perform **external actions** (e.g., API calls, search, computation)

---

## 🧾 Summary

- A **Normal AI Chatbot** gives straightforward answers.
- An **AI Agent Chatbot** acts like a smart assistant:
  - Remembers past conversations  
  - Connects to external tools and systems  
  - Thinks ahead and makes helpful suggestions  
  - Executes logic, searches, and recommendations on the fly  

> 🤖 Chatbots are just **one type** of AI solution. Other categories include:
> - 🔍 Document Search
> - 🎯 Recommendation Engines
> - 🧩 Predictive Analytics
> - 🗣️ Voice Assistants  
> - 🤝 Virtual Agents

AI Agents are the **next evolution of conversational intelligence** — combining interaction, memory, and tools to deliver real value.

--- 



GROQ  is a open source which allow us to use the Llama 3.3 
Code Rabbit is AI Review Platform 
Coupon : CODEBASICS
link : https://www.coderabbit.ai/




## Technical Flow
- User uploads video → **st.file_uploader()** → Temporary file saved using tempfile.

- Display video → **st.video()** → Video shown from temp path.

- User asks question → **st.text_area()**.

- User clicks "Analyze Video" → Validation of the question.

- Upload video to Gemini → upload_file(video_path).

- Gemini AI processes video → Wait for processing with **get_file().**

- AI generates response → **multimodal_Agent.run(analysis_prompt, videos=[processed_video]).**

- Show AI response → st.markdown(response.content).

- Delete temp file → Path(video_path).unlink().