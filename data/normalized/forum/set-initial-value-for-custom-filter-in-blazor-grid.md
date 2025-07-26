# Set initial value for custom filter in Blazor Grid

## Question

**Ray** asked on 17 Jan 2025

Hi, in my existing project I use custom filter rows for the grid: <GridColumn Field="@column.DbName" FieldType="@type" Title="@column.HeaderName.Sanitize()" Width="@(column.DbName==nameof(Worker.BinderId) ? " 230px ": " 200px ")" Lockable="true"> <FilterCellTemplate> @if (type==typeof(string))
{ <CustomTextRowFilter Context="@context" /> }
else if (type==typeof(int) || type==typeof(int?) || type==typeof(decimal) || type==typeof(decimal?))
{ <CustomNumberRowFilter Context="@context" /> }
else if (type==typeof(DateTime) || type==typeof(DateTime?))
{ <CustomDateRowFilter Context="@context" /> }
else if (type==typeof(bool) || type==typeof(bool?))
{ <CustomBooleanRowFilter Context="@context" /> } </FilterCellTemplate> Furthermore I use the OnStateInit and OnStateChanged events so save and restore user settings for filters, groupings etc. private async Task OnStateInitHandler ( GridStateEventArgs<object> args ) {
ShowSpinner=true; var stateValue=await AppStateService.GetAppStateAsync(SelectedProjectGuid, CurrentUser.Id, AppStateType.GridWorkerState); if (! string.IsNullOrWhiteSpace(stateValue))
{ var state=AppStateHelper.GetItem<GridState<object>>(stateValue); if (state !=null )
{ await CleanGridState(state);
args.GridState=state;
}
}

ShowSpinner=false;
} With the filter's initialization I set the value and operator: protected override Task OnInitializedAsync () {
Field=((FilterDescriptor) Context.FilterDescriptor.FilterDescriptors[ 0 ])?.Member;
SetValue(((FilterDescriptor)Context.FilterDescriptor.FilterDescriptors[ 0 ]).Value);
SetOperator(); return base.OnInitializedAsync();
} Up to now every time the grid was loading the filter values have been set correctly and the grid has filtered the records. Now, after updating to a new Telerik version, the grid still filters correctly. But the filter component doesn't get the values and so doesn't show them. The reason is: Before update the process was... Init grid -> OnStateInit -> Init filter component Now it is... Init grid -> Init filter component -> OnStateInit So, the grid state is pulled too late. Has the init sort order been changed? How can I get this solved? Best regards, Rayko

### Response

**Nadezhda Tacheva** commented on 22 Jan 2025

Hi Rayko, We haven't received such a report so far and I do not see records for changing the process flow in the latest version. Can you please provide an isolated runnable sample that reproduces the exact behavior you are getting, so I can debug it? You may use the REPL tool, so you do not need to create a sample app. Once I have, I will be able to share some more insights on the behavior. Thank you in advance!

### Response

**Rayko** commented on 31 Jan 2025

Hi Nadezhda, I was able to separate the issue. Please find the attached sample. The filter is initialized before the grid state once the grouping is added. Without the grouping tags it works as expected. This behaviour was new since version 6.0.0. With 5.1.1 it doesn't appear. Best regards, Rayko

### Response

**Nadezhda Tacheva** commented on 04 Feb 2025

Hi Rayko, Thank you for preparing and providing the sample! I see the issue now and it does seem like a bug to me. I logged the following item on your behalf: OnStateInit is fired too late after child components in Grid are initialized. I also added your vote there and as a creator, you are automatically subscribed to get status updates. Last but not least, I updated your Telerik points as a small gesture of appreciation for your report.
