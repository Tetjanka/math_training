from django.shortcuts import render
from abc import ABC, abstractmethod
import random

class Task:
    def action(self):
        pass


class Addition (Task):
    def action (self):
        numberOne = random.randint(0, 100)
        numberTwo = random.randint(0, 100)
        res = numberOne + numberTwo
        return numberOne, numberTwo, res


class Subtraction (Task):
    def action (self):
        numberOne = random.randint(0, 100)
        numberTwo = random.randint(0, 100)
        if numberOne > numberTwo:
            res = numberOne - numberTwo
            return numberOne, numberTwo, res
        else:
            res = numberTwo - numberOne
            return numberTwo, numberOne, res


class Division (Task):
    def action (self):
        numberOne = random.randint(0, 11)
        numberTwo = random.randint(0, 11)
        res = numberOne * numberTwo
        return res, numberTwo, numberOne



class Multiplication (Task):
    def action (self):
        numberOne = random.randint(0, 11)
        numberTwo = random.randint(0, 11)
        res = numberOne * numberTwo
        return numberOne, numberTwo, res
