# replace yield inside for loop with yield from

def get_content(entry):
    for block in entry.get_blocks():
        yield block


def get_contents(entry):
    yield from entry.get_blocks()
