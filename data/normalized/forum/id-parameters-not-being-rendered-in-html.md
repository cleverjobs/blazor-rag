# Id parameters not being rendered in html

## Question

**Kyl** asked on 13 Apr 2022

There are multiple Telerik components (TileLayoutItem, ButtonGroupButton, ButtonGroupToggleButton, GridCommandButton) that take an Id parameter but do not render that parameter as an id attribute on the HTML that is generated. Rendering the Id parameter in html is a behavior displayed by multiple other Telerik components (TelerikButton, TelerikDropDownList, TelerikDatePicker, etc) and I believe should be the expected behavior. Are there plans to Add an Id parameter to all Telerik components Render all Id parameters on Telerik components as an id attribute in the generated html

## Answer

**Svetoslav Dimitrov** answered on 18 Apr 2022

Hello Kyle, The reason why the GridCommandButton (and the other building blocks you have mentioned) have an Id parameter is that it internally uses the TelerikButton which has the Id. We have added Ids for the elements that would be used in forms, such as the input components (textbox, numeric textbox, dropdowns, and others). The command button would not be used in a form and thus we did not render the Id in the browser. We have an open feature request regarding the addition of an Id for all components. I would love it if you go there and share some feedback on the need for the ids on all components. I have already added your Vote for the feature request and you can click the Follow button to receive email notifications on status updates. Regards, Svetoslav Dimitrov Progress Telerik
