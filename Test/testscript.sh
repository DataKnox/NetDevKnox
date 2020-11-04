sudo ansible-playbook ./mainplay.yml --limit evetesters
pip3 --install --upgrade pip
pip3 install pytest
python3 -m pytest ./Test/testospf.py --disable-warnings