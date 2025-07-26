# GridSearchBox - Know if Filter comes from Search Box

## Question

**Bry** asked on 06 Nov 2023

I have created a routine which will highlight the search string in a grid, much like F3 in your browser. It is working well, by intercepting the GridRead events and applying a <SPAN> around the searched text to highlight it. The problem I have is that I don't know if the search filter in the collection provided comes from the search box or another filter applied to the grid. Is there a way that I can determine the filter comes from the search box so I only apply the highlight if it is the search text? Thanks, Bryan

## Answer

**Georgi** answered on 09 Nov 2023

Hi, Bryan, Yes, it is possible to determine where the filter comes from. You can use either the OnStateChanged event or call the GetState() method of the Grid's reference. Both allow you to access the Grid State, which includes the Grid features controlled by the user. Then, access the search box filter through the state's SearchFilter property. Additionally, we have a knowledge base article on how to Highlight, Format or Bold Grid Search Results that I believe will be helpful. Let me know if additional questions arise. Best regards, Georgi Progress Telerik
