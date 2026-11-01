import os
# ====================== DATA ======================
DOCTORS = [
 ("Dr. Ayesha Khan","Interventional Cardiologist","15 years","Mon-Fri, 9am-2pm"),
 ("Dr. Bilal Ahmed","Heart Failure Specialist","12 years","Mon, Wed, Sat, 4pm-8pm"),
 ("Dr. Sana Malik","Electrophysiologist (Arrhythmia)","10 years","Tue, Thu, 10am-3pm"),
 ("Dr. Usman Raza","Cardiac Surgeon","20 years","Mon-Thu, 9am-1pm"),
 ("Dr. Hina Farooq","Preventive Cardiologist","8 years","Daily, 5pm-9pm"),
 ("Dr. Sameer Akhtar","Myocardial Disease Specialist","8 years","Tue-Sat, 10am-3pm"),
 ("Dr. Hoorain Malik","Thrombosis & Embolism Specialist","9 years","Mon-Thu, 2pm-6pm"),
 ("Dr. Ibrahim Rauf","Cardiac Genetics Specialist","10 years","Daily, 4pm-8pm"),
 ("Dr. Dua Hassan","Geriatric Cardiologist","11 years","Mon-Fri, 9am-2pm"),
 ("Dr. Mustafa Riaz","Cardiac Transplant Specialist","12 years","Tue-Sat, 10am-3pm"),
 ("Dr. Areeba Salman","Heart Valve Imaging Specialist","13 years","Mon-Thu, 2pm-6pm"),
 ("Dr. Waleed Anwar","Vascular Surgery Specialist","14 years","Daily, 4pm-8pm"),
 ("Dr. Saira Imtiaz","Cardiac Risk Assessment Specialist","15 years","Mon-Fri, 9am-2pm"),
 ("Dr. Rameez Jamil","Cardiac Emergency Specialist","16 years","Tue-Sat, 10am-3pm"),
 ("Dr. Alina Shah","Cardiac Medicine Specialist","17 years","Mon-Thu, 2pm-6pm"),
 ("Dr. Yousuf Kareem","Cardiac Surgery & Recovery Specialist","18 years","Daily, 4pm-8pm")  
]
# name, symptoms, causes, treatment, diet, recovery
DISEASES = [
    ("Heart Attack",
     "Severe chest pain or pressure, pain in the left arm or jaw, shortness of breath, sweating, nausea.",
     "Blocked heart arteries, blood clots, smoking, diabetes, high blood pressure.",
     "Emergency angioplasty/stent, clot-dissolving drugs, or bypass surgery. Go to hospital immediately.",
     "Low salt, little fried food or ghee, vegetables, fruit, oats and fish.",
     "Hospital stay may be several days; recovery often takes 6-12 weeks or longer."),

    ("High Blood Pressure",
     "Often no symptoms; sometimes headache, dizziness or blurred vision.",
     "Too much salt, obesity, stress, inactivity, family history, smoking.",
     "Doctor-prescribed medicines, weight management and regular exercise.",
     "Vegetables, fruit, whole grains and low-salt foods; limit processed foods.",
     "May improve within weeks, but long-term monitoring is needed."),

    ("High Cholesterol",
     "Usually no symptoms; detected through a lipid profile blood test.",
     "Diet high in saturated fats, obesity, inactivity and genetics.",
     "Doctor-prescribed medicines, such as statins, and lifestyle changes.",
     "Oats, lentils, almonds, fish, vegetables and olive oil; limit fried foods.",
     "Cholesterol levels may improve within 8-12 weeks."),

    ("Angina",
     "Chest pressure or discomfort during activity, sometimes spreading to the arm or jaw.",
     "Reduced blood flow to the heart due to narrowed arteries.",
     "Medical assessment, prescribed medicines and sometimes stent or bypass surgery.",
     "Heart-healthy diet, weight management and no smoking.",
     "Symptoms may improve within weeks, but ongoing care is often required."),

    ("Heart Failure",
     "Shortness of breath, swollen legs, tiredness and difficulty breathing when lying down.",
     "Previous heart attack, high blood pressure, valve disease or cardiomyopathy.",
     "Prescribed medicines, salt or fluid control and sometimes devices or surgery.",
     "Low-salt foods; follow your doctor's fluid recommendations.",
     "A long-term condition; treatment can improve symptoms and quality of life."),

    ("Arrhythmia",
     "Fast or irregular heartbeat, dizziness, fainting or noticeable palpitations.",
     "Electrical-system problems, heart disease, thyroid problems or excess caffeine.",
     "ECG/Holter testing, prescribed medicines, ablation or a pacemaker when needed.",
     "Limit excess caffeine and energy drinks; maintain a balanced diet.",
     "Depends on the type and treatment; recovery may take days to weeks."),

    ("Coronary Artery Disease",
     "Chest pain, shortness of breath, fatigue or sometimes no symptoms.",
     "Plaque buildup in the coronary arteries, smoking, diabetes and high cholesterol.",
     "Lifestyle changes, prescribed medicines, angioplasty or bypass surgery.",
     "Vegetables, fruit, whole grains, fish and low-saturated-fat foods.",
     "Long-term management is usually required."),

    ("Cardiomyopathy",
     "Breathlessness, fatigue, swollen legs, dizziness or irregular heartbeat.",
     "Genetics, infections, alcohol misuse, high blood pressure or other heart conditions.",
     "Medicines, lifestyle changes and sometimes implanted devices or surgery.",
     "Balanced diet with limited salt if advised by a doctor.",
     "Varies from weeks to months; some types require lifelong care."),

    ("Myocarditis",
     "Chest pain, fatigue, shortness of breath or irregular heartbeat.",
     "Often viral infections; sometimes autoimmune conditions or certain medicines.",
     "Medical evaluation, rest and treatment based on the cause and severity.",
     "Balanced meals, adequate fluids as advised and avoidance of alcohol during recovery.",
     "May take weeks to months; severe cases can take longer."),

    ("Pericarditis",
     "Sharp chest pain that may worsen with deep breathing or lying down.",
     "Often viral infections; sometimes autoimmune disease or other medical conditions.",
     "Doctor-prescribed anti-inflammatory treatment and management of the cause.",
     "Balanced diet and adequate rest; follow medical advice.",
     "Often improves over days to weeks, but recurrence is possible."),

    ("Heart Valve Disease",
     "Shortness of breath, fatigue, chest discomfort, dizziness or swollen ankles.",
     "Age-related changes, congenital defects, infections or rheumatic heart disease.",
     "Monitoring, medicines for symptoms and sometimes valve repair or replacement.",
     "Heart-healthy, balanced diet with salt restriction if advised.",
     "Depends on the affected valve and treatment; follow-up may be lifelong."),

    ("Atrial Fibrillation",
     "Irregular heartbeat, palpitations, tiredness, dizziness or breathlessness.",
     "Age, high blood pressure, heart disease, sleep apnea or excess alcohol.",
     "Medicines to control heart rate or rhythm, stroke-prevention treatment and sometimes ablation.",
     "Balanced diet, limited alcohol and moderation of caffeine.",
     "May be controlled over days to weeks, but long-term management is often needed."),

    ("Bradycardia",
     "Slow heartbeat, weakness, fatigue, dizziness or fainting.",
     "Problems with the heart's electrical system, certain medicines or age-related changes.",
     "Medical evaluation, review of medicines and sometimes a pacemaker.",
     "Balanced diet and avoid changing medicines without medical advice.",
     "Depends on the cause; recovery after pacemaker placement often takes several weeks."),

    ("Tachycardia",
     "Rapid heartbeat, palpitations, dizziness, breathlessness or chest discomfort.",
     "Electrical problems, fever, dehydration, anemia, caffeine or heart disease.",
     "Treatment depends on the type; may include medicines or an electrical procedure.",
     "Stay hydrated if appropriate, limit excess caffeine and avoid energy drinks.",
     "May resolve quickly or require long-term treatment depending on the cause."),

    ("Congenital Heart Disease",
     "Symptoms may include breathlessness, fatigue, blue lips or poor growth; some people have none.",
     "Heart structure differences present from birth due to genetic or developmental factors.",
     "Monitoring, medicines, catheter-based procedures or surgery depending on the defect.",
     "Balanced diet; children may need individualized nutrition advice.",
     "Some defects need no treatment; others require lifelong follow-up."),

    ("Rheumatic Heart Disease",
     "Breathlessness, fatigue, chest discomfort, palpitations or swollen legs.",
     "Heart valve damage following rheumatic fever, which can occur after untreated strep infection.",
     "Medical assessment, prescribed medicines and sometimes valve surgery.",
     "Balanced, heart-healthy diet with salt restriction if recommended.",
     "Long-term monitoring is often required; valve damage may be permanent."),

    ("Aortic Aneurysm",
     "Often no symptoms; severe chest, back or abdominal pain may occur if it becomes an emergency.",
     "Weakening of the aortic wall, high blood pressure, smoking or inherited conditions.",
     "Monitoring, blood-pressure management and surgery when indicated.",
     "Heart-healthy diet, limited salt and no smoking.",
     "Monitoring is ongoing; recovery after surgery may take weeks to months."),

    ("Peripheral Artery Disease",
     "Leg pain while walking, cold feet, slow-healing wounds or weak pulses.",
     "Narrowed arteries, often due to atherosclerosis, smoking, diabetes or high cholesterol.",
     "Supervised exercise, prescribed medicines and sometimes angioplasty or surgery.",
     "Vegetables, fruit, whole grains and foods low in saturated fat.",
     "Often requires lifelong management; walking may improve over weeks or months."),

    ("Pulmonary Hypertension",
     "Shortness of breath, fatigue, chest discomfort, dizziness or swollen legs.",
     "Lung disease, certain heart conditions, blood clots or other underlying causes.",
     "Specialist assessment and medicines targeted to the cause and type.",
     "Balanced diet; follow medical advice about salt and fluid intake.",
     "Usually requires long-term care; progress varies by cause and severity."),

    ("Endocarditis",
     "Fever, chills, fatigue, night sweats, shortness of breath or new heart murmur.",
     "Infection of the inner lining of the heart, often involving a heart valve.",
     "Urgent hospital assessment and antimicrobial treatment; sometimes surgery.",
     "Nutritious balanced meals during treatment, following the care team's advice.",
     "Treatment often lasts several weeks; recovery depends on complications."),

    ("Cardiac Arrest",
     "Sudden collapse, unresponsiveness and no normal breathing.",
     "Dangerous heart rhythm, heart attack or other serious heart conditions.",
     "Call emergency services, start CPR immediately and use an AED if available.",
     "Prevention includes managing risk factors and following medical advice.",
     "Recovery varies widely and requires emergency and follow-up care."),

    ("Hypertrophic Cardiomyopathy",
     "Breathlessness, chest pain, dizziness, fainting or palpitations, especially during exercise.",
     "Inherited gene changes that thicken the heart muscle.",
     "Medicines, avoiding extreme exertion, and sometimes septal reduction surgery or an implanted defibrillator.",
     "Stay well hydrated, limit alcohol and excess salt; follow your cardiologist's advice.",
     "Lifelong follow-up; symptoms often improve within weeks of starting treatment."),

    ("Dilated Cardiomyopathy",
     "Breathlessness, fatigue, swollen legs, palpitations and difficulty breathing when lying flat.",
     "Genetics, viral infection, alcohol misuse, long-term high blood pressure or unknown causes.",
     "Heart-failure medicines, salt control, and sometimes a pacemaker, defibrillator or transplant.",
     "Low-salt diet, avoid alcohol; vegetables, fruit and lean protein; follow fluid advice.",
     "Long-term condition; many people improve over 3-6 months on treatment."),

    ("Mitral Valve Prolapse",
     "Often no symptoms; sometimes palpitations, chest discomfort, tiredness or dizziness.",
     "Floppy mitral valve flaps, often inherited or linked to connective-tissue conditions.",
     "Usually only monitoring; surgery for severe leakage.",
     "Limit caffeine and energy drinks; balanced heart-healthy diet.",
     "Most people live normally with regular check-ups."),

    ("Aortic Stenosis",
     "Chest pain or pressure, breathlessness on effort, dizziness, fainting and tiredness.",
     "Age-related calcium build-up on the aortic valve, a congenital bicuspid valve or rheumatic disease.",
     "Monitoring, then valve replacement (surgical or TAVI) when symptoms appear.",
     "Low-salt, heart-healthy diet; avoid heavy exertion until your doctor advises.",
     "Recovery after valve replacement is often 4-8 weeks."),

    ("Mitral Stenosis",
     "Breathlessness, tiredness, palpitations, cough and swollen ankles.",
     "Mostly rheumatic fever; sometimes calcification with age.",
     "Medicines, balloon valvotomy or valve surgery.",
     "Low-salt diet; limit caffeine.",
     "Procedure recovery is typically a few weeks; lifelong follow-up."),

    ("Ventricular Tachycardia",
     "Very fast heartbeat, dizziness, breathlessness, chest discomfort or fainting.",
     "Previous heart attack, cardiomyopathy, electrolyte imbalance or inherited rhythm disorders.",
     "Emergency rhythm control, ablation or an implanted defibrillator (ICD).",
     "Avoid caffeine, energy drinks and alcohol; keep potassium and magnesium balanced as advised.",
     "Depends on the cause; ICD recovery takes about 4-6 weeks."),

    ("Supraventricular Tachycardia",
     "Sudden racing heartbeat that starts and stops, palpitations, lightheadedness, breathlessness.",
     "Extra electrical pathway in the heart, caffeine, stress or stimulants.",
     "Vagal manoeuvres, medicines or catheter ablation, which often cures it.",
     "Cut caffeine, energy drinks and alcohol; drink enough water.",
     "Episodes often settle in minutes; ablation recovery is a few days."),

    ("Long QT Syndrome",
     "Fainting or seizure-like episodes and palpitations, often triggered by exercise or sudden noise.",
     "Inherited gene changes, certain medicines or low potassium.",
     "Avoiding trigger medicines, beta-blockers, and sometimes an ICD.",
     "Potassium and magnesium-rich foods such as bananas, spinach and yoghurt; avoid energy drinks.",
     "Lifelong management with regular ECG checks."),

    ("Heart Block",
     "Slow heartbeat, dizziness, fainting, tiredness and breathlessness.",
     "Ageing of the conduction system, heart attack, medicines or infections.",
     "Monitoring; a pacemaker for significant block.",
     "Balanced, heart-healthy diet; do not change medicines without advice.",
     "Pacemaker recovery usually takes 4-6 weeks."),

    ("Cardiogenic Shock",
     "Cold clammy skin, confusion, rapid weak pulse, severe breathlessness and very low blood pressure.",
     "Severe heart attack or sudden failure of the heart muscle or a valve.",
     "Intensive care: medicines, oxygen, opening blocked arteries and heart-support devices.",
     "Managed in hospital; later a low-salt, heart-healthy diet.",
     "Needs ICU care; recovery takes weeks to months."),

    ("Deep Vein Thrombosis",
     "Leg pain, swelling, warmth and redness, usually in one leg.",
     "Long immobility, surgery, long travel, pregnancy, cancer or clotting disorders.",
     "Blood thinners, compression stockings and walking; urgent care if breathless.",
     "Stay hydrated and eat a balanced diet; keep vitamin K intake steady if on warfarin.",
     "Treatment usually lasts 3-6 months."),

    ("Pulmonary Embolism",
     "Sudden breathlessness, sharp chest pain on breathing, cough, fast heartbeat or fainting.",
     "A blood clot travelling from the leg veins to the lungs.",
     "Emergency hospital care with blood thinners or clot-dissolving drugs.",
     "Stay hydrated; keep vitamin K intake steady if on warfarin.",
     "Weeks to months; blood thinners are often continued for 3-6 months or more."),

    ("Low Blood Pressure",
     "Dizziness, lightheadedness, fainting, blurred vision and tiredness.",
     "Dehydration, blood loss, heart problems, certain medicines or standing up too quickly.",
     "Treat the cause, stand up slowly, more fluids and salt if your doctor advises.",
     "More water, a little extra salt only if your doctor agrees, small frequent meals.",
     "Often improves within days with fluids; long-term causes need review."),

    ("Aortic Dissection",
     "Sudden tearing chest or back pain, fainting, weak pulse or breathlessness.",
     "High blood pressure, weak aortic wall, inherited conditions or injury.",
     "Emergency surgery or stent graft with strict blood-pressure control.",
     "Low-salt diet and no smoking after recovery.",
     "Recovery takes months; lifelong imaging and follow-up."),

    ("Atherosclerosis",
     "Often none until arteries narrow; then chest pain, leg pain on walking or breathlessness.",
     "Plaque from cholesterol, smoking, diabetes, high blood pressure and inactivity.",
     "Lifestyle change, medicines, angioplasty or bypass when needed.",
     "Oats, lentils, fish, nuts, vegetables and olive oil; avoid fried food, ghee and sweets.",
     "Lifelong control; cholesterol improves in 8-12 weeks."),

    ("Atrial Septal Defect",
     "Breathlessness, tiredness, palpitations, swollen legs; many people have none.",
     "A hole between the upper heart chambers present from birth.",
     "Monitoring, or closure with a catheter device or surgery.",
     "Balanced heart-healthy diet.",
     "Recovery after closure is about 2-6 weeks."),

    ("Ventricular Septal Defect",
     "Fast breathing, poor feeding in babies, tiredness and sweating; small holes may cause none.",
     "A hole between the lower heart chambers present from birth.",
     "Small ones may close on their own; larger ones need surgery or catheter closure.",
     "Infants may need high-calorie feeds as advised by the doctor; older patients a balanced diet.",
     "Recovery after repair is typically 4-8 weeks."),

    ("Unstable Angina",
     "Chest pain at rest, or pain that is increasing and lasting longer than usual.",
     "Narrowed coronary arteries with a partly blocked plaque or clot.",
     "Emergency hospital treatment, angioplasty/stent or bypass.",
     "Heart-healthy low-fat, low-salt diet after treatment.",
     "Hospital stay of several days; recovery 4-8 weeks."),

    ("Hypertensive Heart Disease",
     "Breathlessness, chest pain, swollen legs, palpitations and tiredness.",
     "Long-term uncontrolled high blood pressure.",
     "Strict blood-pressure control and treatment of any heart failure.",
     "Low-salt DASH-style diet with vegetables, fruit and whole grains; avoid pickles and processed food.",
     "Improves over weeks to months with good control."),

    ("Takotsubo Cardiomyopathy",
     "Sudden chest pain and breathlessness after severe emotional or physical stress.",
     "A surge of stress hormones causing temporary weakening of the heart muscle.",
     "Hospital monitoring and supportive care.",
     "Heart-healthy balanced diet; avoid excess caffeine.",
     "Usually recovers within 1-3 months.")
]

