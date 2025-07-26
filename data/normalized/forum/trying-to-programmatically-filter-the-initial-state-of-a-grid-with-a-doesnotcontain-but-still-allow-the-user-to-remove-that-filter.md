# Trying to programmatically filter the initial state of a grid with a DoesNotContain but still allow the user to remove that filter?

## Question

**Jst** asked on 17 Apr 2023

I have a grid that lists some records that have a column called Status. The initial state of the grid does not include any records with a status of "Finished" but I want to allow the user to remove that filter as they need to. When I use the code below it does not allow me to set a default filter in the grid which can be removed by the end user. private async Task OnStateInitHandler ( GridStateEventArgs<FlagVM> args ) { var cfd=new CompositeFilterDescriptor()
{
FilterDescriptors=new FilterDescriptorCollection()
{ new FilterDescriptor() { Member="Status/Name", Operator=FilterOperator.DoesNotContain, Value="Finished", MemberType=typeof ( string ) }
},
LogicalOperator=FilterCompositionLogicalOperator.And
}; var state=new GridState<FlagVM>
{
FilterDescriptors=new List<IFilterDescriptor>() {}
};

state.FilterDescriptors.Add(cfd);
args.GridState=state;
} I've also tried something like this with no luck. I basically want to set the UI filter to an initial state for the user. protected async Task SetGridDefaultFilter () {
GridState<FlagVM> desiredState=new ()
{
FilterDescriptors=new List<IFilterDescriptor>()
{ new CompositeFilterDescriptor(){
FilterDescriptors=new FilterDescriptorCollection()
{ new FilterDescriptor() { Member="Status/Name", Operator=FilterOperator.DoesNotContain, Value="Approved", MemberType=typeof ( string ) }
},
LogicalOperator=FilterCompositionLogicalOperator.And
}
}
}; await GridRef.SetState(desiredState);

## Answer

**Nadezhda Tacheva** answered on 20 Apr 2023

Hi John, This behavior may be caused by different reasons depending on the type of filtering you are using. I will list all options as at this stage, it is not clear what is the used filter type. Filter Menu with CheckBoxList By design of the CheckBoxList, it will include all distinct options available in the Grid data. However, in your current scenario, there are no records with a status of "Finished". Thus, this status will not be automatically included in the CheckBoxList. To handle the scenario, you may provide custom data to the CheckBoxList and include the "Finished" option. Here is a runnable sample: [https://blazorrepl.telerik.com/wxYywkOs016thg5W28.](https://blazorrepl.telerik.com/wxYywkOs016thg5W28.) Standard Filter Menu or Filter Row If the type of the status field is a string and you are using the standard Filter Menu or Filter Row, the value of the filter descriptor can be any string that you set including "Finished". Here is a runnable sample: [https://blazorrepl.telerik.com/cxESmEuV55diagM046.](https://blazorrepl.telerik.com/cxESmEuV55diagM046.) The code you have provided should generally work in this scenario. The only eventual flaw I can see is the Member value of the filter descriptor - it is currently "Status/Name". The Member should match the exact name of the field you are programmatically setting the filter for. Is that the name of the field? For example, if the field is called "Status", the Member of the filter descriptor should be "Status". Otherwise, the filter will not be applied. This specific generally applies to all types of filtering, including the above-listed CheckBoxList filtering. I hope you will find the above information and example useful. Please let us know if any other questions appear. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Jstemper** commented on 20 Apr 2023

The reason it says "Status/Name" is that it is filtering on a child object of the record being displayed in the grid. How would I go about filtering in that case? Status is a child record with a property called Name

### Response

**Svetoslav Dimitrov** commented on 25 Apr 2023

Hello John, You can use the "Status.Name" syntax. One import note is that you must not use the @nameof() expression. Regards, Svetoslav Dimitrov
