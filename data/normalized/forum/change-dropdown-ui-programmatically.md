# Change DropDown UI Programmatically

## Question

**Ser** asked on 03 Nov 2020

Is there a way to change the bound property value and have the dropdown reflect that change in the UI?

## Answer

**Marin Bratanov** answered on 03 Nov 2020

Hello Serge, Here's an example that explains the way this will operate and the framework behaviors that affect it: @page "/" @selectedValue

<br />
<button @onclick="@ChangeValue"> 1. change just value </button>

<button @onclick="@ChangeText"> 2. change just text - will not "work"</button>

<button @onclick="@ChangeEntireParameterRef"> 3. change entire parameter reference</button>

<br /><br />
<TelerikDropDownList Data="@myDdlData" TextField="MyTextField" ValueField="MyValueField" @bind-Value="@selectedValue">
</TelerikDropDownList>

@code { void ChangeValue ( ) { //works because it changes the value of a primitive type parameter selectedValue=4;
} void ChangeText ( ) { //does not work because you change the property of an item in a collection and that //will not propagate down the component tree - Blazor fires OnParametersSet for child //components only when the reference of a complex object changes //like the entire collection, not just a field in one of its items var index=myDdlData.FindIndex(itm=> itm.MyValueField==selectedValue); if (index> -1 )
{
myDdlData[index].MyTextField=DateTime.Now.ToString();
}
} void ChangeEntireParameterRef ( ) { //change the data item - on its own does nothing like in the example above var index=myDdlData.FindIndex(itm=> itm.MyValueField==selectedValue); if (index> -1 )
{
myDdlData[index].MyTextField=DateTime.Now.ToString();
} //create a new reference for the parameter - re-renders the component myDdlData=new List<MyDdlModel>(myDdlData);
} public class MyDdlModel { public int MyValueField { get; set; } public string MyTextField { get; set; }
}

List<MyDdlModel> myDdlData=Enumerable.Range( 1, 20 ).Select(x=> new MyDdlModel { MyTextField="item " + x, MyValueField=x }).ToList(); int selectedValue { get; set; }=3; //usually the current value should come from the view model data } Regards, Marin Bratanov
