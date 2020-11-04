ansible-playbook ./mainplay.yml --limit evetesters
python3 -m pytest ./Test/testospf.py --disable-warnings -s --verbose