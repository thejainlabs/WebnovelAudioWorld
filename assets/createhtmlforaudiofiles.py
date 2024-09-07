import os

# Function to generate HTML content for a given audio file
def generate_html(audio_file_path, folder_name):
    file_name = os.path.splitext(os.path.basename(audio_file_path))[0]
    html_content = f"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Light Novel Audiobook | Webnovel | Fantasy Audiobook | WebnovelAudioWorld</title>

  <!-- favicon -->
  <link rel="icon" href="../../img/favicon.png" type="image/png">

  <!-- Bootstrap icon -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet">

  <!-- Bootstrap Css -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">

    <!-- mystyles -->
    <link rel="stylesheet" type="text/css" href="../../../mystyles.css">
</head>
<body data-bs-theme="dark">



 <header>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container d-flex justify-content-between align-items-center">
        <a class="navbar-brand" href="https://webnovelaudioworld.com/">
          <img class="img-fluid w-50" src="../../img/logo.png" alt="webnovel audio world" />
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
          <ul class="navbar-nav mx-auto">
            <!-- <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Features</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Pricing</a>
            </li> -->
            <li class="nav-item dropdown text-end">
              <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Novel List
              </a>
              <ul class="dropdown-menu p-4 text-end novel-links">
                  <li><a href="../Becoming_the_Villain's_Family.html">Becoming the Villain's Family</a></li>
                  <li><a href="../Castle_Of_Black_Iron.html">Castle Of Black Iron</a></li>
                  <li><a href="../Endless_Path_Infinite_Cosmos.html">Endless Path Infinite Cosmos</a></li>
                  <li><a href="../God_And_Devil_World.html">God And Devil World</a></li>
                  <li><a href="../Great_Demon_king.html">Great Demon king</a></li>
                  <li><a href="../Heavenly_Jewel_Change.html">Heavenly Jewel Change</a></li>
                  <li><a href="../Kingdom's_Bloodline.html">Kingdom's Bloodline</a></li>
                  <li><a href="../Lord_Of_All_Realms.html">Lord Of All Realms</a></li>
                  <li><a href="../Lord_Of_Mysteries.html">Lord Of Mysteries</a></li>
                  <li><a href="../Lord_Of_Mysteries_2.html">Lord Of Mysteries 2</a></li>
                  <li><a href="../Martial_World.html">Martial World</a></li>
                  <li><a href="../Miracle_Throne.html">Miracle Throne</a></li>
                  <li><a href="../Mother_Of_Learning.html">Mother Of Learning</a></li>
                  <li><a href="../My_House_of_Horrors.html">My House of Horrors</a></li>
                  <li><a href="../Nine_Heavenly_Star_Art.html">Nine Heavenly Star Art</a></li>
                  <li><a href="../Otherworldly_Evil_Monarch.html">Otherworldly Evil Monarch</a></li>
                  <li><a href="../Rebirth_Of_The_Thief_Who_Roamed_The_World.html">Rebirth Of The Thief Who Roamed The World</a></li>
                  <li><a href="../Revend_Insanity.html">Revend Insanity</a></li>
                  <li><a href="../Super_Gene.html">Super Gene</a></li>
                  <li><a href="../Supreme_Magus.html">Supreme Magus</a></li>
                  <li><a href="../Swallowed_Star.html">Swallowed Star</a></li>
                  <li><a href="../Tales_Of_Demons_And_Gods.html">Tales Of Demons And Gods</a></li>
                  <li><a href="../The_Storm_Kng.html">The Storm Kng</a></li>
                  <li><a href="../The_Strongest_Legend_Of_Dragon_Ball.html">The Strongest Legend Of Dragon Ball</a></li>
                  <li><a href="../Throne_Of_Magical_Archana.html">Throne Of Magical Archana</a></li>
                  <li><a href="../Transcending_The_Nine_Heavens.html">Transcending The Nine Heavens</a></li>
                  <li><a href="../Unscientific_Beast_Taming.html">Unscientific Beast Taming</a></li>
                  <li><a href="../Warlock_Of_The_Magus_World.html">Warlock Of The Magus World</a></li>
              </ul>
            </li>
          </ul>
          
        </div>
      </div>
    </nav>
  </header>

    <main class="container mt-5">

      <section class="py-5 text-center container">
      <div class="row py-lg-5">
        <div class="col-lg-6 col-md-8 mx-auto">
          <h1 class="fw-light">{" ".join(folder_name.split("_"))} - {" to ".join(file_name.split("-"))}</h1>
          <img src="../../img/novels/{folder_name}.jpg" class="img-thumbnail w-750" alt="...">
          
          <br>
          <h5 class="text-center">Please Donate</h5>
          <a href="https://ko-fi.com/webnovelaudioworld" class="btn btn-warning my-2">Pay-Pal</a>
          <a href="https://paypal.me/webnovelaudioworld" class="btn btn-warning my-2">Ko-fi</a>
        </div>
      </div>
    </section>

    <section>


      <!-- new audio player start-->
      <div class="audio-player text-center">
    <audio id="audio">
        <source src="{file_name}.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
    <div class="time-display">
        <span id="currentTime">00:00</span> / 
        <span id="duration">00:00</span> | 
        <span id="remainingTime">00:00</span>
    </div>
    <div class="controls mt-3">
        <div class="d-flex justify-content-center mb-4">
            <button id="rewind30Btn" class="btn">
                <i class="bi  bi-chevron-double-left"></i>
            </button>
            <button id="rewind10Btn" class="btn">
                <i class="bi  bi-chevron-left"></i>
            </button>
            <button id="playPauseBtn" class="btn play">
                <i class="bi bi-play-fill"></i>
            </button>
            <button id="forward10Btn" class="btn">
                <i class="bi  bi-chevron-right"></i>
            </button>
            <button id="forward30Btn" class="btn">
                <i class="bi bi-chevron-double-right"></i>
            </button>
        </div>
        <div class="d-flex justify-content-center">
            <input id="seekBar" class="slider w-100" type="range" value="0" min="0" max="100" step="1">
            <select id="playbackSpeed" class="form-select w-auto" aria-label="Playback Speed">
                <option value="0.5">0.5x</option>
                <option value="1" selected>1x</option>
                <option value="1.5">1.5x</option>
                <option value="2">2x</option>
            </select>
        </div>
    </div>
</div>

      <!-- new audio player end -->

    </section>
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
      
              
 <!-- google adsense  -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8937783756989937"
     crossorigin="anonymous"></script>

  <!-- bootstrap cdn -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>

  <!-- my JS -->
  <script type="text/javascript" src="../../../audioplayer.js"></script>
</body>
</html>
"""

    return html_content

# Directory containing audio files
audio_dir = 'novels'

# Generate HTML for each audio file
for root, dirs, files in os.walk(audio_dir):
    for filename in files:
        if filename.endswith(".mp3"):
            audio_file_path = os.path.join(root, filename)
            folder_name = os.path.basename(root)
            html_content = generate_html(audio_file_path, folder_name)
            
            # Save the HTML content to a file in the same directory as the audio file
            output_filename = os.path.splitext(filename)[0] + '.html'
            output_path = os.path.join(root, output_filename)
            
            with open(output_path, 'w') as file:
                file.write(html_content)

            print(f"Generated {output_filename} in folder {folder_name}")
