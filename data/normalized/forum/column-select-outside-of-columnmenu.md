# Column Select outside of ColumnMenu

## Question

**Mar** asked on 21 Mar 2023

Hi, We have a problem at the moment with showing/hiding columns in a grid. With the Column Menu it is possible to show/hide columns. If a grid has ten columns then it is ten times the identical menu to select columns, which actually makes no sense. It would make more sense if there was a way to add a single dropdown menu in the GridToolBar that you can use to hide and show columns. Unfortunately, I have not found an option for this. You can, of course, assign a bool value to each column and build your own menu, but in an app with dozens of grids and dozens of columns, this is extremely tedious. We wanted to design our own DropDown element and generate the column selection automatically with a loop over all columns. This is also very cumbersome because the grid doesn't keep the columns as a public property at any point. We currently determine the columns via reflection. Again, it would be nice if there was an easier way.

### Response

**Kristian** commented on 24 Mar 2023

Hi, Martin Did you consider using the GridState to automatically get all of the columns in the Grid? You can access the Column Field and visualize the columns in your custom DropDown. You can also alter the Visibility so if a user checks/unchecks a column, the action can be performed, without the need to add a Visible parameter to all of the columns. Keep in mind, that the State provides you only the Field, but not the Title of the columns, If you need the Title, you still may need to get it using a Reflection. You can also populate a mappings {field -> columnTitle} for each of the columns and get it from there. Kind Regards, Kristian

### Response

**Leland** commented on 20 Mar 2024

Maybe check out this similar question.
