from flask import Flask

main = Flask(__name__)

@main.route("/")
def hello_world():
    return "Hello, Jovian!"

print(__name__)
if __name__ == "__main__":
  main.run(host='0.0.0.0', debug=True)