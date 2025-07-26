# Getting selected rows of nested grid

## Question

**JimJim** asked on 06 Jul 2023

Hello, I am evaluation the Telerik components for Blazor as are company may purchase a subscription. One component that will be used heavily will be the TelerikGrid. I am trying to simply find any methods that the grid provides, however I don't see any in any documentation I have seen. I would simply like to do something like myGrid.SelectedRows() and have it return the collection of the datatype. I am most interested on how to do this with a hierarchical grid. I have a <GridCheckBoxColum> in the <DetailTemplate>. I would like to have a button on top of the detail rows that when clicked, gets all of the rows selected. Eventually, I would like not only to do that, but be able to unselect any rows outside of that detail grid. Basically, I only want to the user to be able to select from one detail grid at a time. Sorry, I know this is a bit long, but I thought I'd find a simple method to call. If someone can please give me some guidance while I am playing around in the sandbox that would be great. Thank you for any help, Jim

### Response

**Deasun** commented on 29 Aug 2023

Not sure if this helps you or not: // loops thru the grids selected rows. int intIDXOn=0; while (intIDXOn <grdYourGridsName.SelectedItems.Count()) { List<YourListTypeForTheGrid> SelectITems=new List<YourListTypeForTheGrid>(); SelectITems=grdYourGridsName.SelectedItems.ToList(); CellValue=SelectITems[intIDXOn].YourFieldNAme.ToString(); // do what you want to do ! intIDXOn +=1; };

### Response

**Jim** commented on 29 Aug 2023

Thank you. I will try this out shortly.
