<h1>Coffee Machine (Python)</h1>

<p>
  This project is a simple <strong>Coffee Machine Simulation</strong> implemented in Python using 
  an object-oriented programming (OOP) approach.<br>
  The machine manages resources (<code>water</code>, <code>milk</code>, <code>coffee</code>), 
  checks ingredient availability, and makes coffee if possible.
</p>

<hr>

<h2>Features</h2>
<ul>
  <li>Object-oriented design with a <strong>CoffeeMaker</strong> class</li>
  <li>Resource management (water, milk, coffee)</li>
  <li>Generates a report of available resources 📊</li>
  <li>Checks whether resources are sufficient before making a drink</li>
  <li>Deducts ingredients when a coffee is made ☕</li>
</ul>

<hr>

<h2>Project Structure</h2>
<pre>
coffee-machine-oop/
│── main.py          # Entry point to run the simulation
│── coffee_maker.py  # Defines the CoffeeMaker class (manages resources & makes coffee)
│── menu.py          # Defines available drinks and their ingredients
│── money_machine.py # (Optional) Handles payment logic if extended
</pre>

<hr>

<h2>Installation &amp; Usage</h2>
<ol>
  <li>Clone the repository:</li>
</ol>
<ol start="2">
  <li>Run the program:</li>
</ol>
<pre><code>python main.py
</code></pre>

<hr>

<h2>Example Output</h2>
<pre>
Water: 300ml
Milk: 200ml
Coffee: 100g
Here is your latte ☕️. Enjoy!
</pre>

<hr>

<h2>🛠 Requirements</h2>
<ul>
  <li>Python 3.x</li>
</ul>

<hr>

<h2>🤝 Contributing</h2>
<p>
  Feel free to <strong>fork</strong> this project and extend it! <br>
  You can add features like a money system, more drinks, or custom ingredient management. 🙌
</p>
