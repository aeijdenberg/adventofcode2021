import json, sys


def desc(ctx, t, path):
    if type(t) == int:
        if ctx['state'] == 0:
            ctx['last_num_path'] = path
        elif ctx['state'] == 1:
            ctx['next_num_path'] = path
            ctx['state'] = 2
    elif ctx['state'] == 0 and len(path) == 4: # explode!
        ctx['explode_path'] = path
        ctx['state'] = 1
    else:
        for idx, tt in enumerate(t):
            desc(ctx, tt, path + [idx])
            if ctx['state'] == 2:
                break

def get_and_set(things, path, f):
    cursor = things
    for x in path[:-1]:
        cursor = cursor[x]
    val_to_set, val_to_return = f(cursor[path[-1]])
    cursor[path[-1]] = val_to_set
    return val_to_return
    
def try_explode(thing):
    ctx = {
        'state': 0,
        'explode_path': None,
        'last_num_path': None,
        'next_num_path': None,
    }       
    desc(ctx, thing, [])
    if ctx['explode_path'] is None:
        return False

    left_val, right_val = get_and_set(thing, ctx['explode_path'], lambda x: (0, x))
    if ctx['last_num_path'] is not None:
        get_and_set(thing, ctx['last_num_path'], lambda x: (x + left_val, None))
    if ctx['next_num_path'] is not None:
        get_and_set(thing, ctx['next_num_path'], lambda x: (x + right_val, None))
    
    return True
    

def split_desc(ctx, t, path):
    if type(t) == int:
        if ctx['state'] == 0:
            if t >= 10:
                ctx['split_path'] = path
                ctx['state'] = 1
    else:
        for idx, tt in enumerate(t):
            split_desc(ctx, tt, path + [idx])
            if ctx['state'] == 1:
                break

def try_split(thing):
    ctx = {
        'state': 0,
        'split_path': None,
    }       
    split_desc(ctx, thing, [])
    if ctx['split_path'] is None:
        return False
    
    get_and_set(thing, ctx['split_path'], lambda x: ([x // 2, x - (x // 2)], None))

    return True


def find_reduce(total):
    while True:
        if try_explode(total):
            continue
        if try_split(total):
            continue
        return

def magnitude(thing):
    if type(thing) == int:
        return thing
    else:
        return (3 * magnitude(thing[0])) + (2 * magnitude(thing[1]))

total = None
for line in open('input'):
    n = json.loads(line.strip())
    if total is None:
        total = n
    else:
        total = [total, n]
    find_reduce(total)

print(magnitude(total))
