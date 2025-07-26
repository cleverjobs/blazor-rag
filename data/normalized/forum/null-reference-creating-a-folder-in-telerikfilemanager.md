# Null reference creating a folder in TelerikFileManager

## Question

**Chr** asked on 28 Nov 2023

I'm getting the following error: Microsoft.AspNetCore.Components.Server.Circuits.RemoteRenderer[100] Unhandled exception rendering component: Object reference not set to an instance of an object. System.NullReferenceException: Object reference not set to an instance of an object. at Telerik.Blazor.Components.TelerikFileManager`1.ConvertToFileEntry(Object dataItem) After I click the create folder button in the TelerikFileManager. I've confirmed that it does reach the OnModelInit() method which does not return null, but never reaches the OnCreate() method. Any ideas what might be causing this?

## Answer

**Christopher** answered on 29 Nov 2023

I figured out the issue, it turned out to be because I was binding CreatedDate and UpdatedDate, but not CreatedDateUTC or UpdatedDateUTC. That could really use a clearer error message as it's not intuitive that setting both would even be required.
