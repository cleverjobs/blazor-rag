# Force DropDownList to lose focus/Blur?

## Question

**Ada** asked on 15 Mar 2022

Problem Description In my code currently we have a Telerik DropDownList that triggers a redraw of a TelerikGrid based on the option selected within the dropdown. The current challenge is that when the DropDownList selection is changed, the focus is still set to the DropDownList. The effect this has is that when a user attempts to click the edit or add buttons within the Grid, the user has to click twice with the mouse. The first click doesn't seem to do anything because it's that click that causes the focus to be taken off of the DropDownList, while the second click actually allows the desired action to be triggered. Note below, how focus is still set to the dropdown The problem is that the DropDownList doesn't have a Blur() event, and none of the Telerik Components within the page (Form, Grid, and all of their child components) have the SetFocusAsync() method. Current Solution in Place The current solution we're using is to have an invisible TelerikTextBox on the page that we call SetFocusAsync on when a selection is made to the DropDownList. This is not the most ideal solution and I am reaching out to see if there is a better way to handle this. Thank you so much, and enjoy your day! ADAM

## Answer

**Apostolos** answered on 18 Mar 2022

Hi Adam, Based on the described behavior I assume that you use the OnChange or OnBlur event of the DropDownList. If this is the case, the focus of the element is not the issue here. More specifically the OnChange event will fire twice, first when the user selects an item and then again when the component loses focus. In this case, the first click on the Grid will blur the DropDownList and fire OnChange again (this is documented). This will make the Grid to refresh its data and cancel out the edit command. Then the second click will work as expected. In the same manner the OnBlur will fire only once when the user loses focus. Again, this will cause the same behavior as above. If this is the case, I suggest you to use the ValueChanged event. The main difference with the OnChange event is that ValueChanged fires upon user interaction only and not when the component loses its focus. In case I am missing something from your scenario, I will advise you to open a ticket so we can investigate the issue further. Regards, Apostolos
