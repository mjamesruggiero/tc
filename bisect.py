#!/usr/bin/python
#
# Thu Apr  5 22:22:12 PDT 2012
# mruggiero
# from think complexity chapter 3
# create a bisection function
def bisect(sorted_list, needle, offset=0):
    """using bisection, find an item in a sorted
    list and return it's place in the index.
    if it's not there, return none"""
    if needle == sorted_list[0]: return offset
    if len(sorted_list) < 2: return None

    pivot = len(sorted_list) / 2
    left_section = sorted_list[:pivot]
    right_section = sorted_list[pivot:]

    #print "1. right section is:"
    #print right_section
    #print "1. left section is:"
    #print left_section
    if needle > left_section[-1]:
        #print "2. right section is:"
        #print right_section
        return bisect(right_section, needle, offset + len(right_section))
    else:
        #print "2. left section is:"
        #print left_section
        return bisect(left_section, needle, offset)

def test_bisect():
    lists = [
        [0, 11,34,56,77],
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17],
        [1,4,5],
        [1,2,3,5,6,7,8,12,14,16]
    ]
    for l in lists:
        found = bisect(l, 8)
        print "list was:"
        print l
        if found:
            print "found needle at %d" % found
        else:
            print "Not found"

if __name__ == '__main__':
    test_bisect()
