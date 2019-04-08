import task1.stack as stack


class Browser:
    def __init__(self):
        self._fs = stack.ArrayStack()  # forwards stack
        self._bs = stack.LinkedListStack()  # backwards stack

    @staticmethod
    def print_url(action, url):
        print(f'action: {action} -- current page is {url}')

    def open(self, url):
        self._bs.push(url)
        self.print_url('open', url)

    def back(self):
        if len(self._bs) == 0 and len(self._fs) == 0:
            print('the action after open!!')
            return
        if len(self._bs) > 0:
            self._fs.push(self._bs.pop())
            if len(self._bs) > 0:
                self.print_url('back', self._bs.peek())
        else:
            print('no pages to back, try go or open')

    def go(self):
        if len(self._bs) == 0 and len(self._fs) == 0:
            print('the action after back!!')
            return
        if len(self._fs) > 0:
            self._bs.push(self._fs.pop())
            self.print_url('go', self._bs.peek())
        else:
            print('no pages to go, try back or open')

    def close(self):
        self._bs.clear()
        self._fs.clear()

    def state(self):
        print(f'fs:{self._fs}')
        print(f'bs:{self._bs}')


if __name__ == '__main__':
    try:
        browser = Browser()
        browser.go()
        browser.back()
        browser.open('www.google.com')
        browser.open('www.github.com')
        browser.open('www.52nlp.com')
        browser.open('spark.apache.com')
        browser.open('www.python.com')
        browser.back()
        browser.back()
        print('----stack state---')
        browser.state()
        browser.back()
        browser.back()
        browser.close()
        browser.state()
    except IndexError as e:
        print(f'test happen error:{e}')
