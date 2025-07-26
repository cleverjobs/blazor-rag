# Error in Step 4 of the Getting Started > Server-Side instructions

## Question

**Dav** asked on 14 Feb 2023

when adding: builder. Services. AddTelerikBlazor (); in step 4 of the 'Server-Side Blazor (Tutorial)' I'm getting this error: IServiceCollection' does not contain a definition for 'Add Telerik Blazor' and no accessible extension method 'Add TelerikBlazor' accepting a first argument of type 'IServiceCollection' could be found (are you missing a using directive or an assembly reference?) Thanks in advance for assistance.

## Answer

**Svetoslav Dimitrov** answered on 17 Feb 2023

Hello David, I created a standard (non-Telerik) Blazor Server App and added the Telerik configuration from the Getting Started article. For me, it works as expected, no issues/exceptions are thrown. As an attached file, you can see the application. Can you check the configuration and compare it against your own (including the sequence of the registered files) and see if there are any differences that might cause the exception? Regards, Svetoslav Dimitrov
