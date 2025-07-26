# Alphabetic pages for Pager Control

## Question

**Kel** asked on 05 Aug 2022

Is there a way to have the pager control display alphabetic pages instead of numeric? I would like to provide to my users a contacts book where it is displayed alphabetically based on contacts name. If not this might be a suggestion for a new control. I am thinking a modern day rolodex.

## Answer

**Nadezhda Tacheva** answered on 10 Aug 2022

Hi Kelly, Generally speaking the Pager is designed to cover cases in which the data collection is split into pages where each page will list an equal set of items. In the described scenario, it is more likely that the separate alphabetical pages contain different count of items which is a use case that the Pager could not cover. That said, the scenario should rather be handled with a custom approach. You can, for example, filter the available items by the letter their name starts with. If we target the Grid, for instance, you can: Add a Toolbar and render buttons for the letters Handle the button clicks to add FilterDescriptor through the Grid State. Thus, you can filter the Grid by the corresponding button value and filter operator "StartsWilth". You may also find the Search Grid on Button Click knowledge base article useful. I hope the above information will help you move forward with your application. Please let me know if further questions are raised. Regards, Nadezhda Tacheva Progress Telerik
