import os
import sys


def main():
    """
    Main function to orchestrate the analysis of an Obsidian vault.
    Prompts the user for the vault path, processes the data, analyzes it, and exports the results.
    """
    global path
    # Prompt the user to input the path to their Obsidian vault
    path = input("Enter your Obsidian vault path: ")

    # Step 1: Get cleaned data by processing the vault and excluding specified paths
    cleaned_data = getting_data(path, excluded_path())

    # Step 2: Analyze the cleaned data to categorize tasks
    analyzed_data = analyzing_data(cleaned_data)

    # Step 3: Export the analyzed data to a summary file
    export_data(analyzed_data, path)

    # Notify the user that the analysis is complete
    print("Analysis created successfully")


def excluded_path() -> list:
    """
    Prompts the user to specify folders to exclude from the analysis.

    Returns:
        list: A list of paths to exclude from processing.
    """
    excluded_paths = []
    while True:
        # Ask the user if they want to exclude any folders
        choice = input("Do you want to exclude any folder?(y/n) ").strip().lower()

        # If the user chooses not to exclude any folders, break the loop
        if choice == "n":
            break
        elif choice == "y":
            while True:
                # Prompt the user to input the path of the folder to exclude
                f_path = input("Enter the path: ")
                excluded_paths.append(f_path)

                # Ask if the user wants to exclude another folder
                another = (
                    input("Do you want to exclude any other path?(y/n) ")
                    .strip()
                    .lower()
                )
                if another != "y":
                    break
        break
    return excluded_paths


def getting_data(raw_data_path: str, excluded_paths: list) -> str:
    """
    Processes the Obsidian vault to extract task data from markdown files.

    Args:
        raw_data_path (str): The path to the Obsidian vault.
        excluded_paths (list): A list of paths to exclude from processing.

    Returns:
        str: The path to the cleaned data file.

    Raises:
        SystemExit: If the specified directory is not found.
    """
    try:
        # Define the path for the cleaned data file
        cleaned_data_file_path = f"{raw_data_path}\\cleaned_data.txt"

        # Open the cleaned data file for writing
        with open(
            cleaned_data_file_path, mode="w", encoding="utf-8"
        ) as cleaned_data_file:
            # Walk through the directory structure of the Obsidian vault
            for root, _, files in os.walk(top=raw_data_path):
                # Skip excluded paths
                if excluded_paths is None or root in excluded_paths:
                    continue

                # Process each file in the directory
                for file in files:
                    # Only process markdown files
                    if not file.endswith(".md"):
                        continue

                    # Construct the full path to the file
                    full_path = os.path.join(root, file)

                    # Open the markdown file and read its contents
                    with open(file=full_path, mode="r", encoding="utf-8") as note:
                        # Extract lines that represent tasks
                        for line in note:
                            if (
                                line.startswith("- [x]")
                                or line.startswith("- [/]")
                                or line.startswith("- [ ]")
                                or line.startswith("- [-]")
                            ):
                                # Write the task line to the cleaned data file
                                cleaned_data_file.write(f"{line}\n")

        # Return the path to the cleaned data file
        return cleaned_data_file_path

    except FileNotFoundError:
        # Exit the program if the directory is not found
        sys.exit("Directory not found.")


def analyzing_data(cleaned_data_file_path: str) -> tuple:
    """
    Analyzes the cleaned data to categorize tasks into completed and incomplete.

    Args:
        cleaned_data_file_path (str): The path to the cleaned data file.

    Returns:
        tuple: A tuple containing two lists:
            - completed: List of completed tasks.
            - not_completed: List of incomplete tasks.
    """
    path = cleaned_data_file_path
    completed = []
    not_completed = []

    # Open the cleaned data file for reading
    with open(path, "r", encoding="utf-8") as cleaned_file:
        # Process each line in the file
        for line in cleaned_file:
            line = line.strip()
            # Categorize tasks based on their status
            if (
                line.startswith("- [ ]")
                or line.startswith("- [/]")
                or line.startswith("- [-]")
            ):
                not_completed.append(line)
            elif line.startswith("- [x]"):
                completed.append(line)

    # Return the categorized tasks
    return completed, not_completed


def export_data(analyzed_data: tuple, path: str):
    """
    Exports the analyzed data into a summary report.

    Args:
        analyzed_data (tuple): A tuple containing two lists:
            - completed_list: List of completed tasks.
            - not_completed_list: List of incomplete tasks.
    """
    completed_list, not_completed_list = analyzed_data

    # Calculate the number of completed and incomplete tasks
    completed = len(completed_list)
    not_completed = len(not_completed_list)
    full = len(completed_list) + len(not_completed_list)

    # Calculate the percentage of completed and incomplete tasks
    complete_percentage = completed / full
    not_completed_percentage = not_completed / full

    # Write the summary and task lists to the analysis file
    with open(f"{path}\\analysis.txt", "w", encoding="utf-8") as file:
        file.write(
            f"You've completed {round(complete_percentage*100,2)}%, you haven't completed {round(not_completed_percentage*100,2)}%\n"
        )
        file.write(f"These are the completed tasks {completed} task.\n")
        for line in completed_list:
            file.write(f"{line}\n")
        file.write(f"These are the not completed tasks {not_completed} task.\n")
        for task in not_completed_list:
            file.write(f"{task}\n")


if __name__ == "__main__":
    # Run the main function when the script is executed
    main()
