from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
    <html>
    <head>
        <title>Hello World - Docker</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background: linear-gradient(to right, #4facfe, #00f2fe);
                color: white;
                height: 100vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }
            h1 {
                font-size: 3em;
                margin-bottom: 10px;
            }
            p {
                font-size: 1.5em;
                margin-bottom: 20px;
            }
            a {
                text-decoration: none;
                background-color: white;
                color: #4facfe;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 1.2em;
                transition: 0.3s;
            }
            a:hover {
                background-color: #00f2fe;
                color: white;
            }
        </style>
    </head>
    <body>
        <h1>Hello World from Morgan</h1>
        <p>This is the first version of my Docker image!</p>
        <a href="https://github.com/bipre2466/hello-world-docker" target="_blank">View the source code on GitHub</a>
    </body>
    </html>
    """

if __name__ == '__main__':
    port = 8080
    print(f"🚀 Server started! Visit: http://localhost:{port} 🚀")
    app.run(host='0.0.0.0', port=port)
