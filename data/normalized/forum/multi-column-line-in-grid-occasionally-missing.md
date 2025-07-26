# Multi-column line in Grid occasionally missing

## Question

**Bob** asked on 14 May 2021

Just updated to the latest release and gave the multi-column option on the grid a try. It worked well for most cases, but on an initial transition from a non-multi-column to a multi-column, part of a grid line is missing. Code is pretty standard stuff, but then, being new to Blazor (or any kind of web programming) I could easily be missing something obvious: <TelerikGrid Data="@lstOpsYields" Sortable="true" Pageable="true" PageSize="20" Width="100%"> <GridColumns> <GridColumn Title="Field" Field="DisplayName" /> <GridColumn> <HeaderTemplate><div style="text-align:center">Expected Yield</div></HeaderTemplate> <Columns> <GridColumn Title=@oAppData.SimpleYear1Heading() Field="ExpectedYieldY1"> <Template> <div style="text-align: right;"> @((context as CCropOperations).ExpectedYieldY1.ToString(cnYieldFormat))</div> </Template> </GridColumn> <GridColumn Title=@oAppData.SimpleYear2Heading() Field="ExpectedYieldY2"> <Template> <div style="text-align: right;">@((context as CCropOperations).ExpectedYieldY2.ToString(cnYieldFormat))</div> </Template> </GridColumn> <GridColumn Title=@oAppData.SimpleYear3Heading() Field="ExpectedYieldY3"> <Template> <div style="text-align: right;">@((context as CCropOperations).ExpectedYieldY3.ToString(cnYieldFormat))</div> </Template> </GridColumn> </Columns> </GridColumn> <GridColumn> <HeaderTemplate><div style="text-align:center">APH less TA</div></HeaderTemplate> <Columns> <GridColumn Title=@oAppData.SimpleYear1Heading() Field="AphTaLessAphY1"> <Template> <div style="text-align: right;"> @((context as CCropOperations).AphTaLessAphY1.ToString(cnYieldFormat)) </div> </Template> </GridColumn> <GridColumn Title=@oAppData.SimpleYear2Heading() Field="AphTaLessAphY2"> <Template> <div style="text-align: right;">@((context as CCropOperations).AphTaLessAphY2.ToString(cnYieldFormat))</div> </Template> </GridColumn> <GridColumn Title=@oAppData.SimpleYear3Heading() Field="AphTaLessAphY3"> <Template> <div style="text-align: right;">@((context as CCropOperations).AphTaLessAphY3.ToString(cnYieldFormat)) </div> </Template> </GridColumn> </Columns> </GridColumn> <GridCommandColumn Title="Edit" Width="5%"> <GridCommandButton OnClick="@((args)=> SelectYield(args.Item as CCropOperations))" Icon="edit" /> </GridCommandColumn> </GridColumns> </TelerikGrid>

## Answer

**Dimo** answered on 18 May 2021

Hi Bob, Thank you for reporting this behavior. I confirm this is a bug and I updated your Telerik points. Possible workarounds include: Move the "Field" column to another position. The problem is exhibited only when the non-grouped column is at first position. Wrap the non-grouped column in its own group, similar to the "Company" column here: [https://demos.telerik.com/blazor-ui/grid/multi-column-headers](https://demos.telerik.com/blazor-ui/grid/multi-column-headers) You can use an empty column title for the group or "leaf" column, but you will still get an extra horizontal border, indeed. I have logged a public item on your behalf that you can track: [https://feedback.telerik.com/blazor/1520106](https://feedback.telerik.com/blazor/1520106) Regards, Dimo Progress Telerik

### Response

**Shahram** commented on 11 Aug 2023

Any update on this bug? I'm facing the same issue with multi header column

### Response

**Dimo** commented on 14 Aug 2023

@Shahram - for the time being there is no specific time line for implementation, sorry about that. Please follow the item for official release information and status updates. I hope the workarounds above are feasible for your scenario. Edit - this fix was in our short-term backlog, so we managed to squeeze it for the coming release. Cheers!
