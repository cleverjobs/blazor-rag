# How to navigate a detail template with the keyboard

## Question

**Mik** asked on 22 Dec 2022

Is there a way to navigate to a hierarchical detail template within the grid using the arrow keys? Currently in keyboard navigation demo, it mentions putting some type of focusable element into the template and hitting the tab key to get to it, but this is rather counter-intuitive for a screen reader user with the keyboard if they are using the arrow keys to navigate the grid cells, and then having to tab to get within the detail. If they tab again it's going to take them out of the grid completely.

## Answer

**Dimo** answered on 23 Dec 2022

Hello Mike, There are a few reasons why there is no built-in arrow navigation between the master the detail Grid rows. Built-in keyboard navigation works in the scope of a single component and requires predefined HTML output. The master and detail Grid instances are not aware of each other. Surely, the master Grid knows that it has a DetailTemplate, but it doesn't know what's inside it. The user may not want to dive into the detail Grids automatically, while going over the master rows. Such automatic navigation may pose distraction and confusion. As a result, cross-Grid keyboard navigation requires manual implementation, depending on the specific scenario and desired UX. Here are a few ideas and possible techniques: Add a button in a command column or any other suitable UI to hint the user how to go to the detail Grid. The user action should focus an element inside the Grid <DetailTemplate> with JavaScript. Keep track of all expanded items in the Grid OnStateChanged event. When you detect a newly expanded master row, focus its detail template. In both cases, use the context of the <DetailTemplate> and the <GridCommandColumn> to know what is the current master row and pass this information to any handlers that need it. All focusable elements will need ID attributes that are unique for each master row and detail template. In the future, you will be able to focus Grid cells programmatically via API. Regards, Dimo

### Response

**Mike** commented on 23 Dec 2022

Hi Dimo, Thanks for the response. However, the workaround is a little inconsistent from an accessibility standpoint. I get that you don't know ahead of time what would be in the Detail Template, but it is wrapped in a td element, so you could still focus around the entire td of that detail template with the arrow keys. Then, like the command column, hitting enter would set the focus to the first focusable element inside the template. Additionally, hitting the escape key could back them out of the template, just like the command column does. This would make things a lot more consistent. And if it isn't possible to know what the first focusable element is, how about creating some sort of OnEnterDetailTemplate event, so that the user could handle setting the focus at that point. This would keep the keyboard functionality of the grid more consistent, with how you do other things. That being said, my primary reason for trying to utilize the detail template is so that I can display a large text field of the main model that the grid is bound to so that it spans across all columns underneath the rest of the columns and not squished into a single column. Is there a way to do that without having to use the detail template to achieve this?

### Response

**Dimo** commented on 27 Dec 2022

Hi Mike, This clarifies things a bit. So the detail template in this case is a purely visual workaround for the visual users. It affects negatively non-visual users, because it moves information from the "regular" table row to a separate table. I believe that keeping all information in a single table is the best for accessibility and non-visual users. It ensures intuitive access without the need for additional user training. For visual users, you can employ one of the following (which will preserve non-visual access): A scrollable container inside a column template. Show part of the information in the cell and all the information in a Tooltip or a Window. You can even consider a mixed approach that includes both a detail template and a column template. In this way, non-visual users will rely on the column template, while visual users will use the detail template. After the holidays, I will double-check with the UX and accessibility guys about the keyboard navigation algorithm for hierarchy. On a side note, you can play with rowspans and colspans via row templates. However, keep in mind the following: I see some online concerns that screen readers do not fully support them. The general recommendation for accessible tables is - "keep them simple". One table row in the Grid is expected to represent one data item. You may need to tweak the data structure to achieve a two-rows-per-one-data-item scenario.

### Response

**Dimo** commented on 03 Jan 2023

P.S. My colleagues from the accessibility team confirmed that the Enter-to-focus approach for the detail cell is a valid option. I logged it for additional discussion, so that they can come up with some internal specification that we will implement. Also, the detail cell container can participate in the keyboard navigation in the master Grid. Thanks for your participation, Mike!
