<h1>Mail Merge Project (Python)</h1>

<p>
  This project automates the process of creating personalized letters for a list of recipients using Python.<br>
  It reads a template letter, replaces placeholders with each recipient's name, and saves the personalized letters 
  into an output folder.
</p>

<hr>

<h2>Features</h2>
<ul>
  <li>Reads a <strong>template letter</strong> with placeholders</li>
  <li>Supports multiple recipient names from a text file</li>
  <li>Automatically generates personalized letters for each recipient</li>
  <li>Saves each letter in a separate file for easy distribution</li>
</ul>

<hr>

<h2>Project Structure</h2>
<pre>
mail-merge/
│── main.py                   # Main script that performs the mail merge
│── Input/
│   │── Letters/
│   │   └── starting_letter.txt   # Template letter with [name] placeholder
│   │── Names/
│       └── invited_names.txt     # List of recipient names
│── Output/
    └── ReadyToSend/           # Folder where personalized letters are saved
</pre>

<hr>

<h2>Installation &amp; Usage</h2>
<ol>
  <li>Clone the repository:</li>
</ol>
<ol start="2">
  <li>Run the script:</li>
</ol>
<pre><code>python main.py
</code></pre>

<hr>

<h2>🛠 Requirements</h2>
<ul>
  <li>Python 3.x</li>
  <li>Basic understanding of file handling in Python</li>
</ul>

<hr>

<h2>🤝 Contributing</h2>
<p>
  Feel free to <strong>fork</strong> this project and improve it! <br>
  Suggestions, enhancements, or feature ideas are always welcome. 🙌
</p>
