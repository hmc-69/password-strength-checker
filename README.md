# Password Strength Checker Website

A beautiful web application to check password strength with a video background and modern UI.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Add a background video:
   - Place a video file named `background.mp4` in the `static/` folder
   - The video will play on loop as the background

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
password_checker/
├── app.py              # Flask backend server
├── main.py             # Password checking logic
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Main HTML page
└── static/
    ├── style.css       # Styling
    ├── script.js       # Frontend JavaScript
    └── background.mp4   # Background video (you need to add this)
```

## Features

- 🎥 Video background on loop
- 🎨 Beautiful blurred glassmorphism overlay
- ⏳ Loading spinner animation
- 💬 Fun Malayalam feedback messages
- 📱 Responsive design

## Note

You'll need to add your own background video file (`background.mp4`) to the `static/` folder. The video should be in MP4 format for best browser compatibility.