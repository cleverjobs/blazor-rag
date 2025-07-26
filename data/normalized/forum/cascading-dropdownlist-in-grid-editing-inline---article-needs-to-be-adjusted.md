# Cascading DropDownList in Grid Editing (Inline) - article needs to be adjusted

## Question

**Ale** asked on 18 Jun 2022

Cascading DropDownList in Grid Editing it will work when you need to select the value in parent drop down, but for example on edit, the value is already selected & the event will not be fired to get filtered data to child dropdown , my sugestion to combine the solution with data being preoladed for the editing item on Grid=> OnEdit event private async Task GridRowEdit ( GridCommandEventArgs args ) {
Console.WriteLine( "GridRowEdit" ); if (args.Item is ProductSubmissionModel model)
{ await ViewModel.LoadLabs(model.Jurisdiction?.Key);
}
}

### Response

**Aleksandr** commented on 18 Jun 2022

and super hack to prevend double firing of onchange (onblur) ( OnChange fires twice ) private int? _jurisdictionSelectedVal=0; //prevent onblur from parent drop down private async Task GridRowEdit ( GridCommandEventArgs args ) {
Console.WriteLine( "GridRowEdit" ); if (args.Item is ProductSubmissionModel model)
{
_jurisdictionSelectedVal=model.Jurisdiction?.Key; await ViewModel.LoadLabs(model.Jurisdiction?.Key);
}
} private async Task JurisdictionChanged ( object obj ) {
Console.WriteLine( "JurisdictionChanged" ); if (_jurisdictionSelectedVal !=( int?)obj)
{
_jurisdictionSelectedVal=( int?)obj; await ViewModel.LoadLabs(( int?)obj);
}
}
