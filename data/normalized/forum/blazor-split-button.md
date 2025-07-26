# Blazor Split Button

## Question

**Dus** asked on 21 Feb 2023

Is there any way to get rid of the Split Button Content? I'd just like to show the arrow and the button options below when clicked. I need to be able to progromattically hide all of the buttons as needed. This would also include the button on display, if needed. Another option that would work for us is to have the content but have it work similar to the arrow button where clicking it would toggle the dropdown. This would allow me to put a menu icon in that area.

### Response

**Hristian Stefanov** commented on 24 Feb 2023

Hi Dustin, I confirm that you can easily get rid of the SplitButton content with some CSS. For that goal, the needed CSS style is " display: none ". I have prepared an example for you: <style>.my-splitbutton.k-button:first -child { display: none;
} </style> <TelerikSplitButton Class=" my-splitbutton "> <SplitButtonContent> </SplitButtonContent> <SplitButtonItems> <SplitButtonItem OnClick="@OnEditAll"> Edit </SplitButtonItem> <SplitButtonItem OnClick="@OnClose"> Close </SplitButtonItem> <SplitButtonItem OnClick="@OnDelete"> Delete </SplitButtonItem> </SplitButtonItems> </TelerikSplitButton> Last action: <strong> @LastAction </strong> @code {
string LastAction { get; set; }

void OnEditAll()
{
LastAction="Edit All";
}

void OnClose()
{
LastAction="Close";
}

void OnDelete()
{
LastAction="Delete";
}
} Please run and test it to see the result. The sample also uses " Class " to specify the desired component instance. Let me know if the above information covers your needs or if I'm missing something from the scenario.

### Response

**Dustin** commented on 24 Feb 2023

This is perfect! Thank you so much!!