# Medicines (general information only - always as prescribed by a doctor)
MEDS = {
 "Heart Attack": "Emergency aspirin (as told by the emergency team), clopidogrel or ticagrelor, heparin, statins, beta-blockers and ACE inhibitors, all given by doctors. Call emergency first.",
 "High Blood Pressure": "ACE inhibitors (e.g. enalapril), ARBs (e.g. losartan), amlodipine or diuretics (e.g. hydrochlorothiazide), chosen by your doctor.",
 "High Cholesterol": "Statins (e.g. atorvastatin, rosuvastatin); sometimes ezetimibe.",
 "Angina": "Aspirin, nitrates (e.g. GTN spray for attacks), beta-blockers and statins.",
 "Heart Failure": "ACE inhibitors, beta-blockers (e.g. bisoprolol), diuretics (e.g. furosemide), spironolactone and SGLT2 inhibitors.",
 "Arrhythmia": "Beta-blockers, calcium-channel blockers or anti-arrhythmics (e.g. amiodarone), depending on the type.",
 "Coronary Artery Disease": "Aspirin, statins, beta-blockers, nitrates and ACE inhibitors.",
 "Cardiomyopathy": "Beta-blockers, ACE inhibitors/ARBs and diuretics, depending on the type.",
 "Myocarditis": "Treatment depends on the cause; heart-failure medicines if needed. Avoid painkillers like NSAIDs and hard exercise unless your doctor advises.",
 "Pericarditis": "NSAIDs (e.g. ibuprofen or aspirin) with colchicine.",
 "Heart Valve Disease": "Diuretics, beta-blockers and anticoagulants (e.g. warfarin) in selected cases; repair or replacement for severe disease.",
 "Atrial Fibrillation": "Beta-blockers or diltiazem to control the rate, anticoagulants (apixaban, rivaroxaban, warfarin) and amiodarone.",
 "Bradycardia": "Usually no medicine; doctors adjust drugs that slow the heart. A pacemaker if needed.",
 "Tachycardia": "Beta-blockers, calcium-channel blockers or anti-arrhythmics, based on the type.",
 "Congenital Heart Disease": "Diuretics, digoxin or other heart medicines for symptoms; procedures correct the defect.",
 "Rheumatic Heart Disease": "Penicillin prophylaxis (e.g. benzathine penicillin), diuretics and anticoagulants if needed.",
 "Aortic Aneurysm": "Beta-blockers or ARBs to lower blood pressure; surgery when the aneurysm is large.",
 "Peripheral Artery Disease": "Aspirin or clopidogrel, statins, cilostazol for walking pain and blood-pressure medicines.",
 "Pulmonary Hypertension": "Specialist drugs such as sildenafil or bosentan, plus diuretics and anticoagulants as needed.",
 "Endocarditis": "Intravenous antibiotics for several weeks in hospital, chosen by the doctor.",
 "Cardiac Arrest": "No home medicine: CPR, defibrillation and hospital drugs. Afterwards beta-blockers or an ICD may be advised.",
 "Hypertrophic Cardiomyopathy": "Beta-blockers (e.g. metoprolol), verapamil or disopyramide.",
 "Dilated Cardiomyopathy": "ACE inhibitors (e.g. enalapril), beta-blockers (e.g. carvedilol), diuretics (e.g. furosemide) and spironolactone.",
 "Mitral Valve Prolapse": "Usually none; a beta-blocker (e.g. propranolol) if palpitations trouble you.",
 "Aortic Stenosis": "No medicine cures it; diuretics may ease breathlessness and blood-pressure drugs are used carefully. Valve replacement is the treatment.",
 "Mitral Stenosis": "Diuretics, beta-blockers for heart rate, anticoagulants (e.g. warfarin) if atrial fibrillation, and penicillin prophylaxis for rheumatic fever.",
 "Ventricular Tachycardia": "Anti-arrhythmics (e.g. amiodarone) or beta-blockers, only under cardiologist supervision.",
 "Supraventricular Tachycardia": "Adenosine (in hospital), beta-blockers or calcium-channel blockers.",
 "Long QT Syndrome": "Beta-blockers (e.g. nadolol, propranolol); avoid medicines that prolong the QT interval.",
 "Heart Block": "No medicine fixes significant heart block; doctors review drugs that slow the heart. A pacemaker is the usual treatment.",
 "Cardiogenic Shock": "Hospital-only drugs such as noradrenaline or dobutamine, given by the ICU team.",
 "Deep Vein Thrombosis": "Anticoagulants (e.g. rivaroxaban, apixaban, warfarin or heparin).",
 "Pulmonary Embolism": "Heparin, then rivaroxaban, apixaban or warfarin; clot-dissolving drugs in hospital.",
 "Low Blood Pressure": "Usually none; fludrocortisone or midodrine only in specific cases.",
 "Aortic Dissection": "IV beta-blockers and pain relief in hospital; lifelong blood-pressure medicines afterwards.",
 "Atherosclerosis": "Statins (e.g. atorvastatin), aspirin and blood-pressure medicines.",
 "Atrial Septal Defect": "Medicines only relieve symptoms (diuretics, rhythm drugs); closure fixes the hole.",
 "Ventricular Septal Defect": "Diuretics (e.g. furosemide) and digoxin for symptoms.",
 "Unstable Angina": "Aspirin, clopidogrel, nitrates, heparin, statins and beta-blockers in hospital.",
 "Hypertensive Heart Disease": "ACE inhibitors/ARBs, amlodipine, diuretics and beta-blockers.",
 "Takotsubo Cardiomyopathy": "ACE inhibitors and beta-blockers while the heart recovers.",
}

