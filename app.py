# 1cm² 당 기공 밀도
stomatal_density = {
    "단풍잎": 72111.6,
    "테이블야자": 23041.5,
    "깻잎": 29387.2,
    "고무나무": 42760.7,
    "몬스테라": 12694.6,
    "스투키": 8675.1
}

# 기공 1개당 하루 CO₂ 흡수량(µg)
co2_per_stomata_per_day = 0.05

# CO₂ 단위 변환 계수
unit_conversion_co2 = {
    "µg": 1,
    "mg": 1e-3,
    "g": 1e-6,
    "kg": 1e-9
}

def leaf_stomata_absorption(plant, width, height, co2_unit="µg"):
    """
    입력:
        plant : 식물 이름 (str)
        width : 잎 가로(cm, float)
        height: 잎 세로(cm, float)
        co2_unit : CO₂ 단위 선택 (str, µg/mg/g/kg)
    출력:
        문자열: 기공 수와 하루 CO₂ 흡수량
    """
    try:
        width = float(width)
        height = float(height)
    except:
        return "숫자를 올바르게 입력해주세요."
    
    if plant not in stomatal_density:
        return "알 수 없는 식물입니다."
    
    density = stomatal_density[plant]
    total_stomata = width * height * density
    co2_absorbed = total_stomata * co2_per_stomata_per_day
    
    # 스투키 특수 처리
    if plant == "스투키":
        total_stomata *= 4
        co2_absorbed *= 4
    
    # 단위 변환
    co2_absorbed_converted = co2_absorbed * unit_conversion_co2.get(co2_unit, 1)
    
    return (f"🌿 {plant} 잎 {width} x {height} cm\n"
            f"- 기공 수: {int(total_stomata):,}개\n"
            f"- 하루 CO₂ 흡수량: {co2_absorbed_converted:,.4f} {co2_unit}")

# =============================
# 사용자 입력 예시
# =============================

if __name__ == "__main__":
    print("식물 6종: 단풍잎, 테이블야자, 깻잎, 고무나무, 몬스테라, 스투키")
    plant = input("식물 선택: ")
    width = input("잎 가로(cm) 입력: ")
    height = input("잎 세로(cm) 입력: ")
    co2_unit = input("CO₂ 단위 선택 (µg/mg/g/kg, 기본 µg): ") or "µg"
    
    result = leaf_stomata_absorption(plant, width, height, co2_unit)
    print(result)
