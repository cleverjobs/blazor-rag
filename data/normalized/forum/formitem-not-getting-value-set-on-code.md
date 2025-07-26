# FormItem not getting value set on code

## Question

**Die** asked on 19 Jan 2024

I am studying the Telerik controls for Blazor, so I've created the following REPL with code found on the docs: [https://blazorrepl.telerik.com/GSuFlZQa06BKC3Xn51](https://blazorrepl.telerik.com/GSuFlZQa06BKC3Xn51) On the REPL everything works perfectly, but when I create a project and use the same code, the fields for the properties Id, FirstName and LastName don't get the values set on code. Also, the button on the TelerikDatePicker does not work, but I don't know if the two problems are related. I am attaching a sample project to reproduce the behavior.

## Answer

**Hristian Stefanov** answered on 24 Jan 2024

Hi Diego, I'm glad to hear that you are starting to explore our Blazor components. Now let me help you fix the matter at hand below. The latest .NET 8 introduces new render modes: ASP.NET Core Blazor render modes. These render modes require some additional configurations in the project so our component can work. More details, you can find on our Getting Started article. For your convenience, I have modified the project on your behalf with the above chagnes, and I'm attaching it back. Regards, Hristian Stefanov Progress Telerik

### Response

**Diego Modolo** commented on 29 Jan 2024

Thank you a lot for your help. I'll keep exploring the controls.
