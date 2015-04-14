# BinTreeParser.py
take IDA PRO memory lines and print binary tree node.

memory example:

	.data:0040467C unk_40467C      db    8				  <--- num  
	.data:0040467D                 db    0
	.data:0040467E                 db    0
	.data:0040467F                 db    0
	.data:00404680                 dd offset unk_40464C   <--- pointer to right node
	.data:00404684                 dd offset unk_404664   <--- pointer to left node
	
output example:

C:\>BinTreeParser.py text.txt unk_404688

	24h (root node)
	        8 (right node)
	                6 (right node)
	                        1 (right node)
	                        7 (left node)
	                16h (left node)
	                        14h (right node)
	                        23h (left node)
	        32h (left node)
	                2Dh (right node)
	                        28h (right node)
	                        2Fh (left node)
	                6Bh (left node)
	                        63h (right node)
	                        0E9h (left node)
