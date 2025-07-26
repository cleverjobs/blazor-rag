# TK Blazor Combobox Opens Keyboard When User Taps

## Question

**bil** asked on 02 Oct 2023

The combobox works find when viewing on desktop browser. But when viewing on mobile devices, it launches the keyboard if the user attempts to select an item from the list. I have set the below flags Filterable=false ClearButton=false Do I just need to not use the combobox component on mobile? Thanks Billy

## Answer

**Svetoslav Dimitrov** answered on 04 Oct 2023

Hello Billy, This is the expected workflow of the Telerik ComboBox when you use it on a mobile device. Let me explain: Let us take a look at the workflow: Your users open the dropdown of the ComboBox to view the items Your users click on an item in order to select it The item is selected and the focus goes to the textbox part of the ComboBox The on-screen (virtual) keyboard is rendered Why is this the expected behavior - in mobile, both on Android and iOS the browsers render the on-screen keyboard when a <input> HTML element receives focus. The ComboBox renders a <input type="text"> together with a button for expanding the popup. When the user selects an item from the list the focus goes into the <input type="text">, thus the on-screen keyboard is rendered. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**billy** commented on 16 Oct 2023

Is there a selection mode that I can assign when media query is below a certain threshold?

### Response

**Svetoslav Dimitrov** commented on 19 Oct 2023

Hello Billy, I did some digging, and here is some additional information. So, the main reason behind this is accessibility compliance. When the user selects an item from the dropdown two things must happen: The dropdown must close and set the focus to the input The focused input allows screen readers like NVDA to read out the value of the ComboBox to people with disabilities. This is also the behavior of the W3 combobox which is used as best practice in terms of accessibility. I hope this clarifies things.