# ====================== CHATBOT ======================
import re, math
DISCLAIMER = "\n\n(This is general information, not medical advice. Take medicines only as prescribed by your doctor. Please consult your cardiologist.)"
EMERGENCY = "WARNING: Severe chest pain, trouble breathing or fainting can be an emergency. Call 1122 (or your local emergency number) or go to the nearest hospital now."
URGENT = {"Heart Attack","Cardiac Arrest","Aortic Dissection","Pulmonary Embolism","Cardiogenic Shock","Unstable Angina"}

ALIASES = {
 "Heart Attack": ["heart attack","myocardial infarction"],
 "High Blood Pressure": ["high blood pressure","blood pressure","hypertension","high bp","bp"],
 "High Cholesterol": ["cholesterol","lipid"],
 "Heart Failure": ["heart failure","congestive"],
 "Arrhythmia": ["irregular heartbeat","irregular heart"],
 "Coronary Artery Disease": ["coronary artery","coronary","cad"],
 "Heart Valve Disease": ["valve disease","valve"],
 "Atrial Fibrillation": ["afib","a-fib"],
 "Bradycardia": ["slow heart"],
 "Tachycardia": ["fast heart","rapid heart"],
 "Congenital Heart Disease": ["congenital"],
 "Rheumatic Heart Disease": ["rheumatic"],
 "Aortic Aneurysm": ["aneurysm"],
 "Peripheral Artery Disease": ["peripheral"],
 "Hypertrophic Cardiomyopathy": ["hypertrophic"],
 "Dilated Cardiomyopathy": ["dilated"],
 "Mitral Valve Prolapse": ["prolapse","mvp"],
 "Ventricular Tachycardia": ["vt"],
 "Supraventricular Tachycardia": ["supraventricular","svt"],
 "Long QT Syndrome": ["long qt","qt"],
 "Heart Block": ["av block"],
 "Deep Vein Thrombosis": ["deep vein","dvt"],
 "Pulmonary Embolism": ["embolism"],
 "Low Blood Pressure": ["low bp","hypotension"],
 "Aortic Dissection": ["dissection"],
 "Atherosclerosis": ["plaque"],
 "Atrial Septal Defect": ["asd","atrial septal"],
 "Ventricular Septal Defect": ["vsd","ventricular septal"],
 "Hypertensive Heart Disease": ["hypertensive heart"],
 "Takotsubo Cardiomyopathy": ["takotsubo","broken heart"],
}
URDU = [("seene mein dard","chest pain"),("seene me dard","chest pain"),("sar dard","headache"),("seena","chest"),
        ("dard","pain"),("saans","breath"),("dhadkan","heartbeat"),("chakkar","dizziness"),("pasina","sweating"),
        ("sujan","swelling"),("thakan","fatigue"),("thakawat","fatigue"),("behoshi","fainting"),("bukhar","fever"),
        ("pairon","leg"),("pair","leg"),("dil","heart")]
