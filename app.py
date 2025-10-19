from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
tasks = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            tasks.append(task)
        return redirect('/')
    
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>To-Do List</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background-color: #f0f2f5;
                padding-top: 50px;
            }
            .container {
                max-width: 600px;
                margin: auto;
            }
            .card {
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }
            ul {
                list-style-type: none;
                padding-left: 0;
            }
            li {
                background: #fff;
                margin-bottom: 10px;
                padding: 10px;
                border-radius: 5px;
                box-shadow: 0 0 5px rgba(0,0,0,0.05);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2 class="text-center text-primary mb-4">📝 My To-Do List</h2>
            <div class="card">
                <form method="POST">
                    <div class="input-group mb-3">
                        <input type="text" name="task" class="form-control" placeholder="Enter a new task" required>
                        <button class="btn btn-outline-primary" type="submit">Add</button>
                    </div>
                </form>
                <ul>
                    {% for task in tasks %}
                        <li>{{ task }}</li>
                    {% else %}
                        <li class="text-muted">No tasks yet. Add one above!</li>
                    {% endfor %}
                </ul>
            </div>
        </div>
    </body>
    </html>
    """, tasks=tasks)

if __name__ == '__main__':
    app.run()
