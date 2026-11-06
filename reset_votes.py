import sqlite3
import os
import database_setup

def reset_all_votes():
    # 1. Reset Database
    conn = sqlite3.connect(database_setup.DB_FILE)
    cursor = conn.cursor()
    
    try:
        # Delete all records from the votes table
        cursor.execute("DELETE FROM votes")
        
        # Reset everyone's voting status so they can vote again
        cursor.execute("UPDATE voters SET has_voted = 0")
        
        conn.commit()
        print("✅ Successfully cleared all votes from the SQLite database!")
        
    except Exception as e:
        print(f"❌ Error resetting database: {e}")
        
    finally:
        conn.close()

    # 2. Reset CSV File
    csv_file = "data/Votess.csv"
    if os.path.exists(csv_file):
        try:
            os.remove(csv_file)
            print("✅ Successfully deleted the Votess.csv file!")
        except Exception as e:
            print(f"❌ Error deleting CSV: {e}")
    else:
        print("ℹ️ No CSV file found (already clear).")

    print("\n🎉 All votes have been deleted! Everyone can now vote again.")

if __name__ == "__main__":
    print("=========================================")
    print("⚠️ WARNING: This will delete ALL vote records!")
    print("=========================================")
    confirm = input("Are you sure you want to proceed? Type 'yes' to clear: ")
    if confirm.lower() == 'yes':
        reset_all_votes()
    else:
        print("Cancelled.")
