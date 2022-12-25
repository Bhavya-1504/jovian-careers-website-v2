from flask import Flask, render_template

main = Flask(__name__)

@main.route("/")
def hello_jovian():
    return render_template('home.html')

print(__name__)
if __name__ == "__main__":
  main.run(host='0.0.0.0', debug=True)