# Focus Telerik widget on validation error

## Question

**Cla** asked on 10 Oct 2024

Hi, my goal is validate a form and focus telerik widget with validation errors. Now i can find the element search for class "k-invalid" but how to get the widget reference so i can call the FocusAsync() method? Thanks

## Answer

**Hristian Stefanov** answered on 14 Oct 2024

Hi Claudio, I can confirm that you can easily focus on the first invalid input without needing to use a template and the FocusAsync() method. This can be achieved with a small JavaScript function called within the OnInvalidSubmit event handler. I've prepared an example for you here: REPL link. Please run and test it to see if it meets your expectations. Regards, Hristian Stefanov Progress Telerik
