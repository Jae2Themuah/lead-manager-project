# null_byte_remover.py
import os

def clean_file(file_path):
    try:
        # First create a backup
        backup_path = file_path + '.bak'
        with open(file_path, 'rb') as original_file:
            original_content = original_file.read()
            
        # Save backup
        with open(backup_path, 'wb') as backup_file:
            backup_file.write(original_content)
            
        # Remove null bytes
        cleaned_content = original_content.replace(b'\x00', b'')
        
        # Write cleaned content back
        with open(file_path, 'wb') as cleaned_file:
            cleaned_file.write(cleaned_content)
            
        null_count = len(original_content) - len(cleaned_content)
        return f"Success! Removed {null_count} null bytes. Backup saved as {backup_path}"
    
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    file_path = input("Enter the path to the file to clean (e.g., myapp/models.py): ")
    if os.path.exists(file_path):
        result = clean_file(file_path)
        print(result)
    else:
        print(f"File not found: {file_path}")