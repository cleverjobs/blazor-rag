# Blazor Grid Group with incell edit. Error when tabbing from the last row in group to next group.

## Question

**Rob** asked on 18 Dec 2024

I'm receiving the following error when I tab from the last row in group to the next group. Unhandled exception rendering component: No parameterless constructor
defined for type 'Telerik.Blazor.Components.Grid.Grouping.GridGroup'. System.MissingMethodException:
No parameterless constructor defined for type
'Telerik.Blazor.Components.Grid.Grouping.GridGroup'. Here is my grid. <TelerikGrid @ref="@TheGrid" Data="Mappings" Groupable="true" OnStateInit="@((GridStateEventArgs<object> args)=> OnStateInitHandler(args))" OnRead="@ReadHandler" OnUpdate="@UpdateHandler" EditMode="@GridEditMode.Incell" Pageable="true" PageSize="15" RowHeight="32" Navigable="true" Sortable="true"> <GridToolBarTemplate> <GridSearchBox Width="200px"></GridSearchBox> <span class="k-toolbar-spacer"></span> <GridCommandButton Command="ExcelExport" Icon="@SvgIcon.FileExcel">Export to Excel</GridCommandButton> <GridCommandButton Command="CsvExport" Icon="@SvgIcon.FileCsv">Export to CSV</GridCommandButton> </GridToolBarTemplate> <GridColumns> <GridColumn Field="@nameof(SiteMappingDto.SiteName)" FieldType="@typeof(string)" Title="Site" Editable="false" /> <GridColumn Field="@nameof(SiteMappingDto.SiteReference)" FieldType="@typeof(string)" Title="Reference" Editable="false" /> <GridColumn Field="@nameof(SiteMappingDto.TagName)" FieldType="@typeof(string)" Title="Tag" Editable="false" /> <GridColumn Field="@nameof(SiteMappingDto.TagDescription)" FieldType="@typeof(string)" Title="Description" Editable="false" /> <GridColumn Field="@nameof(SiteMappingDto.MappingValue)" FieldType="@typeof(string)" Title="Value" Editable="true" /> </GridColumns> </TelerikGrid> And the dto used: public class SiteMappingDto { public SiteMappingDto() { } public int Id { get; set; } public string? SiteName { get; set; } public string? SiteReference { get; set; } public string? TagName { get; set; } public string? TagDescription { get; set; } public int TagOrder { get; set; } public string? MappingValue { get; set; } }

### Response

**Nadezhda Tacheva** commented on 23 Dec 2024

Hi Robert, So far, we haven't received a report for such an issue. I tried to replicate the scenario and test it on my end in this sample: [https://blazorrepl.telerik.com/QolwwdEr483wiV2o00.](https://blazorrepl.telerik.com/QolwwdEr483wiV2o00.) As a result, I do not get an error when tabbing from the last row in a group to the next group. To investigate further, we will need a runnable reproduction that produces the result you are getting. So, can you please modify the sample I sent, so the issue is reproducible there? Please also list the exact steps we need to perform on our end to hit it. Thank you in advance for your cooperation!

### Response

**Robert** commented on 23 Jan 2025

Hi Nadezhda, I believe i've replicated it here. If you select value 1 and tab to the second row it works. If you then tab again to the next group you should see the error. [https://blazorrepl.telerik.com/QzkbGRlF35XpI0Q446](https://blazorrepl.telerik.com/QzkbGRlF35XpI0Q446) Thanks Rob

### Response

**Nadezhda Tacheva** commented on 28 Jan 2025

Hi Robert, Thank you for sending the sample! I revised it and I found the following issues that cause the exception: The Grid uses both its Data parameter and the OnRead event to get the records. This is not a proper configuration - only one of these options must be used but not both. The Grid reference and the OnStateInit handler used object while the Grid works with SiteMappingDto type. The Grid reference and the OnStateInit handler must use typed objects. Here is the updated sample where you can property tab from the last row of a group to the other group: [https://blazorrepl.telerik.com/wJkvQMlO02J5w8wY05.](https://blazorrepl.telerik.com/wJkvQMlO02J5w8wY05.)

### Response

**Robert** commented on 28 Jan 2025

That's solved it. Thank you for the help and information regarding correct configuration.

### Response

**Nadezhda Tacheva** commented on 29 Jan 2025

Thank you for confirming the issue is solved on your end, too, Robert! Should you face any other issues, please do not hesitate to reach out.
