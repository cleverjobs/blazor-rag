# Default DropDownList to first item in Data

## Question

**Dea** asked on 22 Sep 2021

Where a DropDownList is populated dynamically, and mandatory, it makes sense for there to be an option to automatically default to the first item in the list. Especially as there may only be one item in the list, or the first item may account for 99% of cases. It would be great if this could be done via a simple property: DefaultToFirst="true".

## Answer

**Svetoslav Dimitrov** answered on 27 Sep 2021

Hello Dean, You can still achieve the desired behavior by binding the value of the component to the FirstOrDefault() of the data collection. Depending on the business scenario this might be done in the OnInitializedAsync or the OnParametersSetAsync lifecycle hooks that the Blazor framework provides. The reason why would not like to provide this as a built-in feature is that the Telerik component should not intervene with data collection. Exposing such parameters would clutter the API and make them harder to use. Regards, Svetoslav Dimitrov Progress Telerik
