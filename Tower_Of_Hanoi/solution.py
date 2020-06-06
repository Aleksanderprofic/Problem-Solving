"""                 Example
      At the start                 At the end
    _       |       |           |       |       _
   ___      |       |           |       |      ___
  _____     |       |           |       |     _____
 _______    |       |           |       |    _______

 where only smaller disk can be on top of the bigger disk
"""


def tower(n, start, end, middle):
    if n == 1:
        print(f"Move {n} from {start} to {end}")
    else:
        tower(n - 1, start, middle, end)
        print(f"Move {n} from {start} to {end}")
        tower(n - 1, middle, end, start)


tower(4, "A", "C", "B")
