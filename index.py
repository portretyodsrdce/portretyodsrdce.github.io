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
            <!--img src="images/B.jpg" alt="Artist Image" class="header-image"-->
            <h1>Julie Fabišiková</h1>
            <nav>
                <ul>
                    <li><a href="#home" class="cs">Domů</a></li>
                    <li><a href="#about" class="cs">O mně</a></li>
                    <li><a href="#portfolio" class="cs">Portfolio</a></li>
                    <li><a href="#offer" class="cs">Nabídka</a></li>
                    <li><a href="#contact" class="cs">Kontakt</a></li>
                    <li><a href="#home" class="en" style="display:none;">Home</a></li>
                    <li><a href="#about" class="en" style="display:none;">About Me</a></li>
                    <li><a href="#portfolio" class="en" style="display:none;">Portfolio</a></li>
                    <li><a href="#offer" class="en" style="display:none;">Offer</a></li>
                    <li><a href="#contact" class="en" style="display:none;">Contact</a></li>
                </ul>
            </nav>
            <div id="language-switcher">
                <button onclick="switchLanguage('cs')">Česky</button>
                <button onclick="switchLanguage('en')">English</button>
            </div>
        </div>
    </header>
        <section id="home">
            <h2 class="cs">PASTELKAMI NAKRESLÍM VÁŠ PORTRÉT PODLE FOTEK</h2>
            <h2 class="en" style="display:none;">I WILL DRAW YOUR PORTRAIT ACCORDING TO THE PHOTOS WITH CRAYONS</h2>
        </div>
        <img src="images/B.jpg" alt="Art Offer" class="offer-image">
        
          <div class="cs">
            <ul>
                <li>Dárek k důležitým výročím a událostem (narozeniny, svátky, svatby, maturita, promoce...)</li>
                <li>Máte také možnost zvěčnit vaše děti v jejich roztomilosti (a že to uteče jako voda!)</li>
            </ul>
        </div>
        
        <div class="en" style="display:none;">
            <ul>
                <li>Gift for important anniversaries and events (birthdays, holidays, weddings, graduation, commencement...)</li>
                <li>You also have the option to immortalize your children in their cuteness (and it flies by so quickly!)</li>
            </ul>
        </div>
        
        
    </section>
 <div class="container">
    <section id="about">
        <h2 class="cs">O mně</h2>
        <h2 class="en" style="display:none;">About Me</h2>
        <p class="cs">Jsem maminka na plný úvazek a kromě péče o rodinu a domácnost nacházím potěšení v kreslení pastelkami. Zabývám se kresbou portrétů podle fotek, a to nejen dětí a dospělých, ale i domácích mazlíčků (kteří hrají v rodinách nezastupitelnou úlohu a tedy i oni si zaslouží zvěčnit :-).
Kreslením a malbou se bavím od té doby, co jsem jako dítě vzala do ruky tužku. Fascinovaly mě obrazy v galeriích a ilustrace v knihách. Toužila jsem naučit se zachytit podobu lidí a jejich emoce, které se v obličeji promítají. Kromě kreslení mě také lákalo porozumět fungování přírody. Studovala jsem biologii a PřF UK (obor imunologie), přičemž výtvarná činnost pro mě byla oblíbeným koníčkem a také způsobem, jak si vyčistit hlavu a uvolnit se. Dělalo mi radost vyjádřit svůj obdiv ke zvířatům, které spolu s námi obývají Zemi, formou kresby a malby. 
Základy kresby jsem získala během dospívání od Mgr. Jana Majera, který otevřel kroužek pro děti a individuálně se nám s nadšením věnoval. S dalším tvořením jsem pak pokračovala na ZUŠ Vlašim pod vedením Mgr. Jana Dvořáka, který mě zasvětil do mnoha různých výtvarných technik. Nejvíce jsem si oblíbila umělecké vyjádření pomocí barev pastelkami nebo olejovými barvami. V letech 2019 a 2020 jsem absolvovala kurz olejomalby v ateliéru AvvY v Praze.
</p>
        <p class="en" style="display:none;">I am a full-time mom and, in addition to taking care of my family and household, I find pleasure in drawing with crayons. I specialize in drawing portraits from photos, not only of children and adults but also of pets (who play an irreplaceable role in families and therefore also deserve to be immortalized 😊).

I have enjoyed drawing and painting since I was a child and picked up a pencil for the first time. I was fascinated by paintings in galleries and illustrations in books. I longed to learn how to capture the likeness of people and the emotions reflected in their faces. Besides drawing, I was eager to understand the nature. I studied biology at Charles University (Department of Immunology), while artistic activity was a beloved hobby. I took joy in expressing my admiration for animals, through drawing and painting.

