# coding: utf-8
import string


def crypt(word=None, elements=None):
    #import ipdb; ipdb.set_trace()
    result_list = []

    for c in word:
        position = elements.index(c) + 3
        try:
            result_list.append(elements[position])
        except:
            big_list = elements + elements
            result_list.append(big_list[position])

    return result_list


def decrypt(word=None, elements=None):
    #import ipdb; ipdb.set_trace()
    result_list = []

    for c in word:
        position = elements.index(c) - 3
        try:
            result_list.append(elements[position])
        except:
            big_list = elements + elements
            result_list.append(big_list[position])

    return result_list

if __name__ == '__main__':
    alphabet = list(string.ascii_lowercase)
    crazy_list = list(
        'macacbananacasachicobentowolo' +
        'lorafaelzabumbaaimellldeuuussxaropaiadakiwiyyxuxa')

    crazy_list = list(set(crazy_list))

    wordc_1 = ''.join(crypt(word='xyzrafael', elements=alphabet))
    wordc_2 = ''.join(crypt(word='xyzrafael', elements=crazy_list))

    wordd_1 = ''.join(decrypt(word=wordc_1, elements=alphabet))
    wordd_2 = ''.join(decrypt(word=wordc_2, elements=crazy_list))

    print('Encrypted: ', wordc_1)
    print('Decrypted: ', wordd_1)

    print('Encrypted: ', wordc_2)
    print('Decrypted: ', wordd_2)
