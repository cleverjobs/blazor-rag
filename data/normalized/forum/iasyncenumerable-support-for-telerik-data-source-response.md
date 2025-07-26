# IAsyncEnumerable Support for Telerik Data Source Response

## Question

**Vij** asked on 18 Sep 2023

In .NET 8, Microsoft will be introducing support for IAsyncEnumerable JSON deserialization ( Streaming deserialization APIs ). This feature allows for items in a long list to be deserialized as they are streamed to the client from a server, rather than waiting for the entire request to be completed. So it will result in a perceived performance increase. Is there any chance for Progress to look into bringing support for this feature to Telerik DataSource Responses? I can anticipate the data field in the response class makes this a challenging ask. Also, the server-side needs to be able to return yield for async items. I am interested in seeing this feature implemented so the grids in my applications that have many items will begin to be usable sooner.

## Answer

**Dimo** answered on 19 Sep 2023

Hello Vijaychandran, Our components project always targets the lowest .NET version that we must support. (Actually we still target.netstandard2.1, which will change in version 5.0.0 in early 2024). We refrain from multi-targeting. Given the Microsoft .NET support life cycle, the earliest possible time to add .NET 8 features to our source code is 2025. Until then, you can: Use .NET 8 features in your apps if they don't require changes in our source code. Download our source code, make changes to it and rebuild it. Regards, Dimo Progress Telerik
