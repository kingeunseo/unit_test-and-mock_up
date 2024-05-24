# employee.py
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        if amount > 0:
            self.salary += amount
            return True
        return False

    def get_annual_salary(self):
        return self.salary * 12

    def get_details(self):
        # 여기서 가정하는 외부 서비스 호출이 있다고 가정합니다.
        return {"name": self.name, "annual_salary": self.get_annual_salary()}


# test_employee.py
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Alice", 5000)

    def test_initial_salary(self):
        self.assertEqual(self.employee.salary, 5000)

    def test_give_raise(self):
        self.assertTrue(self.employee.give_raise(1000))
        self.assertEqual(self.employee.salary, 6000)
        self.assertFalse(self.employee.give_raise(-1000))
        self.assertEqual(self.employee.salary, 6000)

    def test_annual_salary(self):
        self.assertEqual(self.employee.get_annual_salary(), 5000 * 12)

if __name__ == '__main__':
    unittest.main()


# test_employee_with_mock.py
import unittest
from unittest.mock import MagicMock
from employee import Employee

class TestEmployeeWithMock(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Alice", 5000)
        self.employee.get_details = MagicMock(return_value={
            "name": "Alice",
            "annual_salary": 60000
        })

    def test_mocked_get_details(self):
        details = self.employee.get_details()
        self.assertEqual(details, {
            "name": "Alice",
            "annual_salary": 60000
        })

if __name__ == '__main__':
    unittest.main()
