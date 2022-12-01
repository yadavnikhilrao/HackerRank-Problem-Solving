def count_substring(string, sub_string):
    for i in range(len(string)):
        if string[i] in sub_string:
            return i

if __name__ == '__main__':
