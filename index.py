# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:42:24 2024

@author: matej
"""

<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Moje Umělecké Portfolio</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <div class="header-container">
            <h1>Julie Fabišiková</h1>
            <nav>
                <ul>
                    <li><a href="#about" class="cs">O mně</a><a href="#about" class="en" style="display:none;">About Me</a></li>
                    <li><a href="#portfolio" class="cs">Portfolio</a><a href="#portfolio" class="en" style="display:none;">Portfolio</a></li>
                    <li><a href="#contact" class="cs">Kontakt</a><a href="#contact" class="en" style="display:none;">Contact</a></li>
                </ul>
            </nav>
            <div id="language-switcher">
                <button onclick="switchLanguage('cs')">Česky</button>
                <button onclick="switchLanguage('en')">English</button>
            </div>
        </div>
    </header>
    
    <section id="about">
        <h2 class="cs">O mně</h2>
        <h2 class="en" style="display:none;">About Me</h2>
        <p class="cs">Zde se představte.</p>
        <p class="en" style="display:none;">Introduce yourself here.</p>
    </section>
    <section id="portfolio">
        <h2 class="cs">Portfolio</h2>
        <h2 class="en" style="display:none;">Portfolio</h2>
        
        <div class="cs">
            <h3>Kresba</h3>
            <div>
                <h4>Portréty</h4>
                <div class="gallery">
                    <img src="images/1.jpg" alt="Kresba Portréty 1" onclick="showModal('images/1.jpg', 'Kresba Portréty 1')">
                    <img src="images/2.jpg" alt="Kresba Portréty 2" onclick="showModal('images/2.jpg', 'Kresba Portréty 2')">
                    
                </div>
                <h4>Zvířata</h4>
                <div class="gallery">
                    <img src="images/11.jpg" alt="Kresba Zvířata 2" onclick="showModal('images/11.jpg', 'Kresba Zvířata 2')">
                    
                </div>
            </div>
            
            <h3>Malba</h3>
            <div>
                <h4>Portréty</h4>
                <div class="gallery">
                    <img src="images/4.jpg" alt="Malba Portréty 1" onclick="showModal('images/4.jpg', 'Malba Portréty 1')">
                    <img src="images/3.jpg" alt="Malba Portréty 2" onclick="showModal('images/3.jpg', 'Malba Portréty 2')">
                    
                </div>
                <h4>Zvířata</h4>
                <div class="gallery">
                    <img src="images/5.jpg" alt="Malba Zvířata 1" onclick="showModal('images/5.jpg', 'Malba Zvířata 1')">
                    <img src="images/6.jpg" alt="Malba Zvířata 2" onclick="showModal('images/6.jpg', 'Malba Zvířata 2')">
                    <img src="images/7.jpg" alt="Malba Zvířata 3" onclick="showModal('images/7.jpg', 'Malba Zvířata 3')">
                    <img src="images/8.jpg" alt="Malba Zvířata 4" onclick="showModal('images/8.jpg', 'Malba Zvířata 4')">
                </div>
            </div>
        </div>
        
        <div class="en" style="display:none;">
            <h3>Drawings</h3>
            <div>
                <h4>Portraits</h4>
                <div class="gallery">
                    <img src="images/1.jpg" alt="Kresba Portréty 1" onclick="showModal('images/1.jpg', 'Kresba Portréty 1')">
                    <img src="images/2.jpg" alt="Kresba Portréty 2" onclick="showModal('images/2.jpg', 'Kresba Portréty 2')">
                </div>
                <h4>Animals</h4>
                <div class="gallery">
                    <img src="images/11.jpg" alt="Kresba Zvířata 2" onclick="showModal('images/11.jpg', 'Kresba Zvířata 2')">
                </div>
            </div>
            
            <h3>Paintings</h3>
            <div>
                <h4>Portraits</h4>
                <div class="gallery">
                    <img src="images/4.jpg" alt="Malba Portréty 1" onclick="showModal('images/4.jpg', 'Malba Portréty 1')">
                    <img src="images/3.jpg" alt="Malba Portréty 2" onclick="showModal('images/3.jpg', 'Malba Portréty 2')">
                </div>
                <h4>Animals</h4>
                <div class="gallery">
                    <img src="images/5.jpg" alt="Malba Zvířata 1" onclick="showModal('images/5.jpg', 'Malba Zvířata 1')">
                    <img src="images/6.jpg" alt="Malba Zvířata 2" onclick="showModal('images/6.jpg', 'Malba Zvířata 2')">
                    <img src="images/7.jpg" alt="Malba Zvířata 3" onclick="showModal('images/7.jpg', 'Malba Zvířata 3')">
                    <img src="images/8.jpg" alt="Malba Zvířata 4" onclick="showModal('images/8.jpg', 'Malba Zvířata 4')">
                </div>
            </div>
        </div>
    </section>
    
    <section id="offer">
        
        <div class="offer-text">
            <h2 class="cs">PASTELKAMI NAKRESLÍM VÁŠ PORTRÉT PODLE FOTEK</h2>
            <h2 class="en" style="display:none;">I WILL DRAW YOUR PORTRAIT ACCORDING TO THE PHOTOS WITH CRAYONS</h2>
        </div>
        <img src="images/B.jpg" alt="Art Offer" class="offer-image">
    </section>
    
    <section id="contact">
        <h2 class="cs">Kontakt</h2>
        <h2 class="en" style="display:none;">Contact</h2>
        <form>
            <div class="form-group">
                <label for="name" class="cs">Jméno:</label>
                <label for="name" class="en" style="display:none;">Name:</label>
                <input type="text" id="name" name="name">
            </div>
            
            <div class="form-group">
                <label for="email" class="cs">Email:</label>
                <label for="email" class="en" style="display:none;">Email:</label>
                <input type="email" id="email" name="email">
            </div>
            
            <div class="form-group">
                <label for="message" class="cs">Zpráva:</label>
                <label for="message" class="en" style="display:none;">Message:</label>
                <textarea id="message" name="message"></textarea>
            </div>
            
            <button type="submit" class="cs">Odeslat</button>
            <button type="submit" class="en" style="display:none;">Send</button>
        </form>
    </section>
    
    <!-- Large Image Modal -->
    <div id="imageModal" class="modal" onclick="closeModal()">
        <span class="close">&times;</span>
        <img class="modal-content" id="largeImage">
        <div id="imageCaption"></div>
    </div>
    <script src="script.js"></script>
</body>
</html>
