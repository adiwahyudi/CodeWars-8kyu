def set_alarm(employed, vacation):
    if (employed == True and vacation == False):
        return True
    elif (employed == False or vacation == False):
        return False
    else:
        return False