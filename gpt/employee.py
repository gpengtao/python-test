#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Employee:
    EmployeeCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.EmployeeCount += 1

    def display_count(self):
        print self.EmployeeCount

    def display_employee(self):
        print self.name + " -> " + str(self.salary)

    def show_class_name(self):
        print self.__class__.__name__


def say_hello(man):
    """say hello"""
    print "hello " + man
