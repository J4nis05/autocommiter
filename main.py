import git


def git_commit(msg):
    # Commit Changes
    repo.git.add('--all')
    repo.index.commit(msg)


def git_push():
    # Push changes to GitHub
    origin = repo.remote(name='origin')
    origin.push()


def get_count():
    with open('/scripts/autocommiter/count.txt', 'r') as file:
        number = file.read()
    return int(number)


def add_count(number):
    new_number = number + 1
    with open('/scripts/autocommiter/count.txt', 'w') as f:
        f.write(str(new_number))
    return f"Count increased by 1. It is now at {new_number}."


def get_line(line_number):
    with open('/scripts/autocommiter/source.txt', 'r') as file:
        lines = file.readlines()
        # Check if the line number is valid
        if 1 <= line_number <= len(lines):
            return lines[line_number - 1].strip()
        else:
            print(f"Error: Line number {line_number} is out of range.")
            return lines[1].strip()


def add_line(text):
    with open('/scripts/autocommiter/script.txt', 'a') as file:
        file.write(f"{text}\n")


repo = git.Repo('/scripts/autocommiter/')

count = get_count()              # Get Current Script line
current_text = get_line(count)   # Set Text to insert
add_line(current_text)           # Add Text to Output file
add_count(count)                 # Increase Count by 1
git_commit(f"Added {count}")     # Commit the changes
git_push()                       # Push the changes
