run:
	python3 corrector.py Sample

resetSample:
	rm -fr Sample
	mkdir Sample
	mkdir Sample/Sub\ Directory\ 1
	mkdir Sample/Sub_Directory_2
	touch Sample/file2.txt
	touch Sample/file\ 1.txt
	touch Sample/file_3.txt
	touch Sample/Sub\ Directory\ 1/sub\ file\ 1.txt
	touch Sample/Sub\ Directory\ 1/sub_file_2.txt
	touch Sample/Sub_Directory_2/file4.txt
	touch Sample/Sub_Directory_2/sub\ file_3.txt
	touch Sample/file\ \(4\).txt
