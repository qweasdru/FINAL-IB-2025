from flask import Flask, request, render_template_string
from lxml import etree

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        xml_data = request.form.get("feedback", "")
        try:
            parser = etree.XMLParser(resolve_entities=True)  # Enable XXE
            root = etree.fromstring(xml_data.encode(), parser)
            result = f"Спасибо за отзыв: {root.findtext('message')}"
        except Exception as e:
            result = f"Произошла ошибка при обработке формы."
    return render_template_string("""
        <html>
        <head>
            <title>Отзывы клиентов</title>
            <style>
                body {
                    font-family: sans-serif;
                    background: linear-gradient(to right, #141e30, #243b55);
                    color: white;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                }
                textarea, input[type=submit] {
                    font-size: 1rem;
                    margin-top: 10px;
                    padding: 10px;
                    border-radius: 10px;
                    border: none;
                }
                .box {
                    background: rgba(255, 255, 255, 0.1);
                    padding: 2rem;
                    border-radius: 20px;
                    box-shadow: 0 0 20px rgba(255,255,255,0.2);
                }
            </style>
        </head>
        <body>
            <div class="box">
                <h2>Оставьте отзыв</h2>
                <form method="post">
                    <textarea name="feedback" rows="8" cols="50" placeholder="Ваше сообщение в XML-формате..."></textarea><br>
                    <input type="submit" value="Отправить">
                </form>
                <div style="margin-top: 1rem;">{{ result }}</div>
            </div>
        </body>
        </html>
    """, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
