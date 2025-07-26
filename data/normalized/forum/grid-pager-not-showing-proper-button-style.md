# Grid pager not showing proper button style

## Question

**dca** asked on 10 Mar 2020

The pager for my Blazor UI Grid has been working just fine for over a month but now it is missing the button box around the 1 when I view the first page. The second page has a box around it like a typical button. When I click on the 2 button to display page 2, the 2 button no longer has a box around it but the 1 button does. So it seems to be a css issue with the currently selected page. <TelerikGrid Data="@GridData" TotalCount="@Total" Sortable="true" Pageable="true" PageSize="@PageSize" OnRead="@OnReadHandler"> <GridToolBar> <TelerikButton OnClick="@(()=> SelectAccount(null))" Icon="add">Add Account</TelerikButton> </GridToolBar> <GridColumns> <GridCommandColumn Width="200px" Resizable="false"> <GridCommandButton OnClick="@((args)=> SelectAccount(args.Item as AccountModel))" Icon="edit">Edit</GridCommandButton> <GridCommandButton OnClick="@((args)=> ShowDeleteConfirmationDialog(args.Item as AccountModel))" Icon="delete">Delete</GridCommandButton> </GridCommandColumn> <GridColumn Field="@(nameof(Account.AccountName))" Title="Account Name" /> <GridColumn Field="@(nameof(Account.AccountType))" Title="Account Type" /> <GridColumn Field="@(nameof(Account.OwnerName))" Title="Account Owner" /> <GridColumn Field="@(nameof(Account.Status))" Title="Status" /> </GridColumns> </TelerikGrid>

## Answer

**dcadler** answered on 10 Mar 2020

I attached a png file showing the issue.

### Response

**Svetoslav Dimitrov** answered on 11 Mar 2020

Hello David, We haven't had other such reports and our demos seem to work fine for me: [https://demos.telerik.com/blazor-ui/grid/paging.](https://demos.telerik.com/blazor-ui/grid/paging.) Do they look OK on your end? If yes, the most likely reason for this behavior is something specific on the project, and here are two things I can think of: Could you confirm that there are no CSS rules that might conflict with the rendering of the component? For example, some global selectors for span or li elements. You could try removing parts of the site stylesheets to see if some of them are causing this problem. For example, remove all site-specific styles (leave only the Telerik theme) and if the issue is gone, then it is caused by something in those site-specific stylesheets. In case you are using a custom Telerik Theme built with out Theme Builder, you can try re-generating it from our site by uploading the variables file (read more in the Import Custom Theme section)? Regards, Svetoslav Dimitrov

### Response

**dcadler** answered on 13 Mar 2020

The issue was resolved by upgrading from Telerik Blazor UI 2.5.1 to v2.8.0

### Response

**Svetoslav Dimitrov** answered on 16 Mar 2020

Hello David, I am glad to hear that the update to 2.8.0 solved the problem for you! Regards, Svetoslav Dimitrov
