import pytest
import sys
from io import StringIO
import result
data=[]
with open("test_data1.txt") as file:
    lines=file.readlines()
    for line in lines: 
        data.append(line.split())

def test_f(capsys):
    sys.stdin = StringIO(str(data[0][0])+"\n")
    sys.stdin = StringIO(str(data[0][1])+"\n")
    captured=capsys.readouterr()
    assert captured.out == str(data[0][2])


