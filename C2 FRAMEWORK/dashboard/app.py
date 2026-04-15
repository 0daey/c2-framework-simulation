from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>C2 Framework Dashboard (Simulation)</h1>
    <p>This dashboard would normally show connected agents.</p>
    """

if __name__ == "__main__":
    app.run(port=5000)