# Placeholder Not DefaultText for TelerikDropDownList

## Question

**RobRob** asked on 21 Sep 2023

The Blazor TelerikDropDownList doesn't appear to have a Placeholder property, but does have a DefaultText property. Using the latter as a 'Placeholder' initially works, but the problem is the text becomes another option in the list if it's not already in the list. For example, if I have a list of colors (Red, Green, Blue) and add a DefaultText value of 'Please select a color' the list actually becomes Red, Green, Blue AND Please select a color and the latter has to be accounted for if the user selects it. Anyone know how to extend the TelerikDropDownList component to include a Placeholder property that does not because part of the list? Thanks, Rob

## Answer

**Svetoslav Dimitrov** answered on 26 Sep 2023

Hello, The DropDownList component is equivalent to the <select> element but is prettier. Thus, an item that acts as default selection (i.e., nothing is selected) is available in the list of options so the user can cancel their selection. If you want to avoid that, you can consider changing the DefaultText parameter to null when the Value has been selected. Selected value: @selectedValue
<br />

<TelerikDropDownList Data="@myDdlData" TextField="MyTextField" ValueField="MyValueField" @bind-Value="selectedValue" DefaultText="@( selectedValue==0 ? " Please Select " : null )">
</TelerikDropDownList>

@code { public class MyDdlModel { public int MyValueField { get; set; } public string MyTextField { get; set; }
}

IEnumerable<MyDdlModel> myDdlData=Enumerable.Range( 1, 20 ).Select(x=> new MyDdlModel { MyTextField="item " + x, MyValueField=x }); int selectedValue { get; set; }
} Regards, Svetoslav Dimitrov Progress Telerik
