# I need GridAggregates preformed in the DB not in-memory

## Question

**Víc** asked on 18 Apr 2023

I am trying to show some grid-aggregates in a grid column footer without any groups. But I'm seeing that the grid is geting ALL the records in the database to compute the Agregates. I am using the OnRead event and a DbSet with the ToDataSourceResult() extension method. This is unnacceptable as I have 50k rows in the DB! As you can imagine the aggregates take forever to compute in-memory, but in the DB it woul be a super quick. Also, I am building a generic grid for all my pages, so I need it to be easy to abstract, FYI Any alternatives or workarounds? Could we not build a ExpressionTree for the aggregates and use IQueriable? Thanks in advance! ...
<GridColumns>
<GridColumn Field="@nameof(PedidosDeClientes.Unidades)" Title="Unidades" Width="150px">
<FooterTemplate>
Sum: @context.Sum;
</FooterTemplate>
</GridColumn>
<GridColumn Field="@nameof(PedidosDeClientes.PesoBruto)" Title="PesoBruto" Width="150px">
<FooterTemplate>
Sum: @context.Sum;
</FooterTemplate>
</GridColumn>
</GridColumns>
<GridAggregates>
<GridAggregate Field=@nameof(PedidosDeClientes.Unidades) Aggregate="@GridAggregateType.Sum" />
<GridAggregate Field=@nameof(PedidosDeClientes.PesoBruto) Aggregate="@GridAggregateType.Sum" />
</GridAggregates>
... public async Task OnRead ( GridReadEventArgs args ) { var r=await dbContext.PedidosDeClientes.ToDataSourceResultAsync( args.Request );
args.Data=r.Data;
args.Total=r.Total;
args.AggregateResults=r.AggregateResults;
}

## Answer

**Hristian Stefanov** answered on 21 Apr 2023

Hi Victor, Thank you for bringing up your question, it has provided valuable insight into optimizing our mechanism for calculating aggregates. Currently, all aggregates are calculated based on groups in the Grid. As a result, I have opened a feature request about it on your behalf: Optimize Aggregates without grouping. This improvement will give the option to easily calculate aggregates without grouping. Having said this, I confirm that there is still an approach that will help you achieve the desired result and avoid the described issue. To do so, in the OnRead handler, simply remove the aggregates from the "args.Request," manually calculate the desired aggregates based on the data, and substitute that result instead of relying on the Grid to automatically calculate them from the database. I'm at your disposal if more guidance is needed or if there are any difficulties. Regards, Hristian Stefanov Progress Telerik

### Response

**Víctor** commented on 25 Apr 2023

Yes but this is very much a temporary fix ;) I would like the grid to be able to do it by itself!

### Response

**Hristian Stefanov** commented on 27 Apr 2023

Hi Víctor, I confirm that once the feature for optimization is implemented, the Grid will be able to offer a more automatic approach. Kind Regards, Hristian
