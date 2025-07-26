# Grid Custom RowTemplate

## Question

**Tho** asked on 05 Aug 2024

Hi, is there a way of reimplementing keyboard navigation when using a custom row template? The documentation states that functionality is taken way due to not knowing the current state which is totally fine. Maybe someone has an idea on how to reactivate or add keyboard shortcuts for selection and navigation. Regards, Tom

## Answer

**Dimo** answered on 08 Aug 2024

Hello Tom, In theory, yes, it is technically possible to re-implement keyboard navigation, but the word is spot-on - this will require a lot of manual coding and capturing of key events ( @onkeydown ) inside the row template or even outside the Grid. I haven't come across a case when someone has done that, but perhaps if there is such a customer, they may join the discussion. On the other hand, if keyboard navigation is important, then maybe it's possible to re-evaluate the necessity for a row template? What brings the need for it? Regards, Dimo

### Response

**Thomas** commented on 08 Aug 2024

Hi Dimo, thank you for this clarification. I came across keyboard navigation for grids while researching the possibilities to comply with the European Accessibility Act which comes into effect next year (28.06.2025). It'll affect many companies and I try to evaluate everything I can do that my current project complies. In my current project I've a list of current staff members which include an image and some data (names, internal numbers etc.) that are displayed in one cell per row. (like a info card). I use the grid for this list as it supports searching, grouping etc. When using the mouse it is possible to mark a record as active but when using the keyboard, then this doesn't work anymore as soon as a row template is used. That is totally fine and I don't have a problem finding a solution (via C# or JS). It was just a question if there was a maybe faster way. I'll have a look at "onkeydown" and see what is possible. Currently the Telerik Blazor components offer great support for mouse and keyboard navigation. That helps a lot! Regards, Tom

### Response

**Dimo** commented on 08 Aug 2024

Thanks for the additional information, Tom. In my personal opinion, it may be easier to abandon the card-like UI and use the Grid's built-in tabular layout, rather than implement the whole keyboard navigation feature manually. This is probably not an option that you are considering at this point, but I am mentioning it nevertheless.
