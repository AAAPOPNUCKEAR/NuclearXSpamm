
import glob
from pathlib import Path
from 𝙽𝚄𝙲𝙻𝙴𝙰𝚁 𝚇 𝚂𝙿𝙰𝙼.utils import load_plugins
import logging
from . import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "𝙽𝚄𝙲𝙻𝙴𝙰𝚁×𝚂𝙿𝙰𝙼/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("𝙽𝚄𝙲𝙻𝙴𝙰𝚁 𝚇 𝚂𝙿𝙰𝙼 𝚂𝚄𝚂𝚂𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙳𝙴𝙿𝙻𝙾𝚈𝙴𝙳⚜️ !!")
print("𝙴𝙽𝙹𝙾𝚈 𝚈𝙾𝚄𝚁 𝙵𝙰𝚂𝚃 𝚂𝙿𝙰𝙼 𝙱𝙾𝚃! @AUKAATMEINRAHO")

if __name__ == "__main__":
    MK1.run_until_disconnected()
    
if __name__ == "__main__":
    MK2.run_until_disconnected()

if __name__ == "__main__":
    MK3.run_until_disconnected()
    
if __name__ == "__main__":
    MK4.run_until_disconnected()

if __name__ == "__main__":
    MK5.run_until_disconnected()
    
if __name__ == "__main__":
    MK6.run_until_disconnected()
    
if __name__ == "__main__":
    MK7.run_until_disconnected()

if __name__ == "__main__":
    MK8.run_until_disconnected()
    
if __name__ == "__main__":
    MK9.run_until_disconnected()

if __name__ == "__main__":
    MK10.run_until_disconnected()    
