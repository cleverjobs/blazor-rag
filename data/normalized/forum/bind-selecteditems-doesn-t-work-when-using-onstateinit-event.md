# bind-SelectedItems doesn't work when using OnStateInit event

## Question

**BobBob** asked on 17 Jun 2021

I have a grid where I am setting the initially selected rows and it works fine until I also use the OnStateInit event to set the initial sorting. Once I do that the selections are not set. <TelerikGrid Data="archivePermissions" Height="100%" Width="100%" ScrollMode="GridScrollMode.Scrollable" Sortable="true" SortMode="SortMode.Single" SelectionMode="GridSelectionMode.Multiple" @bind-SelectedItems="selectedUsers" FilterMode="GridFilterMode.FilterRow" OnStateInit="@((GridStateEventArgs<GetArchivePermissionsModel> args)=> OnStateInitHandler(args))"> <GridColumns> <GridCheckboxColumn SelectAll="true" Width="30px" OnCellRender="@GridHelpers.CenterAlign" /> <GridColumn Field="@(nameof(GetArchivePermissionsModel.LastName))" Title="Last Name" /> <GridColumn Field="@(nameof(GetArchivePermissionsModel.FirstName))" Title="First Name" /> <GridColumn Field="@(nameof(GetArchivePermissionsModel.Role))" Title="Role"> <FilterCellTemplate> <TelerikComboBox Data="roles" Value="@filteredRole" FilterOperator="StringFilterOperator.Contains" Width="100%" ValueField="Name" TextField="Name" ValueChanged="@(async (string val)=>
{
filteredRole=val;

var filter=context.FilterDescriptor.FilterDescriptors[0] as FilterDescriptor;
filter.Value=filteredRole;

if (string.IsNullOrEmpty(filteredRole))
{
await context.ClearFilterAsync();
}
else
{
await context.FilterAsync();
}
})"> </TelerikComboBox> </FilterCellTemplate> </GridColumn> </GridColumns> </TelerikGrid> private void GetArchive()
{
var dbRoles=SecurityRepository.GetRoles();
roles=Mapper.Map<IEnumerable <ApplicationRole>, IEnumerable <RoleViewModel>>(dbRoles);

var dbArchive=DatabaseArchivingRepository.GetArchive(ArchiveId);
archive=Mapper.Map<Archive, ArchiveViewModel>(dbArchive);
origName=archive.DisplayName;

archivePermissions=DatabaseArchivingRepository.GetArchivePermissions(ArchiveId).ToList();

selectedUsers=archivePermissions.Where(a=> a.HasAccess).ToList();
}

private void OnStateInitHandler(GridStateEventArgs <GetArchivePermissionsModel> args)
{
var state=new GridState <GetArchivePermissionsModel> {
SortDescriptors=new List <SortDescriptor> ()
{
new SortDescriptor("LastName", ListSortDirection.Ascending)
}
};

args.GridState=state;
}

## Answer

**Marin Bratanov** answered on 19 Jun 2021

Hello Bob, Without seeing this in action I am guessing a little, but here is what I think happens: the view initializes, and the selectedUsers are initialized with the desired initial selection StateInit fires and the grid loads state that state does not contain the desired selected items, so they are cleared from the grid To solve this, I think that you simply need to populate the selected items you want to put in the grid through the StateInit event - the state has the SelectedItems field where you can put them. Note that their Equals comparison must pass correctly, and that defaults to reference (see more here ), so if those selected items are stored with the state you may need to override their Equals method. What I also see as missing from the provided code snippet is the two-way binding of the selected items - when the user selects a new row there isn't a handler for SelectedItemsChanged that will update the view-model accordingly (explicit one, or implicit through @bind-*). You can find examples of both here. Regards, Marin Bratanov
