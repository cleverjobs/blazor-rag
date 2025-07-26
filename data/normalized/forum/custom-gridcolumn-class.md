# Custom gridcolumn class

## Question

**Eri** asked on 17 Nov 2022

I don't see a Class property on the GridColumn object. Is there a way to style a specific column? In my instance, i would like to remove the left border for just 1 of many columsn in the grid. Thanks in advance.

## Answer

**Eric** answered on 17 Nov 2022

I figured it out. You can set the class using the onCellRendor Event OnCellRender="@((e)=> e.Class="no-left-border" )"
