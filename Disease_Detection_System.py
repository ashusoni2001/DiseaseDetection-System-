from tkinter import *
from tkinter import messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tts
from sklearn.ensemble import RandomForestClassifier as rfc

data=pd.read_csv("newdataset2.csv")
df1=pd.read_csv("Symptom-severity.csv")
# print(data)
y=data.iloc[:,1]
x=data.iloc[:,2:]
x_train,x_test,y_train,y_test=tts(x,y,test_size=0.3)
model=rfc(n_estimators=50)
model.fit(x_train,y_train)
score=model.score(x_test,y_test)
print("score of the model is: ",score)
diseases=['Fungal infection',
 'Allergy',
 'GERD',
 'Chronic cholestasis',
 'Drug Reaction',
 'Peptic ulcer diseae',
 'AIDS',
 'Diabetes ',
 'Gastroenteritis',
 'Bronchial Asthma',
 'Hypertension ',
 'Migraine',
 'Cervical spondylosis',
 'Paralysis (brain hemorrhage)',
 'Jaundice',
 'Malaria',
 'Chicken pox',
 'Dengue',
 'Typhoid',
 'hepatitis A',
 'Hepatitis B',
 'Hepatitis C',
 'Hepatitis D',
 'Hepatitis E',
 'Alcoholic hepatitis',
 'Tuberculosis',
 'Common Cold',
 'Pneumonia',
 'Dimorphic hemmorhoids(piles)',
 'Heart attack',
 'Varicose veins',
 'Hypothyroidism',
 'Hyperthyroidism',
 'Hypoglycemia',
 'Osteoarthristis',
 'Arthritis',
 '(vertigo) Paroymsal  Positional Vertigo',
 'Acne',
 'Urinary tract infection',
 'Psoriasis',
 'Impetigo']


def message():
    if (Symptom1.get() == "None" and  Symptom2.get() == "None" and Symptom3.get() == "None" and Symptom4.get() == "None" and Symptom5.get() == "None"):
        messagebox.showinfo("OPPS!!", "ENTER  SYMPTOMS PLEASE")
        print("OPPS!!", "ENTER  SYMPTOMS PLEASE")
    else :
        random_forest()
def random_forest():
    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
    a = np.array(df1["Symptom"])
    b = np.array(df1["weight"])
    for j in range(len(psymptoms)):
        for k in range(len(a)):
            if psymptoms[j]==a[k]:
                psymptoms[j]=b[k]
    nulls = [0,0,0,0,0,0,0,0,0,0,0,0]
    psy = [psymptoms + nulls]
    pred2 = model.predict(psy)
    print(pred2)
    t3.delete("1.0", END)
    t3.insert(END, pred2[0])

root=Tk()
root.title(" Diseases Detection System")

root.configure(bg="light blue")

Symptom1 = StringVar()
Symptom1.set("Please Enter the symptom 1.")
Symptom2 = StringVar()
Symptom2.set("Please Enter the symptom 2.")
Symptom3 = StringVar()
Symptom3.set("Please Enter the symptom 3.")
Symptom4 = StringVar()
Symptom4.set("Please Enter the symptom 4.")
Symptom5 = StringVar()
Symptom5.set("Please Enter the symptom 5.")
w2 = Label(root, justify=CENTER, text=" Diseases Detection System ")
w2.config(font=("Times new Roman", 60),bg='light blue')
w2.grid(row=1, column=0, columnspan=2, padx=100)

S1Lb = Label(root,  text="Symptom 1")
S1Lb.config(font=("Times new Roman", 30),bg='light blue')
S1Lb.grid(row=7, column=1, pady=10 , sticky=W)

S2Lb = Label(root,  text="Symptom 2")
S2Lb.config(font=("Times new Roman", 30),bg='light blue')
S2Lb.grid(row=10, column=1, pady=10 , sticky=W)

S3Lb = Label(root,  text="Symptom 3")
S3Lb.config(font=("Times new Roman", 30),bg='light blue')
S3Lb.grid(row=13, column=1, pady=10 , sticky=W)

S4Lb = Label(root,  text="Symptom 4")
S4Lb.config(font=("Times new Roman", 30),bg='light blue')
S4Lb.grid(row=16, column=1, pady=10 , sticky=W)

S5Lb = Label(root,  text="Symptom 5")
S5Lb.config(font=("Times new Roman", 30),bg='light blue')
S5Lb.grid(row=19, column=1, pady=10 , sticky=W)
def predict():
    random_forest()

