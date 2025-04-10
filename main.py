"""
Input the type you want i.g {type, gender} [type = fantasy, sci-fi, modern, Medieval, etc] [gender = Male, Female, NB, ambiguous, helicopter, fem-boy]
last name typing ina last name as a last name
amount = amount [I want 10 names of the sci-fi type and all female]
check if the input is valid
use a random number to select a random name from the multidimensional list with all the input types you want. Multidimensional
 ex: [namelist =
	["sci-fi"], - 0
	["Fantasy"], - 1
	["Medieval"], - 2
	["Modern"], - 3
blah, blah gender, blah, random num, blah]
print the full thing out.
If you so desire to have more use [loop, multiple names] prints more names, types, random crap.

"""
import random
namelist = {
    "Modern": {
        "Male": ["James", "John", "Michael", "David", "Benjamin", "Nathan", "Ryan", "Ethan", "Jack", "Leo", "Adam", "Julian", "Titus", "Elliot", "Milo"],
        "Female": ["Emma", "Olivia", "Ava", "Sophia", "Isabella", "Mia", "Amelia", "Harper", "Evelyn", "Abigail", "Ella", "Chloe", "Lily", "Charlotte", "Grace"],
        "Non Binary": ["Alex", "Jordan", "Taylor", "Morgan", "Riley", "Avery", "Casey", "Rowan", "Skyler", "Quinn", "Emerson", "Sage", "Cameron", "Finley", "Dakota"],
        "Helicopter": ["Apache", "Black Hawk", "Chinook", "Huey", "Sea Hawk", "Viper", "Osprey", "Merlin", "Gazelle", "Kiowa"],
        "Femboy": ["Lennix", "Micheal", "Ethan", "Louis", "Lachlan", "Gage", "Rohan"],
    },

    "Fantasy": {
        "Male": ["Percival", "Merlin", "Thaddeus", "Kaelen", "Thorian", "Lysander", "Draven", "Gideon", "Zephyros", "Rylan", "Eldrin", "Vesper", "Caspian", "Nokk"],
        "Female": ["Lyra", "Seraphina", "Isolde", "Anya", "Briar", "Elara", "Zephyra", "Rhiannon", "Valkyrie", "Calista", "Elowen", "Miriam", "Aurelia", "Sylvia", "Nimue"],
        "Non Binary": ["Zephyr", "Rune", "Ash", "River", "Sky", "Ember", "Vale", "Rowan", "Sage", "Briar", "Cyan", "Jett", "Fable", "Lux", "Nyx"],
    },
    "Sci-Fi": {
        "Male": ["Kaelix", "Jorvan", "Thalen", "Xyloar", "Rydan", "Vexton", "Zael", "Qorin", "Myrion", "Dravin", "Lorm", "Sylas", "Kiv", "Jerrick", "Valen"],
        "Female": ["Lyra", "Astra", "Nova", "Kaelia", "Xylo", "Rylin", "Vesper", "Zahara", "Quorra", "Myra", "Drava", "Lorna", "Sylvia", "Kiva", "Jerricka"],
        "Non Binary": ["Xylar", "Quillon", "Zephyra", "Kaelix", "Jorin", "Rydan", "Vexta", "Sylvae", "Myrion", "Dravyn", "Lornex", "Kivryn", "Jerricka", "Valenor", "Astral"],
    },
    "Mythology": {
        "Male": ["Apollo", "Thor", "Osiris", "Loki", "Helios", "Anubis", "Odin", "Zeus", "Ares", "Poseidon", "Hercules", "Prometheus", "Orpheus", "Jason", "Rohan"],
        "Female": ["Artemis", "Freya", "Isis", "Hecate", "Athena", "Selene", "Persephone", "Nyx", "Aphrodite", "Demeter", "Diana", "Valkyrie", "Medusa", "Circe", "Pandora"],
        "Non Binary": ["Hesper", "Aether", "Solstice", "Equinox", "Ambrosia", "Ember", "Tempest", "Chroma", "Labyrinth", "Oracle", "Echo", "Flux", "Horizon", "Nebula", "Cinder"],
    },
    "Uruk": {
        "Male": ["Gnash", "Pushkrimp", "Dush", "Kruk", "Azog", "Lugdash", "Rak", "Gromm", "Skak", "Thrak", "Ur-Hakon", "Brûz", "Zog", "Lorm", "Flog"],
        "Female": ["Gnashra", "Borga", "Dusha", "Kruka", "Azoga", "Lugdasha", "Raka", "Gromma", "Skaka", "Thraka", "Ur-Hakona", "Brûza", "Zoga", "Gorgora", "Floga"],
        "Non Binary": ["Bagga", "Vort", "Glim", "Thraz", "Jex", "Rulk", "Pyn", "Zolt", "Darg", "Quiv", "Hyr", "Brev", "Kyn", "Vex", "Jorn"],
    },
    "Goth": {
        "Male": ["Oberon", "Vlad", "Grimm", "Sterling", "Balthazar", "Shadow", "Jet", "Nocturne", "Obsidian", "Xanthos", "Erebus", "Acheron", "Morbius", "Dusk", "Azrael", "Rohan"],
        "Female": ["Ravenna", "Lilith", "Morticia", "Dark Lord", "Seraphina", "Shadow", "Velvet", "Ophelia", "Morwenna", "Elvira", "Persephone", "Wednesday", "Crimson", "Willow", "Obsidian"],
        "Non Binary": ["Acheron", "Beryl", "Corvus", "Ember", "Flint", "Jetlore", "Kryptos", "Mirage", "Noctilux", "Onyx", "Riven", "Sepulchre", "Silvan", "Twilight", "Vesperon"],
    },
    "Alien": {
        "Male": ["Xylar", "Zorgon", "Kaelix", "Vortan", "Ryloth", "Q'orin", "Myrra", "Dravok", "Lornex", "Sylvax", "Kivryn", "Jerrickon", "Valexis", "Zephyron", "Glarth"],
        "Female": ["Lyraxia", "Vespera", "Kaelara", "Zylphia", "Rylona", "Quorinna", "Myrielle", "Dravina", "Lornissa", "Sylvana", "Kivara", "Jerrika", "Valeria", "Zephyra", "Glariel"],
        "Non Binary": ["Xylos", "Zorgonix", "Kaelryn", "Vortalis", "Rylothyn", "Quorvex", "Myrion", "Dravix", "Lornexis", "Sylvorn", "Kivrynex", "Jerrickonix", "Valex", "Zephyronix", "Glarryn"],
    },
    "Medieval": {
        "Male": ["Alaric", "Bartholomew", "Caspian", "Darius", "Evander", "Finnian", "Gideon", "Hadrian", "Isidore", "Jasper", "Lysander", "Matthias", "Oberon", "Peregrine", "Silas"],
        "Female": ["Aeliana", "Beatrix", "Cressida", "Elowen", "Genevieve", "Isolde", "Lyra", "Melisande", "Odelia", "Persephone", "Rowena", "Seraphina", "Theodora", "Vivienne", "Millicent"],
        "Non Binary": ["Avery", "Clement", "Ellis", "Emery", "Florian", "Jules", "Larkin", "Morgan", "Peregrine", "Quentin", "Raven", "Riley", "Sage", "Skylar", "Winter"],
    },
    "Steampunk": {
        "Male": ["Aether", "Bartholomew", "Caspian", "Devereux", "Edison", "Fitzroy", "Gideon", "Horatio", "Ignatius", "Cogsworth", "Lysander", "Maximilian", "Peregrine", "Sebastian", "Theodoric"],
        "Female": ["Auralia", "Beryl", "Celestia", "Dahlia", "Elowyn", "Fiora", "Gwendolyn", "Hypatia", "Juniper", "Kaelia", "Lenore", "Morwenna", "Octavia", "Primrose",  "Tesla"],
        "Non Binary": ["Aetherion", "Cadmium", "Clockwork", "Deverin", "Element", "Gearson", "Indiglo", "Junction", "Leverett", "Meridian", "Pinion", "Rivetson", "Spindle", "Tinker", "Voltarian"],
    },
    "Cyberpunk": {
        "Male": ["Razor", "Chrome", "Vector", "Glitch", "Neon", "Rogue", "Byte", "Zero", "Jax", "Kaito", "Raze", "Synth", "Viper", "Wraith", "Xenon"],
        "Female": ["Ava", "Blake", "Cassia", "Dahlia", "Elara", "Jade", "Kira", "Lena", "Maya", "Nadia", "Raven", "Rina", "Sasha", "Vera", "Zara"],
        "Non Binary": ["Ash", "Cyan", "Devon", "Ember", "Finch", "Kai", "Lennox", "Mercury", "Neon", "Pixel", "Quinn", "Rowan", "FemboyUwU", "Vale", "Alduin"],
    },
}

print("Categories available: Modern, Fantasy, Medieval, Mythology, Uruk, Goth, Alien, Sci-Fi, Steampunk, Cyberpunk")
print("Genders available: Male, Female, Non Binary")
last_name = input("Last name: ")
category = input("Type of Category, pretty person: ")
gender = input("Input Gender: ")
amount = int(input("Amount of names you want generated: "))
if category not in namelist:
    print("Pick another category, please!")
if gender not in namelist[category]:
    print("Pick another gender from the provided list (Male, Female, Non Binary).")
print("\n Generated Names: ")
for num in range(amount):
    namelist = random.choice(namelist[category][gender])
    print(f"{namelist} {last_name}")