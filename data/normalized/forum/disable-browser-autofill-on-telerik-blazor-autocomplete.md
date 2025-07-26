# Disable Browser Autofill On Telerik Blazor Autocomplete

## Question

**bil** asked on 23 Oct 2023

I need to disable the browser's autofill option on our Blazor Autocomplete. How can I accomplish this? THanks Billy

## Answer

**Georgi** answered on 26 Oct 2023

Hi, Billy, If we are talking about automatic browser autofill on page load, I can suggest two possible ways to prevent it: Clear the value with JavaScript, for example from OnAfterRenderAsync. Use a small timeout to execute the code after the browser auto-fills. You can set the autocomplete attribute with JavaScript as well. Render the AutoComplete disabled, so the browser skips it. Then, enable it after a short delay. Additionally, you can find more information on Autofill in the following articles. The overall situation is that browsers may not always obey the rendered autocomplete attribute and developers come up with ideas how to workaround this. [https://stackoverflow.com/questions/34443628/autofill-populating-wrong-fields](https://stackoverflow.com/questions/34443628/autofill-populating-wrong-fields) [https://stackoverflow.com/questions/15738259/disabling-chrome-autofill](https://stackoverflow.com/questions/15738259/disabling-chrome-autofill) Best regards, Georgi Progress Telerik
