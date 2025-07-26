# Grid error "Must be reducible node" when i use aggregates

## Question

**Mar** asked on 25 Mar 2024

Hy, I created a generic class for telerik grids to manage different data models. In this class I use OnRead event for reading data : protected async Task OnReadHandlerAsync ( GridReadEventArgs args ) { try { var query=Service.QueryDto();
query=DefaultFilterCondition is not null? query.Where(DefaultFilterCondition) : query; var dataSourceResult=await query.ToDataSourceResultAsync(args.Request); if (args.Request.Aggregates.Any())
{
args.AggregateResults=dataSourceResult.AggregateResults;
}
args.Data=dataSourceResult.Data;
args.Total=dataSourceResult.Total;
} catch (Exception ex)
{
NotificationService.Error(ex.Message);
}
} As you can see I use the ToDataSourceResult extension on a variable of type IQueryable<TDto> for automatic sorting, filtering,paging,... But now I have a problem: I created a grid that contains aggregates, now for this TelerikGrid the application throws the "must be reducible node exception" when the "ToDataSourceResult" is executed on the IQueyable<TDto> variable. My TelerikGrid with aggregates: @inherits GridReadOnlyComponentBase<SimulationResultService,SimulationResultDto> <TelerikGrid Id="simulationresultgrid" @ref="GridRef" TItem="SimulationResultDto" OnStateInit="@OnStateInitHandler" FilterMode="@GridFilterMode.FilterRow" EditMode="@GridEditMode.None" SelectionMode="@GridSelectionMode.None" Sortable="@true" SortMode="@SortMode.Single" Groupable="@true" LoadGroupsOnDemand="@false" Reorderable="@false" OnRead="@OnReadHandlerAsync"> <GridAggregates> <GridAggregate Field="@nameof(SimulationResultDto.ActualSales)" Aggregate="@GridAggregateType.Sum" FieldType="typeof(decimal)" /> <GridAggregate Field="@nameof(SimulationResultDto.YearImpact)" Aggregate="@GridAggregateType.Sum" FieldType="typeof(decimal)" /> <GridAggregate Field="@nameof(SimulationResultDto.ChangesImpact)" Aggregate="@GridAggregateType.Sum" FieldType="typeof(decimal)" /> </GridAggregates> <NoDataTemplate> <strong> @(_simulationId> 0 ? "Nessun dato presente,eseguire prima una simulazione" : "Scegli la simulazione") </strong> </NoDataTemplate> <GridToolBarTemplate> <span class="k-toolbar-spacer" /> <SimulationSelect SelectedValue="_simulationId" SelectedValueChanged="SimulationIdChanged" Width="30%" /> </GridToolBarTemplate> <GridColumns> <GridColumn Field="@nameof(SimulationResultDto.ActualSales)" Title="Fat. attuale" Width="200px" DisplayFormat="{0:C}" Filterable="false" Groupable="false"> <GroupFooterTemplate> TOT: <TelerikNumericTextBox Width="80%" ReadOnly="@true" Arrows="@false" Decimals="2" Format="C" @bind-Value="@context.Sum" /> </GroupFooterTemplate> </GridColumn> </GridColumns> I know that a solution could be to run the ToList before running the ToDataSourceResult but I would like to know if there is another solution as I work with a large amount of data. Thanks

## Answer

**Svetoslav Dimitrov** answered on 28 Mar 2024

Hello Marko, This exception seems to be connected to a bug in Entity Framework Core 2.1.1 and is logged in their public GitHub repository. As you rightfully said, a fix is to use the ToList() method or downgrade to the 2.0 version of Entity Framework Core. If you are not using EF Core, I would like to request a runnable solution where the issue is reproducible so that we can investigate properly. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Marco** commented on 24 May 2024

Hy Dimitrov, Yes, I'm currently using the last version of the Entity Framework Core package (8.0.5). The downgrade of the Entity Framework Core is not a solution i can use, nor is the ToList() method because i work with tables that contain a large number of elements and I need to optimize calls to my Db. For example, in a grid with pagination as well, I would like to call the Db for only the elements of the current page, after filtering, grouping,sorting.. So, if i understand correctly, the only solution I have is to manually create all the operations in the OnRead event,using the ToList() method only after pagination (Skip() and Take())? Thanks in advance, Marco

### Response

**Svetoslav Dimitrov** commented on 28 May 2024

Hello Marco, It seems that Microsoft believes that this issue is by design. They marked the issue with the closed-by-design label. That being said, this is beyond our control and the workaround remains the same.
