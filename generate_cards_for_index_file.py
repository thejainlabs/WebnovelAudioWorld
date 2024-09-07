import os

def generate_novel_cards(novels_directory, output_file, img_directory):
    try:
        # Get a list of all folders inside the novels directory
        folder_names = [name for name in os.listdir(novels_directory) if os.path.isdir(os.path.join(novels_directory, name))]
        
        # Start building the HTML content for the novel cards
        cards_html = ""

        for folder in folder_names:
            # Sanitize folder names to create file names and inner text (title-case for display)
            folder_display_name = folder.replace('_', ' ').title()  # Format folder names for display
            html_file_name = f"{folder}.html"  # HTML file name
            img_file_name = f"{folder}.jpg"  # Image file name

            # Create the HTML content for each card
            card_html = f"""
<!-- novel card start -->
<div class="col-xl-3 col-lg-4 col-md-6 mb-4">
  <div class="card text-bg-dark">
    <a href="assets/novels/{html_file_name}">
      <img src="assets/img/novels/{img_file_name}" class="card-img" alt="{folder_display_name}">
      <div class="card-img-overlay d-flex flex-column justify-content-end">
        <h5 class="novel-name card-title shadow p-2 bg-body-tertiary rounded bg-opacity-75">{folder_display_name}</h5>
      </div>
    </a>
  </div>
</div>
<!-- novel card end -->\n
"""
            cards_html += card_html

        # Write the generated HTML to the output file
        with open(output_file, "w") as file:
            file.write(cards_html)
        
        print(f"HTML file '{output_file}' has been created successfully with {len(folder_names)} novel cards.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the novels directory, image directory, and output HTML file name
novels_directory = "assets/novels"
output_html = "novels_cards.html"
img_directory = "assets/img/novels"

# Generate the novel cards HTML
generate_novel_cards(novels_directory, output_html, img_directory)
