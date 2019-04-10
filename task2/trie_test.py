import task2.trie as trie


if __name__ == '__main__':
    try:
        t = trie.Trie()
        t.insert('hello')
        t.insert('he')
        t.search('hello')
        print(t.search('he'))
        print(t.search('hel'))
        print(t.search('hello'))
        print(t.starts_with('hell'))
    except Exception as e:
        print(f'test happen error:{e}')
