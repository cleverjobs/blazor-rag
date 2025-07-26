# How to set a maximum length on a TelerikAutoComplete input component?

## Question

**RobRob** asked on 25 Oct 2022

Hi, Is it possible to set the maximum length of the data entered into a TelerikAutoComplete component? I've tried catching keystrokes on the component and throwing away the surplus but this is not acceptable to our users. Cheers Rob

## Answer

**Hristian Stefanov** answered on 28 Oct 2022

Hi Rob, The desired result is easily achievable through the " ValueChanged " event and an " if " block that checks for the value length. Here is one way you can do it - REPL link. Please run and test the REPL sample to see the result. Regards, Hristian Stefanov Progress Telerik
