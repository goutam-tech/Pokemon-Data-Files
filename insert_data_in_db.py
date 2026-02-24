import psycopg2
import csv
import os
from dotenv import load_dotenv

load_dotenv()

# Local Database Credentials;
# dbname_local = os.getenv("DB_NAME_LOCAL")
# user = os.getenv("DB_USER")
# password = os.getenv("DB_PASSWORD")
# host_local = os.getenv("DB_HOST_LOCAL")
# port_local = os.getenv("DB_PORT_LOCAL")

# conn = psycopg2.connect(
#     dbname=dbname_local,
#     user=user,
#     password=password_local,
#     host=host_local,
#     port=port_local
# )

# Cloud Database Credentials;
dbname_cloud = os.getenv("DB_NAME_CLOUD")
user_cloud = os.getenv("DB_USER_CLOUD")
password_cloud = os.getenv("DB_PASSWORD_CLOUD")
host_cloud = os.getenv("DB_HOST_CLOUD")
port_cloud = os.getenv("DB_PORT_CLOUD")

conn = psycopg2.connect(
    dbname=dbname_cloud,
    user=user_cloud,
    password=password_cloud,
    host=host_cloud,
    port=port_cloud
)

cur = conn.cursor()

# Categories Data;
csv_file_path_categories = os.getenv("CSV_PATH_CATEGORIES")

with open(csv_file_path_categories, newline="",) as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        Id = row["Id"]
        Name = row["Name"]
        cur.execute(
            """ INSERT INTO "Categories" ("Id", "Name") 
            VALUES (%s, %s) 
            """, 
            (int(Id), Name)
        )

# Country Data;
csv_file_path_country = os.getenv("CSV_PATH_COUNTRY")

with open(csv_file_path_country, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Id = row["Id"]
        Name = row["Name"]
        cur.execute(
            """ INSERT INTO "Countries" ("Id", "Name") 
            VALUES (%s, %s) 
            """, 
            (int(Id), Name)
        )

#Owners Data;
csv_file_path_owners = os.getenv("CSV_PATH_OWNERS")
with open(csv_file_path_owners, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Id = row["Id"]
        FirstName = row["FirstName"]
        LastName = row["LastName"]
        Gym = row["Gym"]
        CountryId = row["CountryId"]
        cur.execute(
            """ INSERT INTO "Owners" ("Id", "FirstName", "LastName", "Gym", "CountryId") 
            VALUES (%s, %s, %s, %s, %s) 
            """, 
            (int(Id), FirstName, LastName, Gym, int(CountryId))
        )

# Pokemon Data;
csv_file_path_pokemon = os.getenv("CSV_PATH_POKEMON")
with open(csv_file_path_pokemon, newline="") as csvfile: 
    reader = csv.DictReader(csvfile) 
    for row in reader: 
        Id = row["Id"]
        Name = row["Name"] 
        BirthDate = row["BirthDate"] 
        # DD-MM-YYYY 
        cur.execute( 
            """ INSERT INTO "Pokemon" ("Id", "Name", "BirthDate") 
            VALUES (%s, %s, TO_DATE(%s, 'DD-MM-YYYY')) 
            """, 
            (int(Id), Name, BirthDate) 
        )

# PokemonCategory Data;
csv_file_path_pokemon_category = os.getenv("CSV_PATH_POKEMON_CATEGORY")
with open(csv_file_path_pokemon_category, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        PokemonId = row["PokemonId"]
        CategoryId = row["CategoryId"]
        cur.execute(
            """ INSERT INTO "PokemonCategory" ("PokemonId", "CategoryId") 
            VALUES (%s, %s) 
            """, 
            (int(PokemonId), int(CategoryId))
        )

# PokemonOwner Data;
csv_file_path_pokemon_owner = os.getenv("CSV_PATH_POKEMON_OWNER")
with open(csv_file_path_pokemon_owner, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        PokemonId = row["PokemonId"]
        OwnerId = row["OwnerId"]
        cur.execute(
            """ INSERT INTO "PokemonOwner" ("PokemonId", "OwnerId") 
            VALUES (%s, %s) 
            """, 
            (int(PokemonId), int(OwnerId))
        )

# Reviews Data;
csv_file_path_reviews = os.getenv("CSV_PATH_REVIEWS")
with open(csv_file_path_reviews, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        PokemonId = row["PokemonId"]
        OwnerId = row["OwnerId"]
        Title = row["Title"]
        Text = row["Text"]
        Rating = row["Rating"]
        cur.execute(
            """ INSERT INTO "Reviews" ("PokemonId", "OwnerId", "Title", "Text", "Rating") 
            VALUES (%s, %s, %s, %s, %s) 
            """, 
            (int(PokemonId), int(OwnerId), Title, Text, int(Rating))
        )   

# Reviewer Data;
csv_file_path_reviewer = os.getenv("CSV_PATH_REVIEWER")
with open(csv_file_path_reviewer, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Id = row["Id"]
        FirstName = row["FirstName"]
        LastName = row["LastName"]
        cur.execute(
            """ INSERT INTO "Reviewer" ("Id", "FirstName", "LastName") 
            VALUES (%s, %s, %s) 
            """, 
            (int(Id), FirstName, LastName)
        )

# ReviewerReview Data;
csv_file_path_reviewer_review = os.getenv("CSV_PATH_REVIEWER_REVIEW")
with open(csv_file_path_reviewer_review, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ReviewerId = row["ReviewerId"]
        ReviewId = row["ReviewId"]
        cur.execute(
            """ INSERT INTO "ReviewerReview" ("ReviewerId", "ReviewId") 
            VALUES (%s, %s) 
            """, 
            (int(ReviewerId), int(ReviewId))
        )

conn.commit()
cur.close()
conn.close()

print("CSV data inserted successfully!")