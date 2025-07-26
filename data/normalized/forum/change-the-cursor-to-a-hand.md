# Change the cursor to a hand

## Question

**Dav** asked on 24 Nov 2020

I have made my rows clickable by handling the OnRowClick event, but I want the cursor to change to a hand when the cursor is over a row so that the user knows it is clickable. How can I accomplish this?

## Answer

**Lachezar Georgiev** answered on 25 Nov 2020

Hello David, Each table row includes the k-master-row class in its markup. The easiest way to change the cursor to a pointer (hand) is to add a CSS style to table rows. An example style rule would look like this: <style>.k-master-row { cursor: pointer;
} </style> Simply add the above snippet at the bottom of your.razor file and you should see the cursor changed to a pointer. You could also cascade this through a Class you set on the grid instance so that it affects only the grid you want and not all grids/treelists in the project. Please let me know if the above solution works for you. If it doesn't could you provide me with a runnable project or code snippet that I can use to investigate further? Regards, Lachezar Georgiev
