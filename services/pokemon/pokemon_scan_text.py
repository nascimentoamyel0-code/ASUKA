class PokemonScanText:
    def generate(self, pokemon):
        name = pokemon["name"].replace("-", " ").title()
        types = ", ".join(pokemon.get("types", []))
        abilities = ", ".join(pokemon.get("abilities", []))
        stats = pokemon.get("stats", {})

        attack = stats.get("attack", 0)
        sp_attack = stats.get("special-attack", 0)
        speed = stats.get("speed", 0)

        text = f"{name}. Pokémon do tipo {types}. "

        if "mega" in pokemon["name"]:
            base_name = (
                pokemon["name"]
                .replace("-mega", "")
                .replace("-x", "")
                .replace("-y", "")
                .replace("-", " ")
                .title()
            )

            text = (
                f"{name} é a forma Mega Evoluída de {base_name}. "
                f"Essa transformação aumenta drasticamente seu poder de combate"
            )

            if attack >= sp_attack:
                text += f", destacando principalmente seu ataque físico de {attack}"
            else:
                text += f", destacando principalmente seu ataque especial de {sp_attack}"

            if speed >= 100:
                text += f" e sua alta velocidade de {speed}"

            text += ". "

        elif "primal" in pokemon["name"]:
            base_name = pokemon["name"].replace("-primal", "").replace("-", " ").title()

            text = (
                f"{name} é a forma Primordial de {base_name}. "
                f"Seu poder ancestral foi despertado, tornando seus atributos extremamente elevados. "
            )

        elif "gmax" in pokemon["name"]:
            base_name = pokemon["name"].replace("-gmax", "").replace("-", " ").title()

            text = (
                f"{name} é a forma Gigantamax de {base_name}. "
                f"Nessa forma, seu corpo cresce de maneira colossal e seus ataques ganham propriedades especiais. "
            )

        elif "origin" in pokemon["name"]:
            base_name = pokemon["name"].replace("-origin", "").replace("-", " ").title()

            text = (
                f"{name} é a forma Origem de {base_name}. "
                f"Essa forma representa seu estado mais próximo do poder original. "
            )

        text += f"Suas habilidades conhecidas são: {abilities}."

        return text