# Custom NoTemplateData template for TelerikComboBox

## Question

**Nah** asked on 28 Sep 2023

Good day, everyone I found this thread today where you can define a custom template for your NoDataTemplate in MVC and it is implemented on an AutoComplete component. I need to implement something similar to this but for a TelerikComboBox instead and in Blazor, is it possible? Thanks in advance. PS: Sorry, I wrote the title wrong. Is NoDataTemplate instead of "NoTemplateData"

## Answer

**Nahuel** answered on 29 Sep 2023

For those who may wonder about this, as there is no way to implement something like this in Blazor, what I did was combine the OnRead event from the ComboBox to take advantage of the ComboBoxReadEventArgs parameter to read the values from the Filters property that comes inside the Request property. If there's any value, then I can capture that string and display it inside the NoDataTemplate -- I can also create a custom template to add a button inside and reference a function in the onClick callback event. I'll paste a snippet of the code for more clarification: Combobox template: <TelerikComboBox TItem="@MaintenanceGridModel" TValue="@(int?)" @bind-Value="@SelectedCounterparty.CounterpartyID" OnRead="@ReadItems" TextField="@nameof(MaintenanceGridModel.CounterpartyName)" ValueField="@nameof(MaintenanceGridModel.CounterpartyID)" Filterable="true" DebounceDelay="300" FilterOperator="StringFilterOperator.Contains" Placeholder="Select Counterparty" @ref="@comboboxRef"> <NoDataTemplate> <button class="btn-new-item-multiselect btn-new-item k-button" @onclick="@AddItem"> <TelerikFontIcon Class="k-icon k-icon-lg" Icon="@FontIcon.Plus" /> <strong> Add @MissingCounterparty </strong> </button> </NoDataTemplate> </TelerikComboBox> ReadItems function -- everytime the user writes a value inside the ComboBox input, I can capture it like this: @code {
[...] private string MissingCounterparty { get; set; }
[...] protected async Task ReadItems ( ComboBoxReadEventArgs args ) { if (args.Request.Filters.Count> 0 )
{ // This is how I can get the value the user writes inside the input MissingCounterparty=(args.Request.Filters[ 0 ] as FilterDescriptor).Value.ToString(); } var datasourceResult=await CounterpartyList.ToDataSourceResultAsync(args.Request);
args.Data=(datasourceResult.Data as IEnumerable<MaintenanceGridModel>).ToList();
}
} And like that, the @MissingCounterparty variable can store the value and it will be displayed inside the NoDataTemplate and inside the template you can put whatever you want.

### Response

**Hristian Stefanov** commented on 03 Oct 2023

Hi Nahuel, Thank you for sharing your insights and the approach you've found suitable for this scenario, which can be of great value to others facing similar challenges. In terms of our Blazor library features, it's worth highlighting that our components have been in existence for approximately four years. In comparison to more established technologies such as jQuery, Angular, React, and others, which have a longer history and greater maturity, it is natural for our Blazor components to be in a continuous process of evolution and alignment as they strive to catch up. Additionally, it's worth noting that achieving a specific result may not always follow an identical path across different technologies. Variations can occur based on the underlying frameworks and paradigms unique to each technology stack. Kind Regards, Hristian

### Response

**Hristian Stefanov** answered on 28 Sep 2023

Hi Nahuel, I confirm that the NoDataTemplate for our Blazor ComboBox component was introduced in version 4.0. Therefore, to take advantage of this feature, upgrade your version to 4.0 or to our latest 4.5. Here is the documentation for this template: No Data Template docs. Furthermore, for your convenience, here is an article showing what features each version comes with: Release History. Regards, Hristian Stefanov Progress Telerik

### Response

**Nahuel** commented on 28 Sep 2023

Hi Hristian, thank you for your response. I'm already working with the 4.5 version of the library, and I was not asking about how to use the NoDataTemplate. I was asking if it is possible to implement something similar to this thread, but in Blazor. The documentation only states the NoDataTemplate shows a predefined message ("No Data") but says nothing about how we could customize the component even further. So far I tried manipulating the NoDataTemplate content to display the value that's missing and a button to allow the user to add that value as a new entry in the Combobox in combination with Combobox's events but it doesn't work properly. The value displayed on the template is always the one that was previously selected and not the one that is currently missing. So, again, is it possible to implement something similar to the thread I linked before? I honestly feel that this library for Blazor is quite underdeveloped and it lacks a lot of good features that are already available for other technologies (jQuery, Angular, React, MVC, etc.). Some of them are still not implemented yet, even though users have asked for them ~3 years ago.
