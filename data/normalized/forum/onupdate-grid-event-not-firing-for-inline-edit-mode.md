# OnUpdate grid event not firing for inline edit mode

## Question

**Gou** asked on 12 May 2025

With validation enabled for the blazor grid, once all the validation errors are resolved, the OnUpdate event should get fired but it is not. I checked in incell edit mode and it does gets fired but my requirement is to use the inline edit mode. Below is the code that I am using: <TelerikGrid Data="@gridData" Pageable="true" Sortable="true" Width="2500px" PageSize="50" FilterMode="GridFilterMode.FilterMenu" EditMode="GridEditMode.Inline" OnEdit="@OnGridEdit" OnCancel="@OnGridCancel" OnUpdate="@OnGridUpdateHandler"> <GridSettings> <GridValidationSettings Enabled="true" /> </GridSettings> <GridColumns> <GridColumn Field="@nameof(Dto.CNumber)" Title="Customer No." Width="100px" Filterable="true" Sortable="false" /> <GridColumn Field="@nameof(Dto.DistributorLastName)" Title="Distributor Last Name" Width="200px" Filterable="true" /> <GridColumn Field="@nameof(Dto.DistributorNumber)" Title="Distributor No." Width="120px" Filterable="false" Sortable="false" /> <GridColumn Field="@nameof(Dto.DemoDate)" Title="Demo Date" Width="120px" Filterable="true" /> <GridColumn Field="@nameof(Dto.SerialNumber)" Title="RX Serial No." Width="120px" Filterable="false" Sortable="false" /> <GridCommandColumn Width="100px"> <GridCommandButton Command="Edit"> Edit </GridCommandButton> <GridCommandButton Command="Save" ShowInEdit="true"> Save </GridCommandButton> <GridCommandButton Command="Cancel" ShowInEdit="true"> Cancel </GridCommandButton> </GridCommandColumn> </GridColumns> </TelerikGrid>

## Answer

**Dimo** answered on 14 May 2025

Hello Gouri, In inline edit mode OnUpdate fires when the user hits the Save button. If the validation fails, the user must update the row values and hit Save again. You can see this behavior in action here: Grid Inline Editing example Regards, Dimo Progress Telerik

### Response

**Gouri** commented on 14 May 2025

Actually some validations where getting fired for columns which were invisible in grid and that is why OnUpdate event was not getting fired. Thank you for responding.
