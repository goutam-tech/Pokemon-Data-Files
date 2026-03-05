-- Category table
CREATE TABLE "Category" (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL
);

-- Country table
CREATE TABLE "Country" (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL
);

-- Owner table
CREATE TABLE "Owner" (
    Id SERIAL PRIMARY KEY,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Gym VARCHAR(255),
    CountryId INT REFERENCES "Country"(Id) ON DELETE SET NULL
);

-- Pokemon table
CREATE TABLE "Pokemon" (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    BirthDate DATE NOT NULL
);

-- Reviewer table
CREATE TABLE "Reviewer" (
    Id SERIAL PRIMARY KEY,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL
);

-- Review table
CREATE TABLE "Review" (
    Id SERIAL PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Text TEXT NOT NULL,
    Rating INT NOT NULL,
    ReviewerId INT REFERENCES "Reviewer"(Id) ON DELETE CASCADE,
    PokemonId INT REFERENCES "Pokemon"(Id) ON DELETE CASCADE
);

-- PokemonCategory (many-to-many between Pokemon and Category)
CREATE TABLE "PokemonCategory" (
    PokemonId INT REFERENCES "Pokemon"(Id) ON DELETE CASCADE,
    CategoryId INT REFERENCES "Category"(Id) ON DELETE CASCADE,
    PRIMARY KEY (PokemonId, CategoryId)
);

-- PokemonOwner (many-to-many between Pokemon and Owner)
CREATE TABLE PokemonOwner (
    PokemonId INT REFERENCES "Pokemon"(Id) ON DELETE CASCADE,
    OwnerId INT REFERENCES "Owner"(Id) ON DELETE CASCADE,
    PRIMARY KEY (PokemonId, OwnerId)
);
