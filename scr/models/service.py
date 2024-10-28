from repo import *
from entities import *

class User_service:
    def register(self, login: str, password: str, role: str):
        Repo.add_user(User(login=login, password=password, role=role))

    def login(self, login: str, password: str):
        for user in Repo.users:
            if (user.login == login):
                return user.password == password
        return False


class Task_service:
    def leaderboard(self, task_id: int):
        ans = [res for res in Repo.get_results() if res.task_id == task_id]
        ans.sort(key = lambda result: result.score)
        return ans

    def submit(self, user_id: int, task_id: int, filename: str):
        Repo.add_submission(Submission(task_id=task_id, filename=filename, user_id=user_id))

    def feedback(self, submission_id: int, eval_user_id: int, feedback: str):
        Repo.submissions[submission_id].add_feedback(feedback)

    def fix(self, submission_id: int, user_id: int, feedback: str):
        Repo.submissions[submission_id].add_fixes(feedback)

    def set_deadline(self, user_id: int, task_id: int, deadline: datetime):
        task = Repo.get_task(task_id)
        task.deadline = deadline
        Repo.tasks[task_id] = task