INTENTS = [
 ("symptoms", ["symptom","symptoms","signs","sign","lakshan","alamat"]),
 ("causes", ["cause","causes","why","reason","wajah","risk"]),
 ("treatment", ["treat","cure","therapy","ilaj","surgery","procedure"]),
 ("medicine", ["medicine","medication","drug","tablet","dawa","dawai","pill","pills","prescri","capsule"]),
 ("diet", ["diet","food","foods","eat","eating","khana","nutrition","avoid","meal"]),
 ("recovery", ["recover","recovery","how long","kitne din","duration","time"]),
]
LABELS = {"symptoms":"Symptoms","causes":"Causes","treatment":"Treatment",
          "medicine":"Medicines (only as prescribed by your doctor)","diet":"Food / Diet","recovery":"Recovery"}
IDX = {"symptoms":1,"causes":2,"treatment":3,"diet":4,"recovery":5}
ALLK = ["symptoms","causes","treatment","medicine","diet","recovery"]
NAMES = [d[0] for d in DISEASES]

def _norm(msg):
    m = msg.lower()
    for k, v in URDU: m = re.sub(r"\b"+k+r"\b", v, m)
    return m
def _has(m, k):
    return re.search(r"\b"+re.escape(k)+(r"\b" if len(k) <= 3 else ""), m) is not None
def _field(d, k): return MEDS.get(d[0], "Ask your cardiologist.") if k == "medicine" else d[IDX[k]]
def describe(d, kinds=None):
    return "\n".join([d[0]] + [LABELS[k]+": "+_field(d, k) for k in (kinds or ALLK)])

def find_named(m):
    best, blen = None, 0
    for d in DISEASES:
        for k in [d[0].lower()] + ALIASES.get(d[0], []):
            if len(k) > blen and re.search(r"\b"+re.escape(k)+r"\b", m): best, blen = d, len(k)
    if best and best[0] == "High Blood Pressure" and re.search(r"\blow\b|\bkam\b", m):
        best = next(d for d in DISEASES if d[0] == "Low Blood Pressure")
    return best

STOP = set("""with that from this have some often sometimes when your into also and the may can feel feeling felt are was
 very too much getting get gets since last days day week weeks having has had not dont please help tell about what how bad
 little bit like lot after before during while there they them then than but any all its one two more most other over only
 such these those were will would could should just really now today yesterday him her his she he we you our us symptoms
 symptom people none normal noticeable especially occur become""".split())
SYN = {"swelling":"swollen","swell":"swollen","swells":"swollen","tired":"fatigue","tiredness":"fatigue","exhausted":"fatigue",
       "hurts":"pain","hurt":"pain","hurting":"pain","ache":"pain","aching":"pain","weakness":"weak"}
def stems(text):
    out = set()
    for w in re.findall(r"[a-z]+", text.lower()):
        w = SYN.get(w, w)
        if w in STOP or len(w) < 3: continue
        if len(w) > 3 and w.endswith("s"): w = w[:-1]
        out.add(w[:4])
    return out
SYM = [stems(d[1]) for d in DISEASES]
DF = {}
for _s in SYM:
    for _w in _s: DF[_w] = DF.get(_w, 0) + 1
STRONG = {"ches","palp","brea","fain","dizz","swol","fati","murm","coll"}
COMMON = {"Angina","Heart Attack","Coronary Artery Disease","Arrhythmia","Heart Failure","High Blood Pressure","Atrial Fibrillation","Tachycardia","Low Blood Pressure"}

def by_symptoms(m):
    us, scored = stems(m), []
    for i, s in enumerate(SYM):
        common = us & s
        if common:
            sc = sum(math.log(len(DISEASES)/DF[w]) for w in common)
            if DISEASES[i][0] in COMMON: sc *= 2.2
            if {"ches","pain"} <= us and DISEASES[i][0] in ("Heart Attack","Angina"): sc *= 1.8
            scored.append((sc, len(common), i, common))
    if not scored: return []
    scored.sort(key=lambda t: (-t[0], t[2]))
    top = scored[0]
    if top[1] >= 2 or (top[3] & STRONG):
        return [DISEASES[t[2]] for t in scored[:3] if t[0] >= 0.6*top[0]]
    return []

KB = [
 (["diet","food","eat","foods","khana"],"For a healthy heart eat vegetables, fruit, oats, lentils, almonds and fish. Avoid fried food, ghee, excess salt, fast food and sugary drinks. Tell me your disease name for a specific diet."),
 (["exercise","walk","workout"],"With your doctor's approval, walk briskly for 30 minutes, 5 days a week. Stop if you feel chest pain or dizziness."),
 (["medicine","medicines","medication","tablet","drug","dawa","dawai"],"Common heart medicines doctors prescribe include aspirin, statins, beta-blockers, ACE inhibitors, diuretics and blood thinners. Never start or stop them on your own. Tell me your disease name or symptoms for specific details."),
 (["recover","recovery","how long","cure","treatment"],"Recovery depends on the condition: weeks for blood pressure or cholesterol, 6-12 weeks after a heart attack, and ongoing care for heart failure. Tell me the disease name for details."),
 (["smoking","smoke","cigarette"],"Smoking is the biggest enemy of the heart. One year after quitting, heart attack risk drops by about half."),
 (["list of diseases","all diseases","which diseases","what diseases","diseases list"],"I can answer about these heart diseases: " + ", ".join(NAMES) + "."),
 (["hello","hi","hey","salam","assalam"],"Hello! I am the CardioCare assistant. Tell me a heart disease name or your symptoms and I will share the causes, treatment, medicines, food and recovery."),
]


import csv

MEDQUAD_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "medquad_heart_qa.csv"
)

def search_medquad(message):
    try:
        with open(MEDQUAD_FILE, "r", encoding="utf-8-sig", newline="") as file:
            rows = csv.DictReader(file)
            query_words = set(_norm(message).split())
            best_answer = ""
            best_score = 0

            for row in rows:
                question = row.get("question", "")
                answer = row.get("answer", "")
                question_words = set(_norm(question).split())
                score = len(query_words & question_words)

                if score > best_score and score >= 2 and answer.strip():
                    best_score = score
                    best_answer = answer.strip()

            if best_answer:
                return best_answer + DISCLAIMER

    except (OSError, csv.Error):
        pass

    return None
def reply(msg):
    m = _norm(msg)
    if any(w in m for w in ["severe pain","fainting","fainted","emergency","can't breathe","cannot breathe","unconscious","not breathing","collapsed"]): return EMERGENCY
    d = find_named(m)
    if d:
        kinds = [k for k, ws in INTENTS if any(_has(m, w) for w in ws)]
        txt = describe(d, kinds)
        if d[0] in URGENT: txt = EMERGENCY + "\n\n" + txt
        return txt + DISCLAIMER
    hits = by_symptoms(m)
    if hits:
        txt = "Based on what you described, this may be related to: " + hits[0][0] + ".\n\n" + describe(hits[0])
        if len(hits) > 1: txt += "\n\nOther possibilities: " + ", ".join(h[0] for h in hits[1:])
        txt += "\n\nPlease see a cardiologist soon for a proper check-up (ECG / tests)."
        if hits[0][0] in URGENT: txt = EMERGENCY + "\n\n" + txt
        return txt + DISCLAIMER
    best, score = None, 0
    for keys, ans in KB:
        s = sum(1 for k in keys if _has(m, k))
        if s > score: best, score = ans, s

    if not best:
        medquad_answer = search_medquad(msg)
        if medquad_answer:
            return medquad_answer

        return "I can only answer heart-related questions. Tell me a heart disease name or your symptoms (for example: chest pain, breathlessness, dizziness) and I will share causes, treatment, medicines, food and recovery."

    return best + DISCLAIMER



# ====================== FLASK APP ======================
import sqlite3, os
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, g
from werkzeug.security import generate_password_hash, check_password_hash
from jinja2 import DictLoader

try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # normal: folder of app.py
except NameError:
    BASE_DIR = os.getcwd()                                  # Jupyter / Spyder: current folder
DB = os.path.join(BASE_DIR, "hospital.db")

