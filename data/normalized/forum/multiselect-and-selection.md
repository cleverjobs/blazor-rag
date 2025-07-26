# MultiSelect and selection ?

## Question

**Dea** asked on 04 Oct 2022

Is there any way to suppress the selection items appearing in the textbox portion of the control? Example of my issue: As the more items are selected the text box grows and pushes down. We have some pretty big selections we use sometimes and this makes the UI ugly. Would like it not to do that but still have the items the user selected in the control in the backend. Code @* as you type "de", you will only get "Developer" and "Designer" as suggestions instead of the full list *@<TelerikMultiSelect Data="@Roles" @bind -Value="@TheValues" Filterable="true" Placeholder="Write 'de' to see the filtering" ClearButton="true" AutoClose="false"> <MultiSelectSettings> <MultiSelectPopupSettings Height="100px" /> </MultiSelectSettings> </TelerikMultiSelect> @* <ul> @foreach (var item in TheValues) { <li>@item</li> } </ul> *@@code{ List <string> TheValues { get; set; }=new List <string> (); List <string> Roles { get; set; }=new List <string> { "Manager", "Developer", "QA", "Technical Writer", "Support Engineer", "Sales Agent", "Architect", "Designer", "Gandalf", "DeadPool", "Batman", "Driver", "Pilot", "Rebel", "Sith", "Jedi" }; }

## Answer

**Dimo** answered on 07 Oct 2022

Hi Deasun, We have a public feature request for the so-called single tag mode for the MultiSelect. The page provides two different workarounds that are applicable for you - hide the selected items and only display a label with their number make the selected items' container scrollable You can also vote and follow the feature request to receive status updates. Regards, Dimo Progress Telerik
