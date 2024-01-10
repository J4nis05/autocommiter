import git

repo = git.Repo('./')


def gitCommit(msg):
    # Commit Changes
    repo.git.add('--all')
    repo.index.commit(msg)


def gitPush():
    # Push changes to GitHub
    origin = repo.remote(name='origin')
    origin.push()
    print("Changes pushed to GitHub.")


def getCount():
    with open('count.txt', 'r') as file:
        number = file.read()
    return int(number)


def addCount(number):
    new_number = number + 1
    with open('count.txt', 'w') as f:
        f.write(new_number)
    return f"Count increased by 1. It is now at {new_number}."


def getLine(line_number):
    with open('source.txt', 'r') as file:
        lines = file.readlines()
        # Check if the line number is valid
        if 1 <= line_number <= len(lines):
            return lines[line_number - 1].strip()
        else:
            print(f"Error: Line number {line_number} is out of range.")
            return lines[1].strip()


def addLine(line_number):
    with open('script.txt', 'a') as file:
        file.write(f"{line_number}\n")


# current_text = getLine(count)
# print(current_text)

gitCommit("UwU")
gitPush()
