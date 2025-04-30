# 🧑‍💻 Hiring Assistant

## Project Overview
Hiring Assistant is an intelligent chatbot designed for a fictional recruitment agency specializing in technology placements. This chatbot streamlines the initial candidate screening process by collecting essential information and generating tailored technical questions based on the candidate's declared tech stack. The application provides a seamless, conversational experience while gathering valuable data to assist recruiters in the hiring process.

## Functionality

### User Interface
- Clean, intuitive Streamlit interface with a modern design
- Real-time conversation flow with typing indicators
- Progress tracking for candidate information collection
- Sentiment analysis visualization for recruitment insights
- Multilingual support for global candidate interactions

### Chatbot Capabilities

#### Greeting & Information Collection
- Welcomes candidates with a friendly introduction
- Collects essential candidate details:
  - Full Name
  - Email Address
  - Phone Number
  - Years of Experience
  - Desired Position(s)
  - Current Location
  - Tech Stack

#### Technical Question Generation
- Analyzes the candidate's declared tech stack
- Generates 3-5 relevant technical questions tailored to each technology
- Adjusts question difficulty based on the candidate's experience level
- Presents questions in a clear, structured format

#### Context Handling
- Maintains conversation context throughout the interview
- Extracts information from varied responses
- Handles non-linear conversations naturally
- Recognizes when information has already been collected

#### Conversation Management
- Gracefully exits when conversation-ending keywords are detected
- Provides fallback responses for unexpected inputs
- Concludes with a summary of next steps in the recruitment process

## Technical Specifications

### Programming Language & Libraries
- **Python**: Core programming language
- **Streamlit**: Frontend interface development
- **Groq API**: LLM integration for intelligent responses
- **JSON**: Structured data handling and storage

### Architecture
The application follows a modular design with these key components:

1. **User Interface** (`app.py`): Main Streamlit interface and conversation flow management
2. **LLM Integration** (`groq_helper.py`): Manages communication with the Groq API
3. **Prompt Engineering** (`prompts.py`): Sophisticated prompts to guide the LLM's behavior
4. **Session Management**: Streamlit's session state for conversation context
5. **Enhancement Modules**:
   - `data_handler.py`: Manages data processing and storage
   - `language_handler.py`: Provides multilingual support
   - `performance_optimizer.py`: Optimizes response times and caching
   - `ui_enhancer.py`: Creates a polished, responsive UI
   - `sentiment_analyzer.py`: Analyzes candidate sentiment during interviews

### Prompt Engineering
The system employs sophisticated prompt engineering techniques:

- **System Prompt**: Defines the assistant's role, personality, and response format
- **User Message Prompt**: Maintains conversation context with history and current state
- **Technical Question Generation**: Creates tailored questions for the candidate's tech stack
- **Sentiment-Enhanced Prompts**: Incorporates candidate sentiment for more empathetic responses

## Installation Instructions

### Prerequisites
- Python 3.8+
- Groq API key

### Setup Steps

1. Clone the repository:
   ```
   git clone https://github.com/Taskmaster-1/Hiring-Assistant.git
   cd Hiring-Assistant
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
2. Enter your Groq API key if not configured in secrets.toml
3. The chatbot will greet you and begin asking for your information
4. Provide your details when prompted
5. Once your tech stack is collected, the chatbot will generate relevant technical questions
6. Answer the questions to demonstrate your technical proficiency
7. Type "exit" or "bye" when you wish to end the conversation

## Data Handling

### Simulated Data
- The application uses simulated or anonymized data for testing
- Test candidates can be generated through the admin interface

### Data Privacy
- All candidate information is handled in compliance with GDPR
- Data is stored securely and only within the session
- Privacy notices are displayed to candidates at the start of conversation
- Anonymization features are implemented for data protection

## Challenges & Solutions

### Challenge 1: Maintaining Conversation Context
**Solution**: Implemented a sophisticated state management system using Streamlit's session state combined with structured JSON responses from the LLM to track conversation progress and candidate information.

### Challenge 2: Extracting Information from Varied Responses
**Solution**: Designed a context-aware prompt system that includes conversation history and current information state to help the LLM understand what data has been collected and what still needs to be gathered.

### Challenge 3: Handling Non-Linear Conversations
**Solution**: Created a flexible information extraction system that can identify and capture candidate details regardless of the order in which they are provided, allowing for more natural conversation flow.

### Challenge 4: Ensuring Relevant Technical Questions
**Solution**: Developed a specialized prompt engineering approach that generates technical questions only after collecting the complete tech stack, and includes experience level to ensure appropriate difficulty calibration.

### Challenge 5: Performance Optimization
**Solution**: Implemented a caching system to reduce API calls and response times, with built-in performance monitoring to track metrics such as page load time and average response time.

## Optional Enhancements

### Advanced Features
- **Sentiment Analysis**: Analyzes candidate emotions during the conversation to gauge comfort level
- **Multilingual Support**: Detects and adapts to the candidate's preferred language
- **Performance Optimization**: Caching and response time monitoring for efficient operation

### UI Enhancements
- Custom styling with modern design principles
- Real-time typing indicators for a natural conversation feel
- Progress tracking to visualize interview completion
- Sentiment visualization for recruitment insights
- Responsive design for various screen sizes

## Code Quality

### Structure & Readability
- Modular architecture with clear separation of concerns
- Consistent naming conventions and code style
- Comprehensive error handling and fallback mechanisms
- Well-documented code with comments explaining complex logic

### Documentation
- Detailed README with comprehensive project overview
- Installation and usage instructions
- Challenge explanations and solution approaches
- Code comments and docstrings for clarity

## Future Enhancements
- Integration with ATS (Applicant Tracking Systems)
- Enhanced skill assessment based on question responses
- Voice input/output capabilities
- Calendar integration for scheduling follow-up interviews
- Expanded multilingual support for additional languages

## 🏷️ Versioning

Current Version: 1.0.0

## License
Distributed under the MIT License. See `LICENSE` for more information.

## 🌐 Deployed Application

### 🔗 Live 
- **Render**: [https://hiring-assistant.onrender.com]

## Contact
For questions or feedback, please contact: [i.am.vivekyadav5223@gmail.com](mailto:i.am.vivekyadav5223@gmail.com)
