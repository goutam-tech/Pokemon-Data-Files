"""
Generate Review.xlsx for PokemonReviewApp Database
Matches the Review.cs model structure
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
import os

def create_review_file():
    wb = Workbook()
    ws = wb.active
    ws.title = "Reviews"
    
    headers = ["Id", "Title", "Text", "Rating", "ReviewerId", "PokemonId"]
    
    for col, header in enumerate(headers, 1):
        cell = ws.cell(1, col, header)
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color="9966FF", end_color="9966FF", fill_type="solid")
        cell.alignment = Alignment(horizontal="center")
    
    reviews = [
        [1, "Best Starter Ever!", "Bulbasaur is an excellent starter Pokemon with great type coverage and balanced stats.", 5, 1, 1],
        [2, "Powerful Evolution", "Charizard's flying ability combined with fire attacks makes it incredibly versatile in battles.", 5, 1, 6],
        [3, "Defensive Powerhouse", "Blastoise's water cannons are devastating and its shell provides amazing defense.", 5, 2, 9],
        [4, "Electric Companion", "Pikachu refuses to evolve but remains incredibly powerful and loyal.", 5, 1, 25],
        [5, "Psychic Master", "Alakazam's psychic abilities are unmatched. Incredible intelligence and speed.", 5, 4, 65],
        [6, "Dragon Champion", "Dragonite is gentle despite its power. A true champion's Pokemon.", 5, 6, 149],
        [7, "Legendary Power", "Mewtwo's power is almost too much to handle. Requires experienced training.", 5, 4, 150],
        [8, "Mysterious Pokemon", "Mew is adorable yet powerful. Perfect stats across the board!", 5, 4, 151],
        [9, "Fire Starter", "Cyndaquil is a reliable fire-type starter with great potential.", 4, 1, 155],
        [10, "Water Power", "Feraligatr's jaw strength is incredible. Highly recommend!", 5, 2, 160],
        [11, "Cute but Powerful", "Pichu is adorable but needs careful training to avoid self-damage.", 4, 9, 172],
        [12, "Happiness Pokemon", "Togepi brings joy wherever it goes. Great for new trainers.", 5, 10, 175],
        [13, "Electric Sheep", "Ampharos is a fantastic electric type with great special attack.", 5, 12, 181],
        [14, "Sun Pokemon", "Espeon's psychic abilities developed from strong friendship.", 5, 9, 196],
        [15, "Moonlight Pokemon", "Umbreon's dark typing and defense make it perfect for night battles.", 5, 13, 197],
        [16, "Legendary Diving", "Lugia's power over the sea is magnificent. Truly legendary!", 5, 6, 249],
        [17, "Rainbow Pokemon", "Ho-Oh is majestic and its sacred fire is incredibly powerful.", 5, 6, 250],
        [18, "Time Traveler", "Celebi can travel through time! An amazing grass/psychic type.", 5, 4, 251],
        [19, "Rock Solid", "Geodude is tough and perfect for beginner trainers.", 4, 3, 74],
        [20, "Water Ninja", "Greninja is fast and powerful with excellent water/dark typing.", 5, 11, 658],
        [21, "Fighting Spirit", "Machamp's four arms deliver devastating punches!", 5, 14, 68],
        [22, "Ghost Master", "Gengar is my favorite ghost type. Perfect for strategic battles.", 5, 7, 94],
        [23, "Ice Queen", "Lapras is gentle and powerful. Great for water transportation.", 5, 2, 131],
        [24, "Sleeping Giant", "Snorlax is incredibly bulky and surprisingly fast when awake.", 4, 1, 143],
        [25, "Bug Champion", "Scyther's speed and slashing attacks are phenomenal.", 5, 17, 123],
        [26, "Steel Defense", "Steelix has incredible defense. Nearly impenetrable!", 5, 3, 208],
        [27, "Dragon Ruler", "Garchomp is the perfect combination of power and speed.", 5, 7, 445],
        [28, "Aura Pokemon", "Lucario's aura abilities make it unique and powerful.", 5, 8, 448],
        [29, "Flame Body", "Magmar's flame body ability is great for hatching eggs.", 4, 24, 126],
        [30, "Forest Guardian", "Celebi protected our forest. An amazing experience!", 5, 23, 251],
        [31, "Water Starter", "Squirtle Squad member here! Best water starter hands down.", 5, 1, 7],
        [32, "Evolution Master", "Eevee's evolution options make it incredibly versatile.", 5, 4, 133],
        [33, "Poison Expert", "Nidoking has amazing type coverage with poison and ground.", 4, 9, 34],
        [34, "Flying High", "Pidgeot is one of the fastest flying types in Kanto.", 4, 1, 18],
        [35, "Underground Mole", "Dugtrio's ground attacks are super effective!", 4, 3, 51],
        [36, "Grass Specialist", "Vileplume has powerful grass moves and sleep powder.", 4, 7, 45],
        [37, "Water Psychic", "Starmie's dual typing makes it unpredictable in battles.", 5, 2, 121],
        [38, "Fighting Champ", "Hitmonlee's kicks are legendary!", 5, 14, 106],
        [39, "Rare Pokemon", "Chansey is great for healing team members.", 5, 29, 113],
        [40, "Legendary Bird", "Articuno's ice beam is incredibly powerful!", 5, 6, 144],
        [41, "Thunder Bird", "Zapdos controls electricity like no other Pokemon.", 5, 6, 145],
        [42, "Fire Bird", "Moltres is majestic and its fire attacks are devastating.", 5, 6, 146],
        [43, "Dragon Type", "Dratini is cute but will evolve into a powerful dragon.", 4, 12, 147],
        [44, "Grass Type", "Chikorita is an underrated grass starter.", 4, 9, 152],
        [45, "Fire Mouse", "Typhlosion's eruption attack is incredible!", 5, 1, 157],
        [46, "Bug Type", "Heracross is the strongest bug Pokemon I've trained.", 5, 17, 214],
        [47, "Steel Type", "Scizor's metal coating makes it nearly invincible.", 5, 8, 212],
        [48, "Water Dragon", "Kingdra is an excellent water/dragon combination.", 5, 2, 230],
        [49, "Rock Type", "Tyranitar is a pseudo-legendary with amazing stats.", 5, 7, 248],
        [50, "Normal Type", "Persian is fast and elegant. Great for speed battles.", 4, 1, 53],
    ]
    
    for row_data in reviews:
        ws.append(row_data)
    
    ws.column_dimensions['A'].width = 10
    ws.column_dimensions['B'].width = 25
    ws.column_dimensions['C'].width = 70
    ws.column_dimensions['D'].width = 10
    ws.column_dimensions['E'].width = 12
    ws.column_dimensions['F'].width = 12
    
    os.makedirs('report', exist_ok=True)
    output_path = 'report/XLSX/Review.xlsx'
    wb.save(output_path)
    print(f"✓ Review.xlsx created with {len(reviews)} reviews")
    return output_path

if __name__ == "__main__":
    print("=" * 60)
    print("GENERATING REVIEW DATA")
    print("=" * 60)
    create_review_file()
    print("\n✓ File ready for database import!")