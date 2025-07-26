# How can I make the event handlers of the Upload component respect an ErrorBoundary?

## Question

**Chr** asked on 25 Apr 2022

I've discovered that exceptions raised within event-handlers of the Upload component do not respect the ErrorBoundaries above the Upload component itself. Instead, Blazor displays its out-of-the-box "unhandled exception" error. Is there a reason for this? What can I do to make exceptions that are raised within the Upload event-handlers get detected by Error Boudaries?

### Response

**Marin Bratanov** commented on 25 Apr 2022

Hi Chris, Is the ErrorBoundary component wrapping the TelerikUpload only, or is it around the parent component? I am asking because the event handlers are in the parent component, so the ErrorBoundary needs to wrap that as well - so it needs to be one level higher.

### Response

**Chris** commented on 26 Apr 2022

Hi Marin, The ErrorBoundary is at the App.razor level - wrapping the Router. I had also tried adding a lower-level ErrorBoundary as the direct parent of the TelerikUpload - but I was getting the same behavior (Blazor unhandled exception).

### Response

**Marin Bratanov** commented on 27 Apr 2022

Does throwing the same exception from other event handler (like a <button @onclick>) get captured?

### Response

**Chris** commented on 27 Apr 2022

Yes. I've tested it with a button and click-handler like you describe at the same level as the TelerikUpload. It will hit the ErrorBoundary just fine, but not the TelerikUpload.

## Answer

**Nadezhda Tacheva** answered on 02 May 2022

Hi Chris, I am stepping in the discussion to provide some more details. Upload handlers are executed by JavaScript and then sent as a JSInvokable method to the .NET part. Thus, the ErrorBoundary blazor-specific component is not aware of them. This is expected and is due to the way the Upload works. Instead, you can use OnError handler to react to errors. It fires each time a particular request fails - either an upload of a file, or the deletion of a file. I hope this information will help you move forward with your application. Please let us know if any further questions appear. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Chris** commented on 02 May 2022

Hi Nadezhda, I think I understand the usage of the OnError handler. In fact, we already use it. What I'm trying to do is catch exceptions that are thrown *from* the handlers. For example, we are handling the OnUpload event by adding metadata to the request, including the authorization bearer token. If an exception occurs somehow in there, we'd like the custom exception handling implemented in our ErrorBoundary to do what it needs to do (ie, display user-friendly error, log exception, etc). I'm not sure I would agree that the current behavior is "expected" - from the Blazor development perspective. Though, I do understand how it might be "expected" from an internal implementation standpoint.

### Response

**Nadezhda Tacheva** commented on 05 May 2022

Hi Chris, Indeed, the provided information is based on the Upload design and the way it operates. It is not possible to handle the errors from the Upload events with the ErrorBoundary, but you can consider an alternative to still handle them in a way that suits your case.
