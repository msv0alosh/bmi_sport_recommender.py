# -------------------------------------------------
# تحلیل آماری BMI دانشجویان - نمایش کامل مراحل محاسبه
# -------------------------------------------------

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("⚠️ لطفاً عدد معتبر وارد کنید.")

def show_quartile_steps(data, a, n):
    """نمایش مراحل محاسبه چارک aام"""
    print(f"\n--- محاسبه چارک {a} (Q{a}) ---")
    C = (a * n) / 4 + 0.5
    print(f"C = (a × n)/4 + 0.5 = ({a} × {n})/4 + 0.5 = {C:.3f}")
    k = int(C)
    r = C - k
    print(f"قسمت صحیح (k) = {k}, قسمت اعشاری (r) = {r:.3f}")
    
    if k >= n:
        result = data[-1]
        print(f"چون k ≥ n، Q{a} = آخرین داده = {result:.2f}")
        return result
        
    if r == 0:
        result = data[k - 1]
        print(f"چون r = 0، Q{a} = X_{k} = {result:.2f}")
        return result
    else:
        x_k = data[k - 1]
        x_k1 = data[k] if k < len(data) else data[-1]
        result = x_k + r * (x_k1 - x_k)
        print(f"Q{a} = X_{k} + r × (X_{k+1} - X_{k})")
        print(f"Q{a} = {x_k:.2f} + {r:.3f} × ({x_k1:.2f} - {x_k:.2f})")
        print(f"Q{a} = {x_k:.2f} + {r:.3f} × {x_k1 - x_k:.2f} = {result:.2f}")
        return result

# --- جمع‌آوری داده‌ها ---
print("🎓 تحلیل آماری BMI دانشجویان تربیت بدنی")
print("💡 برای پایان، در هر دو سؤال «0» را وارد کنید.")
print("-" * 55)

bmis = []
student_index = 1

while True:
    print(f"\n--- دانشجوی {student_index} ---")
    weight = get_number(f"وزن دانشجوی {student_index} (kg): ")
    height = get_number(f"قد دانشجوی {student_index} (cm): ")
    
    if weight == 0 and height == 0:
        print("\n✅ ورودی داده‌ها تمام شد.")
        break
    
    if weight <= 0 or height <= 0:
        print("⚠️ وزن و قد باید مثبت باشند.")
        continue
    
    bmi = weight / ((height / 100) ** 2)
    bmis.append(bmi)
    print(f"  👤 BMI: {bmi:.2f}")
    student_index += 1

if not bmis:
    print("❌ هیچ داده‌ای وارد نشد.")
    exit()

n = len(bmis)
bmis_sorted = sorted(bmis)

print("\n" + "="*70)
print("🧮 مراحل کامل محاسبه شاخص‌های آماری")
print("="*70)

# --- 1. میانگین ---
print("\n1️⃣ محاسبه میانگین (Mean):")
print("فرمول: X̄ = (ΣX_i) / n")
sum_bmis = sum(bmis)
mean = sum_bmis / n
terms = " + ".join([f"{x:.2f}" for x in bmis])
print(f"ΣX_i = {terms} = {sum_bmis:.2f}")
print(f"n = {n}")
print(f"X̄ = {sum_bmis:.2f} / {n} = {mean:.4f}")

# --- 2. واریانس ---
print("\n2️⃣ محاسبه واریانس جامعه (Population Variance):")
print("فرمول: σ² = Σ(X_i - X̄)² / n")
print(f"میانگین (X̄) = {mean:.4f}")
print("\nمحاسبه مربعات انحرافات:")
sum_sq = 0
for i, x in enumerate(bmis, 1):
    diff = x - mean
    sq = diff ** 2
    sum_sq += sq
    print(f"({x:.2f} - {mean:.4f})² = ({diff:.4f})² = {sq:.4f}")

variance = sum_sq / n
print(f"\nΣ(X_i - X̄)² = {sum_sq:.4f}")
print(f"σ² = {sum_sq:.4f} / {n} = {variance:.4f}")

# --- 3. انحراف معیار ---
print("\n3️⃣ محاسبه انحراف معیار (Standard Deviation):")
print("فرمول: σ = √(σ²)")
std_dev = variance ** 0.5
print(f"σ = √({variance:.4f}) = {std_dev:.4f}")

# --- 4. ضریب تغییرات ---
print("\n4️⃣ محاسبه ضریب تغییرات (CV):")
print("فرمول: CV = (σ / X̄) × 100%")
cv = (std_dev / mean) * 100
print(f"CV = ({std_dev:.4f} / {mean:.4f}) × 100% = {cv:.2f}%")

# --- 5. دامنه ---
print("\n5️⃣ محاسبه دامنه (Range):")
print("فرمول: R = max(X_i) - min(X_i)")
min_val = min(bmis)
max_val = max(bmis)
data_range = max_val - min_val
print(f"min = {min_val:.2f}, max = {max_val:.2f}")
print(f"R = {max_val:.2f} - {min_val:.2f} = {data_range:.2f}")

# --- 6. چارک‌ها ---
print("\n6️⃣ محاسبه چارک‌ها (با فرمول استاد):")
print("فرمول رتبه: C = (a × n)/4 + 0.5")

Q1 = show_quartile_steps(bmis_sorted, 1, n)
Q2 = show_quartile_steps(bmis_sorted, 2, n)
Q3 = show_quartile_steps(bmis_sorted, 3, n)

# --- نتایج نهایی ---
print("\n" + "="*70)
print("📊 نتایج نهایی")
print("="*70)
print(f"تعداد دانشجویان: {n}")
print(f"میانگین: {mean:.4f}")
print(f"واریانس (جامعه): {variance:.4f}")
print(f"انحراف معیار: {std_dev:.4f}")
print(f"ضریب تغییرات: {cv:.2f}%")
print(f"دامنه: {data_range:.2f}")
print(f"چارک اول (Q1): {Q1:.2f}")
print(f"میانه (Q2): {Q2:.2f}")
print(f"چارک سوم (Q3): {Q3:.2f}")

# --- تفسیر ---
print("\n🔍 تحلیل:")
if cv < 10:
    print("• پراکندگی BMI کم است → گروه همگن است.")
elif cv < 20:
    print("• پراکندگی BMI متوسط است.")
else:
    print("• پراکندگی BMI زیاد است.")

if 18.5 <= mean <= 24.9:
    print("• میانگین BMI در محدوده سالم است. ✅")