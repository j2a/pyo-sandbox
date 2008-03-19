# -*- coding: koi8-r -*-
# twistedpythy.tac:  simple TAC for TwistedPythy
# Pythy <the.pythy@gmail.com>

from twisted.application import service

from TwistedPythy import tap

options = {
    'listen-port': 3000,    # ����, �� ������� ����� ����������
    'delay': 5,             # �������� ����� �������
    'encoding': 'utf-8',    # ��������� ����������
    }


application = service.Application("TwistedPythy")
s = tap.makeService(options)
s.setServiceParent(application)
