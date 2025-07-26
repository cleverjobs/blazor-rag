# How to set the Value of TextBox programmatically (without binding)

## Question

**TedTed** asked on 08 Jul 2022

When I try to set 'RefTextBox.Value=value' I get a warning: How is the Value of a TextBox supposed to be set programmatically without binding it to a variable?

## Answer

**Timothy J** answered on 09 Jul 2022

You can "set" in the Razor markup without binding it. If your value (MyValue) is acquired after the first render, issue StateHasChanged after it is acquired. Binds the value (two-way): <TelerikTextBox @bind- Value="@MyValue"> Only sets the value (one-way): <TelerikTextBox Value="@MyValue">

### Response

**Ted** commented on 09 Jul 2022

Tim, Thanks for your response, but I'm asking how to "set [the TextBox value] programmatically without binding it to a variable." Your code above binds it to a variable of course. I want to be able to call something like 'RefTextBox.Value=value;' from anywhere in code, not binding to a variable in the Razor markup.

### Response

**Timothy J** commented on 09 Jul 2022

The 2nd example I gave is not binding it; it is the functional equivalent of what you are trying to do, but it will not give you the warning. BL0005 is a warning, not an error. Manipulating razor components in the code behind is discouraged, but if you are aware of the downfalls, go ahead. I didn't even bother to investigate what the downfalls were, because I knew that I could it the way that made the warning disappear. I can't think of any functional difference between the two methods, so make your own choices.

### Response

**Ted** commented on 09 Jul 2022

Tim, totally appreciate your responses. In your second example, you are binding to a value (i.e., a property belonging to a instance of a class). To modify the TextBox value outside of the component/class that owns "MyValue", I would need to both: a) have access to "MyValue" from outside the class that owns that property, and b) know that the TextBox was bound to that specific property in order to know to set that property value, both of which are false in my senario (my Blazor app is built dynamically, and I want to be able to set TextBox values outside of the Razor code that initially assigns the TextBox values as events occur). btw, if you look at the code for TextBox.Value (get), it simply assigns the property and does nothing else, and I also don't like writing code like this where there is a clear warning. So, hoping there is another approved method to set the value.