app = Flask(__name__, static_folder=os.path.join(BASE_DIR, "static"))
app.secret_key = os.environ.get("SECRET_KEY", "change-this-secret")

# Anatomical-style glowing heart + ECG line (inline SVG, reused in splash and home hero)
HEART_SVG = """<svg class="heart-art" viewBox="0 0 420 500" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<defs>
 <radialGradient id="rv" cx="35%" cy="30%" r="90%"><stop offset="0" stop-color="#cf4046"/><stop offset=".5" stop-color="#8f1a24"/><stop offset="1" stop-color="#3a0a11"/></radialGradient>
 <radialGradient id="lv" cx="40%" cy="28%" r="90%"><stop offset="0" stop-color="#b5262f"/><stop offset=".5" stop-color="#701119"/><stop offset="1" stop-color="#2a060b"/></radialGradient>
 <radialGradient id="at" cx="40%" cy="35%" r="85%"><stop offset="0" stop-color="#c2353c"/><stop offset="1" stop-color="#52101a"/></radialGradient>
 <linearGradient id="ao" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#4b6a96"/><stop offset=".6" stop-color="#22324f"/><stop offset="1" stop-color="#0e1626"/></linearGradient>
 <linearGradient id="pt" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#c13740"/><stop offset="1" stop-color="#5a0f18"/></linearGradient>
 <linearGradient id="vn" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#6b4a8c"/><stop offset="1" stop-color="#2d1f4a"/></linearGradient>
 <filter id="blur14" filterUnits="userSpaceOnUse" x="-100" y="-100" width="640" height="720"><feGaussianBlur stdDeviation="16"/></filter>
 <filter id="blur4" filterUnits="userSpaceOnUse" x="-100" y="-100" width="640" height="720"><feGaussianBlur stdDeviation="4"/></filter>
 <filter id="blur2" filterUnits="userSpaceOnUse" x="-100" y="-100" width="640" height="720"><feGaussianBlur stdDeviation="1.6"/></filter>
 <filter id="tex" filterUnits="objectBoundingBox" x="0" y="0" width="100%" height="100%">
  <feTurbulence type="fractalNoise" baseFrequency="0.012 0.06" numOctaves="3" seed="11" result="t"/>
  <feColorMatrix in="t" type="matrix" values="0 0 0 0 0.12  0 0 0 0 0  0 0 0 0 0.02  0 0 0 1.6 -0.55" result="a"/>
  <feComposite in="a" in2="SourceAlpha" operator="in"/>
 </filter>
 <clipPath id="bodyclip"><path id="bodyp" d="M128 158 C100 180 80 230 88 292 C96 348 142 394 198 432 C220 448 238 460 254 480 C302 446 350 386 356 308 C362 234 334 172 288 150 C250 136 170 134 128 158 Z"/></clipPath>
</defs>

<!-- glow behind -->
<path d="M128 158 C100 180 80 230 88 292 C96 348 142 394 198 432 C220 448 238 460 254 480 C302 446 350 386 356 308 C362 234 334 172 288 150 C250 136 170 134 128 158 Z" fill="#e0242f" opacity=".45" filter="url(#blur14)"/>

<!-- great vessels (behind) -->
<path d="M142 180 C128 132 130 82 144 40" fill="none" stroke="url(#vn)" stroke-width="30" stroke-linecap="round"/>
<path d="M234 70 L231 18" fill="none" stroke="url(#ao)" stroke-width="18" stroke-linecap="round"/>
<path d="M264 58 L270 14" fill="none" stroke="url(#ao)" stroke-width="17" stroke-linecap="round"/>
<path d="M298 62 L310 22" fill="none" stroke="url(#ao)" stroke-width="16" stroke-linecap="round"/>
<path d="M190 176 C180 104 208 52 270 48 C332 44 358 94 354 154 C353 180 350 200 346 218" fill="none" stroke="url(#ao)" stroke-width="52" stroke-linecap="round"/>
<path d="M206 84 C224 56 262 48 300 52" fill="none" stroke="#a9c1e6" stroke-width="6" opacity=".3" stroke-linecap="round" filter="url(#blur2)"/>
<ellipse cx="144" cy="40" rx="14" ry="6.5" fill="#150c26"/>
<ellipse cx="231" cy="18" rx="9" ry="4" fill="#070d18"/>
<ellipse cx="270" cy="14" rx="8.5" ry="4" fill="#070d18"/>
<ellipse cx="310" cy="22" rx="8" ry="3.6" fill="#070d18"/>

<!-- pulmonary trunk -->
<path d="M214 176 C228 128 278 108 322 134" fill="none" stroke="url(#pt)" stroke-width="36" stroke-linecap="round"/>
<path d="M226 150 C244 122 282 112 314 128" fill="none" stroke="#ff9a9a" stroke-width="6" opacity=".25" stroke-linecap="round" filter="url(#blur2)"/>

<!-- atria -->
<path d="M128 160 C90 140 54 170 64 218 C70 248 102 256 126 236 C148 216 152 178 128 160 Z" fill="url(#at)"/>
<path d="M90 176 C78 196 80 224 96 240" fill="none" stroke="#2a060b" stroke-width="3" opacity=".5" stroke-linecap="round"/>
<path d="M104 168 C96 190 100 216 114 232" fill="none" stroke="#2a060b" stroke-width="2.4" opacity=".45" stroke-linecap="round"/>
<path d="M288 152 C330 140 366 172 364 218 C346 198 318 190 290 196 Z" fill="url(#at)"/>
<path d="M314 164 C334 172 346 188 350 204" fill="none" stroke="#2a060b" stroke-width="2.4" opacity=".45" stroke-linecap="round"/>

<!-- ventricles -->
<path d="M128 158 C100 180 80 230 88 292 C96 348 142 394 198 432 C220 448 238 460 254 480 C222 390 208 254 222 150 C190 142 158 142 128 158 Z" fill="url(#rv)"/>
<path d="M222 150 C208 254 222 390 254 480 C302 446 350 386 356 308 C362 234 334 172 288 150 C262 142 240 142 222 150 Z" fill="url(#lv)"/>
<!-- muscle texture -->
<g clip-path="url(#bodyclip)"><g transform="rotate(-38 210 300)"><rect x="-120" y="-120" width="700" height="760" fill="#000" filter="url(#tex)" opacity=".5"/></g></g>

<!-- fat along grooves -->
<path d="M222 152 C208 254 222 390 254 474" fill="none" stroke="#e9b873" stroke-width="12" opacity=".55" stroke-linecap="round" filter="url(#blur2)"/>
<path d="M128 164 C170 150 200 150 222 158" fill="none" stroke="#e9b873" stroke-width="9" opacity=".45" stroke-linecap="round" filter="url(#blur2)"/>
<path d="M222 158 C250 148 276 150 290 160" fill="none" stroke="#e9b873" stroke-width="8" opacity=".4" stroke-linecap="round" filter="url(#blur2)"/>

<!-- coronary arteries (red) and veins (blue-violet) -->
<g fill="none" stroke-linecap="round">
 <path d="M224 160 C212 254 226 386 254 470" stroke="#d1303a" stroke-width="4.2"/>
 <path d="M222 214 C252 222 296 242 318 296" stroke="#c32832" stroke-width="2.8"/>
 <path d="M216 292 C252 302 296 328 312 366" stroke="#c32832" stroke-width="2.4"/>
 <path d="M226 190 C262 176 300 178 330 204" stroke="#c32832" stroke-width="2.6"/>
 <path d="M150 188 C110 252 118 336 170 396" stroke="#d1303a" stroke-width="3.6"/>
 <path d="M128 252 C150 260 170 282 174 314" stroke="#c32832" stroke-width="2.2"/>
 <path d="M140 326 C166 336 186 358 192 392" stroke="#c32832" stroke-width="2"/>
 <path d="M238 168 C232 250 240 360 258 448" stroke="#5a3b86" stroke-width="3" opacity=".8"/>
 <path d="M260 180 C300 220 330 270 322 330" stroke="#5a3b86" stroke-width="2.4" opacity=".7"/>
</g>

<!-- lighting -->
<path d="M110 200 C84 250 90 320 126 372" fill="none" stroke="#fff" stroke-width="16" opacity=".14" stroke-linecap="round" filter="url(#blur4)"/>
<path d="M262 170 C312 190 340 240 336 300" fill="none" stroke="#ff9090" stroke-width="10" opacity=".16" stroke-linecap="round" filter="url(#blur4)"/>
</svg>"""

ECG_SVG = """<svg class="ecg" viewBox="0 0 1400 200" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<path class="ecg-line" d="M0 120 L330 120 L350 120 L380 40 L420 190 L450 120 L520 120 L560 100 L600 120 L860 120 L890 120 L920 20 L960 195 L990 120 L1060 120 L1100 96 L1140 120 L1400 120"
 fill="none" stroke="#ff4d5a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
</svg>"""


