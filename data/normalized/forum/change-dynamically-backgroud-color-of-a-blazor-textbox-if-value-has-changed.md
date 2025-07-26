# Change dynamically Backgroud-Color of a Blazor Textbox if value has changed

## Question

**Hen** asked on 01 Jan 2023

I track changes inside my Objects to enable/disable for example Save or Cancel Buttons in the very moment the user hits a key. Inside my Object I have a Dictionary that list all Properties that have changed during time. I would like to change the Border/Background/Whatever of each Textbox that have changed. I would like to avoid having a Class for each Textbox and I am looking for a kind of generic approach. I am missing an Event like "OnCellRenderHandler" of the Grid-Control. What would be the best solution ? The solution should cover Comboboxes, too... I would be very pleased to get an answer, maybe it is simple but I am still a novice in Terms of Blazor...

## Answer

**Dimo** answered on 04 Jan 2023

Hi Hendrik, I assume that you don't want to define a separate Class variable for each input component. There is no need to do that. You can assign each Class parameter to a method call, which checks if the component is dirty and returns the corresponding class value. I understand that you already have this information, so no extra work here. Here is a simple example. Our input components do not expose inline styles or setting Class via event arguments. So I hope the above suggestion is feasible. Regards, Dimo

### Response

**Hendrik** commented on 04 Jan 2023

Thank you very much. This was the perfect answer. I was not aware that you can bind the result of a method to Control-Properties.
