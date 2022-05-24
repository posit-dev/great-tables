from platform import python_version


def load_text(input_file):
        """Load text from a text file and return as a string."""
        with open(input_file, "r") as file:
            text = file.read()
        return text

print(load_text("table.html"))