I learned the basics of drawing during my adolescence from Mgr. Jan Majer, who opened a workshop for children and worked with us enthusiastically. I continued at the art school in Vlašim under the guidance of Mgr. Jan Dvořák, who introduced me to many different artistic techniques. I became most fond of artistic expression using crayons or oil paints. In 2019 and 2020, I completed an oil painting course at the AvvY studio in Prague.

</p>
    </section>
  </div>
    <section id="portfolio">
        <h2 class="cs">Portfolio</h2>
        <h2 class="en" style="display:none;">Portfolio</h2>
        
        <div class="cs">
            <h3>Kresba</h3>
            <div>
                <h4>Portréty</h4>
                <div class="gallery">
                    <img src="images/1.jpg" alt="Kresba pastelkami, formát A3" onclick="showModal('images/1.jpg', 'Kresba pastelkami, formát A3')">
                    <img src="images/2.jpg" alt="Kresba pastelkami, formát A4" onclick="showModal('images/2.jpg', 'Kresba pastelkami, formát A4')">
                    
                </div>
                <h4>Zvířata</h4>
                <div class="gallery">
                    <img src="images/11.jpg" alt="Kresba suchý pastel, formát A4" onclick="showModal('images/11.jpg', 'Kresba suchý pastel, formát A4')">
                    
                </div>
            </div>
            
            <h3>Malba</h3>
            <div>
                <h4>Portréty</h4>
                <div class="gallery">
                    <img src="images/4.jpg" alt="Dívka s perlou - replika, malba olejovými barvami, technika lazury" onclick="showModal('images/4.jpg', 'Dívka s perlou - replika, malba olejovými barvami, technika lazury')">
                    <img src="images/3.jpg" alt="Malba olejovými barvami, technika Alla prima" onclick="showModal('images/3.jpg', 'Malba olejovými barvami, technika Alla prima')">
                    
                </div>
                <h4>Zvířata</h4>
                <div class="gallery">
                    <img src="images/5.jpg" alt="Malba olejovými barvami, technika Alla prima" onclick="showModal('images/5.jpg', 'Malba olejovými barvami, technika Alla prima')">
                    <img src="images/6.jpg" alt="Malba olejovými barvami, technika Alla prima" onclick="showModal('images/6.jpg', 'Malba olejovými barvami, technika Alla prima')">
                    <img src="images/7.jpg" alt="Malba olejovými barvami, technika Alla prima" onclick="showModal('images/7.jpg', 'Malba olejovými barvami, technika Alla prima')">
                    <img src="images/8.jpg" alt="Malba olejovými barvami, technika Alla prima" onclick="showModal('images/8.jpg', 'Malba olejovými barvami, technika Alla prima')">
                </div>
            </div>
        </div>
        
        <div class="en" style="display:none;">
            <h3>Drawings</h3>
            <div>
                <h4>Portraits</h4>
                <div class="gallery">
                    <img src="images/1.jpg" alt="Crayon drawing, A3 format" onclick="showModal('images/1.jpg', 'Crayon drawing, A3 format')">
                    <img src="images/2.jpg" alt="Crayon drawing, A4 format" onclick="showModal('images/2.jpg', 'Crayon drawing, A4 format')">
                </div>
                <h4>Animals</h4>
                <div class="gallery">
                    <img src="images/11.jpg" alt="Dry pastel drawing, A4 format" onclick="showModal('images/11.jpg', 'Dry pastel drawing, A4 format')">
                </div>
            </div>
            
            <h3>Paintings</h3>
            <div>
                <h4>Portraits</h4>
                <div class="gallery">
                    <img src="images/4.jpg" alt="Girl with a Pearl Earring - replica, oil painting, glaze technique" onclick="showModal('images/4.jpg', 'Girl with a Pearl Earring - replica, oil painting, glaze technique')">
                    <img src="images/3.jpg" alt="Oil painting, Alla prima technique" onclick="showModal('images/3.jpg', 'Oil painting, Alla prima technique')">
                </div>
                <h4>Animals</h4>
                <div class="gallery">
                    <img src="images/5.jpg" alt="Oil painting, glaze technique" onclick="showModal('images/5.jpg', 'Oil painting, glaze technique')">
                    <img src="images/6.jpg" alt="Oil painting, glaze technique" onclick="showModal('images/6.jpg', 'Oil painting, glaze technique')">
                    <img src="images/7.jpg" alt="Oil painting, glaze technique" onclick="showModal('images/7.jpg', 'Oil painting, glaze technique')">
                    <img src="images/8.jpg" alt="Oil painting, glaze technique" onclick="showModal('images/8.jpg', 'Oil painting, glaze technique')">
                </div>
            </div>
        </div>
    </section>
    
    <section id="offer">
        <h2 class="cs">Nabídka</h2>
        <h2 class="en" style="display:none;">Offer</h2>
        
        <div class="offer-text">
                
        <p class="cs">Ceník</p>
        <p class="en" style="display:none;">Price list</p>
    
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
