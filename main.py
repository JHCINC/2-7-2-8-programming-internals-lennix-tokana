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
        "Femboy": ["Lennix", "Micheal", "Ethan", "Louis", "Lachlan", "Gage"],

    },

    "Fantasy": {
        "Male": ["Percival", "Merlin", "Thaddeus", "Kaelen", "Thorian", "Lysander", "Draven", "Gideon", "Zephyros", "Rylan", "Eldrin", "Vesper", "Caspian", "Nokk"],
        "Female": ["Lyra", "Seraphina", "Isolde", "Anya", "Briar", "Elara", "Zephyra", "Rhiannon", "Valkyrie", "Calista", "Elowen", "Miriam", "Aurelia", "Sylvia", "Nimue"],
        "Non Binary": ["Zephyr", "Rune", "Ash", "River", "Sky", "Ember", "Vale", "Rowan", "Sage", "Briar", "Cyan", "Jett", "Fable", "Lux", "Nyx"],








    }



}