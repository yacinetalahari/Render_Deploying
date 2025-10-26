from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>DevProfile | Flask Edition</title>
      <style>
        body {
          margin: 0;
          padding: 0;
          font-family: 'Poppins', sans-serif;
          background: linear-gradient(120deg, #1f1c2c, #928dab);
          color: #fff;
          height: 100vh;
          display: flex;
          justify-content: center;
          align-items: center;
          text-align: center;
          flex-direction: column;
        }
        h1 {
          font-size: 3rem;
          letter-spacing: 1px;
          margin-bottom: 0.5rem;
        }
        h2 {
          font-weight: 400;
          color: #d3d3d3;
          margin-bottom: 2rem;
        }
        .skills {
          display: flex;
          gap: 1rem;
        }
        .skill {
          background: rgba(255, 255, 255, 0.1);
          padding: 0.8rem 1.2rem;
          border-radius: 12px;
          transition: all 0.3s ease;
        }
        .skill:hover {
          background: rgba(255, 255, 255, 0.25);
          transform: scale(1.1);
          cursor: pointer;
        }
        footer {
          position: absolute;
          bottom: 15px;
          font-size: 0.9em;
          opacity: 0.7;
        }
      </style>
    </head>
    <body>
      <h1>Hi, I'm YaSSiNo</h1>
      <h2>Building cool things with technology</h2>
      <div class="skills">
        <div class="skill">Python</div>
        <div class="skill">Flask</div>
        <div class="skill">C++</div>
        <div class="skill">C</div>
        <div class="skill">html</div>
        <div class="skill">Css</div>
        <div class="skill">php</div>
        <div class="skill">JS</div>
        <div class="skill">Next.js</div>
        <div class="skill">Next.js</div>
      </div>
      <footer>© 2025 - Flask DevProfile by Yassino</footer>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
