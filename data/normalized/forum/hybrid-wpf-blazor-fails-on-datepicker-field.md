# Hybrid WPF Blazor fails on DatePicker field

## Question

**JKa** asked on 28 Feb 2024

Hi, The DatePicker gives a runtime error on Hybrid (does works on blazor server) <TelerikDatePicker Value="@entity.OrderDate.Date" Format="dd-MM-yyyy" ValueChanged="@((DateTime d)=> UpdateDateTimeOffsetField(d))" /> If i remove the datapicker tag, there is no problem. I suspect it has something to do with the hybrid stuff Loaded 'C:\Program Files\dotnet\shared\Microsoft.NETCore.App\8.0.2\System.Collections.Immutable.dll'. Skipped loading symbols. Module is optimized and the debugger option 'Just My Code' is enabled. Base.ErrorHandler:HandleError: System.Reflection.TargetInvocationException: Exception has been thrown by the target of an invocation. ---> System.Exception: A Telerik component on the requested view requires a TelerikRootComponent to be added to the root of the MainLayout component of the app. Read more at: [https://docs.telerik.com/blazor-ui/getting-started/what-you-need#project-configuration](https://docs.telerik.com/blazor-ui/getting-started/what-you-need#project-configuration) at Telerik.Blazor.Components.RootComponent.TelerikRootComponentFragment.OnInitializedAsync()

## Answer

**Dimo** answered on 01 Mar 2024

Hi John, Apparently the link in the exception message needs a small update and we will do this in the next release. Otherwise, is the exception message unclear? A Telerik component on the requested view requires a TelerikRootComponent to be added to the root of the MainLayout component of the app. Read more at: Telerik Blazor project configuration (this is the page where the exception message leads to) TelerikRootComponent main documentation Regards, Dimo Progress Telerik
