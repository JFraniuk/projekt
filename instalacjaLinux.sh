cd "$(dirname "$0")" 
py -m venv .venv 
source .venv/Scripts/activate 
pip install -r requirements.txt 
read -p "Press any key to continue..."