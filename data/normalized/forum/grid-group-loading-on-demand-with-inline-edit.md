# Grid Group Loading On Demand with inline edit

## Question

**Rob** asked on 21 May 2024

Hi, [https://docs.telerik.com/blazor-ui/components/grid/grouping/load-on-demand#virtual-scrolling-group-load-on-demand-and-server-side-data-operations](https://docs.telerik.com/blazor-ui/components/grid/grouping/load-on-demand#virtual-scrolling-group-load-on-demand-and-server-side-data-operations) I've followed this example to implement grouping with loading on demand, however I'm having issues with the in line edit. When selecting the edit button, the grid changes to show the update and cancel buttons however the value that was visible is no longer visible and instead the area becomes greyed out. <TelerikGrid TItem="@object" LoadGroupsOnDemand="true" Groupable="false" OnStateInit="@((GridStateEventArgs<object> args)=> OnStateInitHandler(args))" OnRead="@ReadItems" OnUpdate="@UpdateHandler" OnEdit="@EditHandler" ScrollMode="@GridScrollMode.Virtual" FilterMode="@GridFilterMode.FilterRow" EditMode="@GridEditMode.Inline" PageSize="20" RowHeight="60" Navigable="true" Sortable="true" Height="600px"> <GridColumns> <GridColumn Field=@nameof(SiteMappingDto.SiteName) Width="220px" Title="Site" Visible="false"> <GroupHeaderTemplate> <span>Site : @context.Value</span> </GroupHeaderTemplate> </GridColumn> <GridColumn Field="@nameof(SiteMappingDto.TagName)" Title="Tag" Editable="false" /> <GridColumn Field="@nameof(SiteMappingDto.TagDescription)" Title="Description" Editable="false" /> <GridColumn Field="@nameof(SiteMappingDto.MappingValue)" Title="Value" Editable="true" /> <GridCommandColumn> <GridCommandButton Command="Save" Icon="@SvgIcon.Save" ShowInEdit="true">Update</GridCommandButton> <GridCommandButton Command="Edit" Icon="@SvgIcon.Pencil">Edit</GridCommandButton> <GridCommandButton Command="Cancel" Icon="@SvgIcon.Cancel" ShowInEdit="true">Cancel</GridCommandButton> </GridCommandColumn> </GridColumns> </TelerikGrid>

## Answer

**Hristian Stefanov** answered on 24 May 2024

Hi Robert, I have copied the example from the linked documentation and integrated Inline editing. As a result, the editing seems to operate correctly, without the area being greyed out. I'm sharing the sample via this REPL link. Please run and test it to see the result. Let me know if you are facing any difficulties with the example. Regards, Hristian Stefanov Progress Telerik

### Response

**Robert** commented on 26 May 2024

Hi Hristian, This example does work for me and it has helped me fix the the error I was seeing. In summary I was receiving this error: System. NullReferenceException: Object reference not set to an instance of an object. at Telerik. Blazor. Components. Common. Filters. FilterList. TelerikFilterList. GetFilterOperators () at Telerik. Blazor. Components. Common. Filters. FilterList. TelerikFilterList. InitFilterOperators () at Telerik. Blazor. Components. Common. Filters. FilterList. TelerikFilterList. OnInitializedAsync () at Microsoft. AspNetCore. Components. ComponentBase. RunInitAndSetParametersAsync () And the solution for me was to explicitly set the field types for my columns. [https://docs.telerik.com/blazor-ui/knowledge-base/grid-filtering-null-reference](https://docs.telerik.com/blazor-ui/knowledge-base/grid-filtering-null-reference)

### Response

**Robert** commented on 26 May 2024

I have one further question. My method that GetsData for the onRead event returns a list of sites if the request is grouped and the tags for that site if the request is not grouped. What would the filter for the grid do in this scenario? private async Task<DataEnvelope<SiteMappingDto>> GetData(DataSourceRequest request) { DataEnvelope<SiteMappingDto> dataToReturn; if (request.Groups.Count> 0) { //get the site groups var sites=await SiteMappingDataService.GetSites(1); var datasourceResult=sites.ToDataSourceResult(request); dataToReturn=new DataEnvelope<SiteMappingDto> { GroupedData=datasourceResult.Data.Cast<AggregateFunctionsGroup>().ToList(), TotalItemCount=datasourceResult.Total }; } else { // get the tags only for site loaded var tags=await SiteMappingDataService.GetAllMappings(1); var datasourceResult=tags.ToDataSourceResult(request); dataToReturn=new DataEnvelope<SiteMappingDto> { CurrentPageData=datasourceResult.Data.Cast<SiteMappingDto>().ToList(), TotalItemCount=datasourceResult.Total }; } return await Task.FromResult(dataToReturn); }

### Response

**Hristian Stefanov** commented on 28 May 2024

Hi Robert, I'm glad I was able to assist with the initial error. Regarding your second question, could you please provide more details about the issue? I'm not entirely clear on the objective, and it seems to be more of a developer's decision on how to handle the incoming data. I look forward to your update. Kind Regards, Hristian

### Response

**Robert** commented on 28 May 2024

Hi Hristian, Yes I can do that. I'm trying to better understand how the filter will work. I'm grouping my data by site and if the site group is expanded then I retrieve data for that site. I assume because the rows aren't loaded unless the group is expanded that I can't filter on the row details. Is that correct? Is there a way I can work around that?

### Response

**Hristian Stefanov** commented on 31 May 2024

Hi Robert, In the Grid configuration from your initial message, it seems that the LoadGroupsOnDemand is set to true. This loads the data for each individual group on demand, instead of having it always present. Consequently, I can confirm that the rows aren't loaded unless you expand the group. The filtering applies to the existing/loaded data. For more information about loading group data, please refer to our documentation: Load On Demand Group Data. Kind Regards, Hristian
