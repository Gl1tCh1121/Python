<h1>⏱️ Pomodoro Timer (Python Tkinter)</h1>

<p>
  This project is a <strong>Pomodoro Timer</strong> built with Python and the 
  <code>Tkinter</code> GUI toolkit.<br>
  It follows the <strong>Pomodoro Technique</strong>, where you work in focused sessions 
  of 25 minutes, separated by short breaks, with a longer break after every 4 sessions.<br>
  The app includes a visual <strong>tomato image</strong> and plays a sound when a session ends.  
  For convenience, it also provides a <code>pomodoro.exe</code> file to run the application without Python.
</p>

<hr>

<h2>Features</h2>
<ul>
  <li>Work sessions (25 min), short breaks (5 min), and long breaks (20 min)</li>
  <li>Automatic session switching with countdown display</li>
  <li>Checkmark tracking to indicate completed work sessions</li>
  <li>Sound notification when a timer finishes</li>
  <li>Reset and exit functionality</li>
  <li>Bundled <code>pomodoro.exe</code> for direct execution</li>
</ul>

<hr>

<h2> Demo</h2>

<p>
  Below is a quick demonstration of the Password Manager in action:
</p>

<p align="center">
  <img src="https://media.giphy.com/media/ttdRieJAZmHzkJfIVw/giphy.gif" 
       alt="Password Manager Demo" 
       width="600">
</p>

<hr>

<h2 Project Structure</h2>
<pre>
pomodoro-timer/
│── main.py        # Tkinter GUI and timer logic
│── tomato.png     # Tomato image used in the UI
│── pomodoro.exe   # Executable version of the app
</pre>

<hr>

<h2> Installation &amp; Usage</h2>
<ol>
  <li>Clone the repository:</li>
</ol>
<pre><code>git clone https://github.com/Gl1tCh1121/pomodoro-timer.git
cd pomodoro-timer
</code></pre>

<ol start="2">
  <li>Run with Python:</li>
</ol>
<pre><code>python main.py
</code></pre>

<ol start="3">
  <li>Or run directly using the executable:</li>
</ol>
<pre><code>pomodoro.exe
</code></pre>

<hr>

<h2>🖥 Usage</h2>
<ul>
  <li>Click <strong>Start</strong> to begin a Pomodoro session</li>
  <li>Work until the timer reaches 0</li>
  <li>Follow the short or long break prompts</li>
  <li>Checkmarks (✓) indicate completed work sessions</li>
  <li>Click <strong>Reset</strong> to restart the timer</li>
  <li>Click <strong>Exit</strong> to close the app</li>
</ul>

<hr>

<h2>🛠 Requirements</h2>
<ul>
  <li>Python 3.x (if running via source)</li>
  <li>Built-in <code>Tkinter</code> module</li>
  <li><code>winsound</code> (for Windows sound notifications)</li>
</ul>

<hr>

<h2> Contributing</h2>
<p>
  Contributions, suggestions, and feature requests are welcome. <br>
  Feel free to fork this repository and improve the app!
</p>