lr = Button(root, text="Predict",height=2, width=20,bg="blue",activebackground="red", command=predict)
lr.config(font=("Helvetica", 15))
lr.grid(row=22, column=1,pady=10)


symptoms =['itching',
 'skin_rash',
 'continuous_sneezing',
 'shivering',
 'stomach_pain',
 'acidity',
 'vomiting',
 'indigestion',
 'muscle_wasting',
 'patches_in_throat',
 'fatigue',
 'weight_loss',
 'sunken_eyes',
 'cough',
 'headache',
 'chest_pain',
 'back_pain',
 'weakness_in_limbs',
 'chills',
 'joint_pain',
 'yellowish_skin',
 'constipation',
 'pain_during_bowel_movements',
 'breathlessness',
 'cramps',
 'weight_gain',
 'mood_swings',
 'neck_pain',
 'muscle_weakness',
 'stiff_neck',
 'pus_filled_pimples',
 'burning_micturition',
 'bladder_discomfort',
 'high_fever',
 'nodal_skin_eruptions',
 'ulcers_on_tongue',
 'loss_of_appetite',
 'restlessness',
 'dehydration',
 'dizziness',
 'weakness_of_one_body_side',
 'lethargy',
 'nausea',
 'abdominal_pain',
 'pain_in_anal_region',
 'sweating',
 'bruising',
 'cold_hands_and_feets',
 'anxiety',
 'knee_pain',
 'swelling_joints',
 'blackheads',
 'foul_smell_of urine',
 'skin_peeling',
 'blister',
 'dischromic_patches',
 'watering_from_eyes',
 'extra_marital_contacts',
 'diarrhoea',
 'loss_of_balance',
 'blurred_and_distorted_vision',
 'altered_sensorium',
 'dark_urine',
 'swelling_of_stomach',
 'bloody_stool',
 'obesity',
 'hip_joint_pain',
 'movement_stiffness',
 'spinning_movements',
 'scurring',
 'continuous_feel_of_urine',
 'silver_like_dusting',
 'red_sore_around_nose',
 'spotting_urination',
 'passage_of_gases',
 'irregular_sugar_level',
 'family_history',
 'lack_of_concentration',
 'excessive_hunger',
 'yellowing_of_eyes',
 'distention_of_abdomen',
 'irritation_in_anus',
 'swollen_legs',
 'painful_walking',
 'small_dents_in_nails',
 'yellow_crust_ooze',
 'internal_itching',
 'mucoid_sputum',
 'history_of_alcohol_consumption',
 'swollen_blood_vessels',
 'unsteadiness',
 'inflammatory_nails',
 'depression',
 'fluid_overload',
 'swelled_lymph_nodes',
 'malaise',
 'prominent_veins_on_calf',
 'puffy_face_and_eyes',
 'fast_heart_rate',
 'irritability',
 'muscle_pain',
 'mild_fever',
 'yellow_urine',
 'phlegm',
 'enlarged_thyroid',
 'increased_appetite',
 'visual_disturbances',
 'brittle_nails',
 'drying_and_tingling_lips',
 'polyuria',
 'pain_behind_the_eyes',
 'toxic_look_(typhos)',
 'throat_irritation',
 'swollen_extremeties',
 'slurred_speech',
 'red_spots_over_body',
 'belly_pain',
 'receiving_blood_transfusion',
 'acute_liver_failure',
 'redness_of_eyes',
 'rusty_sputum',
 'abnormal_menstruation',
 'receiving_unsterile_injections',
 'coma',
 'sinus_pressure',
 'palpitations',
 'stomach_bleeding',
 'runny_nose',
 'congestion',
 'blood_in_sputum',
 'loss_of_smell']
symptoms.sort()



S1En = OptionMenu(root, Symptom1,*symptoms)
S1En.grid(row=7, column=1)

S2En = OptionMenu(root, Symptom2,*symptoms)
S2En.grid(row=10, column=1)

S3En = OptionMenu(root, Symptom3,*symptoms)
S3En.grid(row=13, column=1)

S4En = OptionMenu(root, Symptom4,*symptoms)
S4En.grid(row=16, column=1)

S5En = OptionMenu(root, Symptom5,*symptoms)
S5En.grid(row=19, column=1)

t3 = Text(root, height=2, width=20)
t3.config(font=("Times new Roman", 20))
t3.grid(row=23, column=1 , padx=10)

root.mainloop()

