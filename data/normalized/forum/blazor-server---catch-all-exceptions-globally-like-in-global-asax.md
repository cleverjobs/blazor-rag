# Blazor server - catch all exceptions globally like in Global.asax

## Question

**Mat** asked on 25 Feb 2022

Is it possible to catch all errors in Blazor Server like in MVC 5 in global.asax on Application_Error and send an email to application administrator? thank you, MAtej

## Answer

**Matthias** answered on 25 Feb 2022

Hi, you can use "ErrorBoundary" since .net 6. Here is an example which catches the errors of all components and then displays an error message. Alternatively you can also send a mail. The benefit of this is, that in case of an error not the whole application stops, but only the affected component. <ErrorBoundary @ref="@_errorBoundary"> <ChildContent> <div class="content"> @Body </div> </ChildContent> <ErrorContent Context="ex"> @if (HandleError(@ex))
{ <div class="container-error"> <div class="error-text"> @ex.Message </div> <div class="error-text-small"> @ex.StackTrace </div> </div> } </ErrorContent> </ErrorBoundary> private ErrorBoundary _errorBoundary; bool HandleError ( Exception ex ) { var msg=ex.Message; var trace=ex.StackTrace; // SEND MAIL TO ADMIN return true;

} This affects all components - if every error in the C# code should be caught globally, I would advise against managing this globally. For this I use try-catch blocks, which optionally log or send a mail in case of an error. With appropriate tests this should happen but rather rarely. Regards Matthias

### Response

**Matej Stare** commented on 25 Feb 2022

Matthias, thank you
