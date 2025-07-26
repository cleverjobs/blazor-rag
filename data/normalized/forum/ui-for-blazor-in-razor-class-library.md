# UI for Blazor in Razor Class Library

## Question

**And** asked on 03 Mar 2020

Hello, Is it possible to use the UI for Blazor within a Razor class library? We have a project where we need to have multiple reusable component libraries that will ideally be based on UI for Blazor, in our current tests we add the nuget package to the Razor class library and it fails to be recognised when trying to consume the namespaces. Also we need to share the App between Server and Client Blazor, once again requiring the UI for Blazor to be with a shared razor library. Thanks, Andy.

## Answer

**Marin Bratanov** answered on 03 Mar 2020

Hello Andy, There shouldn't be an issue with that, our project is also a class library. Just make sure to target netstandard2.1 (see the second paragraph): [https://docs.telerik.com/blazor-ui/upgrade/framework-versions](https://docs.telerik.com/blazor-ui/upgrade/framework-versions) because this is what we target, so older targets won't compile. Regards, Marin Bratanov

### Response

**Andy** answered on 03 Mar 2020

Marin, Thanks for the quick reply, that was the issue. The razor class libs default to 2.0, changed this to 2.1 and it all worked as expected. Just as a comment as I was adding this to a new project didn't look at the "Upgrade" section of the docs as did not think it was relevant. Might be worth adding a line in the Client & Server getting started pages just to highlight the requirement, or even better a getting started with razor class library page. Thanks again, Andy.
