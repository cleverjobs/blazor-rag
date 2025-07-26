# Dynamically add/remove items from form

## Question

**TomTom** asked on 18 Apr 2023

I would like to add a UI component that displays the current list of items that are selected in a multi-select listbox. As selections and deselections are made inside of the list box, those selections are also displayed or removed on a separate part of the page that is visible to the user. Is there a demo available that shows doing something like this or is there a control that already implements this capability? Thanks, T

## Answer

**Svetoslav Dimitrov** answered on 21 Apr 2023

Hello Tom, If I understand your scenario correctly, you would like to render different ListView items based on the selection in the MultiSelect component. If that is indeed correct, you can: Use the value (@bind-Value/Value) of the MultiSelect and pass it as the data source for the ListView component (through the Data parameter) Use the value of the MultiSelect to construct a data source for the ListView component Both of the options above will allow the ListView component to take control over the rendering of the items selected by your users from the MultiSelect component. Let me know if I misunderstood the scenario or if you have any additional questions. Regards, Svetoslav Dimitrov Progress Telerik
