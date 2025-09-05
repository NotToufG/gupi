def scale_minor(root):
    steps=[2,1,2,2,1,2,2]
    s=[root]
    for st in steps:
        s.append(s[-1]+st)
    return s