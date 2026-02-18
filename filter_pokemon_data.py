import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
import sys

def load_pokemon_data(file_path):
    """Load all sheets from the Pokemon database"""
    excel_file = pd.ExcelFile(file_path)
    
    data = {}
    for sheet_name in excel_file.sheet_names:
        data[sheet_name] = pd.read_excel(file_path, sheet_name=sheet_name)
    
    return data

def filter_pokemon(df, filters):
    """
    Filter Pokemon dataframe based on provided criteria
    
    filters: dict with keys like:
        - 'type1': str or list (e.g., 'Fire' or ['Fire', 'Water'])
        - 'type2': str or list
        - 'generation': int or list
        - 'legendary': 'Yes' or 'No'
        - 'min_hp': int
        - 'max_hp': int
        - 'min_attack': int
        - 'min_total_stats': int
        - 'owner_id': int or list
        - 'category': str or list
    """
    filtered_df = df.copy()
    
    # Filter by Type 1
    if 'type1' in filters and filters['type1']:
        if isinstance(filters['type1'], list):
            filtered_df = filtered_df[filtered_df['Type 1'].isin(filters['type1'])]
        else:
            filtered_df = filtered_df[filtered_df['Type 1'] == filters['type1']]
    
    # Filter by Type 2
    if 'type2' in filters and filters['type2']:
        if isinstance(filters['type2'], list):
            filtered_df = filtered_df[filtered_df['Type 2'].isin(filters['type2'])]
        else:
            filtered_df = filtered_df[filtered_df['Type 2'] == filters['type2']]
    
    # Filter by Generation
    if 'generation' in filters and filters['generation']:
        if isinstance(filters['generation'], list):
            filtered_df = filtered_df[filtered_df['Generation'].isin(filters['generation'])]
        else:
            filtered_df = filtered_df[filtered_df['Generation'] == filters['generation']]
    
    # Filter by Legendary status
    if 'legendary' in filters and filters['legendary']:
        filtered_df = filtered_df[filtered_df['Legendary'] == filters['legendary']]
    
    # Filter by HP range
    if 'min_hp' in filters and filters['min_hp']:
        filtered_df = filtered_df[filtered_df['HP'] >= filters['min_hp']]
    if 'max_hp' in filters and filters['max_hp']:
        filtered_df = filtered_df[filtered_df['HP'] <= filters['max_hp']]
    
    # Filter by Attack
    if 'min_attack' in filters and filters['min_attack']:
        filtered_df = filtered_df[filtered_df['Attack'] >= filters['min_attack']]
    
    # Filter by Total Stats
    if 'min_total_stats' in filters and filters['min_total_stats']:
        filtered_df = filtered_df[filtered_df['Total Stats'] >= filters['min_total_stats']]
    
    # Filter by Owner ID
    if 'owner_id' in filters and filters['owner_id']:
        if isinstance(filters['owner_id'], list):
            filtered_df = filtered_df[filtered_df['Owner ID'].isin(filters['owner_id'])]
        else:
            filtered_df = filtered_df[filtered_df['Owner ID'] == filters['owner_id']]
    
    # Filter by Category
    if 'category' in filters and filters['category']:
        if isinstance(filters['category'], list):
            filtered_df = filtered_df[filtered_df['Category'].isin(filters['category'])]
        else:
            filtered_df = filtered_df[filtered_df['Category'].str.contains(filters['category'], case=False, na=False)]
    
    return filtered_df

def filter_trainers(df, filters):
    """Filter trainers based on criteria"""
    filtered_df = df.copy()
    
    if 'country' in filters and filters['country']:
        if isinstance(filters['country'], list):
            filtered_df = filtered_df[filtered_df['Country'].isin(filters['country'])]
        else:
            filtered_df = filtered_df[filtered_df['Country'] == filters['country']]
    
    if 'region' in filters and filters['region']:
        if isinstance(filters['region'], list):
            filtered_df = filtered_df[filtered_df['Region'].isin(filters['region'])]
        else:
            filtered_df = filtered_df[filtered_df['Region'] == filters['region']]
    
    if 'trainer_type' in filters and filters['trainer_type']:
        filtered_df = filtered_df[filtered_df['Trainer Type'].str.contains(filters['trainer_type'], case=False, na=False)]
    
    return filtered_df

def filter_gyms(df, filters):
    """Filter gyms based on criteria"""
    filtered_df = df.copy()
    
    if 'region' in filters and filters['region']:
        if isinstance(filters['region'], list):
            filtered_df = filtered_df[filtered_df['Region'].isin(filters['region'])]
        else:
            filtered_df = filtered_df[filtered_df['Region'] == filters['region']]
    
    if 'type_specialty' in filters and filters['type_specialty']:
        if isinstance(filters['type_specialty'], list):
            filtered_df = filtered_df[filtered_df['Type Specialty'].isin(filters['type_specialty'])]
        else:
            filtered_df = filtered_df[filtered_df['Type Specialty'] == filters['type_specialty']]
    
    return filtered_df

def filter_reviews(df, filters):
    """Filter reviews based on criteria"""
    filtered_df = df.copy()
    
    if 'min_rating' in filters and filters['min_rating']:
        filtered_df = filtered_df[filtered_df['Rating'] >= filters['min_rating']]
    
    if 'media_source' in filters and filters['media_source']:
        filtered_df = filtered_df[filtered_df['Media Source'].str.contains(filters['media_source'], case=False, na=False)]
    
    if 'pokemon_id' in filters and filters['pokemon_id']:
        if isinstance(filters['pokemon_id'], list):
            filtered_df = filtered_df[filtered_df['Pokemon ID'].isin(filters['pokemon_id'])]
        else:
            filtered_df = filtered_df[filtered_df['Pokemon ID'] == filters['pokemon_id']]
    
    return filtered_df

