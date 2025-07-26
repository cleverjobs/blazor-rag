# TelerikGrid Filtering does not display proper value in drop-down

## Question

**Kis** asked on 12 Jan 2022

Hello there I am using Telerik Grid In Grid, I am using default FilterMode="GridFilterMode.FilterRow" for Filtering but it does not display the proper value in the drop-down for Filtering here is my code snippet <TelerikGrid Data="@UsersSource" Height="400px" Pageable="true" PageSize="PaginationHelpers.PageSize" FilterMode="GridFilterMode.FilterRow" Resizable="true" Reorderable="true" OnRowClick="@OnRowClickHandler" SelectionMode="@GridSelectionMode.Multiple" @bind-SelectedItems="@SelectedUsers"> <GridColumns> <GridCheckboxColumn /> <GridColumn Field="@(nameof(User.Name))" Title="@_translator[" NameLabel "]" /> <GridColumn Field="@(nameof(User.Username))" Title="@_translator[" UserNameLabel "]" /> <GridColumn Field="@(nameof(User.BirthDate))" Title="@_translator[" DateOfBirthLabel "]" DisplayFormat="{0: MM/dd/yyyy}" /> <GridColumn Field="@(nameof(User.Role))" Title="@_translator[" RoleLabel "]" /> </GridColumns> </TelerikGrid> the output is like this instead of

## Answer

**Marin Bratanov** answered on 15 Jan 2022

Hi, The "working" screenshot does not have the default filter operator names, which indicates localization is used in the project to change them. The "non-working" case likely faces a problem in the project-specific localization implementation. Regards, Marin Bratanov
