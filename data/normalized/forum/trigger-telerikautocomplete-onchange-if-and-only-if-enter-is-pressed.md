# Trigger TelerikAutoComplete OnChange if and only if Enter is pressed

## Question

**Ric** asked on 04 Mar 2024

As of now, the OnChange event of the AutoComplete component is triggered upon pressing the Enter key or losing focus of the input. In order to only produces changes upon pressing Enter, I use the OnBlur event to change specific boolean values (e.g isInputFocused) so as to modify the behaviour of OnChange conditionally. Is OnBlur always triggered before OnChange? In the future, will a new event be added to the TelerikAutoComplete component which is triggered only upon pressing the Enter key?
