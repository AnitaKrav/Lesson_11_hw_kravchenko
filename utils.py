import json
from typing import List

filename = 'candidates.json'


def load_candidates() -> List[dict]:
    """
    Выгружает данные всех кандидатов из json
    :return: list[dict]
    """
    with open(filename, 'r', encoding='UTF-8') as f:
        candidates = json.load(f)
        return candidates


def format_candidates(candidate: dict) -> str:
    """
    Форматирование строки вывода
    """
    result = '<pre>'
    result += "Имя кандидата: " + candidate['name'] + '<br>'
    result += "Позиция кандидата: " + candidate['position'] + '<br>'
    result += "Навыки: " + candidate['skills'] + '<br>' * 2
    result += '</pre'
    return result


def get_all_candidates() -> List[dict]:
    return load_candidates()


def get_by_pk(pk):
    """
    Поиск кандидата с указанным pk
    :param pk: pk
    :return: данные кандидата,с заданным pk в формате dict
    """
    for candidate in load_candidates():
        if candidate['pk'] == pk:
            return candidate


def get_by_skill(skill_name):
    """
    Поиск кандидатов, имеющих заданный навык
    :param skill_name: навык
    :return: список кандидатов, имеющих заданный навык
    """
    result = []
    candidates = load_candidates()
    for candidate in candidates:
        skills_list = candidate["skills"].split(", ")
        for skill in skills_list:
            if skill == skill_name.lower():
                result.append(candidate)
    return result



