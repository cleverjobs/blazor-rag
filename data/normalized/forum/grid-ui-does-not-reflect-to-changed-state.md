# Grid UI does not reflect to changed state

## Question

**Ale** asked on 28 Aug 2022

dojo: [https://blazorrepl.telerik.com/?_ga=2.175076642.1694966489.1661590183-1931469790.1620243254](https://blazorrepl.telerik.com/?_ga=2.175076642.1694966489.1661590183-1931469790.1620243254) as you can see on example above, the grid is filtered (during the onInitState event), but user look & feel still unchanged, i mean the filter button is not highlited, if you click on the filter button to expand, the filter item 1 is not selected

## Answer

**Dimo** answered on 31 Aug 2022

Hello Aleksandr, The linked REPL is empty. Normally, you need to click the Share button and copy the URL that appears. I tested the described scenario and it works. You can see an example in the Grid State article. If you are using a FilterMenu, then create a CompositeFilterDescriptor instead of a simple FilterDescriptor: @using Telerik.DataSource; void OnStateInitHandler ( GridStateEventArgs<SampleData> args ) { var fdc=new FilterDescriptorCollection();

fdc.Add( new FilterDescriptor() { Member="Id", Operator=FilterOperator.IsLessThan, Value=5, MemberType=typeof ( int ) });
fdc.Add( new FilterDescriptor() { Member="Id", Operator=FilterOperator.IsEqualTo, Value=null, MemberType=typeof ( int ) }); var state=new GridState<SampleData>
{
FilterDescriptors=new List<IFilterDescriptor>()
{ new CompositeFilterDescriptor ()
{
LogicalOperator=FilterCompositionLogicalOperator.And, FilterDescriptors=fdc
}
}
};

args.GridState=state;
} Regards, Dimo Progress Telerik

### Response

**Aleksandr** commented on 31 Aug 2022

excellent, thx for help, works as expected
