
// audio player controls
        const audio = document.getElementById('audio');
const playPauseBtn = document.getElementById('playPauseBtn');
const seekBar = document.getElementById('seekBar');
const playbackSpeed = document.getElementById('playbackSpeed');
const currentTimeDisplay = document.getElementById('currentTime');
const durationDisplay = document.getElementById('duration');
const remainingTimeDisplay = document.getElementById('remainingTime');

// Buttons
const rewind10Btn = document.getElementById('rewind10Btn');
const rewind30Btn = document.getElementById('rewind30Btn');
const forward10Btn = document.getElementById('forward10Btn');
const forward30Btn = document.getElementById('forward30Btn');

// Play/Pause functionality
playPauseBtn.addEventListener('click', () => {
    if (audio.paused) {
        audio.play();
        playPauseBtn.innerHTML = '<i class="bi bi-pause-fill"></i>';
        playPauseBtn.classList.remove('play');
        playPauseBtn.classList.add('pause');
    } else {
        audio.pause();
        playPauseBtn.innerHTML = '<i class="bi bi-play-fill"></i>';
        playPauseBtn.classList.remove('pause');
        playPauseBtn.classList.add('play');
    }
});

// Update the seek bar and time displays
audio.addEventListener('timeupdate', () => {
    const currentTime = audio.currentTime;
    const duration = audio.duration;
    const value = (currentTime / duration) * 100;

    seekBar.value = value;
    updateSeekBarColor(value);

    // Update time displays
    currentTimeDisplay.textContent = formatTime(currentTime);
    durationDisplay.textContent = formatTime(duration);
    remainingTimeDisplay.textContent = formatTime(duration - currentTime);
});

// Seek functionality
seekBar.addEventListener('input', () => {
    const value = seekBar.value;
    audio.currentTime = (value / 100) * audio.duration;
});

// Playback speed control
playbackSpeed.addEventListener('change', () => {
    audio.playbackRate = parseFloat(playbackSpeed.value);
});

// Forward and backward buttons functionality
rewind10Btn.addEventListener('click', () => {
    audio.currentTime = Math.max(0, audio.currentTime - 10);
});

rewind30Btn.addEventListener('click', () => {
    audio.currentTime = Math.max(0, audio.currentTime - 30);
});

forward10Btn.addEventListener('click', () => {
    audio.currentTime = Math.min(audio.duration, audio.currentTime + 10);
});

forward30Btn.addEventListener('click', () => {
    audio.currentTime = Math.min(audio.duration, audio.currentTime + 30);
});

// Update the seek bar color based on played and unplayed parts
function updateSeekBarColor(value) {
    seekBar.style.background = `linear-gradient(to right, #1db954 ${value}%, #333333 ${value}%, #333333 100%)`;
}

// Format time in mm:ss
function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${String(minutes).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
}