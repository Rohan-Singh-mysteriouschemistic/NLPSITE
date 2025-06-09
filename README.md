Flask-based Web Application for NLP Utilities

This application provides a simple interface for users to:
- Register and log in using a local authentication system.
- Perform Named Entity Recognition (NER) using custom or third-party APIs.
- Analyze the sentiment of a given text.
- Check and correct grammar in user-provided input.
- Generate code snippets based on natural language prompts.

The application uses:
- Flask for backend routing and rendering HTML templates.
- A local `Database` module for user registration and login authentication.
- An `Api` module that connects to different NLP utilities such as NER, Sentiment Analysis, Grammar Check, and Code Generation.

To run the app:
- Make sure `Database.py`, `Api.py`, and the HTML templates (`Login.html`, etc.) are present in appropriate folders.
- Run this file directly with Python to start the server on localhost.
- Make sure the NLP Cloud Token has not been exhausted.
