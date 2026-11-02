from pathlib import Path


def create_repo(argv1, argv2):
    current_path = Path(".")
    repo_directory = current_path / ".end"
    if not argv2:
        if argv1 == "init":
            if repo_directory.exists():
                print("Repository already exists")
                return
            repo_directory.mkdir(parents=True)
            print("Repository created")
            return

    if argv1 == "add" and argv2 == ".":
        if not repo_directory.exists():
            print("Repository is not initialized, please create a repository")
            return

        repo_directory = repo_directory / "meow.txt"
        repo_directory.touch(exist_ok=True)
        print("meow.txt added to repository")
        return

    print(f"Invalid command: {argv1} {argv2}")
    return
