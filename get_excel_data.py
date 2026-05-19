import pandas as pd
from pathlib import Path
from typing import Dict, Any

def read_db_memory_file(file_path: str):
    df = pd.read_excel(file_path, sheet_name='Sheet1', header=None)
    
    db_name = str(df.iloc[0, 0]).strip()
    
    result = {
        "db_name": db_name,
        "variables": {}
    }
    
    seen = set()
    
    for i in range(2, len(df)):
        row = df.iloc[i]
        name = str(row[1]).strip() if pd.notna(row[1]) else ""
        
        if name == "" or name.lower() == "nan":
            break
            
        # Chỉ lấy lần đầu tiên (phần Setting)
        if name in seen:
            continue
            
        seen.add(name)
        
        result["variables"][name] = {
            "stt": str(row[0]).strip() if pd.notna(row[0]) else "",
            "name": name,
            "type": str(row[2]).strip() if pd.notna(row[2]) else "",
            "address": str(row[3]).strip() if pd.notna(row[3]) else "",
            "value": str(row[4]).strip() if pd.notna(row[4]) else ""
        }
    
    return result

if __name__ == "__main__":
    file_path = "C:/Users/automation02/Desktop/DB Memory Addres Default.xlsx"
    
    db_dict = read_db_memory_file(file_path)

    print("\n" + "="*60)
    print(f"DB: {db_dict['db_name']}")
    print(f"Tổng số biến: {len(db_dict['variables'])}")
    print("="*60)

    for i, (name, info) in enumerate(db_dict['variables'].items()):
        if i >= len(db_dict['variables']):
            break
        print(f"{info['stt']:>3}. {name:<30} | {info['type']:<8} | Address: {info['address']}")
    print(f"DB: \n {db_dict}")
    # import json
    # with open(f"{db_dict['db_name']}_extracted.json", "w", encoding="utf-8") as f:
    #     json.dump(db_dict, f, ensure_ascii=False, indent=2)
    # print(f"\n💾 Đã lưu file JSON: {db_dict['db_name']}_extracted.json")