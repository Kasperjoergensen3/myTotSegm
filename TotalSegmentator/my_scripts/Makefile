clone_git:
	git clone https://github.com/Kasperjoergensen3/myTotalSegmentator.git


create_env:
	conda create -n BATinf python=3.10
	conda activate BATinf
	pip install -e TotalSegmentator

upload_model:
	python my_scripts/upload_model.py

inference:
	python my_scripts/inference.py