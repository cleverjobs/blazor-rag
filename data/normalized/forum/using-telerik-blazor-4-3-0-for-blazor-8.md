# Using Telerik Blazor 4.3.0 for Blazor 8

## Question

**Rog** asked on 20 Jan 2024

Hi: I am trying to use my Telerik Blazor 4.3.0 with a new Blazor 8 WebApp Server Global project. I keep getting the error: Microsoft.JSInterop.JSException: Maximum call stack size exceeded RangeError: Maximum call stack size exceeded at t ( [https://blazor.cdn.telerik.com/blazor/4.3.0/telerik-blazor.min.js:50:1034368](https://blazor.cdn.telerik.com/blazor/4.3.0/telerik-blazor.min.js:50:1034368) ) Can you help me? Thanks, Roger

## Answer

**Yanislav** answered on 24 Jan 2024

Hello Roger, The first Telerik UI for Blazor package version compatible with.NET 8 is 5.0. See: [https://docs.telerik.com/blazor-ui/system-requirements#supported-net-versions](https://docs.telerik.com/blazor-ui/system-requirements#supported-net-versions) That being said, I recommend using the latest version - 5.0.1. Please try it and let me know if everything works correctly. Regards, Yanislav Progress Telerik
