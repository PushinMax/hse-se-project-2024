from typing import List
from entities import *


class Repo:
    users = []
    submissions = []
    tasks = []
    results = []

    def get_users(self) -> List[User]:
        return self.users

    def get_tasks(self) -> List[Task]:
        return self.tasks

    def get_results(self) -> List[Result]:
        return self.results

    def get_user(self, id: int) -> User:
        return self.users[id]

    def get_task(self, id: int) -> Task:
        return self.tasks[id]

    def get_submission(self, submission_id) -> Submission:
        return self.submission[submission_id]

    def get_result(self, result_id) -> Result:
        return self.results[result_id]

    def add_user(self, user: User):
        self.users.append(user)
        self.users[-1].user_id = len(self.users)

    def add_task(self, task: Task):
        self.tasks.append(task)
        self.tasks[-1].task_id = len(self.tasks)

    def add_submission(self, sub: Submission):
        self.submissions.append(sub)
        self.submissions[-1].submission_id = len(self.submissions)

    def check_role(self, user_id:int, role: str):
        return self.get_user[user_id].role == role

    def check_deadline(self, submission_id: int):
        submission = self.get_submission(submission_id)
        task = self.get_task(submission.task_id)
        return submission.sumbission_time < task.deadline
