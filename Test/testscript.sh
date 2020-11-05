ansible-playbook ./mainplay.yml --limit evetesters
sleep 40
python3 -m pytest ./Test/testospf.py --disable-warnings -s --verbose