Blast off into **Sky Jumper**, the ultimate vertical platformer! Guide your hero as you hop from tile to tile, dodging dangerous goblins and the abyss below—one misstep, and it’s game over.

Use the **← and →** arrows to move across shifting platforms, and hit **↑** to leap skyward. Time your jumps perfectly to land on the special **upper tiles**, which trigger your **Moon Jump** ability—an automatic extra boost that can save you when the platform below disappears.  

Key Features:
- **Simple, addictive controls**: Left/Right to move, Up to jump  
- **High-stakes gameplay**: Avoid falling off-screen or colliding with falling goblins  
- **Moon Jump power-up**: Land on upper tiles to automatically spring back into the air  
- **Dynamic levels**: Platforms scroll as you ascend, keeping you on your toes  

Can you climb high enough to beat your own high score? Strap in and start jumping!
Download EXE file from dist folder.
 



python -m venv .venv
.\.venv\Scripts\activate.bat

pip install pygame pyinstaller
pip freeze > requirements.txt

pyinstaller --onefile --windowed --icon=standing.ico --paths . --hidden-import mainSetting --hidden-import mainSprites --hidden-import images.anim5 --hidden-import mainMusic --add-data "images;images" --add-data "sounds;sounds" --add-data "highscore1.txt;." mainGame.py

--paths . ensures your project root (with mainSetting.py) is on the PYTHONPATH inside the EXE.

--hidden-import guarantees PyInstaller bundles those modules even if it can’t see them via static analysis.