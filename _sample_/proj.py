import os


# import sys

def path_data(b):
    d1 = {"ab": r"C:\Users\Naveen Karna\Desktop",
          "ls /root": "/home/nityaobject/Desktop/prasanna/txt/lsro.txt",
          "ls /home/nityaobject": "/home/nityaobject/Desktop/prasanna/txt/lsh.txt",
          "free -k": "/home/nityaobject/Desktop/prasanna/txt/frek.txt",
          "free -h": "/home/nityaobject/Desktop/prasanna/txt/freh.txt",
          "df -h": "/home/nityaobject/Desktop/prasanna/txt/dfh.txt",
          "df -k": "/home/nityaobject/Desktop/prasanna/txt/dfk.txt"
          }
    if b in d1.keys():
        return get_op(d1.get(b), b) + "\tpython"
    else:
        return 'Path not found'


def get_op(a, key):
    empty1 = ""
    d2 = {"ab": r"\naveen.txt"}
    if key in d2.keys():
        empty1 = a + d2.get(key)

    f = open(empty1, 'r')
    return str(f.read())


if __name__ == '__main__':
    path = "ab"
    print(path_data(path))
