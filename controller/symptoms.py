from main import app,db
from bson import json_util
from flask import request
from durable.lang import *
import json 

diagnoses = []

def capture_diagnosis(c):
    global diagnoses
    diagnoses.append(c)



with ruleset('eye_disease'):
    # Define rule for Blepharitis
    @when_all(m.symptoms.allItems(
        item.matches("burning") |
        item.matches("foreign body sensation")|
        item.matches("red lid margins")|
        item.matches("lids often stuck together in a.m.")|
        item.matches("possible loss of lashes")))
    def blepharitis(p):
        p.assert_fact('diagnosis', {'disease': 'Blepharitis'})

    # Define rule for Stye
    @when_all(m.symptoms.allItems(
        item.matches("lid tenderness")|
        item.matches("pain")|
        item.matches("swelling")|
        item.matches("edema")))
    def stye(p):
        p.assert_fact('diagnosis', {'disease': 'Stye'})

    # Define rule for Anterior Cellulitis
    @when_all(m.symptoms.allItems(
        item.matches("swollen")|
        item.matches("red lids")))
    def anterior_cellulitis(p):
        p.assert_fact('diagnosis', {'disease': 'Anterior Cellulitis'})

    # Define rule for Posterior Cellulitis
    @when_all(m.symptoms.allItems(
        item.matches("swollen red lids")|
        item.matches("swollen red conjunctiva")|
        item.matches("impaired ocular motility")|
        item.matches("pain on eye movement")|
        item.matches("proptosis")))
    def posterior_cellulitis(p):
        p.assert_fact('diagnosis', {'disease': 'Posterior Cellulitis'})

    # Define rule for Nasolacrimal Drainage Obstruction
    @when_all(m.symptoms.allItems(
        item.matches("persistent tearing")|
        item.matches("persistent discharge")|
        item.matches("redness")|
        item.matches("dacryocystitis")))
    def ndo(p):
        p.assert_fact('diagnosis', {'disease': 'Nasolacrimal Drainage Obstruction'})

    # Define rule for Allergic Conjunctivitis
    @when_all(m.symptoms.allItems(
        item.matches("palpebral redness")|
        item.matches("diffuse redness")|
        item.matches("watery")|
        item.matches("white| stringy mucus")|
        item.matches("itching")|
        item.matches("burning eyes")|
        item.matches("lid edema")))
    def allergic_conjunctivitis(p):
        p.assert_fact('diagnosis', {'disease': 'Allergic Conjunctivitis'})

    # Define rule for Bacterial Conjunctivitis
    @when_all(m.symptoms.allItems(
        item.matches("palpebral redness")|
        item.matches("diffuse redness")|
        item.matches("purulent")))
    def bacterial_conjunctivitis(p):
        p.assert_fact('diagnosis', {'disease': 'Bacterial Conjunctivitis'})

    # Define rule for Viral Conjunctivitis
    @when_all(m.symptoms.allItems(
        item.matches("palpebral redness")|
        item.matches("diffuse redness")|
        item.matches("watery")|
        item.matches("serous")|
        item.matches("tender preauricular lymphadenopathy")))
    def viral_conjunctivitis(p):
        p.assert_fact('diagnosis'| {'disease': 'Viral Conjunctivitis'})

    # Define rule for Subconjunctival Hemorrhage
    @when_all(m.symptoms.allItems(
        item.matches("bright red eye")|
        item.matches("no pain")|
        item.matches("no malvision")))
    def subconjunctival_hemorrhage(p):
        p.assert_fact('diagnosis', {'disease': 'Subconjunctival Hemorrhage'})

    # Define rule for Keratitis Sicca
    @when_all(m.symptoms.allItems(
        item.matches("burning")|
        item.matches("gritty sensation")))
    def keratitis_sicca(p):
        p.assert_fact('diagnosis', {'disease': 'Keratitis Sicca'})

    # Define rule for Pingueculum
    @when_all(m.symptoms.allItems(
        item.matches("redness")|
        item.matches("inflamed")))
    def pingueculum(p):
        p.assert_fact('diagnosis', {'disease': 'Pingueculum'})

    # Define rule for Episcleritis
    @when_all(m.symptoms.allItems(
        item.matches("discomfort")|
        item.matches("localized redness")))
    def episcleritis(p):
        p.assert_fact('diagnosis', {'disease': 'Episcleritis'})

    # Define rule for Corneal Abrasion
    @when_all(m.symptoms.allItems(
        item.matches("redness")|
        item.matches("tearing")|
        item.matches("photophobia")|
        item.matches("pain")))
    def corneal_abrasion(p):
        p.assert_fact('diagnosis', {'disease': 'Corneal Abrasion'})

    # Define rule for Viral Keratitis
    @when_all(m.symptoms.allItems(
        item.matches("redness")|
        item.matches("watery discharge")|
        item.matches("foreign body sensation")))
    def viral_keratitis(p):
        p.assert_fact('diagnosis', {'disease': 'Viral Keratitis'})

    # Define rule for Bacterial Keratitis
    @when_all(m.symptoms.allItems(
        item.matches("redness")|
        item.matches("pain")|
        item.matches("purulent discharge")|
        item.matches("decreased vision")))
    def bacterial_keratitis(p):
        p.assert_fact('diagnosis', {'disease': 'Bacterial Keratitis'})

    # Define rule for Hyphema
    @when_all(m.symptoms.allItems(
        item.matches("decreased vision")|
        item.matches("pain")|
        item.matches("redness")|
        item.matches("blood in the anterior chamber")))
    def hyphema(p):
        p.assert_fact('diagnosis', {'disease': 'Hyphema'})

    # Define rule for Hypopyon
    @when_all(m.symptoms.allItems(
        item.matches("decreased vision")|
        item.matches("pain")|
        item.matches("redness")|
        item.matches("pus in the anterior chamber")))
    def hypopyon(p):
        p.assert_fact('diagnosis', {'disease': 'Hypopyon'})

    # Define rule for Angle-Closure Glaucoma
    @when_all(m.symptoms.allItems(
        item.matches("pain")|
        item.matches("headaches")|
        item.matches("nausea")|
        item.matches("vomit")|
        item.matches("perception of rainbow-colored halos around light")|
        item.matches("blur vision")))
    def angle_closure_glaucoma(p):
        p.assert_fact('diagnosis', {'disease': 'Angle-Closure Glaucoma'})

    # Define rule for Iris Iritis
    @when_all(m.symptoms.allItems(
        item.matches("pain")|
        item.matches("photophobia")|
        item.matches("decreased vision")|
        item.matches("circumcorneal injection")|
        item.matches("ciliary flush")|
        item.matches("constricted pupil")|
        item.matches("normal to low iop")))
    def iris_iritis(p):
        p.assert_fact('diagnosis', {'disease': 'Iris Iritis'})

    # Define rule for Cataract
    @when_all(m.symptoms.allItems(
        item.matches("loss of vision")|
        item.matches("no pain")|
        item.matches("degradation of vision")))
    def cataract(p):
        p.assert_fact('diagnosis', {'disease': 'Cataract'})

    # Define rule for Diabetic Retinopathy
    @when_all(m.symptoms.allItems(
        item.matches("visual loss")|
        item.matches("macular edema")|
        item.matches("exudate deposition")|
        item.matches("proliferative disease")|
        item.matches("vitreous hemorrhage")|
        item.matches("retinal detachment")))
    def diabetic_retinopathy(p):
        p.assert_fact('diagnosis', {'disease': 'Diabetic Retinopathy'})

    # Define rule for Hypertensive Retinopathy
    @when_all(m.symptoms.allItems(
        item.matches("left reflex is obscured totally")|
        item.matches("light reflex occupies most of the width of vessels")|
        item.matches("nicking")))
    def hypertensive_retinopathy(p):
        p.assert_fact('diagnosis', {'disease': 'Hypertensive Retinopathy'})

    # Define fallback rule
    @when_all(none(+m.disease))
    def no_diagnosis(p):
        p.assert_fact('diagnosis', {'disease': 'Not Found'})


# Diagnosis ruleset to print out the detected diagnosis
with ruleset('diagnosis'):
    @when_all(+m.disease)
    def print_diagnosis(p,complete):
        disease_name = p.m.disease
        complete(capture_diagnosis(disease_name))
        print(diagnoses)



@app.route('/diagnose', methods=['GET'])
async def index():    
    global diagnoses
    
    try:
        symptoms_request = request.args.get("symptoms").split(",")
        post("eye_disease",{"symptoms":symptoms_request})

        if diagnoses:
            return {
                "message":"Penyakit Ditemukan",
                "data":diagnoses
            }
        
        return {
            "message":"Penyakit tidak ditemukan",
        }
    except BaseException as e:
        return {
            "message":"Penyakit tidak ditemukan",
            "status":404,
            "data": e.__dict__
        }
    
