# TelerikDropDownList funny width!

## Question

**Mar** asked on 23 Sep 2021

I am struggling with getting the dropdown part of Dropdownlist to match. The dropdown part is to small. If I remove bootstrap then it's to far to the right. Have also tried to put the DropDownList outside the grid. Same result. Setting the width doesn't help See the pictures. I have measured the computed values of the animation container and the values are correct. So something else is overwriting the css. I removed all stylesheets except _content/Telerik.UI.for.Blazor/css/kendo-theme-default/all.css Code @page "/DepartmentAccess" <h3> DepartmentAccess </h3> <TelerikGridLayout> <GridLayoutColumns> <GridLayoutColumn Width="300px"> </GridLayoutColumn> <GridLayoutColumn Width="200px"> </GridLayoutColumn> <GridLayoutColumn Width="300px"> </GridLayoutColumn> </GridLayoutColumns> <GridLayoutRows> <GridLayoutRow> </GridLayoutRow> <GridLayoutRow> </GridLayoutRow> <GridLayoutRow> </GridLayoutRow> </GridLayoutRows> <GridLayoutItems> <GridLayoutItem Column="1" Row="1"> Department </GridLayoutItem> <GridLayoutItem Column="1" Row="2"> <div> <TelerikDropDownList TValue="int" TItem="CboItem" Data="UserDepartments" TextField="Name" ValueField="Id" Filterable="true" FilterOperator="StringFilterOperator.Contains" DefaultText="Select Department" ValueChanged="@(UserDepartmentSelected)" PopupHeight="400px" /> </div> </GridLayoutItem> <GridLayoutItem Column="1" Row="3"> Listbox with selected funds for selected department </GridLayoutItem> <GridLayoutItem Column="2" RowSpan="3"> add / remove buttons </GridLayoutItem> <GridLayoutItem Column="3" Row="1"> Avaiable funds </GridLayoutItem> <GridLayoutItem Column="3" Row="2"> Listbox wit avaiable funds </GridLayoutItem> </GridLayoutItems> </TelerikGridLayout>

### Response

**Dimo** commented on 28 Sep 2021

Hello Martin, The dropdown position may shift a little to the left if the <body> margin style is not reset to zero. This phenomenon is visible on the last screenshot. The reason for the other problems is unclear at this point. I tested your code snippet and it works as expected on my side. Can you provide an attached runnable project or a live URL for me to inspect?

### Response

**Martin Herløv** commented on 28 Sep 2021

Thanks will try the body margin reset. first