# 50 starting patients (inserted only once, the first time the database is created)
SEED_PATIENTS = [
 ("Muhammad Ali Raza",58,"Male","Heart Attack","Admitted after chest pain; stent placed. Follow-up in 2 weeks."),
 ("Fatima Noor",46,"Female","High Blood Pressure","BP 150/95 at last visit. Low-salt diet advised."),
 ("Ahmed Hassan",63,"Male","Coronary Artery Disease","Two arteries narrowed; on regular medication, bypass under discussion."),
 ("Ayesha Siddiqui",52,"Female","Angina","Chest tightness on climbing stairs. Stress test booked."),
 ("Bilal Chaudhry",67,"Male","Heart Failure","Swollen ankles and breathlessness. Fluid and salt control."),
 ("Zainab Malik",34,"Female","Arrhythmia","Occasional palpitations. 24-hour Holter monitor ordered."),
 ("Usman Tariq",55,"Male","High Cholesterol","LDL high on lipid profile. Diet change and repeat test in 8 weeks."),
 ("Hina Farooq Khan",41,"Female","Mitral Valve Prolapse","Mild leakage found on echo. Yearly check-up."),
 ("Imran Sheikh",61,"Male","Atrial Fibrillation","Irregular pulse. On blood thinner; INR checked monthly."),
 ("Sana Iqbal",29,"Female","Supraventricular Tachycardia","Sudden racing heartbeat episodes. Ablation consulted."),
 ("Kamran Butt",70,"Male","Aortic Stenosis","Breathless on effort. Valve replacement planned."),
 ("Nida Hussain",38,"Female","Myocarditis","Recovering after viral illness. Rest and no heavy exercise."),
 ("Tariq Mehmood",59,"Male","Unstable Angina","Chest pain at rest. Admitted for monitoring."),
 ("Rabia Akram",44,"Female","Pericarditis","Sharp chest pain on deep breathing. Anti-inflammatory course."),
 ("Faisal Rehman",65,"Male","Peripheral Artery Disease","Leg pain on walking. Supervised walking programme started."),
 ("Mehwish Anwar",50,"Female","Hypertensive Heart Disease","Long-standing high BP. Echo shows thick heart wall."),
 ("Shahid Afridi Khan",72,"Male","Cardiomyopathy","Reduced pumping function. Regular follow-up."),
 ("Samina Bibi",68,"Female","Heart Valve Disease","Valve narrowing; monitored every 6 months."),
 ("Adnan Qureshi",36,"Male","Long QT Syndrome","Fainting episode after exercise. ECG every 6 months."),
 ("Khadija Rauf",27,"Female","Atrial Septal Defect","Small hole between upper chambers; closure planned."),
 ("Zeeshan Ahmed",49,"Male","Coronary Artery Disease","Smoker. Quit advice given and statin started."),
 ("Maryam Tahir",57,"Female","Heart Failure","Tiredness and cough at night. Diuretic dose adjusted."),
 ("Hamza Yousaf",31,"Male","Tachycardia","Fast heartbeat with caffeine intake. Energy drinks stopped."),
 ("Iqra Naveed",24,"Female","Congenital Heart Disease","Born with a valve defect. Yearly echo."),
 ("Rashid Mahmood",74,"Male","Heart Block","Slow pulse and dizziness. Pacemaker fitted last month."),
 ("Shazia Parveen",53,"Female","High Blood Pressure","Headaches in the morning. Medicine started."),
 ("Naveed Akhtar",60,"Male","Heart Attack","Recovering after angioplasty. Cardiac rehab started."),
 ("Amna Javed",39,"Female","Bradycardia","Pulse near 45. Medicines under review."),
 ("Waqas Ali",47,"Male","High Cholesterol","Family history of heart disease. Statin tablet daily."),
 ("Saima Kausar",62,"Female","Angina","Chest discomfort on walking fast. Nitrate spray prescribed."),
 ("Junaid Iqbal",56,"Male","Deep Vein Thrombosis","Swollen left leg after long journey. Blood thinners."),
 ("Lubna Shah",66,"Female","Pulmonary Hypertension","Breathless on mild effort. Specialist follow-up."),
 ("Arslan Mirza",33,"Male","Hypertrophic Cardiomyopathy","Strong family history. Avoid extreme exertion."),
 ("Farah Deeba",48,"Female","Arrhythmia","Skipped beats and dizziness. Beta-blocker started."),
 ("Salman Rafiq",54,"Male","Atherosclerosis","Plaque in neck arteries. Lifestyle change and medicines."),
 ("Bushra Ahmad",43,"Female","Rheumatic Heart Disease","Childhood rheumatic fever. Penicillin injections monthly."),
 ("Danish Sultan",69,"Male","Aortic Aneurysm","Small aneurysm found. Scan every 6 months."),
 ("Asma Rizwan",37,"Female","Low Blood Pressure","Dizziness on standing. More water and slow rising."),
 ("Rizwan Haider",64,"Male","Dilated Cardiomyopathy","Enlarged heart. On heart failure medicines."),
 ("Nadia Pervaiz",51,"Female","Endocarditis","Fever and new murmur. Long antibiotic course in hospital."),
 ("Fahad Mustafa",45,"Male","Ventricular Tachycardia","Fast dangerous rhythm; defibrillator (ICD) discussed."),
 ("Sobia Anjum",35,"Female","Takotsubo Cardiomyopathy","Chest pain after severe stress. Heart recovering."),
 ("Asad Ullah",71,"Male","Cardiogenic Shock","Severe heart attack complication. Intensive care."),
 ("Mahnoor Zahid",30,"Female","Ventricular Septal Defect","Small hole between lower chambers. Monitoring only."),
 ("Yasir Arafat",58,"Male","Pulmonary Embolism","Sudden breathlessness. Admitted and started blood thinners."),
 ("Rukhsana Begum",75,"Female","Mitral Stenosis","Breathlessness and palpitations. Balloon procedure planned."),
 ("Hassan Raza Jafri",42,"Male","Heart Attack","Young patient with strong smoking history. Stent placed."),
 ("Tahira Naseem",60,"Female","Aortic Dissection","Tearing chest pain. Emergency surgery done; recovering."),
 ("Owais Qadir",53,"Male","Supraventricular Tachycardia","Episodes settle with breathing manoeuvre. Review in 3 months."),
 ("Sidra Batool",40,"Female","High Cholesterol","Routine screening found high cholesterol. Diet plan and repeat test in 3 months."),
]
assert len(SEED_PATIENTS) == 50

