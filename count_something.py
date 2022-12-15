import collections


def count(something_list):
    """
    count something_list
    ex) 'a', 'b', 'a' >> {'a': 2, 'b':1}
    """
    count_dict = collections.defaultdict(int)
    for name in something_list:
        count_dict[name] += 1
    return dict(count_dict)


def main():
    last_name_list = ['ushzawa', 'fukuda', 'izumi', 'izumi', 'ebe', 'izumi', 'fukuda']
    print(count(last_name_list))


if __name__ == '__main__':
    main()

