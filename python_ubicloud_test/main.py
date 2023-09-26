from flask import Flask, render_template_string
from waitress import serve

app = Flask(__name__)

@app.route('/')
def hello_world():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World</title>
    </head>
    <body>
        <h1>Hello World!</h1>
    </body>
    </html>
    """
    return render_template_string(html_content)


def main():
    serve(app, host='0.0.0.0', port=8080)

if __name__ == '__main__':
    main()