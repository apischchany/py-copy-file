def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    source = parts[1]
    destination = parts[2]
    if source == destination:
        return

    try:
        with open(source, "r") as src_file, \
                open(destination, "w") as dest_file:
            data = src_file.read()
            dest_file.write(data)
    except FileNotFoundError:
        print("Error: One or both files not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"Error: {e}")
