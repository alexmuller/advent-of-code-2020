def parse_restriction(restriction):
    if 'no other bags' in restriction:
        return []

    parent, children = restriction.split(' bags contain ')
    children = children.split(', ')
    children = [child.replace('.', '').replace('bags', '').replace('bag', '').strip() for child in children]

    return [(parent, child[2:], int(child[:1])) for child in children]
