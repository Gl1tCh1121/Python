<h1> Password Manager (Python Tkinter)</h1>

<p>
  This project is a simple <strong>Password Manager</strong> built with Python and the 
  <code>Tkinter</code> GUI toolkit.<br>
  It allows you to <strong>generate secure passwords</strong>, 
  <strong>save them with associated websites and emails</strong>, and 
  <strong>search saved credentials</strong> stored in a JSON file.
</p>

<hr>

<h2> Features</h2>
<ul>
  <li>Secure random password generator (letters, numbers, symbols)</li>
  <li>Save website, email/username, and password to a <code>data.json</code> file</li>
  <li>Search functionality to retrieve stored credentials</li>
  <li>User confirmation before saving or retrieving sensitive data</li>
  <li>Simple and clean Tkinter-based GUI</li>
</ul>

<hr>

<h2> Demo</h2>

<p>
  Below is a quick demonstration of the Password Manager in action:
</p>

<p align="center">
  <img src="https://media.giphy.com/media/NjJG3xF5jOkgxH6z7l/giphy.gif" 
       alt="Password Manager Demo" 
       width="600">
</p>


<hr>

<h2> Project Structure</h2>
<pre>
password-manager/
│── main.py       # Tkinter GUI and logic
│── logo.png      # Logo displayed in the UI
│── data.json     # JSON file storing credentials (auto-created after first save)
</pre>

<hr>

<h2> Installation &amp; Usage</h2>
<ol>
  <li>Clone the repository:</li>
</ol>
<pre><code>git clone https://github.com/Gl1tCh1121/password-manager.git
cd password-manager
</code></pre>

<ol start="2">
  <li>Run the app:</li>
</ol>
<pre><code>python main.py
</code></pre>

<hr>

<h2> Usage</h2>
<ul>
  <li>Enter a <strong>website</strong>, <strong>email/username</strong>, and <strong>password</strong></li>
  <li>Click <strong>Generate Password</strong> to auto-create a secure password</li>
  <li>Click <strong>Add</strong> to save the credentials to <code>data.json</code></li>
  <li>Use <strong>Search</strong> to look up existing credentials</li>
</ul>

<hr>

<h2> Requirements</h2>
<ul>
  <li>Python 3.x</li>
  <li>Built-in <code>Tkinter</code> module</li>
  <li><code>json</code> module (built-in)</li>
</ul>

<hr>

<h2> Contributing</h2>
<p>
  Contributions, suggestions, and improvements are welcome. <br>
  You can extend this project by adding features like password encryption, 
  master password protection, or exporting/importing data securely.
</p>
