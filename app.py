from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template for the form
HTML_TEMPLATE = """
    <form method="POST">
        <input type="number" name="number1" placeholder="Enter first number">
        <input type="number" name="number2" placeholder="Enter second number">
        <input type="submit" value="Add">
    </form>
    {% if result is not none %}
        <h2>Result: {{ result }}</h2>
    {% endif %}
"""


@app.route("/", methods=["GET", "POST"])
def add():
    result = None
    if request.method == "POST":
        number1 = request.form.get("number1", type=int)
        number2 = request.form.get("number2", type=int)
        result = number1 + number2
    return render_template_string(HTML_TEMPLATE, result=result)


if __name__ == "__main__":
    app.run(debug=True, port=8888)
