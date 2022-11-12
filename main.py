from typing import List

from flask import Flask, render_template

from utils import get_all_candidates, get_by_id, get_candidates_by_name, get_by_skill

app = Flask(__name__)
candidates: List[dict] = get_all_candidates()


@app.route("/")
def show_all_candidates():
    # Главная страница: Все кандидаты
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:id>")
def show_candidate_by_id(id):
    # Поиск кандидата по его id
    candidate = get_by_id(id)
    if not candidate:
        return "Not found"
    else:
        return render_template('card.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def show_candidates_by_name(candidate_name):
    # Выведет список кандидатов, которые имеют указанное имя, или "Not found" - если такого имени ни у кого нет
    candidate_by_name: list = get_candidates_by_name(candidate_name)
    if not candidate_by_name:
        return "Not found"
    else:
        print(candidate_by_name)
        return render_template('search.html', candidates=candidate_by_name, quantity=len(candidate_by_name))


@app.route("/skill/<skill_name>")
def get_candidates_by_skill(skill_name):
    # Выведет список кандидатов, у которых есть указанный навык, или "Not found" - если такого навыка ни у кого нет
    candidates_with_skill = get_by_skill(skill_name)
    if not candidates_with_skill:
        return "Not found"
    else:
        return render_template('skill.html', skill=skill_name, candidates=candidates_with_skill,
                               quantity=len(candidates_with_skill))


app.run()
