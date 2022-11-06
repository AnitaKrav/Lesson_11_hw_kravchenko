from typing import List

from flask import Flask

from utils import format_candidates, get_all_candidates, get_by_pk, get_by_skill

app = Flask(__name__)


@app.route("/")
def get_all():
    # Главная страница
    candidates: List[dict] = get_all_candidates()
    result = ''
    for candidate in candidates:
        result += format_candidates(candidate)
    return result


@app.route("/candidates/<int:pk>")
# Выведет кандидата с выбранным pk
def get_candidate_by_pk(pk):
    candidate = get_by_pk(pk)
    if candidate is None:
        return "Нет такого pk"
    else:
        result = format_candidates(candidate)
        return f"<img src='{candidate['picture']}'>\n {result}"


@app.route("/skills/<skill>")
# Выведет список кандидатов, у которых есть указанный навык
def get_candidates_by_skill(skill):
    candidates = get_by_skill(skill)
    if not candidates:
        return "Not found"
    else:
        result = ''
        for candidate in candidates:
            result += format_candidates(candidate)
        return result


app.run()
