from typing import Optional
from scr.repository.repo import *
from entities import *

class User_service:
    def register(self, login: str, password: str, role: str):
        Repo.add_user(User(login=login, password=password, role=role))

    def login(self, login: str, password: str) -> Optional[User]:
        for user in Repo.users:
            if (user.login == login and user.password == password):
                return Optional(user)
        return Optional(None)

    def allUsers(self):
        return Repo.get_users()


class Task_service:
    def leaderboard(self, task_id: int):
        ans = [res for res in Repo.get_results() if res.task_id == task_id]
        ans.sort(key = lambda result: result.score)
        return ans

    def get_tasks(self):
        return Repo.get_tasks

    def get_submissions(self):
        return Repo.get_submissions

    def add_task(self, desc: str, deadline: datetime, teacher_id: int):
        Repo.add_task(Task(desc=desc, deadline=deadline, teacher_id=teacher_id))

    def submit(self, user_id: int, task_id: int, filename: str):
        if (not Repo.check_role(user_id, "student")):
            return
        Repo.add_submission(Submission(task_id=task_id, filename=filename, user_id=user_id))

    def feedback(self, submission_id: int, eval_user_id: int, feedback: str):
        if (not Repo.check_role(eval_user_id, "teacher")):
            return
        Repo.submissions[submission_id].add_feedback(feedback)

    def fix(self, submission_id: int, user_id: int, feedback: str):
        if (not Repo.check_role(user_id, "student")):
            return
        Repo.submissions[submission_id].add_fixes(feedback)

    def set_deadline(self, user_id: int, task_id: int, deadline: datetime):
        if (not Repo.check_role(user_id, "teacher")):
            return
        task = Repo.get_task(task_id)
        task.deadline = deadline
        Repo.tasks[task_id] = task
