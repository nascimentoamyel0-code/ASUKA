class FormTranslator:
    def __init__(self):
        self.direct_fixes = {
            "groundon": "groudon",
            "groundom": "groudon",
            "virizon": "virizion",

            "mega charizard x": "charizard-mega-x",
            "charizard mega x": "charizard-mega-x",
            "mega charizard y": "charizard-mega-y",
            "charizard mega y": "charizard-mega-y",

            "mega mewtwo x": "mewtwo-mega-x",
            "mewtwo mega x": "mewtwo-mega-x",
            "mega mewtwo y": "mewtwo-mega-y",
            "mewtwo mega y": "mewtwo-mega-y",

            "kyurem branco": "kyurem-white",
            "white kyurem": "kyurem-white",
            "kyurem white": "kyurem-white",
            "kyurem preto": "kyurem-black",
            "black kyurem": "kyurem-black",
            "kyurem black": "kyurem-black",

            "ash greninja": "greninja-ash",
            "greninja ash": "greninja-ash",

            "zygarde completo": "zygarde-complete",
            "zygarde complete": "zygarde-complete",
            "zygarde 10": "zygarde-10",
            "zygarde 50": "zygarde-50",

            "keldeo": "keldeo-ordinary",
            "keldeo resolute": "keldeo-resolute",
            "keldeo resoluto": "keldeo-resolute",

            "landorus": "landorus-incarnate",
            "thundurus": "thundurus-incarnate",
            "tornadus": "tornadus-incarnate",
            "enamorus": "enamorus-incarnate",

            "urshifu g max": "urshifu-single-strike-gmax",
            "urshifu gmax": "urshifu-single-strike-gmax",
            "urshifu gigantamax": "urshifu-single-strike-gmax",
            "urshifu single strike gmax": "urshifu-single-strike-gmax",
            "urshifu rapid strike gmax": "urshifu-rapid-strike-gmax",

            "tauros paldea": "tauros-paldea-combat-breed",
            "paldean tauros": "tauros-paldea-combat-breed",
            "tauros paldea fogo": "tauros-paldea-blaze-breed",
            "tauros paldea agua": "tauros-paldea-aqua-breed",

            "hoopa unbound": "hoopa-unbound",
            "hoopa liberto": "hoopa-unbound",
            "shaymin sky": "shaymin-sky",
            "shaymin ceu": "shaymin-sky",
            "meloetta pirouette": "meloetta-pirouette",
            "wishiwashi school": "wishiwashi-school",
            "wishiwashi cardume": "wishiwashi-school",
            "aegislash blade": "aegislash-blade",
            "aegislash espada": "aegislash-blade",
            "aegislash shield": "aegislash-shield",
            "aegislash escudo": "aegislash-shield",
        }

        self.form_words = {
            "mega": "mega",
            "primal": "primal",
            "primordial": "primal",
            "gigantamax": "gmax",
            "gmax": "gmax",
            "g-max": "gmax",
            "alolan": "alola",
            "alola": "alola",
            "galarian": "galar",
            "galar": "galar",
            "hisuian": "hisui",
            "hisui": "hisui",
            "paldean": "paldea",
            "paldea": "paldea",
            "therian": "therian",
            "incarnate": "incarnate",
            "origin": "origin",
            "origem": "origin",
            "crowned": "crowned",
            "coroado": "crowned",
            "coroada": "crowned",
        }

    def translate(self, name):
        name = name.lower().strip().replace("_", " ").replace("-", " ")

        while "  " in name:
            name = name.replace("  ", " ")

        if name in self.direct_fixes:
            return self.direct_fixes[name]

        words = name.split()

        if len(words) < 2:
            return name.replace(" ", "-")

        first = words[0]
        last = words[-1]

        if first in self.form_words:
            form = self.form_words[first]
            pokemon = "-".join(words[1:])
            return f"{pokemon}-{form}"

        if last in self.form_words:
            form = self.form_words[last]
            pokemon = "-".join(words[:-1])
            return f"{pokemon}-{form}"

        return name.replace(" ", "-")