from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
  return "HELLO WORLD"


if __name__ == "__main__":
  print("Hey")
  app.run(host='0.0.0.0', port=6001, debug=True)