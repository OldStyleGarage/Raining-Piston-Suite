# full_hpt_extractor.py

import os

def extract_entire_hpt(file_path, output_path):
    print(f"📂 Reading full HPT file: {file_path}")

    if not os.path.isfile(file_path):
        print(f"❌ File not found: {file_path}")
        return

    try:
        with open(file_path, "rb") as f:
            data = f.read()
            print(f"✅ Successfully read {len(data)} bytes")

        with open(output_path, "wb") as out:
            out.write(data)
            print(f"📦 Entire file saved to: {output_path}")

    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    # Replace with your actual .hpt filename
    input_file = "RBFZF6666quickbasic popop rumble tune.hpt"
    output_file = "full_dump.bin"
    extract_entire_hpt(input_file, output_file)
