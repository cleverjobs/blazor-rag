# Custom FilterMenuTemplate add additional filters to the standard set.

## Question

**Adr** asked on 07 Jun 2021

When you enable filtering on grid columns the default out of the box implementation gives you 2 textboxes with an "AND" operator between the 2 textboxes. For numeric columns a dropdown with options like "is less than or equal to", "is greater than or equal to" etc is displayed. For string columns a dropdown with "contains" etc is displayed. I would like to utilise the default filter implementation as described above but with the addition of my own custom checkbox filter above that will render all possible distinct values from the database. Is there a Telerik component (similar to the TelerikCheckBoxListFilter component) that I can add to my custom FilterMenuTemplate component that will bring back the default out of the box filter UI for numbers and strings or if I'm implementing my own custom FilterMenuTemplate do I also have to manually re-create these standard filters?

## Answer

**Hristian Stefanov** answered on 10 Jun 2021

Hi Adrian, I fully understand your idea of how you want to filter the data in the Grid. The possible way to have the standard menu filters with an additional checkbox list filter on the same column is to use a FilterMenuTemplate to create a custom filter menu. As you already made a good guess, there is a need to manually re-create these standard filters in the FilterMenuTemplate of the column using our DropDownList component. You can see an example of this approach in our custom filter menu demo here: [https://demos.telerik.com/blazor-ui/grid/custom-filter-menu.](https://demos.telerik.com/blazor-ui/grid/custom-filter-menu.) When you go there, you can click the Sell Start Data filter icon to see the result. I hope this helps you. If there are any other questions, don't hesitate to contact us. Regards, Hristian Stefanov Progress Telerik
