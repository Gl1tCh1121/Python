<h1 align="center">ISS Overhead Notifier</h1>

<p>
  A Python script that notifies you via email when the International Space Station (ISS) is above your location at night.<br>
  <br>
  Look up at the sky and spot the ISS when it passes overhead!
</p>

<hr>

<h2> Features</h2>
<ul>
  <li><b>ISS Location Tracking:</b> Uses <code>http://api.open-notify.org/iss-now.json</code> to check ISS coordinates in real-time.</li>
  <li><b>Nighttime Detection:</b> Uses <code>https://api.sunrise-sunset.org</code> to ensure visibility (only sends emails at night).</li>
  <li><b>Email Notification:</b> Sends an email alert when the ISS is overhead and visible.</li>
  <li><b>Automatic Checks:</b> Runs continuously and checks every 60 seconds.</li>
</ul>

<hr>

<h2>Project Structure</h2>

<pre>
📦 iss-notifier/
 ┣ 📜 main.py        # Main script (ISS tracking + email notifier)
 ┣ 📜 README.md      # Project documentation
</pre>

<hr>

<h2> Getting Started</h2>

<h3>1. Clone the repository</h3>

<h3>2. Install dependencies</h3>
<pre><code>pip install requests
</code></pre>

<h3>3. Configure your details</h3>
<p>In <code>main.py</code>, set your:</p>
<ul>
  <li><code>MY_LAT</code> – Your latitude</li>
  <li><code>MY_LNG</code> – Your longitude</li>
  <li><code>MY_EMAIL</code> – Your Gmail address</li>
  <li><code>MY_PASSWORD</code> – Your Gmail app password (not your regular password!)</li>
</ul>

<h3>4. Run the script</h3>
<pre><code>python main.py
</code></pre>

<hr>

<h2> Example Email</h2>
<pre>
Subject: Look up in the sky

The ISS is above you.
</pre>

<hr>

<h2> Built With</h2>

<ul>
  <li>Python 3.9+</li>
  <li>requests library</li>
  <li>smtplib (built-in)</li>
</ul>

<hr>

<h2> Future Plans</h2>
<ul>
  <li> Add SMS or Telegram notifications</li>
  <li> Add a desktop notification option</li>
  <li> Visualize ISS location on a map</li>
</ul>

<hr>

<h2>🤝 Contributing</h2>
<p>Contributions are welcome! If you'd like to improve the notifier, follow these steps:</p>
<ol>
  <li>Fork the repository</li>
  <li>Create a new branch</li>
  <li>Commit your changes</li>
  <li>Push to your branch</li>
  <li>Open a Pull Request</li>
</ol>
<hr>
