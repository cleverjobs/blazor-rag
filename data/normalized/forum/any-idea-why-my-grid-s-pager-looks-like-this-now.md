# Any idea why my grid's pager looks like this now?

## Question

**Dav** asked on 10 Oct 2022

Here is the code for my grid: <TelerikGrid Data="@RunningCodes" AutoGenerateColumns="false" FilterMode="@GridFilterMode.FilterRow" Pageable="true" PageSize="20"> <GridColumns> <GridColumn Field="@nameof(RunningCode.CodeType)" /> <GridColumn Field="@nameof(RunningCode.Host)" /> <GridColumn Field="@nameof(RunningCode.Name)" /> <GridColumn Field="@nameof(RunningCode.Description)" /> <GridColumn Field="@nameof(RunningCode.LastRunResults)" /> <GridColumn Field="@nameof(RunningCode.NextRun)" /> <GridColumn Field="@nameof(RunningCode.IsBanned)" /> <GridColumn Field="@nameof(RunningCode.StartupType)" /> <GridColumn Field="@nameof(RunningCode.Status)" /> </GridColumns> </TelerikGrid> Any idea why my pager looks like this at the bottom of the grid?

### Response

**Thomas** commented on 11 Oct 2022

Hi David, had something like that after a new version got released. Simply updated my custom css theme. When running blazor app, simply pressed Ctrl+F5 to reload css and it seemed to work. Hope that helps. Best Regards, Thomas