def save_filtered_data(data_dict, output_path):
    """Save filtered data to Excel with formatting"""
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        for sheet_name, df in data_dict.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)
        
        # Apply formatting
        workbook = writer.book
        for sheet_name in workbook.sheetnames:
            ws = workbook[sheet_name]
            
            # Format header row
            for cell in ws[1]:
                cell.font = Font(bold=True, color="FFFFFF")
                cell.fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
                cell.alignment = Alignment(horizontal="center")
            
            # Auto-adjust column widths
            for column in ws.columns:
                max_length = 0
                column_letter = column[0].column_letter
                for cell in column:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(cell.value)
                    except:
                        pass
                adjusted_width = min(max_length + 2, 50)
                ws.column_dimensions[column_letter].width = adjusted_width
    
    print(f"✓ Filtered data saved to: {output_path}")

def main():
    # Load the Pokemon database
    input_file = '"./DB_Create/report/XLSX/*.xlsx"'
    
    print("=" * 60)
    print("POKEMON DATA FILTER - Interactive Mode")
    print("=" * 60)
    
    try:
        data = load_pokemon_data(input_file)
        print(f"✓ Loaded {len(data['Pokemon'])} Pokemon")
        print(f"✓ Loaded {len(data['Trainers'])} Trainers")
        print(f"✓ Loaded {len(data['Gyms'])} Gyms")
        print(f"✓ Loaded {len(data['Reviews'])} Reviews")
    except Exception as e:
        print(f"✗ Error loading data: {e}")
        return
    
    # ========================================
    # DEFINE YOUR FILTERS HERE
    # ========================================
    
    # Example 1: Filter Fire-type Pokemon with high attack
    pokemon_filters = {
        'type1': 'Fire',              # Filter by primary type
        'min_attack': 80,              # Minimum attack stat
        # 'generation': 1,             # Uncomment to filter by generation
        # 'legendary': 'Yes',          # Uncomment to get only legendaries
        # 'min_hp': 70,                # Uncomment to set minimum HP
        # 'min_total_stats': 500,      # Uncomment to set minimum total stats
    }
    
    # Example 2: Filter trainers from specific region
    trainer_filters = {
        'region': 'Kanto',             # Filter by region
        # 'country': 'Japan',          # Uncomment to filter by country
        # 'trainer_type': 'Gym Leader', # Uncomment to filter by type
    }
    
    # Example 3: Filter gyms
    gym_filters = {
        # 'region': 'Johto',           # Uncomment to filter by region
        # 'type_specialty': 'Water',   # Uncomment to filter by type
    }
    
    # Example 4: Filter reviews
    review_filters = {
        'min_rating': 4,               # Minimum rating
        # 'media_source': 'Anime',     # Uncomment to filter by media
    }
    
    # ========================================
    # APPLY FILTERS
    # ========================================
    
    filtered_data = {}
    
    # Filter Pokemon
    if pokemon_filters:
        filtered_data['Pokemon'] = filter_pokemon(data['Pokemon'], pokemon_filters)
        print(f"\n✓ Filtered to {len(filtered_data['Pokemon'])} Pokemon")
    else:
        filtered_data['Pokemon'] = data['Pokemon']
    
    # Filter Trainers
    if trainer_filters:
        filtered_data['Trainers'] = filter_trainers(data['Trainers'], trainer_filters)
        print(f"✓ Filtered to {len(filtered_data['Trainers'])} Trainers")
    else:
        filtered_data['Trainers'] = data['Trainers']
    
    # Filter Gyms
    if gym_filters:
        filtered_data['Gyms'] = filter_gyms(data['Gyms'], gym_filters)
        print(f"✓ Filtered to {len(filtered_data['Gyms'])} Gyms")
    else:
        filtered_data['Gyms'] = data['Gyms']
    
    # Filter Reviews
    if review_filters:
        filtered_data['Reviews'] = filter_reviews(data['Reviews'], review_filters)
        print(f"✓ Filtered to {len(filtered_data['Reviews'])} Reviews")
    else:
        filtered_data['Reviews'] = data['Reviews']
    
    # Include Media Appearances (no filtering)
    filtered_data['Media Appearances'] = data['Media Appearances']
    
    # ========================================
    # SAVE FILTERED DATA
    # ========================================
    
    output_file = 'report/MAIN/pokemon_filtered_results.xlsx'
    save_filtered_data(filtered_data, output_file)
    
    print("\n" + "=" * 60)
    print("FILTERING COMPLETE!")
    print("=" * 60)
    print(f"Download your filtered Excel file from the outputs.")
    print("\nFilter Summary:")
    print(f"  • Pokemon: {len(filtered_data['Pokemon'])} records")
    print(f"  • Trainers: {len(filtered_data['Trainers'])} records")
    print(f"  • Gyms: {len(filtered_data['Gyms'])} records")
    print(f"  • Reviews: {len(filtered_data['Reviews'])} records")
    print(f"  • Media: {len(filtered_data['Media Appearances'])} records")

if __name__ == "__main__":
    main()
