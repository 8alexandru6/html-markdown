from flask import Flask, render_template, request, redirect, url_for
import html2text
import markdown

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    markdown_result = None
    html_result = None

    if request.method == 'POST':
        html_input = request.form.get('html_input')
        markdown_input = request.form.get('markdown_input')
        
        if html_input:
            try:
                markdown_result = html2text.html2text(html_input)
            except Exception as e:
                markdown_result = f"Error converting HTML to Markdown: {e}"
        elif markdown_input:
            try:
                html_result = markdown.markdown(markdown_input, extensions=['extra', 'nl2br', 'sane_lists'])
            except Exception as e:
                html_result = f"Error converting Markdown to HTML: {e}"

    return render_template('index.html', markdown_result=markdown_result, html_result=html_result)


if __name__ == '__main__':
    app.run(debug=True) 