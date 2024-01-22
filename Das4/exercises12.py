# 12.Line Segment Intersection
# You are given four real numbers- a1, b1, a2, b2 - The endpoints of two
# line segments on a line. Find the length of their intersection. Note that the
# order of the endpoints of a segment is irrelevant, i.e. the segments [1;2]
# and [2;1] are considered the same.
a1 = float(input("Enter the first endpoint (a1): "))
b1 = float(input("Enter the second endpoint (b1): "))
a2 = float(input("Enter the first endpoint (a2): "))
b2 = float(input("Enter the second endpoint (b2): "))
segment1 = sorted([a1, b1])
segment2 = sorted([a2, b2])

int_length = max(0, min(segment1[1], segment2[1]) - max(segment1[0], segment2[0]))

print(int_length)