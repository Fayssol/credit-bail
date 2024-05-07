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
    in_template_dir_path = f"{dirname(abspath(__file__))}/{template_dir}"
    in_template_path = in_template_dir_path + template_file
    fichier_in = open(in_template_path,"r")

    #Fichier en sortie accueillant les données fournies
    out_template_dir_path = f"{dirname(abspath(__file__))}/out/{template_dir}"
    out_template_path = out_template_dir_path + "template_out.tex"
    fichier_out = open(out_template_path,"w")
    
    template = fichier_in.read()#Lecture du template
    monContext = context
    monContext["image_path"] = dirname(abspath(__file__))+"/out/images/"
    
    """APPLICATION DE L'ENVIRONNEMENT ÉDITÉ SUR LE TEMPLATE"""
    j2_tamplate = j2_env.from_string(template)
    
    #Écriture dans le fichier en sortie
    fichier_out.write(j2_tamplate.render(monContext))
    fichier_out.close()
    
    mon_pdf = build_pdf(open(out_template_path,"r"))
    out_file_path = out_template_dir_path +pdf_name
    mon_pdf.save_to(out_file_path)
    """FERMETURE DE CANAUX"""
    fichier_in.close()
    return out_file_path
    
    
if __name__ == "__main__":
    
    from test import contrat
    # from askia_admin.models import Contrat
 
    
    # contrats = Contrat.objects.all()
 
  



    # monContext ={"contrat":contrats}
    print(generate_pdf(contrat,"contrats/definition/"))
