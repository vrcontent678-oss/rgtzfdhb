import os
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>VRContent — Everything to entertain your world.</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: #000000;
      color: #ffffff;
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
    }
    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1.75rem 3rem;
      position: fixed;
      top: 0;
      width: 100%;
      z-index: 100;
      background-color: rgba(0, 0, 0, 0.8);
      backdrop-filter: blur(10px);
    }
    .logo {
      font-weight: 700;
      font-size: 1.25rem;
      letter-spacing: -0.03em;
      text-transform: uppercase;
    }
    .nav-btn {
      color: #ffffff;
      text-decoration: none;
      font-size: 0.875rem;
      font-weight: 500;
      border: 1px solid rgba(255, 255, 255, 0.3);
      padding: 0.6rem 1.25rem;
      border-radius: 0px;
      transition: all 0.2s ease;
    }
    .nav-btn:hover {
      background-color: #ffffff;
      color: #000000;
    }
    .hero {
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      padding: 2rem;
      max-width: 1100px;
      margin: 0 auto;
    }
    .hero-title {
      font-size: clamp(2.5rem, 7vw, 5.5rem);
      font-weight: 500;
      letter-spacing: -0.04em;
      line-height: 1.05;
      margin-bottom: 1.5rem;
    }
    .hero-subtitle {
      font-size: clamp(1.1rem, 2vw, 1.5rem);
      font-weight: 300;
      color: #a1a1a1;
      max-width: 650px;
      margin-bottom: 2.5rem;
    }
    .cta-group {
      display: flex;
      gap: 1.25rem;
      flex-wrap: wrap;
      justify-content: center;
    }
    .btn-primary {
      background-color: #ffffff;
      color: #000000;
      padding: 1rem 2.25rem;
      font-size: 0.95rem;
      font-weight: 600;
      text-decoration: none;
      border: 1px solid #ffffff;
      transition: all 0.2s ease;
    }
    .btn-primary:hover {
      background-color: #e5e5e5;
    }
    .btn-secondary {
      background-color: transparent;
      color: #ffffff;
      padding: 1rem 2.25rem;
      font-size: 0.95rem;
      font-weight: 600;
      text-decoration: none;
      border: 1px solid rgba(255, 255, 255, 0.4);
      transition: all 0.2s ease;
    }
    .btn-secondary:hover {
      border-color: #ffffff;
      background-color: rgba(255, 255, 255, 0.1);
    }
    footer {
      position: absolute;
      bottom: 2rem;
      width: 100%;
      text-align: center;
      font-size: 0.8rem;
      color: #555555;
    }
  </style>
</head>
<body>

  <header>
    <div class="logo">VRCONTENT</div>
    <a href="https://discord.com/invite/a9T4WS6X6m" target="_blank" rel="noopener noreferrer" class="nav-btn">Join Community</a>
  </header>

  <main class="hero">
    <h1 class="hero-title">A new home for immersive content.</h1>
    <p class="hero-subtitle">Watch, engage, and connect with the channel’s official community hub.</p>
    
    <div class="cta-group">
      <a href="https://docs.google.com/forms/d/e/1FAIpQLSeL_oO9mv7GHRHwzXIQcQIq780d_nL5Ic5qssltoeFzRyD5Ng/viewform" target="_blank" rel="noopener noreferrer" class="btn-primary">
        Submit Feedback
      </a>
      <a href="https://discord.com/invite/a9T4WS6X6m" target="_blank" rel="noopener noreferrer" class="btn-secondary">
        Join Discord
      </a>
    </div>
  </main>

  <footer>
    &copy; VRContent. All rights reserved.
  </footer>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
