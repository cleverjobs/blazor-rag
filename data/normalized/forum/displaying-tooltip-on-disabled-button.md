# Displaying Tooltip on Disabled Button

## Question

**Jör** asked on 20 Sep 2024

Hello, how can a tooltip be displayed on a disabled button? I have a use case where the user should be informed of the reason for the disabled button through the tooltip. Thank you in advance! [https://blazorrepl.telerik.com/GoENGaYV59uuC3IQ44](https://blazorrepl.telerik.com/GoENGaYV59uuC3IQ44)

## Answer

**Tsvetomir** answered on 20 Sep 2024

Hello Jörg, Thank you for the provided REPL snippet. In general, the disabled HTML elements do not fire mouse events, so the Tooltip can't find out when the user hovers a disabled button. So the observed behavior is expected. However, an alternative is to wrap the disabled button in some other HTML element for example div, and set the Tooltip to target it. To assist you further, I've modified the provided REPL example. I hope this approach serves you well. Regards, Tsvetomir Progress Telerik
