# Combobox with virtual scroll mode and async value changed handler

## Question

**Rob** asked on 21 Dec 2021

<TelerikComboBox TItem="ObjectSelection" TValue="int?" Data="_testObjs" Value="_objSel" ValueExpression="()=> _objSel" ValueChanged="ObjSelected" TextField="@nameof(ObjectSelection.Description)" ValueField="@nameof(ObjectSelection.Id)" ScrollMode="DropDownScrollMode.Virtual" PopupHeight="200px" ItemHeight="20" PageSize="20" ValueMapper="ValueMapper" OnRead="RetrieveObjs" TotalCount="100"> </TelerikComboBox> private IEnumerable <ObjectSelection> _testObjs;
private int? _objSel;

private Task ObjSelected(int? id)
{
return(Task.Run(()=> _objSel=id));
}

public Task RetrieveObjs(ReadEventArgs args)
{
_testObjs=new[]
{
new ObjectSelection {Id=1, Description="Obj 1"},
new ObjectSelection {Id=2, Description="Obj 2"},
new ObjectSelection {Id=3, Description="Obj 3"},
};
return(Task.Delay(300));
} In this scenario, when selecting an object in the combobox, the combobox remains emtpy. If the value changed handler looks like below, the combobox behaves as expected: private void ObjSelected(int? id) {
_objSel=id;
}

### Response

**Dimo** commented on 23 Dec 2021

The code seems to work - here is a runnable REPL page. I open the ComboBox, click on some item and it shows in the component as the selected value. Is there anything else that I should try? If needed, please send another REPL test page.

### Response

**Robert** commented on 23 Dec 2021

When trying your REPL page it's quite obvious that there's a problem. When repeatedly selecting items the combobox sometimes doesn't show the correct item. See this video; Video

### Response

**Stamo Gochev** commented on 28 Dec 2021

Hi Robert, The answer by my colleague Joana provides more details on the scenario. Can you try the suggestion and inform us about the result?

## Answer

**Joana** answered on 28 Dec 2021

Hi Robert, The behavior that you have described is expected. The two-way binding capabilities of the Value parameter assure that the change in the property is saved on the user's page. Thus, when rendering occur the change would not be wiped out. That being said, if you use ValueChanged event instead of two-way binding (@bind-Value="@ObjSelectedProperty") you need to update the value in the event. Like you noted, you need to set the _objSel to the corresponding value. Regards, Joana

### Response

**Robert** commented on 11 Jan 2022

I'm afraid I don't understand. At line 14 in the REPL page made by your colleague, _objSel is set to the selected object in the ValueChanged handler and it doesn't work every time an object is selected. Change to: private void ObjSelected(int? id) { _objSel=id; } and it works every time.

### Response

**Joana** commented on 13 Jan 2022

Hi Robert, I apologize for the confusion. When using two-way binding, asynchronous operations are not supported and might lead exactly to incorrect value selection. The two-way binding should happen fast without any delays and possibility of a race condition. Thus, the technical explanation is that in the components, the event is not awaited. You can see any Microsoft component as well for reference: [https://github.com/dotnet/aspnetcore/blob/main/src/Components/Web/src/Forms/InputBase.cs#L69](https://github.com/dotnet/aspnetcore/blob/main/src/Components/Web/src/Forms/InputBase.cs#L69)
