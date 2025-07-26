# avoid to hide dialog on esc key press

## Question

**Cla** asked on 01 Jul 2024

When i have a TelerikDialog and press ESC key, the dialog is hidden. How to avoid this as a default behaviour? can you add a property for it, for example IgnoreEscapeKey="true"? there is another way to solve? Thanks

## Answer

**Tsvetomir** answered on 04 Jul 2024

Hello Claudio, Thank you for the clear explanation of the scenario you are facing. To handle the described behavior, use the following approach: Use one-way binding for the Visible parameter to handle the Dialog visibility manually and define a VisibleChanged event, which will not update the visibility of the Dialog. This configuration is required to prevent an unexpected behavior of the component. Set the ShowCloseButton parameter to " false ". To see the result from the above approach first-hand, I've prepared this REPL example for you. Please refer to it and let me know if this suits your requirements. Regards, Tsvetomir Progress Telerik
