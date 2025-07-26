# Do I really need to re-write the whole grid filtering functionality just to put a placeholder in my filter box?

## Question

**Dan** asked on 02 Mar 2023

I am using a TelerikGrid, I want to put filters on several columns, I want to keep it clean so I disable the filter buttons and just set default operators, and I want to add a string placeholder to the already provided textbox and this is my issue. the only solution I could find was to use FilterCellTemplate which I have to rewrite the whole filtering and it is only for one column. I would think that there is a property for that that jus sets a placeholder for string searches.

## Answer

**Svetoslav Dimitrov** answered on 07 Mar 2023

Hello Daniel, You are correct, the FilterCellTemplate is the correct way going forward with adding a placeholder to a TextBox. The reason why this is required, and cannot be controlled via a parameter is that not all editors can have a placeholder, one example of that is the CheckBox (when filtering by a boolean). I can agree that this might seem a bit hard-handed for adding a placeholder, but you can make it more reusable and generic by taking advantage of the Dynamic Templates knowledge based article. The article shows how to create a reusable column <Template>, however, the approach will be the same for each RenderFragment. Regards, Svetoslav Dimitrov Progress Telerik
