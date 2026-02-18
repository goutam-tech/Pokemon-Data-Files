"""
MASTER SCRIPT - Generate All Database Files
Runs all individual generation scripts for PokemonReviewApp Database
"""

import sys
sys.path.append('"./DB_Create/report/XLSX')

from generate_category import create_category_file
from generate_country import create_country_file
from generate_pokemon import create_pokemon_file
from generate_owner import create_owner_file
from generate_reviewer import create_reviewer_file
from generate_review import create_review_file
from generate_pokemon_category import create_pokemon_category_file
from generate_pokemon_owner import create_pokemon_owner_file

def main():
    print("=" * 70)
    print("POKEMON REVIEW APP - DATABASE FILE GENERATOR")
    print("=" * 70)
    print("\nGenerating all Excel files for database import...\n")
    
    files_generated = []
    
    try:
        # Generate all files
        print("1/8 - Generating Categories...")
        files_generated.append(create_category_file())
        
        print("\n2/8 - Generating Countries...")
        files_generated.append(create_country_file())
        
        print("\n3/8 - Generating Pokemon...")
        files_generated.append(create_pokemon_file())
        
        print("\n4/8 - Generating Owners...")
        files_generated.append(create_owner_file())
        
        print("\n5/8 - Generating Reviewers...")
        files_generated.append(create_reviewer_file())
        
        print("\n6/8 - Generating Reviews...")
        files_generated.append(create_review_file())
        
        print("\n7/8 - Generating Pokemon-Category Mappings...")
        files_generated.append(create_pokemon_category_file())
        
        print("\n8/8 - Generating Pokemon-Owner Mappings...")
        files_generated.append(create_pokemon_owner_file())
        
        print("\n" + "=" * 70)
        print("ALL FILES GENERATED SUCCESSFULLY!")
        print("=" * 70)
        print("\nFiles created:")
        for i, file_path in enumerate(files_generated, 1):
            print(f"  {i}. {file_path.split('/')[-1]}")
        
        print("\n" + "=" * 70)
        print("DATABASE IMPORT ORDER:")
        print("=" * 70)
        print("Import files in this exact order to maintain foreign key constraints:")
        print("  1. Category.xlsx")
        print("  2. Country.xlsx")
        print("  3. Pokemon.xlsx")
        print("  4. Owner.xlsx")
        print("  5. Reviewer.xlsx")
        print("  6. Review.xlsx")
        print("  7. PokemonCategory.xlsx")
        print("  8. PokemonOwner.xlsx")
        print("\n✓ All files are ready for download and database import!")
        
    except Exception as e:
        print(f"\n✗ Error generating files: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
