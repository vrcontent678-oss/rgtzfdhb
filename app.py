import os
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>VRContent</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background-color: #0f0f12;
      color: #ffffff;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      margin: 0;
    }
    h1 { font-size: 2.5rem; margin-bottom: 0.5rem; }
    p { color: #a0a0ab; margin-bottom: 2rem; }
    .btn-container {
      display: flex;
      gap: 15px;
      flex-wrap: wrap;
    }
    .btn {
      padding: 12px 24px;
      font-size: 1rem;
      font-weight: bold;
      text-decoration: none;
      border-radius: 8px;
      transition: transform 0.2s, background-color 0.2s;
    }
    .btn:hover { transform: translateY(-2px); }
    .btn-form { background-color: #ff4757; color: white; }
    .btn-form:hover { background-color: #ff6b81; }
    .btn-discord { background-color: #5865F2; color: white; }
    .btn-discord:hover { background-color: #4752C4; }
  </style>
</head>
<body>
  <h1>VRContent</h1>
  <p>Watch channel content and join the community.</p>
  
  <div class="btn-container">
    <a class="btn btn-form" href="https://docs.google.com/forms/d/e/1FAIpQLSeL_oO9mv7GHRHwzXIQcQIq780d_nL5Ic5qssltoeFzRyD5Ng/viewform" target="_blank" rel="noopener noreferrer">
      Submit Feedback / Form
    </a>
    <a class="btn btn-discord" href="https://discord.com/invite/a9T4WS6X6m" target="_blank" rel="noopener noreferrer">
      Join Discord
    </a>
  </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)