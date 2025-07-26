# ComboBox with AllowCustom is losing keystrokes randomly at normal typing speed

## Question

**Jon** asked on 04 Jun 2024

This ComboBox, with filtering and custom values enabled, glitches when typing in the box. At a normal typing speed, I'm seeing that about 10% of keystrokes are skipped, or appear briefly and then disappear. <TelerikComboBox Data="@_data" @bind-Value="@_value" AllowCustom="true" Filterable="true" FilterOperator="@StringFilterOperator.Contains" Enabled="@Enabled"> </TelerikComboBox>...
List <string> _data=new() { "Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit" };
string _value { get; set; } Dropped letters are slightly less frequent with DebounceDelay="0" ; it's worse with more items in the list. It seems to occur if you type more than 3-4 letters per second. Also, clicking the cursor in the middle of the text and typing can cause the cursor to jump to the end of the input and jumble your letters around.

## Answer

**Tsvetomir** answered on 07 Jun 2024

Hello Jonathan, Thank you for the detailed explanation of the behavior you are encountering. For the same configuration of the ComboBox, there is an already reported bug in our feedback portal: Entering text quickly in the input field leads to the text blinking and becoming partially cleared. Currently, its status is Planned. You can also subscribe to the public item to receive email notifications for further status updates. Please excuse us for any trouble. Regards, Tsvetomir Progress Telerik

### Response

**Jonathan** commented on 07 Jun 2024

Thank you, I did didn't find a ticket searching "TelerikComboBox". This does look like the same problem as described in the MultiColumnComboBox ticket.

### Response

**Alexey** commented on 19 Sep 2024

Hi, When I try to use TelerikComboBox my text is jumping. How to fix it? Look at example from your resource ( [https://demos.telerik.com/blazor-ui/combobox/custom-values](https://demos.telerik.com/blazor-ui/combobox/custom-values) ) : Link to video: [https://drive.google.com/file/d/1k670qruMsfUez5QPN34bjYv2THWPY8Pk/view?usp=sharing](https://drive.google.com/file/d/1k670qruMsfUez5QPN34bjYv2THWPY8Pk/view?usp=sharing) But when i try to use TelerikComboBox for real application with 120 data items, the text jumps even more and use TelerikComboBox for real data absolutely impossible. Look at real app with TelerikComboBox in action: [https://drive.google.com/file/d/17R9POss9IvMIHITW5FzkyJ8Bh0NQSrkg/view?usp=sharing](https://drive.google.com/file/d/17R9POss9IvMIHITW5FzkyJ8Bh0NQSrkg/view?usp=sharing) My version of the Telerik.UI.for.Blazor is 6.2.0

### Response

**Alexey** commented on 19 Sep 2024

Version of my Telerik

### Response

**Dimo** commented on 19 Sep 2024

@Alexey - I am afraid we have no reliable workaround for this issue at this point. However, we are already researching for a fix. Please follow the bug report for status updates.

### Response

**Alexey** commented on 25 Sep 2024

I have found some permanent solution. It is increase value of "DebounceDelay". I set DebounceDelay="1200" and it make working with TelerikComboBox a little bit smoothly. But this solution bring other Issue: "Autocomplete list" of the TelerikComboBox, which appear after my delay "1200" hide my dialog (move to background) which I open during delay time. And it break all flow of the my Application at all. Do you know how to fix it?

### Response

**Dimo** commented on 25 Sep 2024

A large DebounceDelay can leave the impression that the app is stuck, and encourage the user to start clicking randomly. That's why we don't encourage such an approach, unless there is a specific reason and the user is aware.
