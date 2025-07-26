# How to bind DropDownList to an Enum

## Question

**dca** asked on 21 Jan 2020

Is there a way to bind the Data source for a Blazor UI DropDownList to an Enum, similar to the Kendo described in this link --> [https://www.telerik.com/forums/dropdownlist-with-enums](https://www.telerik.com/forums/dropdownlist-with-enums) ?

## Answer

**Marin Bratanov** answered on 22 Jan 2020

Hello, I made a KB with a few examples: [https://docs.telerik.com/blazor-ui/knowledge-base/dropdown-kb-bind-to-enum](https://docs.telerik.com/blazor-ui/knowledge-base/dropdown-kb-bind-to-enum) Regards, Marin Bratanov

### Response

**chesk345** commented on 28 Jul 2021

I got this to work for me. Is it possible to do this with a TelerikRadioGroup? I tried the same approach with that control but I got and InvalidCastException.

### Response

**Marin Bratanov** commented on 28 Jul 2021

Here's the sample from the article where I just added a radio group bound to the same value and data, which works fine for me in the latest 2.25.0, please give this a try and if it does not help you move forward, I recommend opening a new thread where you can post the problematic code. <TelerikRadioGroup @bind-Value="@selectedValue" Data="@myDdlData" TextField="@nameof(EnumDdlModel.MyTextField)" ValueField="@nameof(EnumDdlModel.MyValueField)"> </TelerikRadioGroup> @selectedValue <br /> @* in this case the value is the enum type *@@selectedValue.GetType() <br /> <TelerikDropDownList Data="@myDdlData" TextField="MyTextField" ValueField="MyValueField" @bind-Value="@selectedValue"> </TelerikDropDownList> @* for a combo box, make sure that custom values and clearing are not available unless you are explicitly OK with that *@<TelerikComboBox Data="@myDdlData" TextField="MyTextField" ValueField="MyValueField" @bind-Value="@selectedValue" ClearButton="false" AllowCustom="false" Filterable="true"> </TelerikComboBox> @code {
public class EnumDdlModel
{
public Telerik.Blazor.AnimationType MyValueField { get; set; }
public string MyTextField { get; set; }
}

Telerik.Blazor.AnimationType selectedValue { get; set; }
List <EnumDdlModel> myDdlData { get; set; }=new List <EnumDdlModel> ();

protected override void OnInitialized()
{
//prepare instances of the model from the list of enum values and a desired string representation for the user
foreach (Telerik.Blazor.AnimationType item in Enum.GetValues(typeof(Telerik.Blazor.AnimationType)))
{
myDdlData.Add(new EnumDdlModel { MyTextField=item.ToString(), MyValueField=item });
}

base.OnInitialized();
}
}
