# Possible to change initial values for incell Add Command?

## Question

**Joh** asked on 01 Jun 2021

Hi there, I'd like to be able to click the Add command button, a child component will popup and I will be able to select an item that will then fill in some fields of the new grid row. I can't seem to get this to work with incell editing though, is this possible?

## Answer

**Dimo** answered on 03 Jun 2021

Hi John, The easiest way to define an initial default value for a new Grid row is via the model constructor. If you need a more flexible approach, then get the Grid state, define a InsertedItem with the desired initial values, and set back the updated Grid state. In this way, the user will enter insert mode. The following Knowledge Base article provides more information for both options: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-default-value-for-new-row](https://docs.telerik.com/blazor-ui/knowledge-base/grid-default-value-for-new-row) Regards, Dimo
