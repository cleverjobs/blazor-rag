# FluentValidation of a Complex Model not working after update to .net 7

## Question

**Nic** asked on 14 Mar 2023

Hi After our update to .Net 7, FluentValidation does not work with complex models anymore. We're using FluentValidation 11.5.1 (latest) Blazored.FluentValidation 2.1.0 (latest) I get the error message: Cannot validate instance of type "The Composed Class Type ". Can only validate Instance of Type "Parent Class". Has somebody a solution for this issue? It worked fine in the previous version. Thank you.

### Response

**Nicolas** commented on 15 Mar 2023

So we found a Solution: At least for Blazor Serverside. The example of Telerik is not working and throws an Exception. We found the solution in the example section of the official Blazored.FluentValidation Repo: [https://github.com/Blazored/FluentValidation/blob/main/samples/BlazorServer/Pages/Index.razor](https://github.com/Blazored/FluentValidation/blob/main/samples/BlazorServer/Pages/Index.razor) This did the Trick for us: 1) Adding ref <FluentValidationValidator @ref="_fluentValidationValidator" DisableAssemblyScanning="@true" /> 1) Using FluentValidationValidator class instead our own Validator private Fl uentValidationValidator? _fluentValidationValidator; 3) As well as dependency injection, which actually makes code cleaner.: services. AddTransient <IValidator <Model>, Validator> ( ); So for anyone new to using Blazored.FluentValidation -> It is a good idea to use the samples provided from git repo. Well coding!

### Response

**Viktor** commented on 08 Aug 2023

In this case there is another issue. What to do when there are two different validators for the same model (validate different sets of properties)? This solution wont work either

## Answer

**Nicolas** answered on 16 Mar 2023

See solution above.
