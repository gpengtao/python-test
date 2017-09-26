#!/usr/bin/python
# -*- coding: UTF-8 -*-

# from gpt.employee import *
import gpt.employee

employee = gpt.employee.Employee("john", 100)

employee.display_employee()
employee.show_class_name()

gpt.employee.say_hello("john")
