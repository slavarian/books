# Python
import requests
from requests import Response

# Flask
from flask import (
    Flask,
    render_template,
    Response as FlaskResponse,
)
from flask.app import Flask as FlaskApp

app: FlaskApp = Flask(__name__)
BOOK_URL = (
    'https://raw.githubusercontent.com/benoitvallon/100-best-books/master/books.json'
)

books: list[dict] = []


@app.route("/")
def main_page() -> str:
    return render_template(
        template_name_or_list='index.html',
        ctx_books=books
    )


# @app.route("/<id>")
# def card_page(id: str) -> FlaskResponse:
#     try:
#         return render_template(
#             "card.html",
#             card=hearthstone_cards[int(id)]
#         )
#     except IndexError:
#         return "So big"

if __name__ == "__main__":
    response: Response = requests.get(BOOK_URL)
    books: list[dict] = response.json()
    app.run(
        port=8020,
        debug=True
    )
