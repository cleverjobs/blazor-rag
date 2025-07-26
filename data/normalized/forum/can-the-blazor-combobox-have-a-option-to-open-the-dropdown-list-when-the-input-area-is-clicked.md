# Can the Blazor Combobox have a option to open the dropdown list when the input area is clicked?

## Question

**Aus** asked on 29 Mar 2024

I would like the Blazor Combobox to open the dropdownlist on clicking the input area when there is a placeholder. Something like OpenListOnClick=true It will cause the Combobox to behave much like the Blazor DropDownList. This was the similar functionality of the RadComboBox in the Telerik UI asp.net Ajax controls found here: [https://demos.telerik.com/aspnet-ajax/combobox/examples/overview/defaultcs.aspx](https://demos.telerik.com/aspnet-ajax/combobox/examples/overview/defaultcs.aspx) Note: when a value has been selected the text becomes highlighted, but when the placeholder is there it puts the carat/cursor at the beginning. Or if there is an simple workaround that would be great.

## Answer

**Hristian Stefanov** answered on 01 Apr 2024

Hi Austin, To open the ComboBox upon clicking its input, you can encapsulate the component within an HTML " div " element and leverage its " onclick " event. Then, utilize the ComboBox component reference to initiate the opening action by invoking the " Open() " method. I have prepared an illustrative example for you: <div @onclick="@(()=> HandleInputClick())"> <TelerikComboBox @ref="@ComboRef" Data="@myDdlData" TextField="MyTextField" ValueField="MyValueField" @bind-Value="selectedValue"> </TelerikComboBox> </div> @code {
private TelerikComboBox<MyDdlModel, int> ComboRef { get; set; }
private int selectedValue { get; set; }

private void HandleInputClick()
{
ComboRef.Open();
}

public class MyDdlModel
{
public int MyValueField { get; set; }
public string MyTextField { get; set; }
}

private IEnumerable <MyDdlModel> myDdlData=Enumerable.Range(1, 20).Select(x=> new MyDdlModel { MyTextField="item " + x, MyValueField=x });
} Additionally, for the text becoming highlighted upon click, we have an open feature request: ComboBox to select all text when clicking in it to type. You can vote for it to raise its priority. The public item in the link also provides an alternative to make the highlighting possible that you can include in the above sample. Let me know if you are facing any difficulties. Regards, Hristian Stefanov Progress Telerik
