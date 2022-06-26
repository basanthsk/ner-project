echo [$(date)]: "START"
echo [$(date)]: "creating environment"
conda create --prefix ./env python=3.9 -y
echo [$(date)]: "activate environment"
source activate ./env
echo[$(date)]: "create folder and file structure"

for DIR in data_ingestion data_preparation data_validation model model_eval model_trainer
do 
    echo "Creating", src/$DIR
    mkdir -p "src"/$DIR
    echo "Creating __init__.py inside above folders"
    touch "src"/$DIR/"__init__.py" "src"/$DIR/$DIR".py" 
    echo "from src."$DIR"."$DIR" import *" > src/$DIR/"__init__.py" 
done    
echo [$(date)]: "install requirements"
pip install -r requirements.txt
echo [$(date)]: "install requirements"
pip install  torch 
echo [$(date)]: "END"

# to remove everything -
# rm -rf env/ .gitignore conda.yaml README.md .git/