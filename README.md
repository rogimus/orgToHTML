# orgToHTML
A short python script to take .org files and convert them into simple html pages. 
I created this with converting my math notes/homeworks/blog posts in mind.

Currently supports theorems and proofs with headings using 

        #+BEGIN_theorem your heading goes here
        #+END_theorem
        
        #+BEGIN_proof heading
        #+END_proof

Here capitalization is important. Spaces are supported in your heading.

Also supports ordered lists:
```
1. list item
2. l2
3. blah
```
          
Becomes:
```
<ol>
  <li> list item </li>
  <li> l2 </li>
  <li> blah </li>
</ol>
```
