from itertools import cycle

ls = '''鸽
 鸽
  鸽
   鸽
    鸽
     鸽
      鸽
       鸽
        鸽
         鸽
          鸽
           鸽
            鸽
             鸽
              鸽
               鸽
                鸽
                 鸽
                  鸽
                   鸽
                    鸽
                     鸽
                      鸽
                       鸽
                        鸽
                         鸽
                          鸽
                         鸽
                        鸽
                       鸽
                      鸽
                     鸽
                    鸽
                   鸽
                  鸽
                 鸽
                鸽
               鸽
              鸽
             鸽
            鸽
           鸽
          鸽
         鸽
        鸽
       鸽
      鸽
     鸽
    鸽
   鸽
  鸽
 鸽'''.splitlines()


def main() -> None:
    n = int(input())

    cls = cycle(ls)
    for i in range(n):
        print(next(cls))


if __name__ == '__main__':
    main()
