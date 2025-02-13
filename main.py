import os
from fracticody_engine import app  # Ensure your app object is correctly 
imported

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render sets a PORT 
environment variable
    app.run(host="0.0.0.0", port=port)
