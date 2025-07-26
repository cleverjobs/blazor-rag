# Side View for Editing

## Question

**Sco** asked on 02 Nov 2020

Is there a good way to use the Popup view for grid editing more like a side view that: - Overlays to the right side of the screen instead of the middle. - Dismisses automatically when you de-select the cell or select another cell. Here is an illustration of what we are trying to accomplish: 4. Inline editing There are many UI solutions for editing table cells: inline boxes (bad when dealing with endless rows), popups (annoying), expandable sections (meh), and others. I don’t think there’s one best practice for this pattern as it depends on the functionality, the data-types, the use-cases, but one of my favorite alternatives (especially as a user) is having a side view (quick view) that pops in from the side once an item is selected. What I like the most about this option is that it maintains the context (unlike popups), easy to use (forms are easy), and works well even for a large number of fields is presented in a vertical scroll view.

## Answer

**Svetoslav Dimitrov** answered on 03 Nov 2020

Hello Scott, You could achieve that by using the TelerikWindow and some CSS. As an attached file, you could see a demo application which implements a similar layout. I would like to note that the CSS rules I applied would not work for every UI, for example, if the page is scrollable the position would not be the same, thus the appearance would fail. Also, as an attached file you could see a screenshot of the project execution. Here is a list of the resources I have used to make this demo: As the base of the application, I have used the custom popup editing form from our public GitHub repository To align the TelerikWindow to the right-hand side of the screen I have used this Knowledge-Based article. This KB article suggests two different approaches, one of which uses the Animation Container Applied some additional CSS rules to align the position of the Window over the Grid. I hope this would be helpful for the implementation of your application. Regards, Svetoslav Dimitrov
