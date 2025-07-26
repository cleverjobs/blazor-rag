# trouble implementing a custom component with binding

## Question

**Ada** asked on 04 Apr 2023

Hello! I'm trying to implement a custom component that uses a numeric text box internally -- just to factor out some redundant markup in my particular situation. A custom component would be a nice fit. I've tried a few different things, but I can't get binding behavior to work. It shows the right value, but doesn't allow any updating. (All entries show as invalid.) I tried it with a Value/ValueChanged approach and also a @bind-Value approach, and couldn't get either to work. I've noticed that my ValueChanged handler (OnValueChanged) is not getting called. I looked at this: [https://docs.telerik.com/blazor-ui/getting-started/value-vs-data-binding](https://docs.telerik.com/blazor-ui/getting-started/value-vs-data-binding) but it didn't illuminate anything for me, really. Any ideas what I'm doing wrong?

## Answer

**Adam** answered on 04 Apr 2023

After some experimentation with a minimal case, I found this has to do with the NumericTextBox having a Max property. If you remove that property, binding from within a custom component works as expected.

### Response

**Dimo** commented on 07 Apr 2023

I suppose that the Max parameter of the NumericTextBox ends up being null. This is not a valid configuration, so since the parameter is always set, provide a (default) value. It can be decimal.MaxValue.
