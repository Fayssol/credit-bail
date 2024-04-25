from posixpath import abspath
from jinja2 import Environment

from latex import build_pdf
from os.path import dirname, abspath


def generate_pdf(context, template_dir="",pdf_name="document.pdf", template_file="template.tex"):
    """INSTACIATION D'UN NOUVEL ENVIRONNEMENT AVEC DES OPTIONS DE BALISES PERSONNALISÉES"""
    j2_env = Environment(
        variable_start_string="\VAR{",
        variable_end_string="}",
        block_start_string="\BLOCK{",
        block_end_string="}",
        comment_start_string="\COMMENT{",
        comment_end_string="}",
    )
    """DECLARATION DE FICHIER"""
    #Fichier à lire contenant le template avec les balises
    fichier_in = open(dirname(abspath(__file__))+"/"+template_dir + template_file,"r")
    
    #Fichier en sortie accueillant les données fournies
    fichier_out = open(dirname(abspath(__file__))+"/out/"+template_dir+"template_out.tex","w")
    
    template = fichier_in.read()#Lecture du template
    monContext = context
    monContext["image_path"] = dirname(abspath(__file__))+"/out/images/"
    
    """APPLICATION DE L'ENVIRONNEMENT ÉDITÉ SUR LE TEMPLATE"""
    j2_tamplate = j2_env.from_string(template)
    
    #Écriture dans le fichier en sortie
    fichier_out.write(j2_tamplate.render(monContext))
    fichier_out.close()
    
    mon_pdf = build_pdf(open(dirname(abspath(__file__))+"/out/"+template_dir+"template_out.tex","r"))
    mon_pdf.save_to(dirname(abspath(__file__))+"/out/"+template_dir+pdf_name)
    """FERMETURE DE CANAUX"""
    fichier_in.close()
    
if __name__ == "__main__":
    
    contrats = [
        {
            'client': {'nom': 'Dupont  Fils'},
            'date_contrat': '01/05/2024',
            'montant_contrat': '10 000',
            'duree': '12',
            'status': 'Actif',
            'etat': 'En cours'
        },
        {
            'client': {'nom': 'Martin SARL KOba gdshhjhhh jhshjshdh'},
            'date_contrat': '15/06/2024',
            'montant_contrat': '8 500',
            'duree': '6',
            'status': 'Actif',
            'etat': 'En cours'
        },
        {
            'client': {'nom': 'Leroux SA'},
            'date_contrat': '10/07/2024',
            'montant_contrat': '25 000',
            'duree': '24',
            'status': 'En attente',
            'etat': 'En cours'
        },
        {
            'client': {'nom': 'Bernard  Cie'},
            'date_contrat': '20/08/2024',
            'montant_contrat': '15 000',
            'duree': '12',
            'status': 'Actif',
            'etat': 'En cours'
        },
        {
            'client': {'nom': 'Dubois Co'},
            'date_contrat': '05/09/2024',
            'montant_contrat': '12 000',
            'duree': '18',
            'status': 'Actif',
            'etat': 'En cours'
        },
        {
            'client': {'nom': 'Durand SAS'},
            'date_contrat': '10/10/2024',
            'montant_contrat': '9 000',
            'duree': '6',
            'status': 'En attente',
            'etat': 'En cours'
        },
        {
            'client': {'nom': 'Lefevre  Fils'},
            'date_contrat': '15/11/2024',
            'montant_contrat': '22 000',
            'duree': '24',
            'status': 'Actif',
            'etat': 'En cours'
        },
        {
            'client': {'nom': 'Moreau  Co'},
            'date_contrat': '20/12/2024',
            'montant_contrat': '13 000',
            'duree': '12',
            'status': 'Actif',
            'etat': 'En cours'
        },
        {
            'client': {'nom': 'Roussel SARL'},
            'date_contrat': '25/01/2025',
            'montant_contrat': '16 000',
            'duree': '24',
            'status': 'En attente',
            'etat': 'En cours'
        },
        {
            'client': {'nom': 'Petit  Fils'},
            'date_contrat': '01/02/2025',
            'montant_contrat': '10 500',
            'duree': '18',
            'status': 'Actif',
            'etat': 'En cours'
        }
    ]

    monContext ={"contrats":contrats}
    generate_pdf(monContext,"contrats/liste/")
