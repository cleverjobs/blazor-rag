# error CS0012: The type 'DataSourceRequest' is defined in an assembly that is not referenced.

## Question

**Yeo** asked on 19 Mar 2023

This error occurred on 2023-03-15. error CS0012: The type 'DataSourceRequest' is defined in an assembly that is not referenced. You must add a reference to assembly 'Telerik.DataSource, Version=2.1.3.0, Culture=neutral, PublicKeyToken=29ac1a93ec063d92'. [RESOLVED] Error CS0012: The type 'DataSourceRequest' is defined in an assembly that is not referenced. You must add a reference to assembly Telerik.DataSource, Version=2.1.3.0 in UI for Blazor | Telerik Forums I know it was discussed at this URL. But when I build the Dockerfile, the error is still there. When will this error be fixed? Package : Telerik.UI.Blazor(4.1.0)

## Answer

**Dimo** answered on 21 Mar 2023

Hello Yeongseok, I confirm that the problem is already fixed. You need to clear the NuGet cache in all environment(s), which restore and build the app. Regards, Dimo
