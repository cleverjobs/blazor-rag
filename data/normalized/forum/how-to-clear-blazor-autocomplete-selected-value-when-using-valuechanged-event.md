# How To Clear Blazor AutoComplete Selected Value When Using ValueChanged Event

## Question

**bil** asked on 22 Sep 2023

I am using the below input utilizing the ValueChanged Event to query data results from the backend to populate the list. In different cases I need to clear the selected value from other Methods, but after it's selected, the only way to clear it is to use the "X" in the autocomplete input. I saw threads stating to clear the @bind-Value="Model.Property" to clear it. But, when using value changed, it will not let me set @bind-Value, I must use ValueExpression lamda. My question is, how can I clear this value from my blazor CodeBehind? Input <TelerikAutoComplete Class="@(this.ProviderSearch.IsUsingMyLocation ? "my-location-on":"my-location-off")" Placeholder="@this.ProviderSearch.SelectedAutocompleteLocation" Data="@this.AutocompleteSuggestions" TItem="Prediction" ValueField="Description" OnChange="@this.OnAutoCompleteSelectedHandler" ValueChanged="@( (string newValue)=> OnAutoCompleteValueChanged(newValue) )" ValueExpression="(()=> this.ProviderSearch.SelectedAutocompleteLocation)" />

## Answer

**Georgi** answered on 26 Sep 2023

Hello, Billy, It is possible to clear the value of the AutoComplete component by using the Value parameter instead of @bind-Value. There are a few differences between the two attributes: Value can be used with both OnChange and ValueChanged. Value needs to be manually updated through the ValueChanged method. Value has to be a string. I have prepared a REPL example where the selected value can be cleared with the OnChange method or a custom button. Let me know if additional information is required. Regards, Georgi Progress Telerik

### Response

**billy** commented on 27 Sep 2023

Thank you Georgi. I'll work at implementing this pattern. Can you also tell me how to avoid the " Index was outside the bounds of the array." when clicking off of the component and dropdown? We query the db as the user types and this error is difficult to diagnose as to where it is occuring. But, if I have a populated list of suggestions and instead of clicking on one of the items I click off of the list, it throws this error. I'd like to either leave the suggestion list in tact or collapse it until the user actually selects one of the items. Can you help with this?

### Response

**Georgi** commented on 29 Sep 2023

Hi, Billy, I have attempted to reproduce the described issue. However, I am able to click off the component without triggering the error in question. Would it be possible to provide a runnable sample with a populated list or modify this REPL example so the issue is reproducible locally and send it back to me? This will allow me to further investigate the scenario and come up with suitable suggestions.
