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


def get_all_candidates() -> List[dict]:
    return load_candidates()


def get_by_id(id):
    """
    Поиск кандидата с указанным id
    :param id: id
    :return: данные кандидата,с заданным id в формате dict
    """
    for candidate in load_candidates():
        if candidate['id'] == id:
            return candidate


def get_candidates_by_name(candidate_name):
    """
    Поиск кандидатов по имени
    :param candidate_name: искомое имя
    :return: список кандидатов с указанным именем
    """
    candidates_by_name = []
    candidates = load_candidates()
    for candidate in candidates:
        names_list = candidate['name'].split(" ")
        # print(names_list)
        for name in names_list:
            if name.lower() == candidate_name.lower():
                candidates_by_name.append(candidate)
                break
    return candidates_by_name

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
            if skill.lower() == skill_name.lower():
                result.append(candidate)
                break
    return result


# print(get_candidates_by_name("adela"))