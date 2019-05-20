---


---

<h1 id="only-for-android">ONLY FOR ANDROID</h1>
<h2 id="index">Index</h2>
<ul>
<li><a href="#what-it-does">What it does</a></li>
<li><a href="#requirements">Requirements</a></li>
<li><a href="#installation">Installation</a></li>
<li><a href="#working-languages">Working languages</a></li>
</ul>
<h2 id="what-it-does">What it does</h2>
<p>This Bot is able to play one of the three selected adventures (could be changed in the config file)<br>
and destroys every ore if your factory is full. This is good to get high level creatures.</p>
<h2 id="requirements">Requirements</h2>
<ul>
<li><a href="#python">Python 3.7</a></li>
<li><a href="#tesseract">Tesseract 4.0</a></li>
<li>Python-Packages:<br>
– <a href="#pure-python-adb">pure-python-adb</a><br>
– <a href="#pytesseract">pytesseract</a><br>
– <a href="#minimal-adb-and-fastboot">Minimal adb and fastboot</a></li>
</ul>
<h3 id="python">Python:</h3>
<p>The main logic is written in python.<br>
<a href="https://www.python.org/downloads/">Download</a></p>
<h3 id="tesseract">Tesseract:</h3>
<p>Tesseract is a optical character recognition engine which is used to detect the different states of the game with the text on your display.<br>
<a href="https://github.com/UB-Mannheim/tesseract/wiki">Download</a><br>
<a href="https://github.com/tesseract-ocr/tesseract">Wiki</a></p>
<h3 id="pure-python-adb">pure-python-adb</h3>
<p>This package is used to interact with the adb server.</p>
<h3 id="minimal-adb-and-fastboot">Minimal adb and fastboot</h3>
<p>This is the host for the adb-server which is used to communicate with the mobile phone.<br>
<a href="https://forum.xda-developers.com/showthread.php?t=2317790">Download</a></p>
<h2 id="installation">Installation</h2>
<h3 id="windows">Windows</h3>
<ol>
<li>Download and install <a href="#python">python</a></li>
<li>Download and install <a href="#minimal-adb-and-fastboot">Minimal adb and fastboot</a></li>
<li>Download the files from the repository and copy the script into a custom directory.</li>
<li>Open the CMD and type:
<ol>
<li>python pip install pure-python-adb</li>
<li>python pip install pytesseract</li>
</ol>
</li>
<li>Download and install <a href="#tesseract">Tesseract</a></li>
<li>Copy the path of the installationdirectory from Tesseract and replace the given Path in the <a href="http://start.py">start.py</a> script with your path.</li>
<li>Edit the selected_raid variable with a number between 1 and 3 depending on what raid should be played</li>
<li>Start Minimal adb and fastboot and type in the upcoming window: adb start-server</li>
<li>Open the Pokemon Rumble Rush app and go to the main menu</li>
<li>Go to the directory with the <a href="http://start.py">start.py</a> file click in the address bar and write cmd and press enter.</li>
<li>Now write: python <a href="http://start.py">start.py</a></li>
<li>Enjoy :)</li>
</ol>
<h3 id="linux">Linux</h3>
<p>Coming soon</p>

