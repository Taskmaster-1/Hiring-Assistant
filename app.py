import streamlit as st
from groq_helper import chat_with_groq
from prompts import system_prompt, user_message_prompt
import json

st.set_page_config(page_title="TalentScout Hiring Assistant", page_icon="🧑‍💻", layout="centered")

st.title("🧑‍💻 TalentScout Hiring Assistant")
st.markdown("### We connect tech talent with great opportunities")


if 'messages' not in st.session_state:
    st.session_state.messages = []
    welcome_message = "👋 Hello! I'm the TalentScout Hiring Assistant. I'll help gather some information about your profile and ask a few technical questions to match you with the right opportunities. Let's start with your full name."
    st.session_state.messages.append({"role": "assistant", "content": welcome_message})

if 'candidate_info' not in st.session_state:
    st.session_state.candidate_info = {
        "name": None,
        "email": None,
        "phone": None,
        "experience": None,
        "desired_position": None,
        "location": None,
        "tech_stack": None,
        "questions_asked": False,
        "conversation_complete": False
    }

api_key = st.secrets.get("GROQ_API_KEY", None)
if not api_key:
    api_key = st.text_input("Please enter your GROQ API key:", type="password")
    if not api_key:
        st.warning("Please provide a GROQ API key to continue.")
        st.stop()


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("Type your response here..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.markdown(user_input)
    
    if any(word in user_input.lower() for word in ['bye', 'goodbye', 'exit', 'quit', 'end']):
        with st.chat_message("assistant"):
            farewell_message = "Thank you for chatting with TalentScout's Hiring Assistant! Your information has been saved. Our recruitment team will review your profile and get back to you soon. Have a great day! 👋"
            st.markdown(farewell_message)
        st.session_state.messages.append({"role": "assistant", "content": farewell_message})
        st.session_state.candidate_info["conversation_complete"] = True
        st.stop()
    
    conversation_history = [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
    
    prompt = user_message_prompt(user_input, conversation_history, st.session_state.candidate_info)
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat_with_groq(api_key, system_prompt(), prompt)
            
            try:
                parsed_response = json.loads(response)
                
                for key, value in parsed_response["candidate_info"].items():
                    if value and value != "unknown" and value != "null":
                        st.session_state.candidate_info[key] = value
                
                st.markdown(parsed_response["response"])
                
                st.session_state.messages.append({"role": "assistant", "content": parsed_response["response"]})
                
                if parsed_response.get("generate_technical_questions", False) and not st.session_state.candidate_info["questions_asked"]:
                    tech_stack = st.session_state.candidate_info["tech_stack"]
                    
                    if tech_stack:
                        with st.spinner("Generating technical questions..."):
                            tech_questions_prompt = f"""
                            Generate 3-5 technical interview questions to assess a candidate's knowledge in the following technologies:
                            {tech_stack}

                            Focus on core concepts, practical applications, and some advanced topics appropriate for their {st.session_state.candidate_info['experience']} years of experience.
                            Format your response as a JSON object with a single 'questions' field containing an array of question strings.
                            Do NOT include any numbering in the questions themselves.
                            Example format:
                            {{
                                "questions": [
                                    "Explain the difference between a list and a tuple in Python.",
                                    "How would you optimize a slow SQL query?",
                                    "Describe the benefits of containerization with Docker."
                                ]
                            }}
                            """

                            questions_response = chat_with_groq(api_key, "", tech_questions_prompt)

                            try:
                                questions_data = json.loads(questions_response)
                                if isinstance(questions_data.get('questions'), list):
                                    formatted_questions = ""
                                    for i, question in enumerate(questions_data['questions']):
                                        clean_question = question.strip()
                                        
                                        if clean_question[0].isdigit() and '.' in clean_question[:3]:
                                            clean_question = clean_question.split('.', 1)[1].strip()
                                        formatted_questions += f"{i+1}. {clean_question}\n\n"
                                else:
                                    formatted_questions = questions_response
                            except json.JSONDecodeError:
                                lines = questions_response.strip().split('\n')
                                formatted_questions = ""
                                for i, line in enumerate(lines):
                                    if line.strip():
                                        clean_line = line.strip()
                                        if clean_line[0].isdigit() and '.' in clean_line[:3]:
                                            clean_line = clean_line.split('.', 1)[1].strip()
                                        formatted_questions += f"{i+1}. {clean_line}\n\n"

                            questions_message = "### Based on your tech stack, here are some technical questions:\n\n" + formatted_questions
                            st.markdown(questions_message)

                            st.session_state.messages.append({
                                "role": "assistant", 
                                "content": questions_message
                            })
                            
                            st.session_state.candidate_info["questions_asked"] = True
                            
                            follow_up = "Please provide your answers to these questions. This will help us better understand your technical expertise."
                            st.markdown(follow_up)
                            st.session_state.messages[-1]["content"] += "\n\n" + follow_up

            except json.JSONDecodeError:
                st.error("I received an invalid response format. Let me try again.")
                fallback_message = "I apologize for the technical issue. Could you please repeat your last answer?"
                st.markdown(fallback_message)
                st.session_state.messages.append({"role": "assistant", "content": fallback_message})

# Displaying the  current collected information (for debugging)
if st.sidebar.checkbox("Show collected candidate information", False):
    st.sidebar.json(st.session_state.candidate_info)