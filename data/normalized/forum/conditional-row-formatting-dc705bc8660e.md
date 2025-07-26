# Conditional Row Formatting

## Question

**Mic** asked on 10 May 2020

Marin: I need to format Grid content on a row by row basis and using the RowTemplate am able to get close to what I want but it's breaking the Select and Hover behavior. What is the best way to do this? @page "/" @page "/formatting" <style> .mygrid-formatting th.k-header { padding: 5px; } .mygrid-formatting .k-master-row td { padding: 2px 4px; border-bottom: 1px solid rgba(33, 37, 41, 0.15); line-height: 1.25rem; vertical-align: @_verticalAlignment; } .mygrid-formatting .k-grid-table .k-master-row { background-color: @_backGroundColor; } .mygrid-formatting .k-grid-table .k-master-row:hover { background-color: rgba(220, 238, 239, 0.50); } .mygrid-formatting .k-grid-table .k-master-row.k-alt { background-color: @_backGroundColor; } .mygrid-formatting .k-grid-table .k-master-row.k-alt:hover { background-color: rgba(220, 238, 239, 0.50); } </style> @if (showForm) { <TelerikGrid Data="@GridData" Class="mygrid-formatting" Height="600px" SelectionMode="GridSelectionMode.Single" Pageable="true" PageSize="30" RowHeight="30" Sortable="true"> <RowTemplate Context="sample"> <td style="@RowStyle(sample.Id)">@sample.Id</td> <td style="@RowStyle(sample.Id)">@sample.Name</td> <td style="@RowStyle(sample.Id)">@sample.LastName</td> <td style="@RowStyle(sample.Id)">@sample.HireDate.ToShortDateString()</td> </RowTemplate> <GridColumns> <GridColumn Field="@(nameof(SampleData.Id))" Title="ID" /> <GridColumn Field="@(nameof(SampleData.Name))" Title="Name" /> <GridColumn Field="@(nameof(SampleData.LastName))" Title="Last Name" /> <GridColumn Field="@(nameof(SampleData.HireDate))" Title="Hired" /> </GridColumns> </TelerikGrid> } @code { public List<SampleData> GridData { get; set; } bool showForm=false; string _verticalAlignment="Center"; string _backGroundColor="White"; protected override async Task OnInitializedAsync() { GridData=await GetData(); showForm=true; } private string RowStyle(int id) { string style=string.Empty; if (id <=15) style="color: red; background-color: white;"; else if (id <=30) style="color: DarkBlue; background-color: AliceBlue;"; else if (id <=45) style="color: green; background-color: Khaki;"; else style="color: Indigo; background-color: Lavender;"; return style; } private async Task<List <SampleData>> GetData() { return Enumerable.Range(1, 100).Select(x=> new SampleData { Id=x, Name=$"name {x}", LastName=$"Surname {x}", HireDate=DateTime.Now.Date.AddDays(-x) }).ToList(); } public class SampleData { public int Id { get; set; } public string Name { get; set; } public string LastName { get; set; } public DateTime HireDate { get; set; } } }

## Answer

**Michael** answered on 13 May 2020

Marin: Sorry to bug you, but could you offer some guidance on my above question? Mike

### Response

**Svetoslav Dimitrov** answered on 13 May 2020

Hello Michael, There is an open Feature Request on our Feedback Portal regarding the conditional formatting of a Grid Row. You can see it from here: [https://feedback.telerik.com/blazor/1456957-conditional-row-class-for-styling.](https://feedback.telerik.com/blazor/1456957-conditional-row-class-for-styling.) I have given a Vote on your behalf to raise its popularity. You can Follow it for email notifications on status updates. Also, in the public thread you can express your ideas on the implementation of this feature. In this thread there is a link to a Knowledge Base article that has a workaround solution. As attached file, you can see a demo project that has Single Item Selection and Hover, when working with RowTemplate (note: selection of items with CheckBox column is not available in the RowTemplate, more information here: [https://docs.telerik.com/blazor-ui/components/grid/templates#row-template](https://docs.telerik.com/blazor-ui/components/grid/templates#row-template) ). The main difference between our two projects is that i have commented out the CSS rules which seem to break the selection. Regards, Svetoslav Dimitrov

### Response

**Marc** commented on 26 Jul 2023

Hai Svetoslav, when using this row-template, I loose my command buttons... How to add these? <GridColumns> <GridColumn Field="@nameof(SubscriberSubscriptionModel.Name)" Title="Subscription" /> <GridColumn Field="@nameof(SubscriberSubscriptionModel.StartDate)" Title="Startdate" /> <GridColumn Field="@nameof(SubscriberSubscriptionModel.EndDate)" Title="Enddate" /> <GridColumn Field="@nameof(SubscriberSubscriptionModel.Paid)" Title="Paid" /> <GridColumn Field="@nameof(SubscriberSubscriptionModel.Active)" Title="Active" /> <GridCommandColumn Width="200px"> <GridCommandButton Command="MyOwnCommand" Class="btn btn-sm btn-primary vsi-btn" OnClick="@EditOnClickHandler" Icon="@FontIcon.Pencil" ThemeColor="@ThemeConstants.Button.ThemeColor.Info"> Edit </GridCommandButton> <GridCommandButton Command="MyOwnCommand" Class="btn btn-sm btn-danger vsi-btn" OnClick="@DeleteOnClickHandler" Icon="@FontIcon.Trash" ThemeColor="@ThemeConstants.Button.ThemeColor.Error"> Delete </GridCommandButton> </GridCommandColumn> </GridColumns>

### Response

**Nadezhda Tacheva** commented on 31 Jul 2023

Hi Marc, Indeed, when using a <RowTemplate>, you are overriding the rendering of the whole Grid row including the Command column. To handle the scenario, you may create custom buttons that will invoke your desired actions. You may add a dedicated <td> element inside the <RowTemplate> and declare the needed TelerikButton instances inside. These custom buttons cannot invoke the built-in commands. However, you may handle their OnClick events to programmatically trigger similar actions through the Grid state. For example: [https://docs.telerik.com/blazor-ui/components/grid/state#initiate-editing-or-inserting-of-an-item.](https://docs.telerik.com/blazor-ui/components/grid/state#initiate-editing-or-inserting-of-an-item.) I hope this helps. Please let us know if any other questions appear.
