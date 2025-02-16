import sys
import os
import time
import json
from flask import Flask, request, jsonify

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

try:
    from core.fractal_cognition import FractalCognition
    from core.fracti_decision_engine import FractiDecisionEngine
    from core.memory_manager import MemoryManager
    from core.fracti_fpu import FractiProcessingUnit
except ImportError as e:
    print(f"❌ Error importing core modules: {e}")
    raise

app = Flask(__name__)

class FractiCodyEngine:
    """FractiCody's AI Core Engine, managing cognition and decision-making."""

    def __init__(self):
        print("🚀 Initializing FractiCody Engine...")
        self.cognition = FractalCognition()
        self.decision_engine = FractiDecisionEngine()
        self.memory = MemoryManager()
        self.fpu = FractiProcessingUnit()
        self.cognition_level = self.cognition.cognition_level
        self.learning_active = True

    def start(self):
        """Starts the AI engine"""
        print("🔹 Activating Fractal Cognition...")
        self.cognition.activate()
        print(f"✅ FractiCody Booted at Cognition Level: {self.cognition_level}")

    def process_input(self, user_input):
        """Processes user input using fractal cognition"""
        return self.cognition.process_input(user_input)

    def make_decision(self, context, options):
        """Uses the decision engine to make logical choices."""
        return self.decision_engine.process_decision(context, options)

@app.route('/command', methods=['POST'])
def command():
    try:
        user_input = request.json.get("command", "").strip()
        if not user_input:
            return jsonify({"error": "Invalid input. Command is required."}), 400

        fracticody = FractiCodyEngine()
        response = fracticody.process_input(user_input)
        return jsonify({"response": response})

    except Exception as e:
        print(f"❌ Error processing command: {e}")
        return jsonify({"error": "An error occurred processing your request."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8181, debug=True)
