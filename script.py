import shutil
import os

# Ensure we're working in the correct directory
print("Current Directory:", os.getcwd())

# Create a zip archive of all files in the current directory
shutil.make_archive(
    base_name="assignment",  # The name of the resulting zip file
    format="zip",            # Archive format
    root_dir=".",            # The root directory to include
    base_dir=".",            # Only include files in the current directory, not the directory itself
    verbose=True
)

print("Zipping complete: 'assignment.zip' created in the current directory.")
