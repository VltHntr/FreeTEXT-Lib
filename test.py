from FreeTEXTlib.Utils import SaveManager, Formater
from FreeTEXTlib.Models import Creator

form = Formater()
form.init_format(Creator("Kempe", "Oliver"))

saver = SaveManager("./data/", form)

saver.save_to_text("test", "Hallo Welt")
