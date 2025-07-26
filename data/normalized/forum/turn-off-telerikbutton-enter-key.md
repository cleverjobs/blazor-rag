# Turn off TelerikButton enter key

## Question

**Ben** asked on 14 Jun 2024

Hi, We have an issue on our site that when you press an enter key on a second custom grid row (not a Telerik Grid, but rather a foreach that makes a new additive row) it will expand the first row when we press enter on any other row. We've boiled it down to it possibly being a Telerik A11Y issue. Is there a way we can stop a the button from reacting to an enter key press? Kind regards, Benjamin,

### Response

**Hristian Stefanov** commented on 18 Jun 2024

Hi Benjamin, Could you provide more details on the specific accessibility issue you're encountering, including the configuration you're using and the Telerik components involved? Overall, I confirm that our button component complies with the official accessibility standards. It also follows the WAI-ARIA best practices for implementing keyboard navigation for its component role and is tested against popular screen readers. Enter key press is part of these requirements. Kind Regards, Hristian

### Response

**Benjamin** commented on 18 Jun 2024

Hi Hristian, It's not so much an accessibility issue, The issue comes in that we made a custom add grid that's a very minimal design. With this it is essentially a foreach loop that adds a new row with each new item. When we're on any of the rows and press enter, it triggers the first row's button. No matter what we do we cannot remove that functionality

### Response

**Hristian Stefanov** commented on 20 Jun 2024

Hi Benjamin, Thank you for getting back to me with more details. However, I'm still not completely sure about the exact scenario. In general, there are several approaches to prevent the Enter key from triggering buttons or other HTML elements. For instance, you can set the button's TabIndex parameter to -1, which prevents it from being focused via the keyboard and thus stops the Enter key from activating it. Another useful method is to use preventDefault in the onkeydown or onkeypress event handlers. Kind Regards, Hristian

### Response

**Benjamin** commented on 20 Jun 2024

Hi Hristian, I'll give try to these and revert back. Kind regards,

### Response

**Hristian Stefanov** commented on 24 Jun 2024

Hi Benjamin, Take as much time as you need to review the information. Kind Regards, Hristian

### Response

**Benjamin** commented on 11 Jul 2024

Hi, Sorry it's taken so long to get back to you, sadly adding TabIndex -1 did not fix this. Below is an example of our layout, When we are on any of the inputs and press enter it does will trigger the Edit button above the inputs, resulting in this: No matter what we always get that button to trigger, and from what we can see it's not something we've done to cause this. The component hierarchy is: HTML Legend (error wrapper) Foreach (looping over each item) { Text containing collapsible summary of input and Edit and Delete TelerikButtons } { Floating labels Telerik Input (Multicolumncombobox, TelerikNumericTextbox, TelerikTextbox) TelerikButtons to Add, Save and Delete }

### Response

**Hristian Stefanov** commented on 15 Jul 2024

Hi Benjamin, Based on your latest information, it sounds like you have an "Edit" button within a form, and each time you press Enter, the button submits the form and triggers validation. To prevent the form from submitting when you press Enter, make sure the "Edit" button's ButtonType parameter is set to " Button," like this: <TelerikButton ButtonType="@ButtonType.Button"> Edit </TelerikButton> Kind Regards, Hristian

### Response

**Benjamin** commented on 17 Jul 2024

Hi Hristian, That seemed to do the trick, I can't believe I used the wrong type of button :D Thanks for the assistance!
