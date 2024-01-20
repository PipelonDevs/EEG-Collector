
import os


def list_files(path, extension=None):
    """
    Lists all files in a directory with a given extension.
    parameters:
    """
    if extension is None:
        return os.listdir(path)
    
    extension = extension.replace(".", "")
    return [f for f in os.listdir(path) if f.endswith(f".{extension}")]



if __name__ == "__main__":
    print(list_files("./Datasets/GameDatasets"))
    print(list_files("./Datasets/GameDatasets/user123_league of legends_2024-01-15"))
    print(list_files("./Datasets/GameDatasets/user123_league of legends_2024-01-15", extension="json"))