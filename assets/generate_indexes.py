import os
import re

def extract_number(filename):
    """Extracts a number from the filename for sorting purposes."""
    match = re.search(r'(\d+)', filename)
    return int(match.group(1)) if match else float('inf')  # Return infinity if no number is found

def generate_folder_index_html(folder_path, files, output_folder):
    """Generates an HTML index file for a given folder and its HTML files."""
    folder_name = os.path.basename(folder_path)
    
    # Sort files numerically based on extracted numbers
    sorted_files = sorted(files, key=lambda file: extract_number(os.path.basename(file)))
    
    html_content = f"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Light Novel Audiobook | Webnovel | Fantasy Audiobook | WebnovelAudioWorld</title>

    <!-- favicon -->
  <link rel="icon" href="../img/favicon.png" type="image/png">

  <!-- Bootstrap css -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  
  <!-- my css -->
  <link rel="stylesheet" type="text/css" href="../../mystyles.css">
</head>
<body data-bs-theme="dark">
  <header>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container">
        <a class="navbar-brand" href="https://webnovelaudioworld.com/">
          <img class="img-fluid w-50" src="../img/logo.png" alt="webnovel audio world" /></a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse justify-content-center" id="navbarNavDropdown">
            <ul class="navbar-nav">
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Novel List
              </a>
              <ul class="dropdown-menu p-4 text-end novel-links" id="novel-links">
                <li><a href="Becoming_the_Villain's_Family.html">Becoming the Villain's Family</a></li>
                <li><a href="Castle_Of_Black_Iron.html">Castle Of Black Iron</a></li>
                <li><a href="Endless_Path_Infinite_Cosmos.html">Endless Path Infinite Cosmos</a></li>
                <li><a href="God_And_Devil_World.html">God And Devil World</a></li>
                <li><a href="Great_Demon_king.html">Great Demon king</a></li>
                <li><a href="Heavenly_Jewel_Change.html">Heavenly Jewel Change</a></li>
                <li><a href="Kingdom's_Bloodline.html">Kingdom's Bloodline</a></li>
                <li><a href="Lord_Of_All_Realms.html">Lord Of All Realms</a></li>
                <li><a href="Lord_Of_Mysteries.html">Lord Of Mysteries</a></li>
                <li><a href="Lord_Of_Mysteries_2.html">Lord Of Mysteries 2</a></li>
                <li><a href="Martial_World.html">Martial World</a></li>
                <li><a href="Miracle_Throne.html">Miracle Throne</a></li>
                <li><a href="Mother_Of_Learning.html">Mother Of Learning</a></li>
                <li><a href="My_House_of_Horrors.html">My House of Horrors</a></li>
                <li><a href="Nine_Heavenly_Star_Art.html">Nine Heavenly Star Art</a></li>
                <li><a href="Otherworldly_Evil_Monarch.html">Otherworldly Evil Monarch</a></li>
                <li><a href="Rebirth_Of_The_Thief_Who_Roamed_The_World.html">Rebirth Of The Thief Who Roamed The World</a></li>
                <li><a href="Revend_Insanity.html">Revend Insanity</a></li>
                <li><a href="Super_Gene.html">Super Gene</a></li>
                <li><a href="Supreme_Magus.html">Supreme Magus</a></li>
                <li><a href="Swallowed_Star.html">Swallowed Star</a></li>
                <li><a href="Tales_Of_Demons_And_Gods.html">Tales Of Demons And Gods</a></li>
                <li><a href="The_Storm_Kng.html">The Storm Kng</a></li>
                <li><a href="The_Strongest_Legend_Of_Dragon_Ball.html">The Strongest Legend Of Dragon Ball</a></li>
                <li><a href="Throne_Of_Magical_Archana.html">Throne Of Magical Archana</a></li>
                <li><a href="Transcending_The_Nine_Heavens.html">Transcending The Nine Heavens</a></li>
                <li><a href="Unscientific_Beast_Taming.html">Unscientific Beast Taming</a></li>
                <li><a href="Warlock_Of_The_Magus_World.html">Warlock Of The Magus World</a></li>
              </ul>
            </li>
          </ul>
          <form class="d-flex" role="search">
            <input id="novelSearch" class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
          </form>
        </div>
      </div>
    </nav>
  </header>
  <main class="container mt-5">
    <section class="py-5 text-center container">
      <div class="row py-lg-5">
        <div class="col-lg-6 col-md-8 mx-auto">
          <h1 class="fw-light">{" ".join(folder_name.split("_"))}</h1>
          <img src="../img/novels/{folder_name}.jpg" class="img-thumbnail w-750" alt="...">
          <!-- Accordian start -->
          <div class="accordion" id="accordionExample">
            <div class="accordion-item">
              <h2 class="accordion-header">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="false" aria-controls="collapseOne">
                  Description
                </button>
              </h2>
              <div id="collapseOne" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
                <div class="accordion-body">
                  <p class="lead text-body-secondary">After the Catastrophe, every rule in the world was rewritten.
                    In the Age of Black Iron, steel, iron, steam engines and fighting force became the crux in which human beings depended on to survive.
                    A commoner boy by the name Zhang Tie was selected by the gods of fortune and was gifted a small tree which could constantly produce various marvelous fruits. At the same time, Zhang Tie was thrown into the flames of war, a three-hundred-year war between the humans and monsters on the vacant continent. Using crystals to tap into the potentials of the human body, one must cultivate to become stronger.
                    The thrilling legends of mysterious clans, secrets of Oriental fantasies, numerous treasures and legacies in the underground world — All in the Castle of Black Iron!</p>
                </div>
              </div>
            </div>
          </div>
          <!-- Accordian Close -->
          <br>
          <h5 class="text-center">Please Donate</h5>
          <a href="https://ko-fi.com/webnovelaudioworld" class="btn btn-warning my-2">Pay-Pal</a>
          <a href="https://paypal.me/webnovelaudioworld" class="btn btn-warning my-2">Ko-fi</a>
        </div>
      </div>
    </section>
    <ul class="novel-list justify-content-center">
