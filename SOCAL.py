# spanish_oak_cal_extract.py

def extract_calibration_block(input_file, output_file):
    try:
        with open(input_file, "rb") as f:
            data = f.read()

        # Calibration block: 0x40000 to 0x7FFFF (256KB)
        start = 0x40000
        end = 0x80000
        cal_block = data[start:end]

        with open(output_file, "wb") as out:
            out.write(cal_block)
            print(f"✅ Calibration block extracted: {output_file}")
            print(f"📏 Size: {len(cal_block)} bytes (0x{len(cal_block):X})")

    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    extract_calibration_block("full_dump.bin", "spanish_oak_cal.bin")
