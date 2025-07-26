# DropDownList not showing options

## Question

**Gau** asked on 31 Jul 2024

I am trying to add a dropdown list. But the options for drop down are not rendering. Here is a mockup of what I am trying to do: Note: I am on trial account at the moment. @page "/telerik-enum-dropdown"
@using Telerik.Blazor.Components <div class="form-group"> <label for="telerikDropDown"> Delivery Week </label> <TelerikDropDownList Data="@deliveryWeeks" @bind-Value="@selectedDeliveryWeek" Id="telerikDropDown" TextField="Text" ValueField="Value"> </TelerikDropDownList> </div> @code {
private string selectedDeliveryWeek;
private List <DropDownItem> deliveryWeeks;

protected override void OnInitialized()
{
deliveryWeeks=Enum.GetValues(typeof(DeliveryWeek))
.Cast <DeliveryWeek> ()
.Select(dw=> new DropDownItem
{
Text=dw.ToString(),
Value=dw.ToString()
}).ToList();
}

public class DropDownItem
{
public string Text { get; set; }
public string Value { get; set; }
}
public enum DeliveryWeek
{
Week1,
Week2,
Week3,
Week4,
Week5
}
} Renders this. But nothing happens when I click on it. It should show me the options for dropdown.

## Answer

**Gaurav** answered on 31 Jul 2024

Fixed it. Had to add correct render mode to App.Razor <Routes @rendermode="@RenderMode.InteractiveServer" />
