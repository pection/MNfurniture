import os


def usewalk():
    for root, dirname, filenames in os.walk("./../.."):
        for filename in filenames:
            print(os.path.join(root, filename))


usewalk()
