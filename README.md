# opt-dependency-dist

If you want to replicate the experiments, execute the main files _drab.py_ and _mur.py_ 

By executing these you can respectively create the treebanks for all the books by Iris Murdoch and Margaret Drabble.

The execution requires some hours to be runned, this is why we keep two different files.

If you want to analyze the treebanks without re-executing calculations, you can find them in the folders _treebanks-drab.py_ and _treebaks-mur.py_

Also, we provide the script _process_treebank.py_ that, by using LAL library, analyzes the treebanks of the two authors and create, for each book, summary files with measures and statistics that will be stored in folder _outLAL_

The data (books) we used for carrying out our experiments on Margaret Drabble and Iris Murdoch are not open-access. Given that, we provide a _demo.py_ file, containing a demo of our experiments
over two freely available books: A Christmas Carol, by Charles Dickens and The Great Gatsby by F. Scott Fitzgerald. This file will produce 2 treebanks, one per book, that will be stored in folder _treebanks-demo_


If you want to check the correctness of the treebanks of the two writers, please execute the _check_errs.py_ script.

__IMPORTANT__: If you want to run either _process_treebank.py_ or _check_errs.py_, please pass as first argument of the script the authors you want to analyze:
"mur" for Iris Murdoch
"drab" for Margaret Drabble


Finally, we publish the Project Gutenberg license, because we removed that from the _txt_ files used for the demo, in order to avoid parser overloading.


## License for A Christmas Carol ##

The Project Gutenberg eBook of The Great Gatsby, by F. Scott Fitzgerald

This eBook is for the use of anyone anywhere in the United States and
most other parts of the world at no cost and with almost no restrictions
whatsoever. You may copy it, give it away or re-use it under the terms
of the Project Gutenberg License included with this eBook or online at
www.gutenberg.org. If you are not located in the United States, you
will have to check the laws of the country where you are located before
using this eBook.

Title: The Great Gatsby

Author: F. Scott Fitzgerald

Release Date: January 17, 2021 [eBook #64317]
[Most recently updated: January 24 2021]

Language: English

Character set encoding: UTF-8

Produced by: Alex Cabal for the Standard Ebooks project, based on a
             transcription produced for Project Gutenberg Australia.


## License for The Great Gatsby ##

The Project Gutenberg EBook of A Christmas Carol, by Charles Dickens

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project Gutenberg License included
with this eBook or online at www.gutenberg.org


Title: A Christmas Carol
       A Ghost Story of Christmas

Author: Charles Dickens

Release Date: August 11, 2004 [EBook #46]
Last Updated: March 4, 2018

Language: English

Character set encoding: UTF-8


Produced by Jose Menendez





=======
>>>>>>> e6399edeefa2af6ef1451bc1f44e3f04279aaf1f
