from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai

app = Flask(__name__, template_folder='.')
CORS(app)

# Set up OpenAI API key
openai.api_key = "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"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_story', methods=['POST'])
def generate_story():
    data = request.json
    prompt = data.get('prompt', '')
    
    # Debugging: Print the received prompt to check if it's being sent correctly
    print(f"Received prompt: {prompt}")

    try:
        # Use the correct API method for the latest version of OpenAI
        response = openai.completions.create(
            model="gpt-3.5-turbo",
            prompt=f"Write a story based on: {prompt}",
            max_tokens=200,
            temperature=0.7
        )

        story = response['choices'][0]['text'].strip()  # Access the generated story
        return jsonify({'story': story})

    except Exception as e:
        print(f"Error while generating story: {e}")  # Log the error
        return jsonify({'error': 'Failed to generate story. Please try again later.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
