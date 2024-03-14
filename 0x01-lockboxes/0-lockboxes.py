#!/usr/bin/python3
""" Lockboxes """


def CanUnlockAll(boxes):
    """
    Determine if all the boxes cn be opened
    """
    keys = set([0] + boxes[0])
    locked = set()

    for box in boxes:
        ibox = boxes.index(box)
        
        if ibox not in keys:
            if max(keys) > ibox:
                locked.add(ibox)
                continue

        keys |= set(box)
    for key in locked:
        if key in keys:
            keys |= set(boxes[key])
    
    return not bool(locked - keys)
    