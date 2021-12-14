# fibonacci sequence

def fibonacci_(idx):
    if idx <= 1:
        return idx 
    return fibonacci_(idx - 1) + fibonacci_(idx - 2)
print(fibonacci_(3))