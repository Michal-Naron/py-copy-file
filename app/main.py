def copy_file(command: str) -> None:
    if command == "":
        return
    if len(command.split()) != 3:
        return
    cp, file, file_copy = command.split()
    if cp != "cp":
        return
    if file == file_copy:
        return
    try:
        with open(file, "r") as file1, open(file_copy, "w") as file_copy1:
            old_file = "".join(file1.readlines())
            file_copy1.write(old_file)
    except FileNotFoundError:
        return
