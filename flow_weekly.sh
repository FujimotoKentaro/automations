#! /bin/zsh
cd ~/automations/
source venv/bin/activate

cd weekly_report
python main.py

deactivate