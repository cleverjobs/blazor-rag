# Set indeterminate state by UI

## Question

**Pet** asked on 11 Feb 2021

Hi, in the demo [https://demos.telerik.com/blazor-ui/checkbox/overview](https://demos.telerik.com/blazor-ui/checkbox/overview) the indeterminate state is set by code. It is possible, that the user can toggle also the indeterminate state? Now a user can not go back to the indeterminate state (or null in the bool? column) if the value is set to true or false. Regards, Peter

## Answer

**Marin Bratanov** answered on 11 Feb 2021

Hi Peter, The Indeterminate state is not something the user can or should be able to set - the checkbox in general is a hard boolean editor - it has two states - on and off (selected and unselected, checked and unchecked), and this is what the user can choose. The Indeterminate state is a bonus we provide to application developers so they can show the user that the value is undefined right now, for any reason that is up to the application. If you want to set that value, you do it through the parameter, and if you need to tie it to a user action that's also OK. What I mean with this is that there is only one action in the checkbox - selecting it which toggles it between checked and unchecked. There simply isn't a second element in it to provide a different action - namely - marking it as Indeterminate. If you want to, you cold use the ValueChanged or OnChange event to set the Indeterminate state based on the application logic you have, but the checkbox can't do it for you because it would mean creating an ambiguous action - selecting could now go either way and is unclear. Here's an example of toggling that parameter when the user selects the checkbox that you can tweak to match your needs: <TelerikCheckBox Value="@IsSelected" ValueChanged="@( (bool v)=> ValueChangedHandler(v) )" Indeterminate="@IsIndeterminate"></TelerikCheckBox>
<br />
selected: @IsSelected
<br />
Indeterminate: @IsIndeterminate
@code{ bool IsSelected { get; set; } bool IsIndeterminate { get; set; } void ValueChangedHandler ( bool v ) {
IsSelected=v;
IsIndeterminate=!v;
}
} Regards, Marin Bratanov

### Response

**Peter** answered on 12 Feb 2021

Hi Marin, I want use it for incell-edit in a Grid for a bool? Column "Ok" of a database table, with default null. The user shoud set True or False. And to null back to correct the input. The states on the Grid are now : Indeterminate -> Checked -> UnChecked -> Checked -> is a edit-Click. I want change it to : Indeterminate -> Checked -> UnChecked -> Indeterminate-> Checked But the Update Handler report only True or False. Not Null for Indeterminate. The Code: Checkbox3State.razor <TelerikCheckBox TValue="bool?" Value="@Value" ValueChanged="@( (bool? v)=> ValueChangedHandler(v) )" Indeterminate="@(!Value.HasValue)"></TelerikCheckBox> @code{ bool? _value; bool? _lastvalue; [Parameter] public bool? Value { get { return _value; } set { _lastvalue=_value; _value=value; } } [Parameter] public EventCallback<bool?> OnChange { get; set; } [Parameter] public EventCallback<bool?> ValueChanged { get; set; } void ValueChangedHandler(bool? v) { Console.WriteLine($"_lastvalue: {_lastvalue} Value: {Value} v: {v}"); if (v.HasValue && !v.Value && _lastvalue.HasValue && _lastvalue.Value) { Value=null; } ValueChanged.InvokeAsync(Value); OnChange.InvokeAsync(Value); } } The gridcolum use it: <GridColumn Field=@nameof(ViewModel.Ok)> <Template> <Checkbox3State Value="@((context as ViewModel).Ok)" /> </Template> </GridColumn> Which event use the grid OnUpdate to get informed by the changed value? Regards, Peter

### Response

**Peter** answered on 12 Feb 2021

Hi Marin, the code was not working. Correct is: Checkbox3State.razor <TelerikCheckBox TValue="bool?" Value="@Value" ValueChanged="@( (bool? v)=> ValueChangedHandler(v) )" Indeterminate="@(!Value.HasValue)"></TelerikCheckBox> @code{ bool? _lastvalue; [Parameter] public bool? Value { get; set; } [Parameter] public EventCallback<bool?> ValueChanged { get; set; } void ValueChangedHandler(bool? v) { if (v.HasValue && v.Value && _lastvalue.HasValue && !_lastvalue.Value) v=null; _lastvalue=v; Value=v; ValueChanged.InvokeAsync(v); } } In a page it works, also set to null: <Checkbox3State @bind-Value="@test1" /> @(test1.HasValue?test1.Value.ToString():"null") <Checkbox3State @bind-Value="@test2" /> @(test2.HasValue?test2.Value.ToString():"null") @code { bool? test1; bool? test2; } But this work not with OnUpdate in a grid. In the Update-Handler the value has only True or False. Also if I use @bind-value. Regards, Peter

### Response

**Marin Bratanov** answered on 13 Feb 2021

Hello Peter, The checkbox is binary. Its value is either true, or false. This is what you get out of it when used as an editor. If you want a third state, you must handle the data operations yourself, e.g. ,by also using the IndeterminateChanged event to know when the user moves it out of this third state. As for the grid - a very likely reason for this behavior is that the mode the grid uses does not use a nullable boolean. Or, the Value that comes from the custom editor is never null. I made a sample for you that seems to work fine for me so you can also compare against it in order to move forward with your implementation. Regards, Marin Bratanov

### Response

**Peter** answered on 14 Feb 2021

Hi Marin, Yes, a component Checkbox3State.razor mus use IndeterminateChanged: <TelerikCheckBox Value="@CheckBoxValue" Indeterminate="@Indeterminate" ValueChanged="@( (bool v)=> ValueChangedHandler(v) )" IndeterminateChanged="((bool val)=> IndeterminateChangedHandler(val))" /> @using Microsoft.Extensions.Logging; @inject ILogger<Checkbox3State> logger; @code{ bool Indeterminate { get; set; } bool CheckBoxValue { get; set; } bool IndeterminateChangedWasCalled; bool ValueChangedWasCalled; [Parameter] public bool? Value { get { return Indeterminate ? null : CheckBoxValue; } set { //don't set Value from the handlers. Handler must use Indeterminate, CheckBoxValue Indeterminate=!value.HasValue; CheckBoxValue=value.HasValue ? value.Value : false; logger.LogDebug($"ValueSet {Name} Indeterminate: {Indeterminate} CheckBoxValue {CheckBoxValue}"); } } [Parameter] public EventCallback<bool?> ValueChanged { get; set; } [Parameter] public string Name { get; set; } private void ValueChangedHandler(bool v) { //states: Indeterminate, true, false, Indeterminate, ... if (!IndeterminateChangedWasCalled || ValueChangedWasCalled) { logger.LogDebug($"ValueChangedHandler START {Name} v: {v} Indeterminate: {Indeterminate} CheckBoxValue {CheckBoxValue}"); if (v==true) { //add state Indeterminate logger.LogDebug("ValueChangedHandler: Extra State Indeterminate"); Indeterminate=true; //extra Indeterminate state CheckBoxValue=false; // the next state after Click is True } else CheckBoxValue=v; ValueChanged.InvokeAsync(Value); logger.LogDebug($"ValueChangedHandler END {Name} v: {v} Indeterminate: {Indeterminate} CheckBoxValue {CheckBoxValue}"); } else { //do nothing, IndeterminateChangedHandler was called before logger.LogDebug($"ValueChangedHandler first call after IndeterminateChanged"); } ValueChangedWasCalled=true; } private void IndeterminateChangedHandler(bool value) { logger.LogDebug($"IndeterminateChangedHandler {Name} value {value} CheckBoxValue {CheckBoxValue}"); Indeterminate=value; CheckBoxValue=true; // After Indeterminate set true ValueChanged.InvokeAsync(Value); IndeterminateChangedWasCalled=true; } } This works now correct in a page: <Checkbox3State @bind-Value="@test1" Name="test1" /> @(test1.HasValue ? test1.Value.ToString() : "null") <Checkbox3State @bind-Value="@test2" Name="test2" /> @(test2.HasValue ? test2.Value.ToString() : "null") <Checkbox3State @bind-Value="@test3" Name="test3" /> @(test3.HasValue ? test3.Value.ToString() : "null") Regards, Peter

### Response

**Peter** answered on 14 Feb 2021

I want use InCell Edit in a grid. The default behavior is: Click in the Cell to start Edit Mode, then Edit, Update on Return or Leave cell. This ist not usefull for a Checkbox Cell. The user expect the update on the first click. I use the Edithandler to toggle between the states: null, true, false: public async Task EditHandler(GridCommandEventArgs args) { if (args.Field=="IsOnLeave" ) { SampleData item=(SampleData)args.Item; //states Indeterminate/null> True> False item.IsOnLeave=item.IsOnLeave.HasValue?(item.IsOnLeave.Value ? false: null ) : true; await UpdateHandler(args); args.IsCancelled=true; } } This works fine with the grid definition: TelerikGrid Data=@MyData EditMode="@GridEditMode.Incell" Pageable="true" Height="300px" OnUpdate="@UpdateHandler" OnEdit="@EditHandler"> <GridColumns> <GridColumn Field=@nameof(SampleData.ID) Editable="false" Title="ID" /> <GridColumn Field=@nameof(SampleData.Name) Title="Name" /> <GridColumn Field=@nameof(SampleData.IsOnLeave) Title="On Vacation"> <Template> @{ var value=(context as SampleData).IsOnLeave; var indeterminate=!value.HasValue; <TelerikCheckBox Value="@value" Indeterminate="@indeterminate" /> } </Template> </GridColumn> </GridColumns> </TelerikGrid> Regards, Peter

### Response

**Marin Bratanov** answered on 15 Feb 2021

Hi Peter, Indeed, handling those events is important, and so is setting correct values. As for the InCell edit mode - if you want the first click to affect the data you could use the Template, but it is then very important to handle those custom editing events on your own so that they get stored in the data source, the grid does not know this editing is happening and it will not fire the OnUpdate event. By the way, our next release (planned for the end of the month) will have improvements on the InCell editing - Tab and Shift+Tab will move the focus between edtable cells in the same row, Enter will move to the next row in the same column - and that will allow for more efficient, faster data input, so it may be something you would want to know. On a side note, if you would like to, you could post your example of tri-state checkbox editing with single click in this repo (just fork it, then do a PR) and we award such contributions with Telerik points. Regards, Marin Bratanov
