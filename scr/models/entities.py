from datetime import datetime


class User:
    def __init__(self, id: int, name: str, surname: str, login: str, password: str, role: str, group_id: str) -> None:
        self.id       = id
        self.login    = login
        self.password = password
        self.role     = role

class Submission:
    def __init__(self, submission_id: int, user_id: int, task_id: int, datetime: datetime):
        self.submission_id = submission_id
        self.sumbission_time = datetime
        self.user_id = user_id
        self.task_id = task_id
        self.filename = None
        self.feedback = []
        self.fixes = []

    def add_feedback(self, feedback: str):
        self.feedback.append(feedback)

    def add_fixes(self, fixes: str):
        self.fixes.append(fixes)

class Task:
    def __init__(self, task_id: int, desc: str, deadline: datetime, teacher_id: int):
        self.task_id = task_id
        self.desc = desc
        self.teacher_id = teacher_id
        self.deadline = deadline

    def set_deadline(self, deadline: datetime):
        self.deadline = deadline

class Result:
    def __init__(self, result_id: int, user_id: int, task_id: int, score: int):
        self.result_id = result_id
        self.user_id = user_id
        self.score = score
        self.task_id = task_id
