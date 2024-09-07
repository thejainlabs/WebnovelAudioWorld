import os

def generate_html(directory, output_file):
    try:
        # Get a list of all folders inside the specified directory
        folder_names = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
        
        # Start building the HTML content
        html_content = "<html>\n<head>\n<title>Folder List</title>\n</head>\n<body>\n<ul>\n"
        
        # Add each folder name wrapped in <li> and <a> tags
        for folder in folder_names:
            html_content += f'  <li><a href="../{folder}.html">{" ".join(folder.split("_"))}</a></li>\n'
        
        # Close the HTML content
        html_content += "</ul>\n</body>\n</html>"
        
        # Write the HTML content to the output file
        with open(output_file, "w") as file:
            file.write(html_content)
        
        print(f"HTML file '{output_file}' has been created successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the directory and the output HTML file name
directory_path = r"novels"
output_html = "folders_list.html"

# Generate the HTML file
generate_html(directory_path, output_html)
