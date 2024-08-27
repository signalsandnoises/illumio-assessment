This challenge was completed using Python 3 in a Jupyter notebook. Output files were generated and committed. For easy verification, you can run `demo.py` with any Python 3.X interpreter; it contains all the same code in the Jupyter notebook.

Alternatively, you can just click on assessment.ipynb.

----


Assumptions made:
* The only protocol codes we expect to see are the first 146. The code can easily be modified to accomodate all 255 possible values.
* The lookup table only contains up to 10,000 mappings of <16 characters, and can be encoded using 8-bit ASCII, so it can easily sit in memory in <2MB.
  

Tests performed:
* Just reading from the data given in CSV form and stripping whitespace!

Analysis:
* All mappings are performed using O(1) operations. All input files are parsed once-over. The full program runs in optimal O(n) time complexity, using O(1) additional space complexity.
