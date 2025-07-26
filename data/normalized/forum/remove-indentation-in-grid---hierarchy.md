# remove indentation in Grid - Hierarchy

## Question

**Han** asked on 08 Mar 2024

How can I change the indentation of the child items in hierarchical grids. I want the children to start at the same beginning as the parent element

## Answer

**Dimo** answered on 12 Mar 2024

Hi Hans, There are two ways to make the detail table align with the master table: Use a TreeList Hide the Grid hierarchy column, but this is basically a more complex way to achieve a TreeList-like look. You will need custom CSS to hide the hierarchy column, column templates to add custom expand/collapse buttons and custom C# to manage the Grid hierarchy. At this point I don't see a reason for all this manual work. If you simply need to align the columns and prefer to use a Grid instead of a TreeList, then check this KB article that may serve you well: Align Grid column headers when using hierarchy Regards, Dimo Progress Telerik
