# Listview with different Item Templates

## Question

**Hen** asked on 09 Jul 2024

I tried to figure out how to use different Item Templates within a Listview but I failed. is it not possible ?

## Answer

**Dimo** answered on 11 Jul 2024

Hi Hendrik, The ListView component has one item <Template> for all its items. If you wish to render different content for different items, then use conditional statements inside the template. See a similar example in the Grid inline editing example. <GridCommandColumn> <GridCommandButton Command="Edit"> Edit </GridCommandButton> @if ((context as ProductDto).ProductId % 2==0)
{ <GridCommandButton Command="Delete" Icon="@SvgIcon.Trash"> Delete </GridCommandButton> } <GridCommandButton Command="Save"> Update </GridCommandButton> <GridCommandButton Command="Cancel"> Cancel </GridCommandButton> </GridCommandColumn> Regards, Dimo Progress Telerik
