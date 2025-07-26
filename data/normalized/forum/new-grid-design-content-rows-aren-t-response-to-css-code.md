# New grid design-content rows aren`t response to CSS code.

## Question

**Mic** asked on 18 Apr 2023

Hello, I got a new project going on, which includes unique design. I am using Telerik grid for Blazor for functionality but trying to change the contents look. I have managed to change the header row style like you can see above with the following code: .k-grid-header-wrap { border-radius: 15px; margin-block: 5px;
} but the inside rows don't response to the CSS lines (except the background): .k-master-row,.k-table-alt-row { margin-block: 15px; background: #fff!important; border-radius: 15px!important;
} So the question is - is it possible to add margin between the girds lines and furthermore add more style properties (specific to the grids content)? and if yes, could someone please provide an example for this? thanks ahead, Michael.

## Answer

**Dimo** answered on 21 Apr 2023

Hi Michael, Styling tables like that is tricky, but possible. Here is a runnable REPL example. The milestones are: Custom white row and cell backgrounds will become visible if you remove the white background of elements behind the cells. Space between rows can be added, but I don't see how to control it at cell level (e.g. the first and last cells on a row will have side "margin", which is not necessary) I recommend the following documentation article, which is a must for every developer who wants to customize the appearance of our components: How to override theme styles. Also, with complex customizations that may or may not be possible, you can experiment with a plain HTML table in order to verify if something is possible. When done, you can port the custom CSS to our Grid and find which theme styles to override. Regards, Dimo Progress Telerik