"""
    # Add links to all HTML files in the folder
    for file in sorted_files:
        html_content += f'<li class="novel-item w-75"> <a class="novel-link" href="{file}"> <div class="novel-card"><h5 class="novel-title">Chapter: {os.path.basename(file).rstrip(".html").replace("-", " to ")}</h5></div> </a> </li>\n'

    html_content += """
    </ul>
  </main>

  <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
    <div class="col-md-4 d-flex align-items-center">
      <a href="/" class="mb-3 me-2 mb-md-0 text-body-secondary text-decoration-none lh-1">
        <svg class="bi" width="30" height="24"><use xlink:href="#bootstrap"></use></svg>
      </a>
      <span class="mb-3 mb-md-0 text-body-secondary">© 2024 Webnovel Audio World</span>
    </div>

    <ul class="nav col-md-4 justify-content-end list-unstyled d-flex">
      <li class="ms-3"><a class="text-body-secondary" href="https://x.com/webnovelaudio"><i class="bi bi-twitter-x"></i></a></li>
      <li class="ms-3"><a class="text-body-secondary" href="https://www.instagram.com/webnovelaudioworld"><i width="24" height="24" class="bi bi-instagram"></i></a></li>
      
    </ul>
  </footer>

  <!-- bootstrap cdn -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>

  <!-- google adsense  -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8937783756989937"
     crossorigin="anonymous"></script>

  <!-- my JS -->
  <script type="text/javascript" src="../../myscript.js"></script>
</body>
</html>
"""
    index_file_name = f"{folder_name}.html"
    index_file_path = os.path.join(output_folder, index_file_name)
    with open(index_file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

def generate_all_indexes(root_folder, output_folder):
    """Generates index HTML files for all sub-folders in the root folder."""
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Traverse the directory tree and create an index file for each sub-folder
    for root, dirs, files in os.walk(root_folder):
        # Ignore files in the root folder
        if root == root_folder:
            continue
        
        # List HTML files in the current directory
        html_files = [os.path.relpath(os.path.join(root, file), root_folder) for file in files if file.endswith('.html')]
        
        if html_files:
            # Generate an index file for the current folder
            generate_folder_index_html(root, html_files, output_folder)

if __name__ == '__main__':
    root_folder = 'novels'  # Replace with your target folder path
    output_folder = 'novels'  # Replace with the path where you want to store index HTML files
    generate_all_indexes(root_folder, output_folder)
