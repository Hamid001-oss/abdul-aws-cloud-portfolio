from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>AWS ECS Portfolio</title>
        </head>
        <body>
            <h1>Docker Application Running on AWS ECS</h1>
            <p>Cloud & DevOps Portfolio</p>
            <p>Containerized with Docker and designed for Amazon ECS.</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "aws-ecs-portfolio"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
