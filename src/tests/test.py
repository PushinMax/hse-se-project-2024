import random
import secrets
import string
from entities import *
from service import *
from typing import Optional
import unittest
import os
from flask import Flask, request


class TestCase(unittest.TestCase):
    def test_login(self):
        alphabet = string.ascii_letters + string.digits
        size = 1000
        for i in range(1000):
            login = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
            password = ''.join(secrets.choice(alphabet) for i in range(20))
            user = User_service.register(login=login, password=password, role=("student", "teacher")[i == 0])
        self.assertEqual(len(User_service.allUsers()), size)

    def test_task_creation(self):
        teacher_id = 0
        size = 1000
        for i in range(1000):
            desc = ''.join(random.choices(string.ascii_uppercase + string.digits, k=25))
            datetime = datetime.datetime(2024, 10, i % 30)
            Task_service.add_task(desc, deadline=datetime, teacher_id=teacher_id)

        self.assertEqual(len(Task_service.get_tasks()), size)

    def test_set_deadline(self):
        num = random(1000)
        time = datetime.datetime.now()
        Task_service.set_deadline(0, num, datetime.datetime.now())
        self.assertEquals(Task_service.get_tasks()[num].deadline, time)

        time = datetime.datetime.now()
        Task_service.set_deadline(1, num, datetime.datetime.now())
        self.assertNotEquals(Task_service.get_tasks()[num].deadline, time)

    def test_submission(self):
        teacher_id = 0
        user_id = 1
        task_id = random(1000)
        filename = open('m.txt', 'w+')
        filename.write("My solution")
        filename.close()
        Task_service.submit(user_id, task_id, 'm.txt')

        Task_service.feedback(teacher_id, task_id, "You forgot second case")
        Task_service.get_tasks()[task_id].score = 8

        Task_service.fixed(user_id, task_id, "m1.txt")

        Task_service.feedback(teacher_id, task_id, "Thats right")
        Task_service.get_tasks()[task_id].score = 10
