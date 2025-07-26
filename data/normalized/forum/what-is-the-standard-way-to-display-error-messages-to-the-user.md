# What is the standard way to display error messages to the user?

## Question

**Wil** asked on 15 May 2021

What is the standard way to display error messages to the user? I have an ASP.NETCore, EFCore, Blazor-Server, Kendo-Blazor-UI application. A user accomplishing a record change with TelerikGrid might trigger a DbUpdateConcurrencyException in BankAccountService.Update(). I want to catch the exception, then give the user a useful action such as, "Another user, (*cough* Bob H. in Accounting), made insignificant changes to account (#45678) while you were making your very important modifications. Please refresh your browser, review Bob's changes, then submit your modifications, again. Be sure to thank Bob later." How is this communication back to the user best accomplished in a standard way? Thanks!

## Answer

**Hristian Stefanov** answered on 19 May 2021

Hi Will, The best way to display different error messages is by adding a custom validator (with remote validation) in the Editor Template of your Grid. This approach is the best to accomplish this good communication with the user. You can also check this Remote Validation example upon Insert or Update in Grid, where you can see another approach of the remote validation usage on the server. It showcases how to prevent updates or inserts of items when they don't satisfy certain conditions that cannot be implemented through the standard DataAnnotation validation. I hope this helps and if you have any other questions, please let me know. Regards, Hristian Stefanov
