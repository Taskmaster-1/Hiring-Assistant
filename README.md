# TalentScout Hiring Assistant

## Project Overview
TalentScout Hiring Assistant is an AI-powered chatbot designed to assist recruitment agencies in the initial screening of tech candidates. The chatbot collects essential candidate information and generates relevant technical questions based on the candidate's declared tech stack.

## Features
- **Automated Information Collection**: Gathers candidate details including name, contact information, experience, desired position, location, and tech stack.
- **Dynamic Technical Question Generation**: Creates tailored technical questions based on the candidate's specific tech skills.
- **Conversational UI**: Provides a natural chat interface for candidates to interact with.
- **Context Awareness**: Maintains conversation context to ensure a smooth interview experience.
- **Conversation Exit Handling**: Gracefully concludes conversations when candidates indicate they're finished.

## Technical Details

### Libraries and Tools Used
- **Streamlit**: Frontend interface and session management
- **Groq API**: LLM provider for conversation intelligence
- **Python**: Core programming language
- **JSON**: Structured data handling

### Architecture
The application follows a modular design with these key components:

1. **User Interface** (`app.py`): Handles the Streamlit UI, display logic, and conversation flow.
2. **LLM Integration** (`groq_helper.py`): Manages communication with the LLM API.
3. **Prompt Engineering** (`prompts.py`): Contains carefully crafted prompts to guide the LLM's behavior.
4. **Session Management**: Uses Streamlit's session state to maintain conversation context.

### Prompt Design
The system employs sophisticated prompt engineering techniques:

- **System Prompt**: Defines the assistant's role, conversation flow, and response format
- **User Message Prompt**: Includes conversation history and current state to maintain context
- **Technical Question Generation**: Creates questions specifically matched to the candidate's skills

## Installation Instructions

### Prerequisites
- Python 3.8+
- Groq API key

### Setup Steps

1. Clone the repository:
   ```
   git clone https://github.com/Taskmaster-1/Talentscout-hiring-chatbot.git
   cd Talentscout-hiring-chatbot
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Groq API key:
   - Create a `.streamlit/secrets.toml` file with:
     ```
     GROQ_API_KEY = "your-groq-api-key"
     ```
   - Alternatively, you can enter your API key when prompted in the app

4. Run the application:
   ```
   streamlit run app.py
   ```

## Usage Guide

1. Start the application using the command above
2. The chatbot will greet you and begin asking for information
3. Provide your details when prompted
4. Once your tech stack is collected, the chatbot will generate relevant technical questions
5. Answer the questions or type "exit" to end the conversation

## Challenges & Solutions

### Challenge 1: Maintaining Conversation Context
**Solution**: Used a combination of Streamlit's session state and structured JSON responses from the LLM to track conversation progress and candidate information.

### Challenge 2: Extracting Information from Varied Responses
**Solution**: Implemented a context-aware prompt system that includes conversation history and current information state to help the LLM understand what information has already been collected.

### Challenge 3: Handling Non-Linear Conversations
**Solution**: Designed the prompt system to extract information even when it's provided out of the expected sequence, allowing for more natural conversation flow.

### Challenge 4: Technical Question Relevance
**Solution**: Generated questions only after collecting the complete tech stack, and included experience level in the prompt to ensure appropriate difficulty.

## Future Enhancements
- Sentiment analysis to gauge candidate comfort level
- Multi-language support
- Skill level assessment based on question responses
- Integration with ATS (Applicant Tracking Systems)
- More sophisticated conversation handling for complex scenarios

## Data Privacy Considerations
- All candidate information is stored only in session state and is not persisted
- No data is shared with third parties
- Candidates are informed about data handling at the start of conversation

## 🏷️ Versioning

Current Version: 1.0.0

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.


## 📞 Contact

Gmail - [i.am.vivekyadav5223@gmail.com](mailto:i.am.vivekyadav5223@gmail.com)