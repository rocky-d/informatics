from random import randint


class PageExchanger(object):

    def __init__(self, len_frames: int, pages: list[int], debug = False) -> None:
        self.len_frames: int = len_frames
        self.pages: list[int] = pages
        self.debug: bool = debug

    def __print(self, *args, **kwargs) -> None:
        if self.debug:
            print(*args, **kwargs)

    def opt(self) -> float:
        page_loss: int = 0
        frames: list[int | None] = [None for _ in range(self.len_frames)]
        indexes: list[int | None] = [None for _ in range(self.len_frames)]
        for i, num in enumerate(self.pages):
            self.__print(frames)
            if num in frames:
                continue
            else:  # elif num not in frames:
                page_loss += 1
                longest = -1, -1
                for j in range(self.len_frames):
                    indexes[j] = self.pages.index(frames[j], i + 1) if frames[j] in self.pages[i + 1:] else len(self.pages)
                    if len(self.pages) == indexes[j]:
                        longest = self.pages, j
                        break
                    elif longest[0] < indexes[j]:
                        longest = indexes[j], j
                frames.pop(longest[1])
                frames.insert(0, num)
        else:
            self.__print(frames)
        return page_loss / len(self.pages)

    def fifo(self) -> float:
        page_loss: int = 0
        frames: list[int | None] = [None for _ in range(self.len_frames)]
        for i, num in enumerate(self.pages):
            self.__print(frames)
            if num in frames:
                continue
            else:  # elif num not in frames:
                page_loss += 1
                frames.pop(-1)
                frames.insert(0, num)
        else:
            self.__print(frames)
        return page_loss / len(self.pages)

    def lru(self) -> float:
        page_loss: int = 0
        frames: list[int | None] = [None for _ in range(self.len_frames)]
        for i, num in enumerate(self.pages):
            self.__print(frames)
            if num in frames:
                frames.remove(num)
                frames.insert(0, num)
            else:  # elif num not in frames:
                page_loss += 1
                frames.pop(-1)
                frames.insert(0, num)
        else:
            self.__print(frames)
        return page_loss / len(self.pages)

    def sc(self) -> float:
        page_loss: int = 0
        frames: list[int | None] = [None for _ in range(self.len_frames)]
        tags: list[bool] = [True for _ in range(self.len_frames)]
        for i, num in enumerate(self.pages):
            self.__print(frames)
            if num in frames:
                tags[frames.index(num)] = True
            else:  # elif num not in frames:
                page_loss += 1
                while tags[-1]:
                    frames.insert(0, frames.pop(-1))
                    tags.pop(-1)
                    tags.insert(0, False)
                else:
                    frames.pop(-1)
                    frames.insert(0, num)
                    tags.pop(-1)
                    tags.insert(0, True)
        else:
            self.__print(frames)
        return page_loss / len(self.pages)

    def clock(self) -> float:
        page_loss: int = 0
        frames: list[int | None] = [None for _ in range(self.len_frames)]
        tags: list[bool] = [True for _ in range(self.len_frames)]
        pointer = self.len_frames - 1
        for i, num in enumerate(self.pages):
            self.__print(frames)
            if num in frames:
                tags[frames.index(num)] = True
            else:  # elif num not in frames:
                page_loss += 1
                pointer = (pointer + 1) % self.len_frames
                while tags[pointer]:
                    tags[pointer] = False
                    pointer = (pointer + 1) % self.len_frames
                else:
                    frames[pointer] = num
                    tags[pointer] = True
        else:
            self.__print(frames)
        return page_loss / len(self.pages)


def random_pages(max_page: int, len_pages: int) -> list[int]:
    pages = []
    for _ in range(len_pages):
        pages.append(randint(a = 1, b = max_page))
    return pages


if __name__ == '__main__':
    len_frames_ = int(input('主存页框数：'))
    max_page_ = int(input('总页面数：'))
    len_pages_ = int(input('页面随机调用次数：'))

    pages_ = random_pages(
        max_page = max_page_,
        len_pages = len_pages_
    )
    # print('页面调用顺序：')
    # print(f"{pages_ = }")
    # print()

    # pageExchanger = PageExchanger(
    #     len_frames = len_frames_,
    #     pages = [6, 7, 6, 5, 9, 6, 8, 9, 7, 6, 9, 6],
    #     debug = True
    # )
    pageExchanger = PageExchanger(
        len_frames = len_frames_,
        pages = pages_,
        debug = False
    )
    print('缺页中断率：')
    print(f"{pageExchanger.opt() = }")
    print()
    print(f"{pageExchanger.fifo() = }")
    print()
    print(f"{pageExchanger.lru() = }")
    print()
    print(f"{pageExchanger.sc() = }")
    print()
    print(f"{pageExchanger.clock() = }")
    print()
