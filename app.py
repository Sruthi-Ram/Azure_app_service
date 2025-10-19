from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Azure Flask Demo</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background-color: #f8f9fa;
                padding-top: 50px;
            }
            .container {
                text-align: center;
            }
            .card {
                margin-top: 30px;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1 class="display-4 text-primary">🚀 Hello from Azure App Service!</h1>
            <div class="card">
                <p class="lead">Your Flask app is live and running on Azure.</p>
                <p>Now you can build out features, connect databases, and scale globally.</p>
                <a href="https://portal.azure.com" class="btn btn-success">Go to Azure Portal</a>
            </div>
        </div>
    </body>
    </html>
    """)

if __name__ == '__main__':
    app.run()
