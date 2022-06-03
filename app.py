from flask import Flask, abort

from utils import load_json, preformat_candidates, get_candidate_by_id, get_candidate_by_skill


app = Flask(__name__)


@app.route("/")
def page_index():
    """
    Main page

    :return: List of candidates
    """
    return f"<pre>\n{preformat_candidates(load_json())}\n</pre>"


@app.route("/candidates/<int:uid>")
def page_candidate(uid: int):
    """
    Page with info about the candidate by id

    :param uid: candidate's id
    :return: info about the candidate
    """
    candidate: list = get_candidate_by_id(uid)
    if candidate is None:
        abort(404)
    else:
        return f"<pre>\n" \
               f"<img src={candidate[0]['picture']}></img>\n" \
               f"{preformat_candidates(candidate)}\n" \
               f"</pre>"


@app.route("/skills/<skill>")
def page_skills(skill: str):
    """
    Page with list of the candidates filtered by their skills

    :param skill: skill for filter
    :return: list of the candidates filtered by their skills
    """
    candidates: list = get_candidate_by_skill(skill)
    return f"<pre>\n{preformat_candidates(candidates)}\n</pre>"


if __name__ == "__main__":
    app.run()
