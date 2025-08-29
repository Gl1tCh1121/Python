<h1>Flashcard App (Python Tkinter)</h1>

<p>
  This project is a <strong>Flashcard App</strong> built with Python and the 
  <code>Tkinter</code> GUI toolkit.<br>
  It helps users learn <strong>German–English vocabulary</strong> using flashcards. 
  Each card shows a German word, and after 3 seconds, it flips to reveal the English translation. 
  Known words are removed from the learning pool and saved for future sessions.
</p>

<hr>

<h2>Features</h2>
<ul>
  <li>Displays German words and flips to show the English translation after 3 seconds</li>
  <li>Interactive buttons for marking words as <strong>known</strong> ✅ or <strong>unknown</strong> ❌</li>
  <li>Progress is saved in <code>words_to_learn.csv</code> so you continue where you left off</li>
  <li>Uses <strong>Pandas</strong> for data handling and <strong>Tkinter Canvas</strong> for visuals</li>
</ul>

<hr>

<h2>Project Structure</h2>
<pre>
flashcard-app/
│── main.py                   # Tkinter GUI and logic
│── data/
│    ├── german_words.csv      # Original dataset of German–English words
│    └── words_to_learn.csv    # Updated dataset excluding known words
│── images/
│    ├── card_front.png        # Flashcard front design
│    ├── card_back.png         # Flashcard back design
│    ├── right.png             # Check button image
│    └── wrong.png             # Cross button image
</pre>

<hr>

<h2> Installation &amp; Usage</h2>
<ol>
  <li>Clone the repository:</li>
</ol>
<pre><code>git clone https://github.com/Gl1tCh1121/flashcard-app.git
cd flashcard-app
</code></pre>

<ol start="2">
  <li>Install dependencies:</li>
</ol>
<pre><code>pip install pandas
</code></pre>

<ol start="3">
  <li>Run the app:</li>
</ol>
<pre><code>python main.py
</code></pre>

<hr>

<h2>🖥 Usage</h2>
<ul>
  <li>Click <strong>❌</strong> if you don’t know the word</li>
  <li>Click <strong>✅</strong> if you know the word</li>
  <li>Known words will be removed and saved into <code>words_to_learn.csv</code></li>
  <li>The app automatically continues until all words are learned</li>
</ul>

<hr>

<h2>🛠 Requirements</h2>
<ul>
  <li>Python 3.x</li>
  <li><code>pandas</code> library</li>
  <li><code>tkinter</code> (comes pre-installed with Python)</li>
</ul>

<hr>

<h2> Contributing</h2>
<p>
  Contributions are welcome! You can extend this project by adding new languages, 
  statistics tracking, or exporting progress in different formats.
</p>
