echo. ##################### TEST PATH #####################
cd .\src\tests
python -m pytest tst_001.py tst_002.py tst_003.py --junit-xml=../results/results.xml 
pause

