# GridCommandButton Text change

## Question

**Vis** asked on 29 Jan 2021

Hello Teams When I clicking the GridCommandButton the text should be change to remove and I have attached the Image with explanation. <TelerikGrid Data=@users Groupable="false" Sortable="true" FilterMode="GridFilterMode.FilterMenu" Resizable="true" Reorderable="true" PageSize=@GridConstants.PageSize Pageable=@GridConstants.Pageable Class="ecm-grid"> <GridColumns> <GridColumn Field="@nameof(ManageUsrAndGrp.User.Name)" Title="User Name" /> <GridColumn Field="@nameof(ManageUsrAndGrp.User.FullName)" Title="Full Name"></GridColumn> <GridCommandColumn Resizable="false"> <GridCommandButton Command="Edit" OnClick="@AddUser">Add</GridCommandButton> </GridCommandColumn> </GridColumns> </TelerikGrid> Thanks, Vishnu Vardhanan
