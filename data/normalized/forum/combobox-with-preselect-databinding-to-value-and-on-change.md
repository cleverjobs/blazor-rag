# ComboBox with PreSelect, Databinding to Value and On Change

## Question

**Dom** asked on 18 Oct 2022

Hello, I need a ComboBox that receives data via databinding (Data="@Series"), selects a value in the combobox via C# code (@bind-Value="SelectedSeries") and then executes ( OnChange="@OnComboSeriesValueChanged") a function as if a user had selected a value. But Telerik does not allow double binding to the control. Who is supposed to understand this!? This restriction is unnecessary!!! My use case is quite normal after all. Not working example "...'ValueChanged' is used two or more times..." <TelerikComboBox Data="@Series" OnChange="@MyOnChangeHandler" ValueChanged="@((string value)=> OnComboSeriesValueChanged(value))" @bind-Value="SelectedSeries" TItem="string" TValue="string" AllowCustom="false" Filterable="true" Placeholder="Select a Series." Width="100%" @ref="SeriesComboBoxRef"> </TelerikComboBox> Thanks for your help

## Answer

**Dominik** answered on 19 Oct 2022

The Solution is to use the One-Way Binding. <TelerikDropDownList Data="@Customers" Value="@SelectedCustomerString" ValueChanged="@((string value)=> OnComboCustomerValueChanged(value))" ValueField="CustomerShortName" TextField="CustomerShortName" TItem="UserCustomerDto" TValue="string" DefaultText="Select a Customer." Width="100%"> </TelerikDropDownList> IMPORTANT!!! But you have to set the Selected-Value programmatically!!!! private void OnComboCustomerValueChanged ( string val ) {
SelectedCustomerString=val;
} WHY Telerik... Why is everything so complicated and weird??? I lose so much time using your Blazor Controls. PLEAE INVEST MORE TIME IN REAL EXAMPLES!!!!

### Response

**Dimo** answered on 20 Oct 2022

Hi Dominik, The observed behavior and requirements are related entirely to Blazor and .NET. Every Blazor component parameter Foo can be used in one of two ways: two-way binding: @bind-Foo="..." one-way binding: Foo="..." FooChanged="..." Two way binding requires an empty FooChanged handler to be defined, and the Blazor framework is simply calling/using it automatically. If you try to use two-way binding with a separate FooChanged handler, this means that you will have two duplicate handlers and naturally, .NET won't allow this - it's like having two methods (overloads) with the same signature. That's why we expose an OnChange handler that does not prevent two-way binding. I am not sure what brings the need to use two-way binding, ValueChanged and OnChange at the same time in your case? And yes, if you use the ValueChanged handler yourself, this means that you need to update the Value manually, because the Blazor framework is no longer doing that automatically. This is ValueChanged example in the documentation shows this. Regards, Dimo