TEMPLATES = {
"base.html": """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CardioCare Hospital</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Fraunces:opsz,wght@9..144,600;9..144,800&display=swap" rel="stylesheet">
<style>
:root{--bg:#081a20;--bg2:#0c262e;--card:#0f2f39;--line:#1d4654;--nav:#0b3a47;--txt:#e8f1f4;--mut:#8fb0ba;--red:#c8242b;--red2:#a51b21}
*{box-sizing:border-box}
body{margin:0;font-family:'DM Sans',Segoe UI,Arial,sans-serif;background:var(--bg);color:var(--txt)}
h1,h2,h3{margin-top:0;font-family:'Fraunces',Georgia,serif}
a{color:#ff7b84}
nav{background:var(--nav);color:#fff;display:flex;align-items:center;gap:4px;padding:12px 64px;flex-wrap:wrap;position:sticky;top:0;z-index:20}
nav .brand{font-family:'Fraunces',Georgia,serif;font-weight:800;font-size:24px;margin-right:auto;color:#fff;text-decoration:none;padding:0}
nav a{color:#fff;text-decoration:none;padding:6px 10px;border-radius:6px;font-size:15px;font-weight:500}
nav a:hover{background:rgba(255,255,255,.15)}
.wrap{max-width:1100px;margin:28px auto;padding:0 16px}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:20px;box-shadow:0 6px 20px rgba(0,0,0,.25);margin-bottom:20px}
input,select,textarea{width:100%;padding:10px 12px;margin:6px 0 12px;border:1px solid var(--line);border-radius:10px;font:inherit;background:var(--bg2);color:var(--txt)}
input::placeholder,textarea::placeholder{color:#6b8d98}
input:focus,select:focus,textarea:focus{outline:2px solid var(--red);border-color:transparent}
label{color:var(--mut);font-size:14px}
button,.btn{background:var(--red);color:#fff;border:0;padding:12px 28px;border-radius:999px;cursor:pointer;font:inherit;font-weight:700;text-decoration:none;display:inline-block}
button:hover,.btn:hover{background:var(--red2)}
.btn-sm{padding:5px 14px;font-size:13px}
.btn-ghost{background:transparent;border:2px solid rgba(255,255,255,.8)}
.btn-ghost:hover{background:rgba(255,255,255,.15)}
table{width:100%;border-collapse:collapse}
th,td{text-align:left;padding:10px;border-bottom:1px solid var(--line);font-size:14px}
th{background:var(--bg2);color:#ffb3b8}
td{word-break:break-word}
.flash{background:#3b2f0b;border:1px solid #b8860b;color:#ffe6a3;padding:10px 14px;border-radius:10px;margin-bottom:14px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px}
.small{color:var(--mut);font-size:13px}
.row2{display:grid;grid-template-columns:1fr 1fr;gap:12px}

/* ---------- hero (same look as the reference) ---------- */
.hero{position:relative;overflow:hidden;min-height:540px;display:flex;align-items:center;padding:40px 64px;
background:linear-gradient(90deg,rgba(7,26,32,.96) 0%,rgba(7,26,32,.78) 45%,rgba(7,20,26,.35) 100%),url('/static/bg.jpg') center/cover,
radial-gradient(circle at 78% 45%,#3a0d12 0%,#0a1f26 60%)}
.hero .txt{position:relative;z-index:3;max-width:620px}
.hero h1{font-size:76px;line-height:1.05;font-weight:800;margin:0 0 22px}
.hero p{font-size:19px;line-height:1.7;color:#dfeaee;margin:0 0 30px}
.hero .heart-art{position:absolute;right:5%;top:50%;transform:translateY(-50%);height:96%;will-change:transform;z-index:1;animation:beat 1.4s ease-in-out infinite;transform-origin:center}
.hero .ecg{position:absolute;left:0;bottom:6%;width:100%;height:150px;z-index:2;opacity:.9}
.ecg-line{stroke-dasharray:2200;stroke-dashoffset:2200;animation:draw 5s linear infinite;filter:drop-shadow(0 0 6px #ff4d5a)}
@keyframes draw{to{stroke-dashoffset:0}}
@keyframes beat{0%,100%{transform:translateY(-50%) scale(1)}12%{transform:translateY(-50%) scale(1.035)}24%{transform:translateY(-50%) scale(1)}}

/* ---------- inner pages background ---------- */
body.inner{
 background:
  linear-gradient(180deg,rgba(8,26,32,.45) 0%,rgba(8,26,32,.30) 50%,rgba(8,26,32,.60) 100%),
  url('/static/bg.jpg') center/cover no-repeat fixed;
 background-color:#081a20;
 min-height:100vh}
body.inner .card{background:rgba(15,47,57,.82);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px)}
body.inner h2{text-shadow:0 2px 12px rgba(0,0,0,.5)}

/* ---------- delete button ---------- */
.btn-del{background:transparent;border:1.5px solid #ff6b73;color:#ff8a91;padding:6px 16px;border-radius:999px;
 font-size:13px;font-weight:700;white-space:nowrap;cursor:pointer}
.btn-del:hover{background:#c8242b;color:#fff;border-color:#c8242b}
th.act,td.act{width:100px;white-space:nowrap;text-align:right}
td.act form{margin:0;display:inline}
th.num,td.num{white-space:nowrap;word-break:normal;overflow-wrap:normal;width:1%;text-align:center}

@media(max-width:800px){
 nav{padding:12px 16px}
 .hero{padding:40px 20px;min-height:480px}
 .hero h1{font-size:46px}
 .hero .heart-art{opacity:.35;right:-20%}
 .row2{grid-template-columns:1fr}
}
</style></head><body class="{% if request.endpoint in ('dashboard','appointments','diseases','doctors','chat') %}inner{% endif %}">
<nav>
 <a class="brand" href="{{ url_for('home') }}">&#9829; CardioCare</a>
 {% if session.uid %}
 <a href="{{ url_for('dashboard') }}">Patients</a>
 <a href="{{ url_for('appointments') }}">Appointments</a>
 <a href="{{ url_for('diseases') }}">Diseases</a>
 <a href="{{ url_for('doctors') }}">Doctors</a>
 <a href="{{ url_for('chat') }}">Chatbot</a>
 <a href="{{ url_for('logout') }}">Log out</a>
 {% else %}
 <a href="{{ url_for('login') }}">Log in</a>
 <a href="{{ url_for('register') }}">Sign up</a>
 {% endif %}
</nav>
{% block hero %}{% endblock %}
<div class="wrap">
 {% with msgs = get_flashed_messages() %}{% for m in msgs %}<div class="flash">{{ m }}</div>{% endfor %}{% endwith %}
 {% block body %}{% endblock %}
</div></body></html>""",

"splash.html": """<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>CardioCare</title>
<meta http-equiv="refresh" content="3;url=/home">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;700&family=Fraunces:opsz,wght@9..144,800&display=swap" rel="stylesheet">
<style>body{margin:0;height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;
background:radial-gradient(circle at 50% 40%,#3a0d12 0%,#081a20 65%);color:#fff;font-family:'DM Sans',Segoe UI,Arial,sans-serif;text-align:center}
h1{font-family:'Fraunces',Georgia,serif;font-size:44px;margin:10px 0}
.heart-art{height:260px;animation:b 1.2s infinite}@keyframes b{50%{transform:scale(1.08)}}
a{color:#fff;margin-top:20px;padding:10px 28px;border-radius:999px;background:#c8242b;text-decoration:none;font-weight:700}</style></head>
<body>""" + HEART_SVG + """<h1>CardioCare Hospital</h1><p>Caring for your heart...</p><a href="/home">Enter</a></body></html>""",

"index.html": """{% extends "base.html" %}
{% block hero %}<div class="hero">
""" + HEART_SVG + ECG_SVG + """
<div class="txt">
<h1>Your heart is our care.</h1>
<p>Book appointments, manage patient records, learn about heart diseases and ask our heart chatbot anything, all in one place.</p>
<a class="btn" href="{{ url_for('login') }}">Log in</a>
<a class="btn btn-ghost" href="{{ url_for('register') }}">Sign up</a>
</div></div>{% endblock %}
{% block body %}
<div class="grid">
 <div class="card"><h3>&#128104;&#8205;&#9877;&#65039; Expert Doctors</h3><p>Cardiologists, surgeons and rhythm specialists.</p></div>
 <div class="card"><h3>&#128203; Patient Records</h3><p>Save and manage patient records securely.</p></div>
 <div class="card"><h3>&#128197; Appointments</h3><p>Book appointments with the right doctor.</p></div>
 <div class="card"><h3>&#129728; Heart Diseases</h3><p>Symptoms, causes, treatment, diet and recovery.</p></div>
 <div class="card"><h3>&#129302; Heart Chatbot</h3><p>Ask questions about heart health anytime.</p></div>
</div>{% endblock %}""",

"auth.html": """{% extends "base.html" %}
{% block body %}
<div class="card" style="max-width:420px;margin:30px auto">
{% if mode=='error' %}<h2>Something went wrong</h2><p>Please go back and try again. If it keeps happening, check the terminal window for the error message.</p><a class="btn" href="{{ url_for('home') }}">Go to Home</a>
{% else %}<h2>{{ 'Sign up' if mode=='register' else 'Log in' }}</h2>
<form method="post">
{% if mode=='register' %}<label>Name</label><input name="name" required>{% endif %}
<label>Email</label><input type="email" name="email" required>
<label>Password</label><input type="password" name="password" required minlength="4">
<button type="submit">{{ 'Sign up' if mode=='register' else 'Log in' }}</button>
</form>
<p class="small">
{% if mode=='register' %}Already have an account? <a href="{{ url_for('login') }}">Log in</a>
{% else %}New here? <a href="{{ url_for('register') }}">Sign up</a>{% endif %}</p>
{% endif %}
</div>{% endblock %}""",

"dashboard.html": """{% extends "base.html" %}
{% block body %}
<div class="grid">
 <div class="card"><h3>Total Patients</h3><h1>{{ patients|length }}</h1></div>
 <div class="card"><h3>Appointments</h3><h1>{{ n_app }}</h1></div>
</div>
<div class="card"><h2>Add Patient</h2>
<form method="post">
<div class="row2"><div><label>Name</label><input name="name" required></div>
<div><label>Age</label><input type="number" name="age" min="1" max="120" required></div></div>
<div class="row2"><div><label>Gender</label><select name="gender"><option>Male</option><option>Female</option><option>Other</option></select></div>
<div><label>Condition</label><input name="condition" required></div></div>
<label>Notes</label><textarea name="notes" rows="2"></textarea>
<button type="submit">Save Patient</button></form></div>
<div class="card"><h2>Patient Records <span class="small">({{ patients|length }} total)</span></h2>
<input id="ps" placeholder="Search patient by name, condition..." oninput="fp()">
<div style="overflow-x:auto"><table id="pt">
<tr><th class="num">#</th><th>Name</th><th class="num">Age</th><th>Gender</th><th>Condition</th><th>Notes</th><th class="act">Action</th></tr>
{% for p in patients %}<tr><td class="num">{{ loop.index }}</td><td>{{ p['name'] }}</td><td class="num">{{ p['age'] }}</td><td>{{ p['gender'] }}</td>
<td>{{ p['condition'] }}</td><td>{{ p['notes'] }}</td>
<td class="act"><form method="post" action="{{ url_for('delete_patient', pid=p['id']) }}" onsubmit="return confirm('Delete this patient?')">
<button class="btn-del" type="submit">Delete</button></form></td></tr>
{% else %}<tr><td colspan="7">No patients yet.</td></tr>{% endfor %}
</table></div></div>
</table></div></div>
</table></div></div>
<script>function fp(){var q=document.getElementById('ps').value.toLowerCase();
document.querySelectorAll('#pt tr').forEach(function(r,i){if(i===0)return;r.style.display=r.innerText.toLowerCase().indexOf(q)>-1?'':'none'})}</script>
{% endblock %}""",

"appointments.html": """{% extends "base.html" %}
{% block body %}
<div class="card"><h2>Book Appointment</h2>
{% if patients %}
<form method="post">
<label>Patient</label><select name="patient_id">{% for p in patients %}<option value="{{ p['id'] }}">{{ p['name'] }}</option>{% endfor %}</select>
<label>Doctor</label><select name="doctor">{% for d in doctors %}<option>{{ d[0] }}</option>{% endfor %}</select>
<div class="row2"><div><label>Date</label><input type="date" name="date" required></div>
<div><label>Time</label><input type="time" name="time" required></div></div>
<label>Reason</label><input name="reason" required>
<button type="submit">Book</button></form>
{% else %}<p>Please add a patient on the <a href="{{ url_for('dashboard') }}">Patients page</a> first.</p>{% endif %}</div>
<div class="card"><h2>All Appointments</h2><div style="overflow-x:auto"><table>
<tr><th>Patient</th><th>Doctor</th><th>Date</th><th>Time</th><th>Reason</th></tr>
{% for a in apps %}<tr><td>{{ a['pname'] }}</td><td>{{ a['doctor'] }}</td><td>{{ a['date'] }}</td><td>{{ a['time'] }}</td><td>{{ a['reason'] }}</td></tr>
{% else %}<tr><td colspan="5">No appointments yet.</td></tr>{% endfor %}
</table></div></div>{% endblock %}""",

"diseases.html": """{% extends "base.html" %}
{% block body %}
<h2>Heart Diseases</h2>
<input id="q" placeholder="Search disease..." oninput="f()">
<div class="grid" id="list">
{% for d in diseases %}
<div class="card item"><h3>{{ d[0] }}</h3>
<p><b>Symptoms:</b> {{ d[1] }}</p><p><b>Causes:</b> {{ d[2] }}</p>
<p><b>Treatment:</b> {{ d[3] }}</p><p><b>Diet:</b> {{ d[4] }}</p><p><b>Recovery:</b> {{ d[5] }}</p></div>
{% endfor %}</div>
<script>function f(){var q=document.getElementById('q').value.toLowerCase();
document.querySelectorAll('.item').forEach(function(e){e.style.display=e.innerText.toLowerCase().indexOf(q)>-1?'':'none'})}</script>
{% endblock %}""",

"doctors.html": """{% extends "base.html" %}
{% block body %}
<h2>Our Doctors</h2>
<div class="grid">
{% for d in doctors %}<div class="card"><h3>&#128104;&#8205;&#9877;&#65039; {{ d[0] }}</h3>
<p><b>{{ d[1] }}</b></p><p>Experience: {{ d[2] }}</p><p>Timing: {{ d[3] }}</p></div>{% endfor %}
</div>{% endblock %}""",

"chat.html": """{% extends "base.html" %}
{% block body %}
<div class="card"><h2>&#129302; Heart Health Chatbot</h2>
<div id="box" style="height:380px;overflow-y:auto;background:#0a232b;border:1px solid #1d4654;border-radius:10px;padding:12px;margin-bottom:10px"></div>
<div style="display:flex;gap:8px"><input id="m" placeholder="Ask about heart attack, BP, cholesterol, diet..." style="margin:0" onkeydown="if(event.key==='Enter')send()">
<button onclick="send()">Send</button></div></div>
<script>
function add(t,me){var d=document.createElement('div');d.textContent=t;
d.style.cssText='white-space:pre-wrap;margin:8px 0;padding:10px 14px;border-radius:14px;max-width:80%;'+
(me?'background:#c8242b;color:#fff;margin-left:auto':'background:#123c48;border:1px solid #1d4654;color:#e8f1f4');
var b=document.getElementById('box');b.appendChild(d);b.scrollTop=b.scrollHeight}
add('Hello! Ask me about heart diseases, symptoms, diet or recovery.',false);
function send(){var i=document.getElementById('m'),t=i.value.trim();if(!t)return;add(t,true);i.value='';
fetch('/api/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:t})})
.then(function(r){return r.json()}).then(function(j){add(j.reply,false)}).catch(function(){add('Error, try again.',false)})}
</script>{% endblock %}""",
}
app.jinja_env.loader = DictLoader(TEMPLATES)


