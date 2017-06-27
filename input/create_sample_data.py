# python input/create_sample_data.py

import random
output_file = open('./input/train','w')
# output_file2 = open('./input/validate','w')
for i in range(451):
    n1 = random.randrange(10)
    n2 = random.randrange(10)
    n3 = random.randrange(10)
    n4 = random.randrange(10)
    # n5 = n1 * n2 * n3 * n4
    n5 = n1 + n2 + n3 + n4
    output_file.write("%s %s %s %s %s \n" % (n1, n2, n3, n4, n5))

# for i in range(50):
#     n1 = random.randrange(10)
#     n2 = random.randrange(10)
#     n3 = random.randrange(10)
#     n4 = random.randrange(10)
#     # n5 = n1 * n2 * n3 * n4
#     n5 = n1 + n2 + n3 + n4
#     output_file2.write("%s %s %s %s %s \n" % (n1, n2, n3, n4, n5))

output_file.close()
# output_file2.close()
print "output file created successfully"
