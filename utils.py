import json

CANDIDATES = "candidates.json"


def load_json(file: json = CANDIDATES) -> list[dict]:
    with open(file, encoding="utf-8") as f:
        return json.load(f)


def preformat_candidates(lst: list[dict]) -> str:
    brief = ""
    for candidate in lst:
        brief += f"Имя кандидата: {candidate['name']}\n" \
                 f"Позиция кандидата: {candidate['position']}\n" \
                 f"Навыки: {candidate['skills']}\n\n"
    return brief


def get_candidate_by_id(uid: int) -> list[dict] | None:
    lst: list[dict] = load_json()
    for candidate in lst:
        if candidate['id'] == uid:
            return [candidate]
    return None


def get_candidate_by_skill(skill: str) -> list[dict]:
    lst = load_json()
    candidates = []
    for candidate in lst:
        skills = candidate['skills'].lower().split(", ")
        if skill.lower() in skills:
            candidates.append(candidate)
    return candidates
