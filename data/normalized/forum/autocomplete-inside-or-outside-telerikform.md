# Autocomplete inside or outside TelerikForm

## Question

**Lor** asked on 16 Dec 2024

Hi all, I would like to implement an autocomplete with server side search but I'm having problems. If I don't insert it in a telerik form, it works (leaving aside small visual and selection bugs). This is the code: <TelerikAutoComplete Data="@VeicoloAutoCompleteData" Value="@VeicoloAutoCompleteValue" ValueChanged="@( (string newValue)=> OnVeicoloAutoCompleteValueChanged(newValue) )" OnChange="@OnChangeVeicoloAutoComplete" ValueField="@( nameof(DropDownModel.Text) )" MinLength="3" DebounceDelay="150">
<ItemTemplate>
<strong>@context.Text</strong>
</ItemTemplate>
</TelerikAutoComplete> What I want to achieve is that after inserting 3 characters, the call to the server starts and returns the values ​​that contain the inserted text private List<DropDownModel> VeicoloAutoCompleteData { get; set; }=new (); private string VeicoloAutoCompleteValue { get; set; } private async Task OnVeicoloAutoCompleteValueChanged ( string newValue ) { if (newValue.Length <3 )
{
VeicoloAutoCompleteValue=newValue; return;
} var request=new DataSourceRequest()
{
Skip=0,
Filters=new List<IFilterDescriptor>(),
Sorts=new List<SortDescriptor>(),
Aggregates=new List<AggregateDescriptor>(),
Groups=new List<GroupDescriptor>()
};
request.Page=1;
request.PageSize=10; var fs1=new FilterDescriptorCollection();
fs1.Add( new FilterDescriptor( "Targa", FilterOperator.Contains, newValue));
request.Filters=new List<IFilterDescriptor>()
{ new CompositeFilterDescriptor()
{
FilterDescriptors=fs1,
LogicalOperator=FilterCompositionLogicalOperator.Or,
}
}; var veicoli=await _veicoloService.GetAll(request);
VeicoloAutoCompleteValue=newValue;
VeicoloAutoCompleteData=veicoli.ToDropDownModel();
} private DropDownModel? userChoiceVeicolo; private async void OnChangeVeicoloAutoComplete ( object theUserChoice ) { if (userChoiceVeicolo is not null && userChoiceVeicolo.Text.Equals(( string )theUserChoice, StringComparison.InvariantCultureIgnoreCase))
{ return;
} var choice=VeicoloAutoCompleteData.FirstOrDefault(x=> x.Text.Equals(( string )theUserChoice, StringComparison.InvariantCultureIgnoreCase));
userChoiceVeicolo=choice; if (userChoiceVeicolo is not null )
_veicolo=await _veicoloService.GetById(userChoiceVeicolo.Value);
} Is this code correct? I read that there are bugs on the double activation of the onchange and I found this solution, which is a bit buggy anyway. If I insert this input in a form tag instead I can't make it work because it asks me for a valueExpression. But I don't know what to put. Basically I would like to save either the choice in a separate variable (as above but inside a form) Or save the choice in a subobject of the model I'm working on. How should I do it? Thanks for the help
