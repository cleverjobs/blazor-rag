# TelerikGrid Filtering does not display proper value in drop-down

## Question

**Kis** asked on 12 Jan 2022

Hello there I am using Telerik Filtering, here is my code snippet <TelerikGrid Data="@UsersSource" Height="400px" Pageable="true" PageSize="PaginationHelpers.PageSize" FilterMode="GridFilterMode.FilterRow" Resizable="true" Reorderable="true" OnRowClick="@OnRowClickHandler" SelectionMode="@GridSelectionMode.Multiple" @bind-SelectedItems="@SelectedUsers"> <GridColumns> <GridCheckboxColumn /> <GridColumn Field="@(nameof(User.Name))" Title="@_translator[" NameLabel "]" /> <GridColumn Field="@(nameof(User.Username))" Title="@_translator[" UserNameLabel "]" /> <GridColumn Field="@(nameof(User.BirthDate))" Title="@_translator[" DateOfBirthLabel "]" DisplayFormat="{0: MM/dd/yyyy}" /> <GridColumn Field="@(nameof(User.Role))" Title="@_translator[" RoleLabel "]" /> </GridColumns> </TelerikGrid> but this does not show the proper value in Filetering drop-down, it's show like this instead of

## Answer

**Marin Bratanov** answered on 15 Jan 2022

Hello, This is a duplicate of [https://www.telerik.com/forums/telerikgrid-filtering-does-not-display-proper-value-in-drop-down](https://www.telerik.com/forums/telerikgrid-filtering-does-not-display-proper-value-in-drop-down) I recommend opening one thread for an issue you are facing, as this keeps all information in the same place. Regards, Marin Bratanov