def db():
    if "db" not in g:
        g.db = sqlite3.connect(DB); g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(_):
    d = g.pop("db", None)
    if d: d.close()

def init_db():
    c = sqlite3.connect(DB)
    c.executescript("""
    create table if not exists users(id integer primary key, name text, email text unique, password text);
    create table if not exists patients(id integer primary key, name text, age integer, gender text, condition text, notes text);
    create table if not exists appointments(id integer primary key, patient_id integer, doctor text, date text, time text, reason text);
    create table if not exists meta(k text primary key, v text);""")
    if c.execute("select 1 from meta where k='seeded'").fetchone() is None:
        c.executemany("insert into patients(name,age,gender,condition,notes) values(?,?,?,?,?)", SEED_PATIENTS)
        c.execute("insert into meta(k,v) values('seeded','1')")
    c.commit(); c.close()

def login_required(f):
    @wraps(f)
    def w(*a, **k):
        if "uid" not in session:
            flash("Please log in first."); return redirect(url_for("login"))
        return f(*a, **k)
    return w

@app.route("/")
def splash(): return render_template("splash.html")

@app.route("/home")
def home(): return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        f = request.form
        try:
            db().execute("insert into users(name,email,password) values(?,?,?)",
                (f["name"], f["email"].lower(), generate_password_hash(f["password"], method="pbkdf2:sha256")))
            db().commit(); flash("Account created. Please log in."); return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("This email is already registered.")
    return render_template("auth.html", mode="register")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = db().execute("select * from users where email=?", (request.form["email"].lower(),)).fetchone()
        if u and check_password_hash(u["password"], request.form["password"]):
            session["uid"], session["name"] = u["id"], u["name"]; return redirect(url_for("dashboard"))
        flash("Incorrect email or password.")
    return render_template("auth.html", mode="login")

@app.route("/logout")
def logout(): session.clear(); return redirect(url_for("home"))

@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    if request.method == "POST":
        f = request.form
        try: age = max(1, min(120, int(f.get("age", "1"))))
        except ValueError: age = 1
        db().execute("insert into patients(name,age,gender,condition,notes) values(?,?,?,?,?)",
            (f["name"].strip(), age, f.get("gender", "Other"), f["condition"].strip(), f.get("notes", "").strip())); db().commit()
        flash("Patient record saved."); return redirect(url_for("dashboard"))
    rows = db().execute("select * from patients order by id").fetchall()
    n_app = db().execute("select count(*) from appointments").fetchone()[0]
    return render_template("dashboard.html", patients=rows, n_app=n_app)

@app.route("/patients/<int:pid>/delete", methods=["POST"])
@login_required
def delete_patient(pid):
    db().execute("delete from patients where id=?", (pid,)); db().commit(); return redirect(url_for("dashboard"))

@app.route("/appointments", methods=["GET", "POST"])
@login_required
def appointments():
    if request.method == "POST":
        f = request.form
        db().execute("insert into appointments(patient_id,doctor,date,time,reason) values(?,?,?,?,?)",
            (int(f["patient_id"]), f["doctor"], f["date"], f["time"], f["reason"])); db().commit()
        flash("Appointment booked."); return redirect(url_for("appointments"))
    pts = db().execute("select id,name from patients").fetchall()
    apps = db().execute("select a.*, coalesce(p.name,'(deleted patient)') pname from appointments a left join patients p on p.id=a.patient_id order by date,time").fetchall()
    return render_template("appointments.html", patients=pts, apps=apps, doctors=DOCTORS)

@app.route("/diseases")
@login_required
def diseases(): return render_template("diseases.html", diseases=DISEASES)

@app.route("/doctors")
@login_required
def doctors(): return render_template("doctors.html", doctors=DOCTORS)

@app.route("/chat")
@login_required
def chat(): return render_template("chat.html")

@app.route("/api/chat", methods=["POST"])
@login_required
def api_chat(): return jsonify(reply=reply((request.get_json(silent=True) or {}).get("message", "")))

init_db()

@app.errorhandler(500)
def server_error(e):
    return render_template("auth.html", mode="error"), 500

if __name__ == "__main__":
    print("Open http://127.0.0.1:5050")
    app.run(debug=False, port=5050)
