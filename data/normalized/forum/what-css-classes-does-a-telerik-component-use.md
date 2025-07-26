# What css classes does a Telerik component use?

## Question

**Pau** asked on 30 Sep 2022

Hi I want to change the look and feel of some components, I think i need to override some k-xxx styles How do i know which component uses which styles. So for example the TelerikTextBox , if i want to change the border, which style does it use now? Paul

## Answer

**Hristian Stefanov** answered on 05 Oct 2022

Hi Paul, There are so many CSS classes responsible for different parts of the Blazor components. The easiest way to see the components CSS classes is to use your browser dev tools to inspect the page HTML. I have prepared an example with TelerikTextBox for you to demonstrate one of the classes: <style>.k-textbox { border-color: red;
} </style> <p> TextBox value: @StringValue </p> <TelerikTextBox @bind-Value="@StringValue" /> @code {
string StringValue { get; set; }
} Regards, Hristian Stefanov Progress Telerik
