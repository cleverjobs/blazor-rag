# How do I simply remove the text in the textbox in a TelerikAutoComplete?

## Question

**JoeJoe** asked on 26 Sep 2023

Tried setting the Value but the textbox refuses to change the displayed text.

## Answer

**Georgi** answered on 29 Sep 2023

Hi, Joe, There are two ways this can be done depending on whether you are using the ValueChanged event or not: If you are using the event, then one-way binding has to be used via Value syntax. Alternatively, if you would prefer to use two-way binding and aren't using ValueChanged then @bind-Value syntax can be used. I have prepared both a Value REPL example and a @bind-Value REPL example. More information on value binding can be found in the following article: Value Binding vs Data Binding Let me know if additional questions arise. Kind regards, Georgi Progress Telerik
