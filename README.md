Higher/lower game for DotA2 hero winrates per bracket. 
Used my old code which i used for GUI game, i created a web app which does the same. 

 -Part of the code scraps https://www.dotabuff.com/ for data (which is only done once i run that function). Data from the link is saved to `.json` file.  

 -User chooses bracket when the page loads, which sends data to server. Python does the processing depending on the bracket ( randomizes two heroes and finds winner ). That data is returned as JsonResponse where Ajax reads from and JS updates HTML elements to show the game. Score is tracked and updated with JS

Packages used:  

-*BeautifulSoup4*  
-*requests*